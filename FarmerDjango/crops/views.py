from rest_framework.views import APIView
from .serializers import SoilSerializer
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from .models import Soil
import pandas as pd
import joblib


# Create your views here.
class SoilProfileView(APIView):
    serializer_class = SoilSerializer
    # create a get weather info method and get ph method


    def post(self, request):
        data = request.data
        serializer = self.serializer_class(data=data)
        if not serializer.is_valid():
            return Response({
                    'status': False,
                    'message': "Invalid data provided",
                    'error': serializer.errors
            }, status=HTTP_400_BAD_REQUEST)
        n = data.get('n')
        p = data.get('p')
        k = data.get('k')
        temperature = data.get('temperature')
        humidity = data.get('humidity')
        ph = data.get('ph')
        rainfall = data.get('rainfall')
        # get temperature, humidity and rainfall data from weather api and ph from IOT device later on
        data = [[n, p, k, temperature, humidity, ph, rainfall]]
        df = pd.DataFrame(data, columns=['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall'])
        full_pipeline = joblib.load('../saved_model/02-05-2023_20-47-39_full_pipeline.pkl')
        xgb_clf = joblib.load('../saved_model/02-05-2023_20-47-39_xgb_clf.pkl')

        prepared_data = full_pipeline.transform(df)
        prediction = xgb_clf.predict(prepared_data)

        target_encoder = joblib.load('../saved_model/02-05-2023_20-47-39_target_encoder.pkl')

        target_value = target_encoder.inverse_transform(prediction)
        profile = Soil(n=n, p=p, k=k, temperature=temperature, humidity=humidity, ph=ph, rainfall=rainfall)
        profile.save()

        return Response({
            'status': True,
            'message': f"I recommend you plant {target_value[0]}",
        }, status=HTTP_200_OK)

FROM python:3.11-slim

WORKDIR /muasya

COPY ./requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000


ENTRYPOINT ["python3", "FarmerDjango/manage.py"]
CMD ["runserver", "0.0.0.0:8000"]
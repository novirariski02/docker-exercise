FROM python:3.7                                 #base image
WORKDIR /app                                    #define directory apps on container
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "data_ingestion_script.py"]


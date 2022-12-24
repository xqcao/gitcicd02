FROM python:alpine
WORKDIR /webapp
COPY ./requirements.txt ./
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5001
CMD ["python","app.py"]
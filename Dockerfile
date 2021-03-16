FROM python:3.8.7-alpine 
WORKDIR /RTUIT_PROJECT
COPY requirements.txt /RTUIT_PROJECT
RUN pip3 install -r requirements.txt 
COPY . /RTUIT_PROJECT
ENTRYPOINT ["python3"] 
CMD ["app.py"]
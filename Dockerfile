FROM python:3.6-stretch
WORKDIR /flaskproject
COPY requirements.txt /flaskproject
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
COPY . /flaskproject
ENTRYPOINT ["python3"] 
CMD ["main.py"]
FROM python:3.7.7-buster

COPY . /app
WORKDIR /app
RUN pip install --upgrade pip
RUN pip install -r requirement.txt 
# EXPOSE 5000
ENTRYPOINT [ "python" ] 
CMD [ "main.py" ] 
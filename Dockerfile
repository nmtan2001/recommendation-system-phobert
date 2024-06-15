FROM ubuntu

WORKDIR /src

COPY requirements.txt ./

RUN apt-get update
RUN apt-get -y install python3 
RUN apt-get -y install python3-pip
RUN pip3 --no-cache-dir install Django tensorflow py_vncorenlp --break-system-packages
COPY grabText_ext/ ./grabText_ext/
COPY mysite/ ./mysite/

RUN cd mysite
RUN ["python3", "manage.py runserver"]
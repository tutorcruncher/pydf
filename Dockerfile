FROM python:3.6

RUN pip install aiohttp==2.1.0
RUN pip install python-pdf==0.33

LABEL maintainer 's@muelcolvin.com'

ADD ./docker.py /run.py
ENTRYPOINT ["/run.py"]

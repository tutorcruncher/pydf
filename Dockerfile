FROM python:3.6

RUN pip install aiohttp==2.1.0
ADD ./pydf /pydf
ADD setup.py /setup.py
RUN python /setup.py install

LABEL maintainer 's@muelcolvin.com'

ADD ./docker.py /run.py
ENTRYPOINT ["/run.py"]

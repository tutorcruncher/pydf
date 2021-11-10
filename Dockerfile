FROM python:3.8

LABEL maintainer='s@muelcolvin.com'

RUN pip install aiohttp==3.7.3
ADD ./pydf /pydf
ADD setup.py /
RUN pip install -e .

ADD ./docker-entrypoint.py /
ENTRYPOINT ["/docker-entrypoint.py"]

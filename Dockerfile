FROM python:3.6

RUN pip install aiohttp==2.1.0
ADD ./pydf /pydf
ADD setup.py /
RUN pip install -e .

LABEL maintainer 's@muelcolvin.com'

ADD ./docker-entrypoint.py /
ENTRYPOINT ["/docker-entrypoint.py"]

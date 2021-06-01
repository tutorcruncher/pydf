#!/usr/bin/env python3.8
"""
pydf

pdf generation in docker.

To generate PDF POST (or GET with data if possible) you HTML data to /generate.pdf.

Extra arguments can be passed using http headers; any header starting "pdf-" or "pdf_" will
have that prefix removed, be converted to lower case and passed to wkhtmltopdf.

For example:

    docker run -rm -p 8000:80 -d samuelcolvin/pydf
    curl -d '<h1>this is html</h1>' -H "pdf-orientation: landscape" http://localhost:8000/generate.pdf > created.pdf
    open "created.pdf"
"""
import os
import logging
from time import time

from aiohttp import web
from pydf import AsyncPydf

logger = logging.getLogger('main')
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
handler.setLevel(logging.INFO)
logger.addHandler(handler)


async def index(request):
    return web.Response(text=__doc__)


async def generate(request):
    start = time()
    config = {}
    for k, v in request.headers.items():
        if k.startswith('Pdf-') or k.startswith('Pdf_'):
            config[k[4:].lower()] = v
    data = await request.read()
    if not data:
        logger.info('Request with no body data')
        raise web.HTTPBadRequest(text='400: no HTML data to convert to PDF in request body\n')
    try:
        pdf_content = await app['apydf'].generate_pdf(data.decode(), **config)
    except RuntimeError as e:
        logger.info('Error generating PDF, time %0.2fs, config: %s', time() - start, config)
        return web.Response(text=str(e) + '\n', status=418)
    else:
        logger.info('PDF generated in %0.2fs, html-len %d, pdf-len %d', time() - start, len(data), len(pdf_content))
        return web.Response(body=pdf_content, content_type='application/pdf')

app = web.Application()
app.router.add_get('/', index)
app.router.add_route('*', '/generate.pdf', generate)
app['apydf'] = AsyncPydf()

port = int(os.getenv('PORT', '80'))
logger.info('starting pydf server on port %s', port)
web.run_app(app, port=port, print=lambda v: None)

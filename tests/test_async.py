import asyncio

import pytest

from pydf import AsyncPydf

from .utils import pdf_text


def test_async_pdf_gen():
    apydf = AsyncPydf()
    loop = asyncio.get_event_loop()

    pdf_content = loop.run_until_complete(apydf.generate_pdf('<html><body>Is this thing on?</body></html>'))
    assert pdf_content[:4] == b'%PDF'
    text = pdf_text(pdf_content)
    assert 'Is this thing on?\n\n\x0c' == text


def test_invalid_argument():
    apydf = AsyncPydf()
    loop = asyncio.get_event_loop()
    with pytest.raises(RuntimeError) as exc_info:
        loop.run_until_complete(apydf.generate_pdf('hello', foobar='broken'))
    assert 'error running wkhtmltopdf, command' in str(exc_info)

from io import BytesIO, StringIO

import pdfminer.layout
import pytest
from pdfminer import high_level

from pydf import generate_pdf, get_extended_help, get_help, get_version


def get_pdf_text(pdf_data: bytes) -> str:
    laparams = pdfminer.layout.LAParams()
    output = StringIO()
    high_level.extract_text_to_fp(BytesIO(pdf_data), output, laparams=laparams)
    return output.getvalue()


def test_generate_pdf_with_html():
    pdf_content = generate_pdf('<html><body>Is this thing on?</body></html>')
    assert pdf_content[:4] == b'%PDF'
    text = get_pdf_text(pdf_content)
    assert 'Is this thing on?\n\n\x0c' == text


def test_generate_pdf_with_html_meta_data():
    pdf_content = generate_pdf(
        '<html><body>Is this thing on?</body></html>',
        title='title foobar',
        subject='the subject',
        author='Samuel Colvin',
        creator='this is the creator'
    )
    assert pdf_content[:4] == b'%PDF'
    beginning = pdf_content.decode('utf8', 'ignore')[:300]
    print(beginning)
    assert """
<<
/Title (title foobar)
/Author (Samuel Colvin)
/Subject (the subject)
/Creator (this is the creator)""" in beginning


def test_unicode():
    pdf_content = generate_pdf(u'<html><body>Schrödinger</body></html>')
    assert pdf_content[:4] == b'%PDF'


def test_extra_arguments():
    pdf_content = generate_pdf(
        '<html><body>testing</body></html>',
        quiet=False,
        grayscale=True,
        lowquality=True,
        margin_bottom='20mm',
        margin_left='20mm',
        margin_right='20mm',
        margin_top='20mm',
        orientation='Landscape',
        page_height=None,
        page_width=None,
        page_size='Letter',
        image_dpi='300',
        image_quality='70',
    )
    assert pdf_content[:4] == b'%PDF'


def test_custom_size():
    pdf_content = generate_pdf(
        '<html><body>testing</body></html>',
        page_height='50mm',
        page_width='50mm',
    )
    assert pdf_content[:4] == b'%PDF'


def test_extra_kwargs():
    pdf_content = generate_pdf(
        '<html><body>testing</body></html>',
        header_right='Page [page] of [toPage]'
    )
    assert pdf_content[:4] == b'%PDF'


def test_generate_url():
    with pytest.raises(ValueError) as exc_info:
        generate_pdf('www.google.com')
    assert 'pdf generation from urls is not supported' in str(exc_info)


def test_bad_arguments():
    with pytest.raises(RuntimeError) as exc_info:
        generate_pdf('hellp', foobar='broken')
    assert 'error running wkhtmltopdf, command' in str(exc_info)


def test_get_version():
    print(get_version())


def test_get_help():
    get_help()


def test_get_extended_help():
    get_extended_help()

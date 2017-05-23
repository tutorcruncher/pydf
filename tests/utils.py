from io import BytesIO, StringIO

import pdfminer.layout
from pdfminer import high_level


def pdf_text(pdf_data: bytes) -> str:
    laparams = pdfminer.layout.LAParams()
    output = StringIO()
    high_level.extract_text_to_fp(BytesIO(pdf_data), output, laparams=laparams)
    return output.getvalue()

pydf
====


|BuildStatus| |codecov| |PyPI| |license|

PDF generation in python using
`wkhtmltopdf <http://wkhtmltopdf.org/>`__.

Wkhtmltopdf binaries are precompiled and included in the package making
pydf easier to use, in particular this means pydf works on heroku.

Currently using **wkhtmltopdf 0.12.4 (with patched qt)**, requires **Python 3.6+**.

Install
-------

::

    pip install python-pdf

For python 2 use ``pip install python-pdf==0.30.0``.

Basic Usage
-----------

.. code:: python

    import pydf
    pdf = pydf.generate_pdf('<h1>this is html</h1>')
    with open('test_doc.pdf', 'wb') as f:
        f.write(pdf)

Async Usage
-----------

Generation of lots of documents with wkhtmltopdf can be slow as wkhtmltopdf can only generate one document
per process. To get round this pydf uses python 3's asyncio ``create_subprocess_exec`` to generate multiple pdfs
at the same time. Thus the time taken to spin up processes doesn't slow you down.

.. code:: python

    from pathlib import Path
    from pydf import AsyncPydf

    async def generate_async():
        apydf = AsyncPydf()

        async def gen(i):
            pdf_content = await apydf.generate_pdf('<h1>this is html</h1>')
            Path(f'output_{i:03}.pdf').write_bytes(pdf_content)

        coros = [gen(i) for i in range(50)]
        await asyncio.gather(*coros)

    loop = asyncio.get_event_loop()
    loop.run_until_complete(generate_async())


See `benchmarks/run.py <https://github.com/tutorcruncher/pydf/blob/master/benchmark/run.py>`__
for a full example.

Locally generating an entire invoice goes from 0.372s/pdf to 0.035s/pdf with the async model.

API
---

**generate\_pdf(source, [\*\*kwargs])**

Generate a pdf from either a url or a html string.

After the html and url arguments all other arguments are passed straight
to wkhtmltopdf

For details on extra arguments see the output of get\_help() and
get\_extended\_help()

All arguments whether specified or caught with extra\_kwargs are
converted to command line args with ``'--' + original_name.replace('_', '-')``.

Arguments which are True are passed with no value eg. just --quiet,
False and None arguments are missed, everything else is passed with
str(value).

**Arguments:**

-  ``source``: html string to generate pdf from or url to get
-  ``quiet``: bool
-  ``grayscale``: bool
-  ``lowquality``: bool
-  ``margin_bottom``: string eg. 10mm
-  ``margin_left``: string eg. 10mm
-  ``margin_right``: string eg. 10mm
-  ``margin_top``: string eg. 10mm
-  ``orientation``: Portrait or Landscape
-  ``page_height``: string eg. 10mm
-  ``page_width``: string eg. 10mm
-  ``page_size``: string: A4, Letter, etc.
-  ``image_dpi``: int default 600
-  ``image_quality``: int default 94
-  ``extra_kwargs``: any exotic extra options for wkhtmltopdf

Returns string representing pdf

**get\_version()**

Get version of pydf and wkhtmltopdf binary

**get\_help()**

get help string from wkhtmltopdf binary uses -h command line option

**get\_extended\_help()**

get extended help string from wkhtmltopdf binary uses -H command line
option

**execute\_wk(\*args)**

Low level function to call wkhtmltopdf, arguments are added to
wkhtmltopdf binary and passed to subprocess with not processing.

.. |BuildStatus| image:: https://travis-ci.org/tutorcruncher/pydf.svg?branch=master
   :target: https://travis-ci.org/tutorcruncher/pydf
.. |codecov| image:: https://codecov.io/github/tutorcruncher/pydf/coverage.svg?branch=master
   :target: https://codecov.io/github/tutorcruncher/pydf?branch=master
.. |PyPI| image:: https://img.shields.io/pypi/v/python-pdf.svg?style=flat
   :target: https://pypi.python.org/pypi/python-pdf
.. |license| image:: https://img.shields.io/pypi/l/python-pdf.svg
   :target: https://github.com/tutorcruncher/pydf

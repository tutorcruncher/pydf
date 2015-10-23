pydf
====

[![codecov.io](https://codecov.io/github/tutorcruncher/pydf/coverage.svg?branch=master)](https://codecov.io/github/tutorcruncher/pydf?branch=master)
[![Build Status](https://travis-ci.org/tutorcruncher/pydf.svg?branch=master)](https://travis-ci.org/tutorcruncher/pydf)

PDF generation in python using [wkhtmltopdf](http://wkhtmltopdf.org/).

Wkhtmltopdf binaries are precompiled and included in the package making pydf easier to use,
in particular this means pydf works on heroku.

Based on [pywkher](https://github.com/jwmayfield/pywkher) but significantly extended.

Currently using **wkhtmltopdf v. 0.12.2** (beta).

## Install

    pip install python-pdf

(pydf was taken, but I guess python-pdf is a clearer name anyway.)

## Basic Usage

```python
import pydf
pdf = pydf.generate_pdf('<h1>this is html</h1>')
open('test_doc.pdf', 'w').write(pdf)

pdf = pydf.generate_pdf('www.google.com')
open('google.pdf', 'w').write(pdf)
```

## API

#### generate_pdf(source, [**kwrags])

Generate a pdf from either a url or a html string.

After the html and url arguments all other arguments are
passed straight to wkhtmltopdf

For details on extra arguments see the output of get_help()
and get_extended_help()

All arguments whether specified or caught with extra_kwargs are converted
to command line args with "'--' + original_name.replace('_', '-')"

Arguments which are True are passed with no value eg. just --quiet, False
and None arguments are missed, everything else is passed with str(value).

**Arguments:**

* `source`: html string to generate pdf from or url to get
* `quiet`: bool
* `grayscale`: bool
* `lowquality`: bool
* `margin_bottom`: string eg. 10mm
* `margin_left`: string eg. 10mm
* `margin_right`: string eg. 10mm
* `margin_top`: string eg. 10mm
* `orientation`: Portrait or Landscape
* `page_height`: string eg. 10mm
* `page_width`: string eg. 10mm
* `page_size`: string: A4, Letter, etc.
* `image_dpi`: int default 600
* `image_quality`: int default 94
* `extra_kwargs`: any exotic extra options for wkhtmltopdf

Returns string representing pdf

#### get_version()

Get version of pydf and wkhtmltopdf binary

#### get_help()

get help string from wkhtmltopdf binary
uses -h command line option

#### get_extended_help()

get extended help string from wkhtmltopdf binary
uses -H command line option

#### execute_wk(*args)

Low level function to call wkhtmltopdf, arguments are added to wkhtmltopdf binary and passed to subprocess with not processing.

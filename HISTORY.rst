.. :changelog:

History
-------

v0.37.0 (2018-12-19)
....................
* upgrade wkhtmltopdf binary to "wkhtmltopdf 0.12.5 for Ubuntu 18.04 (bionic)", #11. Requires heroku-18

v0.36.0 (2017-06-13)
....................
* allow alternative wkhtmltopdf binary via ``WKHTMLTOPDF_PATH`` environment variable

v0.35.0 (2017-06-06)
....................
* add docker auto tagging

v0.34.0 (2017-06-06)
....................
* improve error output

v0.33.0 (2017-05-24)
....................
* remove pdf metadata modification as it can break some pdf viewers

v0.32.0 (2017-05-24)
....................
* set ``cache_dir`` for ``generate_pdf`` by default

v0.31.0 (2017-05-23)
....................
* move to python 3.6 +
* add ``async`` generation for roughly 10x speedup

v0.30.0
.......
* uprev wkhtmltopdf from **0.12.2 (beta)** to **0.12.4**.
* code cleanup
* this is the same as ``v0.3``, I made a mistake when versioning

v0.21.0
.......
* correct permissions on wkhtmltopdf binary.

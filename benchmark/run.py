from pathlib import Path
from time import time

from pydf import generate_pdf


THIS_DIR = Path(__file__).parent.resolve()
html = (THIS_DIR / 'invoice.html').read_text()
PDF_CACHE = THIS_DIR / 'pdf_cache'
if not PDF_CACHE.exists():
    Path.mkdir(PDF_CACHE)
OUT_DIR = THIS_DIR / 'output'
if not OUT_DIR.exists():
    Path.mkdir(OUT_DIR)


start = time()
count = 20
for i in range(count):
    pdf = generate_pdf(
        html,
        title='Benchmark',
        author='Samuel Colvin',
        subject='Mock Invoice',
        page_size='A4',
        zoom='1.25',
        margin_left='8mm',
        margin_right='8mm',
        cache_dir=PDF_CACHE,
    )
    print(f'{i:03}: {len(pdf)}')
    file = OUT_DIR / f'output_{i:03}.pdf'
    file.write_bytes(pdf)
time_taken = (time() - start) / count
print(f'time taken: {time_taken:0.3f}')

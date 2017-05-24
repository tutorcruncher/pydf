import asyncio
from pathlib import Path
from time import time

from pydf import AsyncPydf, generate_pdf


THIS_DIR = Path(__file__).parent.resolve()
html = (THIS_DIR / 'invoice.html').read_text()
OUT_DIR = THIS_DIR / 'output'
if not OUT_DIR.exists():
    Path.mkdir(OUT_DIR)


def go_sync():
    count = 10
    for i in range(count):
        pdf = generate_pdf(
            html,
            page_size='A4',
            zoom='1.25',
            margin_left='8mm',
            margin_right='8mm',
        )
        print(f'{i:03}: {len(pdf)}')
        file = OUT_DIR / f'output_{i:03}.pdf'
        file.write_bytes(pdf)
    return count

start = time()
count = go_sync()
time_taken = (time() - start) / count
print(f'sync, time taken per pdf: {time_taken:0.3f}s')

async def go_async():
    apydf = AsyncPydf()

    async def gen(i_):
        pdf = await apydf.generate_pdf(
            html,
            page_size='A4',
            zoom='1.25',
            margin_left='8mm',
            margin_right='8mm',
        )
        print(f'{i_:03}: {len(pdf)}')
        f = OUT_DIR / f'output_{i_:03}.pdf'
        f.write_bytes(pdf)

    count = 20
    coros = map(gen, range(count))
    await asyncio.gather(*coros)
    return count


start = time()
loop = asyncio.get_event_loop()
count = loop.run_until_complete(go_async())
time_taken = (time() - start) / count
print(f'async time taken per pdf: {time_taken:0.3f}s')

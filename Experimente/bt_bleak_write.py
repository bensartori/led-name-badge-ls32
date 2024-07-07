import asyncio
from array import array

from bleak import BleakClient


address = "54:14:A7:80:FA:59"


buf = array('B', [119, 97, 110, 103, 0, 0, 0, 1, 52, 51, 51, 51, 51, 51, 51, 51, 0, 5, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 24, 7, 7, 15, 11, 59, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 16, 48, 48, 252, 48, 48, 48, 52, 24, 0, 0, 1, 2, 3, 6, 12, 26, 19, 17, 25, 15, 120, 204, 135, 252, 66, 129, 129, 129, 129, 67, 189, 0, 0, 0, 128, 128, 224, 48, 16, 40, 40, 208, 0, 126, 126, 90, 24, 24, 24, 24, 24, 60, 0, 0, 126, 126, 90, 24, 24, 24, 24, 24, 60, 0, 128, 64, 32, 16, 8, 4, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 128, 64, 32, 0, 1, 2, 3, 4, 5, 15, 31, 63, 127, 255, 0, 16, 48, 48, 252, 48, 48, 48, 52, 24, 0])


async def main(address):
    async with BleakClient(address, timeout=20) as client:
        #print(f'Services of {client.address}')
        #for s in client.services:
        #    print(f'{s.uuid}: {s.description} {s.characteristics}')
        print(f"Connected: {client}")

        chunk_siz = client.mtu_size - 7
        need_padding = len(buf) % chunk_siz
        if need_padding:
            buf.extend((0,) * (chunk_siz - need_padding))

        print(f'buf_size: {len(buf)}')
        print(f'chunk_siz: {chunk_siz}')
        for c in range(0, len(buf), chunk_siz):
            await client.write_gatt_char('FEE1', buf[c:c+chunk_siz], False)
            print(f'written: {c}-{c+chunk_siz}: {buf[c:c+chunk_siz]}')


asyncio.run(main(address))



#     client = BleakClient(address)
#     try:
#         await client.connect()
#         model_number = await client.read_gatt_char(MODEL_NBR_UUID)
#         print("Model Number: {0}".format("".join(map(chr, model_number))))
#     except Exception as e:
#         print(e)
#     finally:
#         await client.disconnect()

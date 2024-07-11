import asyncio
from array import array

from bleak import BleakClient

from lednamebadge import LedNameBadge, SimpleTextAndIcons


address = "54:14:A7:80:FA:59"

# buf = array('B', [119, 97, 110, 103, 0, 0, 0, 1, 54, 48, 48, 48, 48, 48, 48, 48, 0, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 24, 7, 9, 15, 16, 15, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 126, 126, 90, 24, 24, 24, 24, 24, 60, 0, 0, 0, 0, 0, 120, 12, 124, 204, 204, 118, 0, 0, 0, 0, 0, 124, 198, 192, 192, 198, 124, 0, 0, 224, 96, 96, 108, 118, 102, 102, 102, 230, 0, 0, 0, 0, 0, 120, 12, 124, 204, 204, 118, 0, 0, 0, 0, 0, 204, 204, 204, 204, 204, 118, 0, 0, 0, 0, 0, 124, 198, 192, 192, 198, 124, 0, 0, 224, 96, 96, 108, 118, 102, 102, 102, 230, 0])

creator = SimpleTextAndIcons()
scene_x_bitmap = creator.bitmap("Hello :HEART2: World!")
scene_y_bitmap = creator.bitmap("Complete example ahead.")
scene_z_bitmap = creator.bitmap("Das ist ja toll hier :bicycle: :owncloud:.")

lengths = (scene_x_bitmap[1], scene_y_bitmap[1], scene_z_bitmap[1])
buf = array('B')
buf.extend(LedNameBadge.header(lengths, (3,3,4,3), (6,4,0), (0, 1, 0), (1, 0), 100))
buf.extend(scene_x_bitmap[0])
buf.extend(scene_y_bitmap[0])
buf.extend(scene_z_bitmap[0])

if len(buf) > 8192:
    print("Buffer too big!")
    exit(1)

async def main(address):
    async with BleakClient(address, timeout=40) as client:
        #print(f'Services of {client.address}')
        #for s in client.services:
        #    print(f'{s.uuid}: {s.description} {s.characteristics}')
        print(f"Connected: {client}")

        services = client.services
        for s in services:
            print(f"service: {s}")

        chunk_size = 16
        need_padding = len(buf) % chunk_size
        if need_padding:
            buf.extend((0,) * (chunk_size - need_padding))
        print(f'buf_size: {len(buf)}')
        print(f'chunk_siz: {chunk_size}')

        for c in range(0, len(buf), chunk_size):
            await client.write_gatt_char('FEE1', buf[c:c+chunk_size], True)
            print(f'written: {c}-{c+chunk_size}: {buf[c:c+chunk_size]}')


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

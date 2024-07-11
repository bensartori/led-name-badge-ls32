import asyncio
from array import array

from bleak import BleakClient

address = "54:14:A7:80:FA:59"
MANUFACTURER_NAME_STRING_UUID = "2A29"
MODEL_NUMBER_STRING_UUID = "2A24"
SERIAL_NUMBER_STRING_UUID = "2A25"
HARDWARE_REVISION_STRING_UUID = "2A27"
FIRMWARE_REVISION_STRING_UUID = "2A26"
SOFTWARE_REVISION_STRING_UUID = "2A28"
SYSTEM_ID_UUID = "2A23"
REGULATORY_CERTIFICATION_DATA_LIST_UUID = "2A2A"
PNP_ID_UUID = "2A2A"

ALL = {
    'MANUFACTURER_NAME_STRING_UUID': MANUFACTURER_NAME_STRING_UUID,
    'MODEL_NUMBER_STRING_UUID': MODEL_NUMBER_STRING_UUID,
    'SERIAL_NUMBER_STRING_UUID': SERIAL_NUMBER_STRING_UUID,
    'HARDWARE_REVISION_STRING_UUID': HARDWARE_REVISION_STRING_UUID,
    'FIRMWARE_REVISION_STRING_UUID': FIRMWARE_REVISION_STRING_UUID,
    'SOFTWARE_REVISION_STRING_UUID': SOFTWARE_REVISION_STRING_UUID,
    #'SYSTEM_ID_UUID': SYSTEM_ID_UUID,
    'REGULATORY_CERTIFICATION_DATA_LIST_UUID': REGULATORY_CERTIFICATION_DATA_LIST_UUID,
    #'PNP_ID_UUID': PNP_ID_UUID,
    #'DATA': 'FEE1'
    #'DEVICE_NAME': "2a00",
    'ANHUI': 'FEE1',
}


# UUIDs': [
# '00001800-0000-1000-8000-00805f9b34fb',
# '00001801-0000-1000-8000-00805f9b34fb',
# '0000180a-0000-1000-8000-00805f9b34fb',
# '0000fee0-0000-1000-8000-00805f9b34fb'


buf = array('B', [119, 97, 110, 103, 0, 0, 0, 1, 52, 51, 51, 51, 51, 51, 51, 51, 0, 5, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 24, 7, 7, 14, 46, 13, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 16, 48, 48, 252, 48, 48, 48, 52, 24, 0, 0, 0, 1, 2, 3, 6, 12, 26, 19, 17, 25, 15, 0, 120, 204, 135, 252, 66, 129, 129, 129, 129, 67, 189, 0, 0, 0, 0, 128, 128, 224, 48, 16, 40, 40, 208, 0, 0, 126, 126, 90, 24, 24, 24, 24, 24, 60, 0, 0, 0, 126, 126, 90, 24, 24, 24, 24, 24, 60, 0, 0, 128, 64, 32, 16, 8, 4, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 128, 64, 32, 0, 0, 1, 2, 3, 4, 5, 15, 31, 63, 127, 255, 0, 0, 16, 48, 48, 252, 48, 48, 48, 52, 24, 0, 0])


async def main(address):
    async with BleakClient(address, timeout=20) as client:
        #print(f'Services of {client.address}')
        #for s in client.services:
        #    print(f'{s.uuid}: {s.description} {s.characteristics}')
        print(f"Connected: {client}")

        for k, v in ALL.items():
            value = await client.read_gatt_char(v)
            print(f"{k} ({v}): {"".join(map(chr, value))} ({" ".join(map(hex, value))})")


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

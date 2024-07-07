import asyncio
from bleak import BleakScanner

async def main():
    devices = await BleakScanner.discover()
    for d in devices:
        name = d.details['props'].get('Name', '')
        print(f'{d.address}: {d.name} RSSI: {d.rssi} {'*** ' if name == 'LSLED' else ''}')
        print(f'  Details: {d.details}')
        print(f'  Metadata: {d.metadata}')

asyncio.run(main())

# 54:14:A7:80:FA:59: LSLED RSSI: -73
# Details: {'path': '/org/bluez/hci0/dev_54_14_A7_80_FA_59', 'props': {'Address': '54:14:A7:80:FA:59', 'AddressType': 'public', 'Name': 'LSLED', 'Alias': 'LSLED', 'Paired': True, 'Bonded': True, 'Trusted': True, 'Blocked': False, 'LegacyPairing': False, 'Connected': False, 'UUIDs': ['00001800-0000-1000-8000-00805f9b34fb', '00001801-0000-1000-8000-00805f9b34fb', '0000180a-0000-1000-8000-00805f9b34fb', '0000fee0-0000-1000-8000-00805f9b34fb'], 'Modalias': 'bluetooth:v07D7p0000d0110', 'Adapter': '/org/bluez/hci0', 'ServicesResolved': False, 'RSSI': -78, 'TxPower': 0}}
# Metadata: {'uuids': ['00001800-0000-1000-8000-00805f9b34fb', '00001801-0000-1000-8000-00805f9b34fb', '0000180a-0000-1000-8000-00805f9b34fb', '0000fee0-0000-1000-8000-00805f9b34fb'], 'manufacturer_data': {}}
#
# 00001800-0000-1000-8000-00805f9b34fb -> 1800 GAP Service
# 00001801-0000-1000-8000-00805f9b34fb -> 1801 GATT Service
# 0000180a-0000-1000-8000-00805f9b34fb -> Device Information Service
# 0000fee0-0000-1000-8000-00805f9b34fb -> Anhui Huami Information Technology Co., Ltd.


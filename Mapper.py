"""
Put input device id in settings for mappers.
Using:
    1) Add controller in XOutput and map "A" button with your controller
    2) Run script in XOutput folder
    3) ???
    4) Profit
"""

import json
import sys

DEFAULT_INPUT_TYPES = {'A':     '44',
                       'B':     '45',
                       'X':     '47',
                       'Y':     '48',
                       'L1':    '50',
                       'R1':    '51',
                       'L3':    '57',
                       'R3':    '58',
                       'Start': '55',
                       'Back':  '122',
                       'Home':  '54',
                       'LX':    '16',
                       'LY':    '12',
                       'RX':    '8',
                       'RY':    '4',
                       'L2':    '52',
                       'R2':    '53',
                       'UP':    '1000',
                       'DOWN':  '1001',
                       'LEFT':  '1002',
                       'RIGHT': '1003',}


def main(file_name='settings.json', force_map=False):
    """
    :param file_name:
    :param force_map: map even there is already InputDevice in controller mappings
    :return:
    """
    with open(file_name, 'r') as f:
        settings_json = json.load(f)

    for controller_index, controller in enumerate(settings_json['Mapping']):
        input_device_id = controller['Mappings']['A']['Mappers'][0]['InputDevice']
        if input_device_id:
            for button_name, button_map in controller['Mappings'].items():
                if button_map['Mappers'][0]['InputDevice'] is None or force_map:
                    button_map['Mappers'][0]['InputType'] = DEFAULT_INPUT_TYPES[button_name]
                    button_map['Mappers'][0]['MaxValue'] = 1
                    if button_name != 'Back':
                        button_map['Mappers'][0]['InputDevice'] = input_device_id
                    else:
                        button_map['Mappers'][0]['InputDevice'] = 'Keyboard'  # Because of controller ¯\_(ツ)_/¯

                    settings_json['Mapping'][controller_index]['Mappings'][button_name].update(button_map.copy())
                # controller['Mappings'][button_name] = button_map
    pass


if __name__ == '__main__':
    file_name = 'settings.json'  # It's default file name of XOutput

    main()


#!/usr/bin/env python

import click

@click.command()
def convert_sid_to_hex():
    input_string = click.prompt("Enter the SID:")
    prefix = 'S-1-5-21-'

    # Split the input string after the constant prefix
    components = input_string.split(prefix, 1)
    if len(components) > 1:
        remaining_string = components[1]
        split_values = remaining_string.split('-')
        output_list = []
        for i in split_values:
            decimal_number = int(i)
            hexadecimal_value = hex(decimal_number)[2:].zfill(8)
            little = ' '.join([hexadecimal_value[i:i+2] for i in range(len(hexadecimal_value)-2, -2, -2)])
            bytes_list = little.split()
            formatted_bytes = ', '.join([f"0x{byte.upper()}" for byte in bytes_list]) 
            output_list.append(formatted_bytes)
        final_output = ', '.join(output_list)
        print("Here is your SID in HEX:")
        print("0x01, 0x04, 0x00, 0x00, 0x00, 0x00, 0x00, 0x05, 0x15, 0x00, 0x00, 0x00, " + final_output)

if __name__ == '__main__':
    convert_sid_to_hex()


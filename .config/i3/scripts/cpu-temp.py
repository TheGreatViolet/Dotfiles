#!/usr/bin/env python3

import psutil


def main():
    # Thresholds for CPU temperature
    # Make sure CPU_MED_THRESHOLD is less than CPU_HIGH_THRESHOLD
    # Thresholds should be in Celsius

    CPU_MED_THRESHOLD = 60
    CPU_HIGH_THRESHOLD = 70

    cpu_temp = psutil.sensors_temperatures()['coretemp'][0].current
    rounded_temp = round(cpu_temp)

    # First print is for long version in i3bar
    # Second print is for short version in i3bar

    print(f'  {rounded_temp}°C ')
    print(f'{rounded_temp}°C')

    # Sets text color

    print('#3b4252')

    # Defines color for CPU temperature
    # Colors base on Nord color palette

    if (rounded_temp >= CPU_MED_THRESHOLD):
        if (rounded_temp < CPU_HIGH_THRESHOLD):
            print('#bf616a')
        else:
            print('#d08770')
    else:
        print('#8fbcbb')


if __name__ == '__main__':
    main()

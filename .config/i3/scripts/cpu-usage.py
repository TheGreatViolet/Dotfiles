#!/usr/bin/env python3

import psutil


def main():
    # Thresholds for CPU usage
    # Make sure CPU_MED_THRESHOLD is less than CPU_HIGH_THRESHOLD

    CPU_HIGH_THRESHOLD = 90
    CPU_MED_THRESHOLD = 70

    cpu_usage = psutil.cpu_percent(interval=1)

    rounded_usage = round(cpu_usage)

    # First print is for long version in i3bar
    # Second print is for short version in i3bar

    if (rounded_usage < 10):
        print(f'  0{rounded_usage}% ')
        print(f'{rounded_usage}%')
    else:
        print(f'  {rounded_usage}% ')
        print(f'{rounded_usage}%')

    # Sets text color
    print('#3b4252')

    # Defines color for CPU usag
    # Colors based on Nord color palette

    if (rounded_usage >= CPU_MED_THRESHOLD):
        if (rounded_usage < CPU_HIGH_THRESHOLD):
            print('#bf616a')
        else:
            print('#d08770')
    else:
        print('#8fbcbb')


if __name__ == '__main__':
    main()

#!/usr/bin/env python3

import shutil


def main():
    # Default disk is whatever is mounted at /

    total, used, _free = shutil.disk_usage('/')

    # Convert to GB

    total = total / (1024 * 1024 * 1024)
    used = used / (1024 * 1024 * 1024)

    # Round to nearest integer

    total = round(total)
    used = round(used)

    # First print is for long version in i3bar
    # Second print is for short version in i3bar

    print(f'  {used}GB/{total}GB ')
    print(f'{used}/{total}')

    # Sets text color

    print('#3b4252')

    # Defines color for disk usage
    # Color based on Nord color palette

    print('#8fbcbb')


if __name__ == '__main__':
    main()

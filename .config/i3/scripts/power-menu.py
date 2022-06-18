#!/usr/bin/env python3

import os


def main():
    if os.getenv('BLOCK_BUTTON') == '1':
        os.system('~/.config/rofi/powermenu/powermenu.sh')

    # First print is for the long version in i3bar
    # Second print is for the short version in i3bar
    print(' 襤 ')
    print('襤')

    # Sets text color
    print('#3b4252')

    # Sets background color
    print('#8fbcbb')


if __name__ == "__main__":
    main()

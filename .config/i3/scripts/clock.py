#!/usr/bin/env python3

from datetime import datetime


def main():
    time = datetime.now().strftime('%H:%M')
    date = datetime.now().strftime('%a %d %b')

    print(f' {time} {date} ')
    print(f'{time} {date}')

    # Sets text color
    print('#3b4252')

    # Background color
    print('#8fbcbb')


if __name__ == '__main__':
    main()

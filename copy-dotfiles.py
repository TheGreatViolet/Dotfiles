#!/usr/bin/env python3

# Script to copy dotfiles to working directory

from glob import escape
import os
import shutil


def main():
    # Folders located in ~/.config
    CONFIGFILES = [
        'i3',
        'rofi',
        'xfce4',
    ]

    # Misc files
    MISCFILES = [
        '~/.zshrc'
    ]

    # Copying config files

    # Config files get placed in .config
    for configfile in CONFIGFILES:
        sourcedir = os.path.expanduser(f'~/.config/{configfile}')
        targetdir = os.path.join('.config', configfile)

        isdir = os.path.isdir(sourcedir)

        if os.path.exists(targetdir):
            shutil.rmtree(targetdir)

        if isdir:
            shutil.copytree(sourcedir, targetdir)
        else:
            shutil.copy(sourcedir, targetdir)

    # Misc files get placed in home
    for miscfile in MISCFILES:
        sourcedir = os.path.expanduser(miscfile)
        targetdir = os.path.join('home', miscfile)

        isdir = os.path.isdir(sourcedir)

        if os.path.exists(targetdir):
            os.remove(targetdir)

        if isdir:
            shutil.copytree(sourcedir, targetdir)
        else:
            shutil.copy(sourcedir, targetdir.replace('~', ''))


if __name__ == '__main__':
    main()

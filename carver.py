#!/usr/bin/env python3

# Allowed imports by project requirements
import binascii
from hashlib import md5
from _md5 import md5
import os
import sys

FILE_MARKERS = {'jpg': (b'\xFF\xD8', b'\xFF\xD9'),
                'png': (b'\x50\x4E\x47', b'\x49\x45\x4E\x44'),
                'pdf_markers': (b'\x25\x50\x44\x46', b'\x25\x25\x45\x4F\x46')}
directory_name = "./Malcy"


def main():
    # Create the folder named "Malcy" if it doesn't exist
    if os.path.isdir(directory_name) is False:
        os.mkdir(directory_name)

    # TODO: Parse cmdline arguments


if __name__ == "__main__":
    main()

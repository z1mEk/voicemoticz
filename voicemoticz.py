#!/usr/bin/env python3

from processor import txtProcessor
import sys

phrase = sys.argv[1]
txtp = txtProcessor()
ar = txtp.GoProcess(phrase)
print(ar)

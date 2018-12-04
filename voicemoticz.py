#!/usr/bin/env python3

from processor import txtProcessor
import sys

phrase = sys.argv[1]
if len(sys.argv) > 2:
  ga = sys.argv[2]
else:
  ga = 0
txtp = txtProcessor()
ar = txtp.GoProcess(text=phrase, ga=ga)
print(ar)

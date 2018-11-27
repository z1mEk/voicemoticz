#!/usr/bin/env python3

from processor import txtProcessor
import sys

fraza = sys.argv[1]

txtp = txtProcessor()
ar = txtp.GoProcess(fraza)

print(ar)

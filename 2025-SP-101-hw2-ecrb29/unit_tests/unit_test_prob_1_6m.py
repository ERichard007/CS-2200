#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

### Open files and populate lists ###
accept_file = open("unit_tests/inputs/1_6m_accepts.txt", "r")
reject_file = open("unit_tests/inputs/1_6m_rejects.txt", "r")
accept_list = accept_file.readlines()
reject_list = reject_file.readlines()

### Remove newlines ###
for i in range(len(accept_list)):
    accept_list[i] = accept_list[i][:-1]
for i in range(len(reject_list)):
    reject_list[i] = reject_list[i][:-1]

### Test Inputs ###
from prob_1_6m import prob_1_6m
test_machine = prob_1_6m

UNEXPECTED = []

for w in accept_list:
    if (w not in test_machine):
        UNEXPECTED.append(w)

for w in reject_list:
    if (w in test_machine):
        UNEXPECTED.append(w)

if len(UNEXPECTED) > 0:
    print("UNEXPECTED RESULT ON THESE INPUTS: ", end="")
    if len(UNEXPECTED) > 10:
        print("[", end="")
        for i in range(9):
            print(f"\'{UNEXPECTED[i]}\'", end=", ")
        print(f"\'{UNEXPECTED[9]}\', ...]")
    else:
        print(UNEXPECTED)
    sys.exit(1)

### Clean up ###
accept_file.close()
reject_file.close()

#!/usr/bin/env python

import os
import sys
import ControlCPULimit

if __name__ == '__main__':
    if os.geteuid() != 0:
        print ("This program must be run as root. Aborting.")
        exit(0)
    else:
        print ControlCPULimit.startControl(sys.argv)

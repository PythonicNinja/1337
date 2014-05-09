#!/usr/bin/env python
import os
import sys
from sys import path
from os.path import dirname, abspath
if __name__ == "__main__":
    SITE_ROOT = dirname(dirname(abspath(__file__)))
    path.append(SITE_ROOT)
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pro_tips.settings.local")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)

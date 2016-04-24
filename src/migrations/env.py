# -*- coding: utf-8 -*-

import os
import sys

from wuffi.core.db import migrations

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Add `BASE_DIR` to system path to get ability to import application modules
sys.path.append(BASE_DIR)
# Configure settings module
os.environ.setdefault('WUFFI_SETTINGS_MODULE', 'config.settings.base')


migrations.run()

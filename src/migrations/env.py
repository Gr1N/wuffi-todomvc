# -*- coding: utf-8 -*-

import os
import logging
import logging.config
import sys

from alembic import context

from wuffi.core.db import migrations

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Add `BASE_DIR` to system path to get ability to import application modules
sys.path.append(BASE_DIR)
# Configure settings module
os.environ.setdefault('WUFFI_SETTINGS_MODULE', 'config.settings.base')

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# Interpret the config file for Python logging.
# This line sets up loggers basically.
logging.config.fileConfig(config.config_file_name)

if context.is_offline_mode():
    migrations.run_offline(context)
else:
    migrations.run_online(context)

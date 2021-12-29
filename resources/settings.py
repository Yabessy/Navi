# settings.py
"""Contains global settings"""

import os
import sqlite3
from typing import NamedTuple

import bot as bot_py


# Import some stuff from the main file to make it available everywhere
bot = bot_py.bot
DEBUG_MODE = bot_py.DEBUG_MODE

BOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_FILE = os.path.join(BOT_DIR, 'database/navi_db.db')

NAVI_DB = sqlite3.connect(DB_FILE, isolation_level=None).row_factory = sqlite3.Row

LOG_FILE = os.path.join(BOT_DIR, 'logs/discord.log')

DONOR_COOLDOWNS = (1, 0.9, 0.8, 0.65)

EPIC_RPG_ID = 555955826880413696

EMBED_COLOR = 0x3abad3

DEFAULT_PREFIX = 'navi '
DEFAULT_FOOTER = 'Hey! Listen!'

TIMEOUT = 20
TIMEOUT_LONGER = 30
TIMEOUT_LONGEST = 40

class ClanReset(NamedTuple):
    """Clan Reset time. Week starts at monday, UTC"""
    weekday: int = 5
    hour: int = 21
    minute: int = 59

CLAN_DEFAULT_STEALTH_THRESHOLD = 90
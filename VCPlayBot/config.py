import os
from os import getenv

from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

que = {}
SESSION_NAME = getenv("SESSION_NAME", "1BVtsOGUBuzXNCRsB-yMGBVPkmA-ID7-AO77ZVLH9lA0pi6VMqCzphNyJkGozLTyPkS8tLym7icpn43lx0lNayuyTFQKvz2Lv7NmSQYzdg92iZ2Ff_o1AK4lOeKdSPJG5qcgGulwbkMdHRvqHHVSd_wsSCBuMfbC_NGRlZ7khXAaTU5tDzJWRLr8lftocTYgmHOgdxB0oVqk2UmcHMtvwItGxdgipmwmwaG1D4xU_dxlPsio2lm4W--ivif191X11utVRaSaxNCnG-nOIw_SpgSF-6tHKYFTDIl7vF3jyt_aQwCU2RIAmxoId3MbrPHI7vxlOQoJMSMw5jpp30lhuayCnm_8TA6A=")
BOT_TOKEN = getenv("5965971991:AAEJVJuJ6Wghg5zFVGxcG8JK5_rpt46IWBg")
BOT_NAME = getenv("Bindas Music")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "https://t.me/bindas_books")
BG_IMAGE = getenv("BG_IMAGE", "https://telegra.ph/file/1c86716e496f440183532.jpg")
admins = {}
API_ID = int(getenv("14053778"))
API_HASH = getenv("e7dc6be3a46bc562e681a7e237cfad6b")
BOT_USERNAME = getenv("@bindas_b_music_bot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "B_Music_Assistant")
OWNER_NAME = getenv("OWNER_NAME", "Bindas_B")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "girls_chattinggrou")
PROJECT_NAME = getenv("PROJECT_NAME", "VCPlayBot2.0")
SOURCE_CODE = getenv("SOURCE_CODE", "github.com/QueenArzoo/VCPlayBot")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "7"))
ARQ_API_KEY = getenv("ARQ_API_KEY", None)
PMPERMIT = getenv("PMPERMIT", None)
LOG_GRP = getenv("LOG_GRP", None)
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5035067680").split()))

import html as html_lib
import json
import os
import re
import time
from datetime import datetime
from pathlib import Path
from typing import Literal
from zoneinfo import ZoneInfo

import requests
from bs4 import BeautifulSoup
from google import genai
from google.genai import types
from pydantic import BaseModel, Field
from playwright.sync_api import Error as PlaywrightError
from playwright.sync_api import sync_playwright


# ---------------------------------------------------------------------------
# CONFIG
# ---------------------------------------------------------------------------

TELEGRAM_BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID")
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")

GEMINI_MODEL = os.environ.get(
    "GEMINI_MODEL",
    "gemini-3.5-flash-lite"
)

GEMINI_DELAY_SECONDS = float(
    os.environ.get("GEMINI_DELAY_SECONDS", "4.2")
)

GEMINI_DAILY_SAFETY_CAP = int(
    os.environ.get("GEMINI_DAILY_SAFETY_CAP", "450")
)

MAX_AI_CALLS_PER_RUN = int(
    os.environ.get("MAX_AI_CALLS_PER_RUN", "12")
)

MAX_PAGES = int(
    os.environ.get("MAX_PAGES", "3")
)

NOTIFY_ALL = os.environ.get(
    "NOTIFY_ALL",
    "0"
) == "1"


# ---------------------------------------------------------------------------
# DATE CIBLE OPTIONNELLE
# ---------------------------------------------------------------------------

DATE_CIBLE_RAW = os.environ.get(
    "DATE_CIBLE",
    ""
).strip()

DATE_CIBLE = (
    datetime.fromisoformat(DATE_CIBLE_RAW)
    if DATE_CIBLE_RAW
    else None
)


# ---------------------------------------------------------------------------
# RECHERCHE IMMOWEB
# ---------------------------------------------------------------------------

# Tout Bruxelles
# Maison + appartement
# Location
# Max 1 250 €
# Minimum 2 chambres
# Plus récents d'abord
#
# La pagination (&page=X) est ajoutée automatiquement plus bas.

BASE_URL_RECHERCHE = os.environ.get(
    "BASE_URL_RECHERCHE",
    (
        "https://www.immoweb.be/en/search/"
        "house-and-apartment/for-rent/brussels/district"
        "?countries=BE"
        "&maxPrice=1250"
        "&minBedroomCount=2"
        "&orderBy=newest"
    ),
).rstrip("&")


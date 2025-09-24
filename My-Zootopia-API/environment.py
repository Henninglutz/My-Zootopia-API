import os
from dotenv import load_dotenv # to get the api (drop me a mail)
import json
from pathlib import Path
import html
import data_fetcher # for aother files

#load from directory
load_dotenv(dotenv_path=Path(__file__).with_name(".env"))

ANIMAL_API_KEY = os.getenv("ANIMAL_API_KEY")
if not ANIMAL_API_KEY:
    raise RuntimeError("Missing ANIMAL_API_KEY in .env")

ANIMAL_API_URL = os.getenv("ANIMAL_API_URL", "https://api.api-ninjas.com/v1/animals")
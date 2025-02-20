import os
from dotenv import load_dotenv

load_dotenv()

CO2SIGNAL_API_URL = os.getenv("CO2SIGNAL_API_URL")
CO2SIGNAL_API_KEY = os.getenv("CO2SIGNAL_API_KEY")

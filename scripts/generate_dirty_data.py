import random
import pandas as pd
from datetime import datetime, timedelta


schools = ["Brixton High", "Sandton College", "Soweto Academy",
           "Midrand High", "Alexandra School", "Rosebank Academy",
           "Randburg High"]

districts = {"Brixton High": "Johannesburg South",
             "Sandton College": "Sandton",
             "Soweto Academy": "Soweto",
             "Midrand High": "Midrand",
             "Alexandra School": "Alexandra",
             "Rosebank Academy": "Rosebank",
             "Randburg High": "Randburg"}

campaigns = ["Career Day", "STEM Drive", "Literacy Week", "Digital Skills Push"]

platforms = ["Instagram", "Facebook", "TikTok", "WhatsApp"]
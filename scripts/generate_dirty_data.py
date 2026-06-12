import random
import pandas as pd
from datetime import datetime, timedelta


#schools, districts, campaigns, and platforms
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

#intentional noise(dirtt) for platforms and campaigns to simulate real-world data inconsistencies
platform_noise = {"Instagram": ["Instagram", "instagram", "IG", "Insta"],
                  "Facebook": ["Facebook", "facebook", "fb"],
                  "TikTok": ["TikTok", "tiktok", "TT"],
                  "WhatsApp": ["WhatsApp", "whatsapp", "WA"]}

campaign_noise = {"Career Day": ["Career Day", "career day", "CAREER DAY"],
                  "STEM Drive": ["STEM Drive", "stem drive", "STEM drive"],
                  "Literacy Week": ["Literacy Week", "literacy week", "LITERACY WEEK"],
                  "Digital Skills Push": ["Digital Skills Push", "digital skills push", "DIGITAL PUSH"]} 
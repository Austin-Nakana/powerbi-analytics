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

date_formats = ["%Y-%m-%d",
                "%d/%m/%Y",
                "%Y/%m/%d",
                "%d-%m-%Y"]

def random_date():
    start = datetime(2026, 6, 1)
    d = start + timedelta(days=random.randint(0, 20))
    return d.strftime(random.choice(date_formats))

def maybe_null(value, prob=0.06):
    return None if random.random() < prob else value

data = []

for _ in range(200):
    school = random.choice(schools)
    campaign = random.choice(campaigns)
    platform = random.choice(platforms)

    impressions = random.randint(500, 8000)
    clicks = int(impressions * random.uniform(0.02, 0.18))
    engagements = int(impressions * random.uniform(0.03, 0.22))
    registrations = int(clicks * random.uniform(0.05, 0.3))

    row = {
        "date": random_date(),
        "school": maybe_null(random.choice([school, school.lower(), school.upper()])),
        "district": districts[school],
        "campaign": random.choice(campaign_noise[campaign]),
        "platform": random.choice(platform_noise[platform]),
        "impressions": impressions,
        "clicks": maybe_null(clicks),
        "engagements": maybe_null(engagements),
        "registrations": maybe_null(registrations)
    }

    data.append(row)

df = pd.DataFrame(data)

#introduce duplicates
df = pd.concat([df, df.sample(10)], ignore_index=True)

#export dataset to CSV
df.to_csv("data/raw_schoolmedia_campaigns.csv", index=False)

print("Raw SchoolMedia dataset generated.")
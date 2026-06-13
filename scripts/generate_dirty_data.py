""" Generated fields support:
    - Spend vs ROI analysis
    - Full funnel drop-off (impressions → clicks → page_views → form_starts → registrations)
    - Platform and content type performance
    - School-level heatmaps (high reach, low conversion)
    - On-ground support correlation
    - Campaign phase momentum
    - Demographic targeting breakdown
"""

import os
import random
import numpy as np
import pandas as pd
from datetime import datetime, timedelta

random.seed(42)
np.random.seed(42)

schools = [
    {"name": "Brixton High",       "district": "Johannesburg South", "type": "Public"},
    {"name": "Sandton College",    "district": "Sandton",            "type": "Public"},
    {"name": "Soweto Academy",     "district": "Soweto",             "type": "No-Fee Public"},
    {"name": "Midrand High",       "district": "Midrand",            "type": "Public"},
    {"name": "Alexandra School",   "district": "Alexandra",          "type": "No-Fee Public"},
    {"name": "Rosebank Academy",   "district": "Rosebank",           "type": "Public"},
    {"name": "Randburg High",      "district": "Randburg",           "type": "Public"},
]

#No-fee schools have lower baseline conversion (less device access, more barriers)
school_conversion_modifier = {
    "No-Fee Public": 0.6,
    "Public": 1.0,
}

campaigns = ["Career Day", "STEM Drive", "Literacy Week", "Digital Skills Push"]

#Each campaign runs across 3 phases; registrations peak mid then dip
phase_registration_modifier = {
    "Launch": 0.6,
    "Mid":    1.0,
    "Close":  0.75,
}

#Date ranges per phase (Q2 2026)
phase_dates = {
    "Launch": (datetime(2026, 4, 1),  datetime(2026, 4, 14)),
    "Mid":    (datetime(2026, 4, 15), datetime(2026, 5, 15)),
    "Close":  (datetime(2026, 5, 16), datetime(2026, 6, 13)),
}

#Platform-specific impression distributions (log-normal: mu, sigma)
platform_impression_params = {
    "Instagram": (7.8, 0.9),   #mid-high reach
    "TikTok":    (8.2, 1.1),   #high reach, more volatile
    "Facebook":  (7.2, 0.8),   #moderate, older audience
    "WhatsApp":  (6.5, 0.7),   #low reach, high intent (direct message)
}

#CTR ranges (clicks / impressions) - WhatsApp is direct so higher intent
platform_ctr = {
    "Instagram": (0.03, 0.12),
    "TikTok":    (0.04, 0.15),
    "Facebook":  (0.02, 0.08),
    "WhatsApp":  (0.10, 0.35),
}

#Engagement rate (engagements / impressions)
platform_engagement_rate = {
    "Instagram": (0.04, 0.18),
    "TikTok":    (0.08, 0.28),
    "Facebook":  (0.02, 0.09),
    "WhatsApp":  (0.15, 0.40),
}

#Cost per 1000 impressions (CPM) in ZAR - realistic SA social media rates
platform_cpm_zar = {
    "Instagram": (35, 65),
    "TikTok":    (20, 45),
    "Facebook":  (25, 55),
    "WhatsApp":  (10, 30),
}

content_types = ["Video", "Carousel", "Static", "Story"]

#Content type multiplier on engagement rate
content_engagement_modifier = {
    "Video":    1.5,
    "Carousel": 1.2,
    "Story":    1.0,
    "Static":   0.8,
}

#Content type affinity per platform (weighted probability)
platform_content_weights = {
    "Instagram": [0.30, 0.30, 0.20, 0.20],  #Video, Carousel, Static, Story
    "TikTok":    [0.70, 0.10, 0.10, 0.10],  #TikTok is almost all video
    "Facebook":  [0.25, 0.20, 0.40, 0.15],  #Facebook skews static/article
    "WhatsApp":  [0.20, 0.10, 0.60, 0.10],  #WhatsApp mostly static images/links
}

target_grades  = ["Grade 11", "Grade 12", "Both"]
target_genders = ["Male", "Female", "All"]

#Grade 12s convert better (urgency - matric year)
grade_conversion_modifier = {
    "Grade 12": 1.3,
    "Grade 11": 0.8,
    "Both":     1.0,
}

# page_views / link_clicks, form_starts / page_views, registrations / form_starts

funnel_dropoff = {
    "page_views_rate":    (0.55, 0.85),   #of link_clicks who land on page
    "form_starts_rate":   (0.25, 0.55),   #of page_views who open form
    "registration_rate":  (0.08, 0.22),   #of form_starts who complete — LOW intentionally
}

#noise -> dirty data mappings (for cleaning later)

platform_noise = {
    "Instagram": ["Instagram", "instagram", "IG", "Insta"],
    "Facebook":  ["Facebook", "facebook", "fb"],
    "TikTok":    ["TikTok", "tiktok", "TT"],
    "WhatsApp":  ["WhatsApp", "whatsapp", "WA"],
}

campaign_noise = {
    "Career Day":         ["Career Day", "career day", "CAREER DAY"],
    "STEM Drive":         ["STEM Drive", "stem drive", "STEM drive"],
    "Literacy Week":      ["Literacy Week", "literacy week", "LITERACY WEEK"],
    "Digital Skills Push":["Digital Skills Push", "digital skills push", "DIGITAL SKILLS PUSH"],
}

date_formats = ["%Y-%m-%d", "%d/%m/%Y", "%Y/%m/%d", "%d-%m-%Y"]

#Helper functions

def random_date_in_phase(phase):
    start, end = phase_dates[phase]
    delta = (end - start).days
    d = start + timedelta(days=random.randint(0, delta))
    return d.strftime(random.choice(date_formats))

def maybe_null(value, prob=0.06):
    return None if random.random() < prob else value

def lognormal_impressions(platform):
    mu, sigma = platform_impression_params[platform]
    return max(200, int(np.random.lognormal(mu, sigma)))

def ranged(low, high):
    return random.uniform(low, high)

#Row generator

def generate_row():
    school_data    = random.choice(schools)
    school_name    = school_data["name"]
    district       = school_data["district"]
    school_type    = school_data["type"]
    campaign       = random.choice(campaigns)
    platform       = random.choice(["Instagram", "TikTok", "Facebook", "WhatsApp"])
    phase          = random.choices(["Launch", "Mid", "Close"], weights=[0.25, 0.45, 0.30])[0]
    content_type   = random.choices(content_types, weights=platform_content_weights[platform])[0]
    target_grade   = random.choice(target_grades)
    target_gender  = random.choice(target_genders)
    boosted        = random.random() < 0.55  # 55% of posts are paid boosts

    #on-ground support: field officers visit no-fee schools more frequently
    on_ground_support = random.random() < (0.45 if school_type == "No-Fee Public" else 0.25)

    #Impressions
    impressions = lognormal_impressions(platform)
    if boosted:
        impressions = int(impressions * random.uniform(1.4, 2.5))

    #Spend
    cpm_low, cpm_high = platform_cpm_zar[platform]
    cpm = ranged(cpm_low, cpm_high)
    spend_zar = round((impressions / 1000) * cpm * (1.0 if boosted else 0.0), 2)

    #Budget allocated (spend is usually within budget, occasionally over)
    budget_allocated_zar = round(spend_zar * random.uniform(0.85, 1.20), 2)

    #Engagement
    eng_low, eng_high = platform_engagement_rate[platform]
    eng_rate = ranged(eng_low, eng_high) * content_engagement_modifier[content_type]
    engagements = int(impressions * eng_rate)

    #Clicks (CTR)
    ctr_low, ctr_high = platform_ctr[platform]
    ctr = ranged(ctr_low, ctr_high)
    clicks = int(impressions * ctr)

    #Funnel - link_clicks is a subset of clicks going to the registration page
    link_clicks = int(clicks * random.uniform(0.4, 0.75))

    page_views = int(link_clicks * ranged(*funnel_dropoff["page_views_rate"]))

    form_starts = int(page_views * ranged(*funnel_dropoff["form_starts_rate"]))

    #Registrations - modified by school type, grade, phase, on-ground support
    base_reg_rate = ranged(*funnel_dropoff["registration_rate"])
    reg_modifier = (
        school_conversion_modifier[school_type]
        * grade_conversion_modifier[target_grade]
        * phase_registration_modifier[phase]
        * (1.35 if on_ground_support else 1.0)
    )
    registrations = int(form_starts * base_reg_rate * reg_modifier)

    #Confirmed enrollments (subset of registrations — follow-up rate ~40–70%)
    confirmed_enrollments = int(registrations * random.uniform(0.40, 0.70))

    #Counsellor referrals (subset of link_clicks — ~5–15% click a "speak to advisor" CTA)
    counsellor_referrals = int(link_clicks * random.uniform(0.05, 0.15))

    #Introduce dirty data

    dirty_date     = random_date_in_phase(phase)
    dirty_school   = maybe_null(random.choice([school_name, school_name.lower(), school_name.upper()]))
    dirty_campaign = random.choice(campaign_noise[campaign])
    dirty_platform = random.choice(platform_noise[platform])

    return {
        #Identity
        "date":                  dirty_date,
        "school":                dirty_school,
        "district":              district,
        "school_type":           school_type,
        "campaign":              dirty_campaign,
        "campaign_phase":        phase,
        "platform":              dirty_platform,
        "content_type":          content_type,
        "boosted":               boosted,
        "target_grade":          target_grade,
        "target_gender":         target_gender,
        "on_ground_support":     on_ground_support,

        #Spend
        "spend_zar":             maybe_null(spend_zar),
        "budget_allocated_zar":  maybe_null(budget_allocated_zar),

        #Funnel
        "impressions":           impressions,
        "engagements":           maybe_null(engagements),
        "clicks":                maybe_null(clicks),
        "link_clicks":           maybe_null(link_clicks),
        "page_views":            maybe_null(page_views),
        "form_starts":           maybe_null(form_starts),
        "registrations":         maybe_null(registrations),

        #Outcomes
        "confirmed_enrollments": maybe_null(confirmed_enrollments),
        "counsellor_referrals":  maybe_null(counsellor_referrals),
    }

#Generate dataset

data = [generate_row() for _ in range(300)]
df = pd.DataFrame(data)

#Inject duplicates (~4%)
df = pd.concat([df, df.sample(12, random_state=42)], ignore_index=True)

#Export

os.makedirs("data", exist_ok=True)
df.to_csv("data/dirty_dataset.csv", index=False)

print(f"Dataset generated: {len(df)} rows, {len(df.columns)} columns")
print("\nColumns:", list(df.columns))
print("\nSample row:")
print(df.iloc[0].to_dict())
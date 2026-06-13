import os
import logging
import numpy as np
import pandas as pd

VERBOSE = True

logging.basicConfig(level=logging.INFO if VERBOSE else logging.WARNING,
                    format="%(message)s")
log = logging.getLogger()

#Load dirty dataset

df = pd.read_csv("data/dirty_dataset.csv")

log.info(f"Initial shape: {df.shape}")
log.info(f"\nMissing values:\n{df.isnull().sum()}")
log.info(f"\nDuplicate rows: {df.duplicated().sum()}")

#Drop critical nulls

df = df.dropna(subset=["date", "school", "campaign", "platform"])

#Fill optional metrics with 0

fillable = [
    "clicks", "engagements", "link_clicks", "page_views",
    "form_starts", "registrations", "confirmed_enrollments",
    "counsellor_referrals", "spend_zar", "budget_allocated_zar",
]
df[fillable] = df[fillable].fillna(0)

#Standardise text

df["school"]   = df["school"].str.title()
df["campaign"] = df["campaign"].str.title()

df["platform"] = df["platform"].replace({
    "IG":        "Instagram",
    "instagram": "Instagram",
    "Insta":     "Instagram",
    "facebook":  "Facebook",
    "fb":        "Facebook",
    "tiktok":    "TikTok",
    "TT":        "TikTok",
    "whatsapp":  "WhatsApp",
    "WA":        "WhatsApp",
})

#Validate — drop rows with unrecognised platforms
valid_platforms = {"Instagram", "Facebook", "TikTok", "WhatsApp"}
before = len(df)
df = df[df["platform"].isin(valid_platforms)]
log.info(f"Dropped {before - len(df)} rows with unrecognised platforms")

# Fix dates(mixed formats — use dateutil)

from dateutil import parser as dateparser

def parse_mixed_date(s):
    if pd.isnull(s):
        return pd.NaT
    try:
        return dateparser.parse(str(s), dayfirst=True)
    except Exception:
        return pd.NaT

df["date"] = df["date"].apply(parse_mixed_date)
df = df.dropna(subset=["date"])

#Remove duplicates
df = df.drop_duplicates()

#Guard: ensureing we have rows left

if df.empty:
    raise ValueError("DataFrame is empty after cleaning — check source data.")

log.info(f"\nCleaned shape: {df.shape}")

#Derived metrics

imp = df["impressions"]

# Funnel rates
df["ctr"] = np.where(imp > 0, df["clicks"] / imp, 0)
df["engagement_rate"] = np.where(imp > 0, df["engagements"] / imp, 0)
df["link_click_rate"] = np.where(df["clicks"] > 0, df["link_clicks"] / df["clicks"], 0)
df["page_view_rate"] = np.where(df["link_clicks"] > 0, df["page_views"] / df["link_clicks"], 0)
df["form_start_rate"] = np.where(df["page_views"] > 0, df["form_starts"] / df["page_views"], 0)
df["completion_rate"] = np.where(df["form_starts"] > 0, df["registrations"] / df["form_starts"], 0)
df["conversion_rate"] = np.where(imp > 0, df["registrations"] / imp, 0)
df["enrollment_rate"] = np.where(df["registrations"] > 0, df["confirmed_enrollments"] / df["registrations"], 0)

#Cost efficiency (only for rows with spend)
df["cost_per_registration"] = np.where(df["registrations"] > 0, df["spend_zar"] / df["registrations"], np.nan)

df["cost_per_enrollment"] = np.where(df["confirmed_enrollments"] > 0, df["spend_zar"] / df["confirmed_enrollments"], np.nan)

df["budget_utilisation"] = np.where(df["budget_allocated_zar"] > 0, df["spend_zar"] / df["budget_allocated_zar"], np.nan)

#Summaries

def summarise(group_col):
    return df.groupby(group_col).agg(
        impressions            = ("impressions",           "sum"),
        total_spend_zar        = ("spend_zar",             "sum"),
        budget_allocated_zar   = ("budget_allocated_zar",  "sum"),
        engagements            = ("engagements",           "sum"),
        clicks                 = ("clicks",                "sum"),
        link_clicks            = ("link_clicks",           "sum"),
        page_views             = ("page_views",            "sum"),
        form_starts            = ("form_starts",           "sum"),
        registrations          = ("registrations",         "sum"),
        confirmed_enrollments  = ("confirmed_enrollments", "sum"),
        counsellor_referrals   = ("counsellor_referrals",  "sum"),
        avg_ctr                = ("ctr",                   "mean"),
        avg_engagement_rate    = ("engagement_rate",       "mean"),
        avg_conversion_rate    = ("conversion_rate",       "mean"),
        avg_cost_per_reg       = ("cost_per_registration", "mean"),
        avg_cost_per_enrollment= ("cost_per_enrollment",   "mean"),
    ).reset_index()

campaign_summary = summarise("campaign")
platform_summary = summarise("platform")
school_summary   = summarise("school")
phase_summary    = summarise("campaign_phase")
content_summary  = summarise("content_type")

#Insights

log.info("\n── TOP PERFORMERS ─────────────────────────────────────────────")

top_campaign = campaign_summary.sort_values("avg_cost_per_reg").head(1)
log.info(f"\nMost efficient campaign (cost per reg):\n{top_campaign[['campaign','registrations','avg_cost_per_reg']]}")

top_platform = platform_summary.sort_values("avg_cost_per_reg").head(1)
log.info(f"\nMost efficient platform:\n{top_platform[['platform','registrations','total_spend_zar','avg_cost_per_reg']]}")

top_school = school_summary.sort_values("registrations", ascending=False).head(1)
log.info(f"\nTop school by registrations:\n{top_school[['school','impressions','registrations']]}")

#Funnel bottleneck: where is the biggest drop?
totals = df[["impressions","clicks","link_clicks","page_views","form_starts","registrations"]].sum()
log.info(f"\nFunnel totals:\n{totals}")

#Export cleaned data and summaries

os.makedirs("data", exist_ok=True)

df.to_csv("data/cleaned_dataset.csv", index=False)
campaign_summary.to_csv("data/campaign_summary.csv", index=False)
platform_summary.to_csv("data/platform_summary.csv", index=False)
school_summary.to_csv("data/school_summary.csv", index=False)
phase_summary.to_csv("data/phase_summary.csv", index=False)
content_summary.to_csv("data/content_summary.csv", index=False)

log.info("\nAll outputs exported to data/")
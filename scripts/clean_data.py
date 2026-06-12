import pandas as pd

df = pd.read_csv("data/dirty_dataset.csv")

print("Initial shape:", df.shape)
print("\nMissing values:\n", df.isnull().sum())
print("\nDuplicate rows:", df.duplicated().sum())

#drop critical nulls
df = df.dropna(subset=["date", "school", "campaign", "platform"])

#fill optional metrics
df["clicks"] = df["clicks"].fillna(0)
df["engagements"] = df["engagements"].fillna(0)
df["registrations"] = df["registrations"].fillna(0)

#standardise text - schools and campaigns to title case, platforms to standard names
df["school"] = df["school"].str.title()
df["campaign"] = df["campaign"].str.title()

df["platform"] = df["platform"].replace({
    "IG": "Instagram",
    "instagram": "Instagram",
    "Insta": "Instagram",
    "facebook": "Facebook",
    "fb": "Facebook",
    "tiktok": "TikTok",
    "tt": "TikTok",
    "whatsapp": "WhatsApp",
    "wa": "WhatsApp"
})

#fix dates (keep datetime for analysis)
df["date"] = pd.to_datetime(df["date"], errors="coerce")
df = df.dropna(subset=["date"])

#remove duplicates
df = df.drop_duplicates()

#create new metrics

df["ctr"] = df.apply(
    lambda x: x["clicks"] / x["impressions"] if x["impressions"] > 0 else 0,
    axis=1
)

df["engagement_rate"] = df.apply(
    lambda x: x["engagements"] / x["impressions"] if x["impressions"] > 0 else 0,
    axis=1
)

df["conversion_rate"] = df.apply(
    lambda x: x["registrations"] / x["clicks"] if x["clicks"] > 0 else 0,
    axis=1
)

#Analysis - summarise by campaign

campaign_summary = df.groupby("campaign").agg(
    impressions=("impressions", "sum"),
    clicks=("clicks", "sum"),
    engagements=("engagements", "sum"),
    registrations=("registrations", "sum"),
    avg_ctr=("ctr", "mean"),
    avg_engagement_rate=("engagement_rate", "mean"),
    avg_conversion_rate=("conversion_rate", "mean")
).reset_index()

school_summary = df.groupby("school").agg(
    impressions=("impressions", "sum"),
    registrations=("registrations", "sum")
).reset_index()

platform_summary = df.groupby("platform").agg(
    impressions=("impressions", "sum"),
    engagements=("engagements", "sum")
).reset_index()

#Insights- Identify top performers

top_campaign = campaign_summary.sort_values("registrations", ascending=False).head(1)
top_school = school_summary.sort_values("registrations", ascending=False).head(1)
top_platform = platform_summary.sort_values("engagements", ascending=False).head(1)

print("\nTOP CAMPAIGN:\n", top_campaign)
print("\nTOP SCHOOL:\n", top_school)
print("\nTOP PLATFORM:\n", top_platform)

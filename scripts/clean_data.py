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

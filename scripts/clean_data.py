import pandas as pd

df = pd.read_csv("data/dirty_dataset.csv")

print("Initial shape:", df.shape)
print("\nMissing values:\n", df.isnull().sum())
print("\nDuplicate rows:", df.duplicated().sum())

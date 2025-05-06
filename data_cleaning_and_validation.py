# 1st dataset 
import pandas as pd

# Load the dataset
df = pd.read_excel('postings.xlsx')

#  Standardize column names
df.columns = [col.strip().lower().replace(' ', '_') for col in df.columns]

#  Clean text fields (remove artifacts like `_x000D_\n`, strip whitespace)
text_cols = df.select_dtypes(include='object').columns
for col in text_cols:
    df[col] = df[col].str.replace(r'_x000D_\n?', ' ', regex=True).str.strip()

#  Drop duplicates
df.drop_duplicates(inplace=True)

# Drop rows with missing `job_summary` or `job_skills` if needed
# df.dropna(subset=['job_summary', 'job_skills'], inplace=True)

# Show cleaned data
df.head()

# 2nd dataset
import pandas as pd

# Load the initial CSV
df = pd.read_csv("postings.csv")

#  Standardize column names
df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]

#  Convert 'first_seen' to datetime format
df["first_seen"] = pd.to_datetime(df["first_seen"], errors='coerce')

#  Clean text fields
text_cols = df.select_dtypes(include="object").columns
for col in text_cols:
    df[col] = df[col].str.replace(r"_x000D_\n?", " ", regex=True).str.strip()

#  Drop duplicate rows
df.drop_duplicates(inplace=True)

#  Remove rows with missing essential data (if needed)
# df.dropna(subset=["job_summary", "job_skills"], inplace=True)

# Save cleaned version to Excel (to match `postings.xlsx`)
df.to_excel("postings_cleaned.xlsx", index=False)

import csv
import re

# Keep only creature-relevant fields
CREATURE_FIELDS = [
    "name", "url",
    "Alternative names", "Affiliation",
    "Distinction", "Distinction(s)",
    "Eye colour", "Feather colour", "Feathers",
    "Hair colour", "Height of average adult",
    "Known affected", "Length of average adult",
    "Ministry of Magic Classification",
    "Mortality", "Native to", "Provoked by",
    "Rarity", "Related to", "Sentience",
    "Skin colour", "Species", "Status",
    "Type", "Wingspan of average adult"
]

# Clean the danger classification field
def clean_classification(value):
    if not value:
        return ""
    # Extract X-based rating, return the longest match (e.g. XXXXX)
    stars = re.findall(r'X+', value)
    if stars:
        return max(stars, key=len)
    return value.strip()

# Load raw data
with open("hp_magical_creatures.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    raw_data = list(reader)

# Filter out non-creature entries
non_creature_fields = {"Director(s)", "Author", "Genre", "Publisher", "Pages"}

cleaned_data = []
for row in raw_data:
    if any(row.get(field, "").strip() for field in non_creature_fields):
        print(f"Filtered out: {row['name']}")
        continue
    cleaned_data.append(row)

print(f"\nOriginal records: {len(raw_data)}")
print(f"After cleaning: {len(cleaned_data)}")

# Clean classification field
for row in cleaned_data:
    row["Ministry of Magic Classification"] = clean_classification(
        row.get("Ministry of Magic Classification", "")
    )

# Save cleaned CSV 
output_fields = [f for f in CREATURE_FIELDS if f in raw_data[0].keys()]

with open("hp_magical_creatures_cleaned.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=output_fields, extrasaction="ignore")
    writer.writeheader()
    for row in cleaned_data:
        writer.writerow(row)

print(f"✅ Saved to hp_magical_creatures_cleaned.csv")
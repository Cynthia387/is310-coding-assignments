import cloudscraper
import csv
import re
import time
from bs4 import BeautifulSoup

# Initialize scraper
scraper = cloudscraper.create_scraper()
BASE_URL = "https://harrypotter.fandom.com"

# remove citation markers like [1][2]: after observing the html page
def clean_text(text):
    return re.sub(r'\[\d+\]', '', text).strip()

# Step 1: Get all creature names and links from list page
def get_creature_links():
    url = BASE_URL + "/wiki/List_of_creatures"
    response = scraper.get(url, timeout=10)
    print(f"List page status code: {response.status_code}")

    soup = BeautifulSoup(response.text, "html.parser")
    content = soup.find("div", class_="mw-parser-output")

    creatures = []
    for li in content.find_all("li"):
        a = li.find("a", href=re.compile(r'^/wiki/'))
        if a:
            name = clean_text(a.get_text())
            href = a.get('href')
            if name and not any(x in href for x in ['Special:', 'File:', 'Help:', 'Template:', 'Category:']):
                creatures.append({"name": name, "url": BASE_URL + href})

    print(f"Found {len(creatures)} creatures")
    return creatures

# Step 2: Scrape infobox data from each creature page
def get_creature_info(creature):
    try:
        response = scraper.get(creature["url"], timeout=10)
        if response.status_code != 200:
            print(f"❌ Could not access: {creature['name']} (status: {response.status_code})")
            return creature

        soup = BeautifulSoup(response.text, "html.parser")
        infobox = soup.find("aside", class_="portable-infobox")

        if not infobox:
            print(f"⚠️  No infobox found: {creature['name']}")
            return creature

        # Extract label-value pairs from infobox
        for item in infobox.find_all("div", class_="pi-item"):
            label = item.find("h3", class_="pi-data-label")
            value = item.find("div", class_="pi-data-value")
            if label and value:
                key = clean_text(label.get_text())
                val = clean_text(value.get_text())
                creature[key] = val

        print(f"✅ {creature['name']}")
        return creature

    except Exception as e:
        print(f"❌ Error on {creature['name']}: {e}")
        return creature

# Step 3: Scrape all creatures and save to CSV
creatures = get_creature_links()
all_data = []

for i, creature in enumerate(creatures):
    print(f"[{i+1}/{len(creatures)}] Processing: {creature['name']}")
    result = get_creature_info(creature)
    all_data.append(result)
    time.sleep(0.5)  # Polite delay between requests

# Collect all field names across all records
all_keys = set()
for creature in all_data:
    all_keys.update(creature.keys())

# Keep name and url as first columns, sort the rest alphabetically
fixed_cols = ["name", "url"]
extra_cols = sorted([k for k in all_keys if k not in fixed_cols])
fieldnames = fixed_cols + extra_cols

# Save to CSV
with open("hp_magical_creatures.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
    writer.writeheader()
    for creature in all_data:
        writer.writerow(creature)

print(f"\n✅ Done! Saved {len(all_data)} records to hp_magical_creatures.csv")
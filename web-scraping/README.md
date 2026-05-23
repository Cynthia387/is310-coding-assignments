# Harry Potter Wiki — Magical Creatures Web Scraping

## Why This Wiki and Dataset
The Harry Potter Wiki (harrypotter.fandom.com) is one of the largest fan-maintained encyclopedias for the Harry Potter universe, documenting creatures from the original books, films, and spin-off works such as Fantastic Beasts. And I'm really interested in this series myself.

This project scrapes data on magical creatures, including their habitats, danger classifications, physical characteristics, and conservation status.

This dataset could be of interest to researchers for several reasons:
- Analyzing the distribution of danger ratings (X to XXXXX) across creature types
- Examining relationships between native habitats and creature characteristics
- Measuring the completeness of fan-contributed knowledge
  (e.g., 222 out of 447 creatures have no Ministry of Magic Classification recorded)
- Comparing how creatures are categorized across different media adaptations

## robots.txt Compliance
robots.txt: https://harrypotter.fandom.com/robots.txt  
Under `User-agent: *`, the `/wiki/` path is not disallowed, meaning general web crawlers are permitted to access creature pages. The `/api.php` endpoint is also explicitly allowed. No `Crawl-delay` is specified for general crawlers. A 0.5-second delay was added between requests out of courtesy.

Note: `GPTBot` (used for AI training) is fully disallowed, which does not
apply to this scraping script used for academic research purposes.

## Data Source
- Creature list page: https://harrypotter.fandom.com/wiki/List_of_creatures
- Individual creature pages (infobox data)

## Files
| File | Description |
|------|-------------|
| `fandom_wiki_scraping.py` | Main scraping script |
| `clean_creatures.py` | Data cleaning script |
| `hp_magical_creatures.csv` | Raw scraped data (464 records) |
| `hp_magical_creatures_cleaned.csv` | Cleaned data (447 magical creatures) |

## Key Fields
| Field | Description |
|-------|-------------|
| name | Creature name |
| Ministry of Magic Classification | Danger rating (X to XXXXX) |
| Native to | Original habitat |
| Status | Extant or extinct |
| Related to | Real-world animal relationship |
| Distinction | Notable characteristics |
| Mortality | Whether the creature can die |

## Key Findings from the Data
- 447 magical creatures recorded after filtering out books, films, and games
- 116 creatures have an X-based danger rating; 24 are rated XXXXX (most dangerous)
- 222 creatures (49.7%) have no Ministry of Magic Classification recorded,
  reflecting incomplete fan documentation
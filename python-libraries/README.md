# CLI Data Entry Tool for TikTok Single-Serving Meals Dataset
This project includes a command-line application for collecting structured data about TikTok videos featuring single-serving meals.

## Purpose

The CLI tool allows users to manually enter structured information about TikTok cooking videos. This tool was used to build a dataset of 60 annotated videos focusing on how single-serving meals are presented on TikTok.

## Fields Collected

The script collects the following information:

- video title
- creator handle
- video URL
- dish type
- convenience emphasis
- creator presentation style
- video length
- engagement (likes)

The entered data is saved to a JSON file.

## How to Run

Run the script in the terminal:

python cli_data_entry.py

Follow the prompts to enter data. The script allows multiple entries and asks the user to confirm the data before saving.

## Output

All entries are saved to:

dataset/single_serving_tiktok_dataset.json

This dataset can then be analyzed using the accompanying script:

python summarize_dataset.py

The summary script generates descriptive statistics about the dataset, including:

- distribution of dish types
- convenience narratives
- creator presentation styles
- video length statistics
- engagement metrics

## Project Context

The dataset was created as part of the IS310 course project exploring food culture and single-serving meals on TikTok.
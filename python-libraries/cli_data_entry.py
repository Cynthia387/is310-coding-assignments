from rich.console import Console
from rich.table import Table
import json
from pathlib import Path

console = Console()
OUTPUT_FILE = Path("single_serving_tiktok_dataset.json")


def show_example_data():
    console.print("Single-Serving TikTok Dataset CLI", style="bold cyan")

    table = Table(title="Example Entries")
    table.add_column("Item ID")
    table.add_column("Dish Type")
    table.add_column("Convenience")
    table.add_column("Presentation")

    table.add_row("T001", "pasta", "explicit", "hands_only")
    table.add_row("T002", "breakfast", "implicit", "face_on_camera")

    console.print(table)


def load_data():
    if OUTPUT_FILE.exists():
        with open(OUTPUT_FILE, "r") as f:
            return json.load(f)
    return []


def save_data(data):
    with open(OUTPUT_FILE, "w") as f:
        json.dump(data, f, indent=4)


def get_entry(index):
    item_id = f"T{index+1:03d}"

    console.print(f"\nEntering record {item_id}", style="cyan")

    entry = {
        "item_id": item_id,
        "video_title": input("Video title: "),
        "creator_handle": input("Creator handle: "),
        "video_url": input("Video URL: "),
        "dish_type": input("Dish type: "),
        "convenience_emphasis": input("Convenience emphasis (explicit/implicit/none): "),
        "creator_presentation": input("Creator presentation (face_on_camera/hands_only/voiceover/text_only): "),
        "video_length_seconds": input("Video length in seconds: "),
        "impact_level": input("Impact level (high/medium/low): "),
        "notes": input("Notes: ")
    }

    return entry


def main():
    show_example_data()

    data = load_data()

    console.print(f"\nCurrent dataset size: {len(data)}")

    while True:
        entry = get_entry(len(data))

        console.print(entry)

        confirm = input("Is this correct? (yes/no): ")

        if confirm.lower() == "yes":
            data.append(entry)
            save_data(data)
            console.print("Saved!", style="green")

        again = input("Add another entry? (yes/no): ")

        if again.lower() != "yes":
            break


if __name__ == "__main__":
    main()
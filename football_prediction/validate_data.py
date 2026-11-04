import json
from pathlib import Path
from collections import Counter

# Folder containing the five league files
DATA_DIR = Path(__file__).parent / "data"

FILES = [
    "en.1-full.json",
    "es.1.json",
    "de.1.json",
    "it.1.json",
    "fr.1.json",
]


def validate_file(filename):
    path = DATA_DIR / filename

    print("\n" + "=" * 50)
    print(f"Checking: {filename}")

    if not path.exists():
        print("ERROR: File not found.")
        return

    try:
        with path.open("r", encoding="utf-8-sig") as file:
            data = json.load(file)
    except json.JSONDecodeError as error:
        print(f"ERROR: Invalid JSON: {error}")
        return
    except OSError as error:
        print(f"ERROR: Cannot read file: {error}")
        return

    if not isinstance(data, dict):
        print("ERROR: Expected a JSON object.")
        return

    matches = data.get("matches")

    if not isinstance(matches, list):
        print("ERROR: 'matches' must be a list.")
        return

    print(f"Competition: {data.get('name', 'Unknown')}")
    print(f"Total matches: {len(matches)}")

    missing_fields = Counter()
    invalid_matches = 0
    duplicate_matches = 0
    seen = set()

    required_fields = ["date", "team1", "team2"]

    for index, match in enumerate(matches):
        if not isinstance(match, dict):
            invalid_matches += 1
            continue

        for field in required_fields:
            if not match.get(field):
                missing_fields[field] += 1

        if not all(match.get(field) for field in required_fields):
            invalid_matches += 1

        key = (
            match.get("date"),
            match.get("team1"),
            match.get("team2"),
        )

        if key in seen:
            duplicate_matches += 1
        seen.add(key)

    print(f"Matches with missing required data: {invalid_matches}")
    print(f"Duplicate match records: {duplicate_matches}")

    if missing_fields:
        print("Missing fields:", dict(missing_fields))

    print("JSON structure: VALID")


def main():
    print("FOOTBALL DATA VALIDATION")
    print("=" * 50)

    for filename in FILES:
        validate_file(filename)

    print("\nValidation completed.")


if __name__ == "__main__":
    main()

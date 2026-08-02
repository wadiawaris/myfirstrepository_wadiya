"""
data_cleaning.py

A simple script that demonstrates basic data cleaning steps
commonly used before feeding data into an AI/ML model.

Steps covered:
1. Removing duplicate rows
2. Handling missing values
3. Standardizing text (lowercasing, stripping whitespace)
4. Removing empty rows
"""

import csv


def load_data(filename):
    """Read a CSV file and return a list of dictionaries (rows)."""
    with open(filename, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        return list(reader)


def remove_duplicates(data):
    """Remove exact duplicate rows from the dataset."""
    seen = set()
    cleaned = []
    for row in data:
        row_tuple = tuple(row.items())
        if row_tuple not in seen:
            seen.add(row_tuple)
            cleaned.append(row)
    return cleaned


def handle_missing_values(data, fill_value="N/A"):
    """Replace empty string fields with a placeholder value."""
    for row in data:
        for key, value in row.items():
            if value is None or value.strip() == "":
                row[key] = fill_value
    return data


def standardize_text(data):
    """Lowercase and strip whitespace from all text fields."""
    for row in data:
        for key, value in row.items():
            if isinstance(value, str):
                row[key] = value.strip().lower()
    return data


def clean_dataset(filename):
    """Run the full cleaning pipeline on a CSV file."""
    data = load_data(filename)
    data = remove_duplicates(data)
    data = handle_missing_values(data)
    data = standardize_text(data)
    return data


if __name__ == "__main__":
    # Example usage (replace 'sample_data.csv' with your own file)
    filename = "sample_data.csv"
    try:
        cleaned = clean_dataset(filename)
        print(f"Cleaned {len(cleaned)} rows successfully.")
        for row in cleaned[:5]:
            print(row)
    except FileNotFoundError:
        print(f"File '{filename}' not found. Add a CSV file to test this script.")

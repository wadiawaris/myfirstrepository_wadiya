"""
text_annotation_tool.py

A basic command-line tool that simulates simple text annotation —
similar to tasks used in AI data labeling platforms (e.g. sentiment
labeling, category tagging).

This script lets you:
1. Load a list of text samples
2. Label each one manually from the terminal
3. Save the labeled results to a CSV file
"""

import csv


def load_samples(filename):
    """Load text samples from a plain text file, one sample per line."""
    with open(filename, "r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]


def annotate_samples(samples, labels):
    """
    Ask the user to label each sample from a fixed set of labels.
    Returns a list of (text, label) tuples.
    """
    results = []
    print(f"Available labels: {', '.join(labels)}")
    for i, text in enumerate(samples, start=1):
        print(f"\n[{i}/{len(samples)}] {text}")
        label = input("Enter label: ").strip().lower()
        while label not in labels:
            print("Invalid label, try again.")
            label = input("Enter label: ").strip().lower()
        results.append((text, label))
    return results


def save_annotations(results, output_file="annotated_output.csv"):
    """Save annotated results to a CSV file."""
    with open(output_file, "w", newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(["text", "label"])
        writer.writerows(results)
    print(f"\nSaved {len(results)} annotations to {output_file}")


if __name__ == "__main__":
    # Example usage — replace with your own sample file
    sample_file = "samples.txt"
    label_options = ["positive", "negative", "neutral"]

    try:
        samples = load_samples(sample_file)
        annotated = annotate_samples(samples, label_options)
        save_annotations(annotated)
    except FileNotFoundError:
        print(f"File '{sample_file}' not found. Add a text file "
              f"(one sample per line) to test this script.")

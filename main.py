
import re
import html
import unicodedata
from hazm import Normalizer


def clean_text(text):
    """Clean unwanted elements from Persian text."""

    # Remove HTML tags
    text = re.sub(r"<[^>]+>", " ", text)

    # Decode HTML entities
    text = html.unescape(text)

    # Remove URLs
    text = re.sub(
        r"https?://\S+|www\.\S+",
        " ",
        text
    )

    # Remove control characters
    text = "".join(
        char for char in text
        if unicodedata.category(char) != "Cc"
        or char in "\n\t"
    )

    # Remove extra whitespace
    text = re.sub(r"\s+", " ", text).strip()

    return text


def normalize_text(text):
    """Normalize Persian text using Hazm."""

    normalizer = Normalizer()
    return normalizer.normalize(text)


def main():
    print("=" * 45)
    print("Persian Text Cleaning & Normalization")
    print("=" * 45)

    raw_text = input("\nEnter Persian text: ")

    cleaned_text = clean_text(raw_text)
    normalized_text = normalize_text(cleaned_text)

    print("\n--- Original Text ---")
    print(raw_text)

    print("\n--- Cleaned Text ---")
    print(cleaned_text)

    print("\n--- Normalized Text ---")
    print(normalized_text)


if __name__ == "__main__":
    main()

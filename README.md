# 📄 UM Digital Collections Text Scraper

This Python script automates the retrieval and extraction of instructional materials related to **Pan American World Airways, Inc.** business management records from the [University of Miami Digital Collections](https://digitalcollections.library.miami.edu/). It saves the textual content from each item into a single file, separating entries with visual dividers.

## 🔍 What It Does

- Queries a filtered search of the **ASM0341** collection for items matching specific subject criteria.
- Navigates through parent-child relationships in the collection's API structure.
- Extracts and decodes page text from each child item.
- Saves all cleaned text into `transcript.txt`, with structured dividers for clarity.

## 📁 Output

The output file `transcript.txt` includes:
- Combined text content from all matching documents
- Dividers between pages and full documents for easier readability and post-processing

---

## 🚀 Getting Started

### Requirements

- Python 3.x
- `beautifulsoup4` (install via pip if not already installed)

```bash
pip install beautifulsoup4

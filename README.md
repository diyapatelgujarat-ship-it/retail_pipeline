# Automated Multi-Branch Retail Data Pipeline

## 1. Why would someone find your project useful?
Retail networks process thousands of daily transactions across multiple branches with inconsistent manual entry formats. This pipeline automates ingestion, filters out corrupt or fraudulent records, validates schema rules, and aggregates clean operational metrics instantly.

## 2. What problem are you proposing to solve?
Manual data handling leads to inaccurate sales reporting, unhandled null values, negative revenue anomalies, and branch misalignment. This script eliminates human error through defensive procedural validation and stateless functional transformations.

## 3. What kind of data will your project work for?
Structured operational transaction logs containing transaction IDs, branch IDs, dates, customer loyalty tiers, item counts, and gross revenue figures.

## 4. How will you make the project easy to build?
The project relies exclusively on Python's robust standard library with clean modular separation (`schema`, `validator`, `transformer`, `reporter`), an executable entry point (`main.py`), and automated unit tests.

## 5. Who did what parts?
Project Contributor: Diya Patel

Project Role: Sole Developer / Individual Project
---
### Running the Project
```bash
python main.py

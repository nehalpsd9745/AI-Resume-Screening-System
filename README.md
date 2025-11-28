# AI-Resume-Screening-ystem

A local, privacy-focused machine learning system for resume analysis. Convert resumes to text, train a classifier, predict job categories, and generate improvement advice — all offline on your machine.

---

## Overview

Resume-Analyser helps in:
- Converting resumes (CSV/PDF) into plain text
- Classifying resumes into job categories using ML
- Providing structured resume improvement advice
- Allowing full offline usage for privacy

---

## Features

- Resume-to-text extraction
- TF-IDF + Logistic Regression baseline model
- Optional sentence-transformer embeddings for semantic understanding
- Predict job roles from resume text
- Advice module to assess resume quality (MVP)
- Fully CLI-driven and configurable

---

## Installation

### 1. Create and activate a virtual environment
```bash
python -m venv .venv
. .venv/Scripts/activate  # Windows PowerShell: .venv\Scripts\Activate.ps1
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
pip install numpy==1.26.0 --force-reinstall
```

---

## Dataset Setup

Recommended structure:
```
data/
  raw/
    UpdatedResumeDataSet.csv       # Training source
  test/
    sample_resume.pdf              # Test resumes (PDF)
  processed/
    converted/                     # Output after text extraction
```

Example datasets (Kaggle):
- UpdatedResumeDataSet.csv
- Resume Dataset (PDF)

---

## Usage

### 1. Convert Data to Text

CSV to text:
```bash
python src/convert_dataset.py \
  --csv data/raw/UpdatedResumeDataSet.csv \
  --outdir data/processed/converted
```

PDF directory to text:
```bash
python src/convert_test_data.py \
  --pdfdir data/test \
  --outdir data/processed/converted_test
```

---

### 2. Train the ML Classifier
```bash
python src/train_classifier.py
```

This saves:
- Trained model
- TF-IDF vectorizer (or embeddings)

inside `models/`

---

### 3. Predict Job Category
```bash
python src/predict.py --input <path_to_text_file>
```

Example output: Data Science, HR, Cybersecurity, etc.

---

### 4. Generate Resume Advice
```bash
python src/advice.py --input <path_to_text_file>
```

Checks include:
- Resume length
- Missing common sections (Skills, Projects, Education)
- Technical keyword presence
- Soft skill mentions
- Career path alignment

This module will improve in future versions.

---

## Configuration

Modify `config.yaml` to adjust model and advice settings:
```yaml
model:
  embedding: all-MiniLM-L6-v2
  tfidf_max_features: 1000
  advice_threshold: 0.5
```

---

## Project Structure

```
src/
  convert_dataset.py
  convert_test_data.py
  train_classifier.py
  predict.py
  advice.py
models/
data/
assets/
config.yaml
README.md
requirements.txt
```

---

## Roadmap

Future improvements planned:
- Additional ML models (SVM, RandomForest, XGBoost, Transformers)
- Evaluation framework with metrics and visualization
- Enhanced resume quality scoring
- Streamlined CLI naming conventions
- Optional web interface for live analysis

---

## Contributing

Contributions are welcome.
Submit a pull request or open an issue for discussion.

---

## License

This is an open-source project.
The license file (if provided) applies.

---

## Acknowledgements

Datasets sourced from publicly available Kaggle resume datasets.


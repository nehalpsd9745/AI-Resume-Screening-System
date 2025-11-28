# AI-Resume-Screening-ystem
# Resume-Analyser

Local, private, and offline resume classification + improvement analysis using Machine Learning.

---

## Status & Tech

| Category | Details |
|---------|---------|
| Language | Python 3.8+ |
| ML Model | TF-IDF + Logistic Regression (baseline) |
| Optional Embeddings | Sentence-Transformers (MiniLM) |
| Interface | Command-line utilities |
| Privacy | 100% offline processing |

---

## Why this Project?

Most resume analyzers send data to cloud servers.  
This tool avoids that:

- No uploads
- No tracking
- Full control over your data
- Easy model experimentation for research and learning

---

## Feature Summary

| Feature | Description |
|--------|-------------|
| Resume Conversion | CSV + PDF → Plain text |
| Classification | Predict job role/category |
| Advice System | Basic quality checks & suggestions |
| Configurable | Settings via `config.yaml` |
| Extendable | Add new ML models easily |

---

## Quick Workflow (Visual Guide)

```
          +--------------+
          |  CSV / PDF   |
          +------+-------+
                 |
                 v
        +--------+---------+
        | Convert to Text  |
        +--------+---------+
                 |
                 v
      +----------+-----------+
      | Train ML Classifier  |
      +----------+-----------+
                 |
                 v
      +----------+-----------+
      | Predict Resume Role  |
      +----------+-----------+
                 |
                 v
      +----------+-----------+
      | Generate Resume Tips |
      +----------------------+
```

---

## Setup

### Create virtual environment
```bash
python -m venv .venv
. .venv/Scripts/activate  # Windows PowerShell: .venv\Scripts\Activate.ps1
```

### Install dependencies
```bash
pip install -r requirements.txt
pip install numpy==1.26.0 --force-reinstall
```

---

## Data Structure (Recommended)

```
data/
  raw/
    UpdatedResumeDataSet.csv
  test/
    sample_resume.pdf
  processed/
    converted/
```

---

## How to Use

### 1) Convert resumes to text

CSV → text files
```bash
python src/convert_dataset.py \
  --csv data/raw/UpdatedResumeDataSet.csv \
  --outdir data/processed/converted
```

PDF directory → text files
```bash
python src/convert_test_data.py \
  --pdfdir data/test \
  --outdir data/processed/converted_test
```

---

### 2) Train ML model
```bash
python src/train_classifier.py
```

Outputs saved in:  
```
models/
```

---

### 3) Predict job category from resume text
```bash
python src/predict.py --input <path_to_text_file>
```

Example output:  
```
Predicted Category: Data Science
```

---

### 4) Generate resume improvement advice (MVP)
```bash
python src/advice.py --input <path_to_text_file>
```

Advice checks include:
- Resume length
- Missing essential sections
- Missing technical keywords
- Soft skills detection
- Role fit evaluation

---

## Config
Edit `config.yaml`:

```yaml
model:
  embedding: all-MiniLM-L6-v2
  tfidf_max_features: 1000
  advice_threshold: 0.5
```

---

## Project Tree

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
requirements.txt
README.md
```

---

## Roadmap

- More ML models (SVM, XGBoost, Transformers)
- Detailed evaluation reports
- Better scoring / ranking system
- Resume parsing improvements
- Optional Web UI (Streamlit)
- Multi-label job category support

---

## Credits

Uses public Kaggle resume datasets for experimentation.


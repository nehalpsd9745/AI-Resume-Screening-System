# Resume-Analyser

Local, privacy-friendly resume analysis and classification using traditional ML and modern embeddings. Convert resumes, train a classifier, predict categories, and generate actionable advice — all on your machine.


## Features

- Resume-to-text conversion for CSV and PDF datasets
- TF‑IDF + Logistic Regression baseline classifier
- Optional sentence-transformer embeddings for richer features
- Simple CLI scripts for converting, training, predicting, and advice
- Configurable via `config.yaml`

## Quickstart

1. Create and activate a virtual environment (recommended).

```bash
python -m venv .venv
. .venv/Scripts/activate  # Windows PowerShell: .venv\Scripts\Activate.ps1
```

2. Install dependencies.

```bash
pip install -r requirements.txt
# Temporary compatibility pin
pip install numpy==1.26.0 --force-reinstall
```

3. Prepare data (see Data section) and run the pipeline below.

## Data

- Training data: [Kaggle: UpdatedResumeDataSet.csv](https://www.kaggle.com/datasets/gauravduttakiit/resume-dataset?select=UpdatedResumeDataSet.csv)
- Test data: [Kaggle: Resume Dataset](https://www.kaggle.com/datasets/snehaanbhawal/resume-dataset)

Recommended layout:

```
data/
  raw/
    UpdatedResumeDataSet.csv
  test/
    <your_pdf_files>.pdf
  processed/
    converted/
```

## Usage

### 1) Convert resume data to plain text

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

> The CLI naming may be refined in future iterations.

### 2) Train the classifier

```bash
python src/train_classifier.py
```

Example output plot:
![./assets/Logistic_Regression_Test.png](./assets/Logistic_Regression_Test.png)

> Additional algorithms will be experimented with in future updates.

### 3) Predict a category for a processed resume

```bash
python src/predict.py --input <path_to_text_file>
```

### 4) Generate resume advice (MVP)

```bash
python src/advice.py --input <path_to_text_file>
```

The current advice checks for:

1. **Length** — is the resume too short?
2. **Missing keywords** — e.g., "Python", "machine learning"
3. **Missing sections** — Experience, Projects, Education, Skills
4. **Soft skills** — mentions of communication, leadership, etc.
5. **Role match** — proximity to a target career path (e.g., Data Science)

> This is an early MVP and will evolve.

## Configuration

Tune behavior via `config.yaml`:

```yaml
model:
  embedding: all-MiniLM-L6-v2
  tfidf_max_features: 1000
  advice_threshold: 0.5
```

## Project Structure

```
src/
  convert_dataset.py        # CSV → text conversion
  convert_test_data.py      # PDF dir → text conversion
  train_classifier.py       # Train baseline classifier
  predict.py                # Predict class for a resume text
  advice.py                 # Generate heuristic advice (MVP)
models/                     # Saved models/artifacts
data/                       # Raw/test/processed data
assets/                     # Plots and images
```

## Roadmap

- Experiment with additional classifiers (SVM, RandomForest, XGBoost)
- Improve advice heuristics and scoring
- Add evaluation on held-out test sets and reporting
- Streamline CLI and naming for consistency
- Optional lightweight web UI

## Contributing

Contributions, issues, and feature requests are welcome! Feel free to open a PR or issue.


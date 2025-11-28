# TrustCheck

Small assurance layer that scores the reliability of LLM-generated intents using round-trip checks, heuristics and sanity tests.

## Why
LLMs are useful but error-prone; TrustCheck demonstrates lightweight, practical assurance mechanisms.

## Features
- Round-trip verification (NL -> intent -> NL)
- Similarity scoring (SequenceMatcher)
- Rule-based sanity checks (missing fields, action ambiguity)
- Streamlit demo showing score and flagged issues

## Quick Start
1. Clone:
   ```
   git clone https://github.com/zain-ramzan/intentify.git
   ```
2. Create venv and install:
   ```
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```
3. Run:
   ```
   streamlit run app.py
   ```

## Outputs
- `confidence_score`: 0..1
- `issues`: list of flagged problems
- `roundtrip_similarity` metric

## Evaluation
- Correlate score with human judgement
- False-positive/false-negative rates of issue detector

## Files
- `app.py`, `check.py`, `requirements.txt`

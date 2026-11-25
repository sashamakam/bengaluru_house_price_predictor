# Bengaluru House Price Predictor

A machine-learning API for estimating Bengaluru residential property prices from location, floor area, bedroom count, and bathroom count. Predictions are returned in lakhs of Indian rupees.

## Run the API

From the repository root, with [uv](https://docs.astral.sh/uv/) installed:

```sh
uv sync
uv run uvicorn backend.main:app --port 8000
```

Open <http://localhost:8000/docs> to try `POST /predict`. Supply `location`, `total_sqft`, `bath`, and `bhk`. Run the backend from the repository root so it can load the saved artifacts under [models](models).

## Data and project status

- [data/raw](data/raw) and [data/processed](data/processed) contain the raw and cleaned data snapshots.
- [notebooks/eda.ipynb](notebooks/eda.ipynb) contains exploratory analysis and preprocessing. Run it with `notebooks/` as its working directory.
- The checked-in training notebook is empty. The saved model supports inference.
- The React frontend and `GET /locations` are scaffolds. Use the prediction endpoint or FastAPI docs to try the model.

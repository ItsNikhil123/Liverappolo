from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from typing import List
import numpy as np
import pandas as pd
import json
import joblib
import uvicorn
from pathlib import Path
import os

app = FastAPI(title="LiverApollo", description="Liver Disease Prediction System")

# Load model and scaler with error handling
try:
    scaler = joblib.load('./models/scaler.pkl')
    model = joblib.load('./models/liverappolo.pkl')
    print("✓ Model (LiverZeus) and scaler loaded successfully")
except Exception as e:
    print(f"⚠️ Error loading model: {e}")
    scaler = None
    model = None


class LiverData(BaseModel):
    age: float
    gender: float
    tbilirubin: float
    dbilirubin: float
    alp: float
    alt: float
    ast: float
    tpro: float
    albumin: float
    agratio: float


class PredictionRequest(BaseModel):
    data: LiverData


@app.get("/health")
def health_check():
    """Check server health status"""
    return {
        "status": "healthy",
        "model_loaded": model is not None,
        "scaler_loaded": scaler is not None
    }


@app.get("/", response_class=HTMLResponse)
async def read_root():
    """Serve the main HTML page"""
    try:
        html_file = Path(__file__).parent / "templates" / "liverappolo.html"
        if html_file.exists():
            return html_file.read_text(encoding='utf-8')
        return "<h1>LiverApollo - Liver Disease Prediction System</h1>"
    except Exception as e:
        print(f"Error loading HTML: {str(e)}")
        return "<h1>LiverApollo - Liver Disease Prediction System</h1><p>Error loading page template. Please refresh.</p>"


@app.post('/predict')
def posting(request: PredictionRequest):
    """Make a prediction for liver disease"""
    try:
        if model is None or scaler is None:
            return {
                "error": "Model not loaded",
                "prediction": None,
                "probability": None,
                "message": "Server error: Model files not available"
            }
        
        # Convert the nested data object to a DataFrame with feature names
        features_dict = {
            'age': request.data.age,
            'gender': request.data.gender,
            'tbilirubin': request.data.tbilirubin,
            'dbilirubin': request.data.dbilirubin,
            'alp': request.data.alp,
            'alt': request.data.alt,
            'ast': request.data.ast,
            'tpro': request.data.tpro,
            'albumin': request.data.albumin,
            'agratio': request.data.agratio
        }
        # Create DataFrame with proper feature names
        data = pd.DataFrame([features_dict])
        scaled_data = scaler.transform(data)
        prediction = model.predict(scaled_data)[0]
        
        # Get prediction probability if available
        probability = None
        try:
            if hasattr(model, 'predict_proba'):
                probability = float(model.predict_proba(scaled_data)[0][1])
            else:
                probability = float(prediction)
        except:
            probability = float(prediction)
        
        return {
            "prediction": int(prediction),
            "probability": probability,
            "message": "Positive - Disease likely detected" if prediction == 1 else "Negative - No disease detected"
        }
    except Exception as e:
        return {
            "error": str(e),
            "prediction": None,
            "probability": None,
            "message": f"Prediction error: {str(e)}"
        }


if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))
    uvicorn.run("app:app", host="0.0.0.0", port=port, reload=False)


# LiverApollo - Liver Disease Prediction System

A machine learning-powered web application for predicting liver disease using patient medical data. Built with FastAPI, scikit-learn, and deployed on Render.

## 🎯 Overview

LiverApollo is an intelligent diagnostic system that predicts the likelihood of liver disease based on clinical lab results. The system uses advanced machine learning models trained on liver patient datasets and provides real-time predictions through an intuitive web interface.

## ✨ Features

- **Real-time Predictions**: Get instant predictions with confidence scores
- **Multiple ML Models**: Ensemble approach using Logistic Regression and Gradient Boosting
- **RESTful API**: FastAPI-powered backend with comprehensive endpoints
- **Web Interface**: User-friendly HTML interface for easy data input
- **Health Monitoring**: Built-in health check endpoints
- **Model Persistence**: Pre-trained models and scalers for instant predictions
- **Docker Support**: Containerized deployment for easy scaling
- **CI/CD Pipeline**: Automated testing and deployment via GitHub Actions

## 📊 Dataset

The model is trained on liver patient medical data with the following features:

| Feature | Description |
|---------|-------------|
| `age` | Patient age |
| `gender` | Gender (0=Female, 1=Male) |
| `tbilirubin` | Total Bilirubin |
| `dbilirubin` | Direct Bilirubin |
| `alp` | Alkaline Phosphatase |
| `alt` | Alanine Aminotransferase |
| `ast` | Aspartate Aminotransferase |
| `tpro` | Total Protein |
| `albumin` | Albumin |
| `agratio` | Albumin-Globulin Ratio |

**Target Variable**: Binary classification (0=No Disease, 1=Disease)

### Data Preprocessing

- Removed unnamed indices
- Gender encoding: Female → 0, Male → 1
- Outlier removal (AST < 700)
- Class imbalance handling using SMOTE (Synthetic Minority Oversampling Technique)
- Feature scaling using StandardScaler

## 🤖 Model Information

### Models Used

1. **Logistic Regression**
   - Probability threshold: 0.459
   - Fast inference, interpretable predictions

2. **Gradient Boosting Classifier**
   - Probability threshold: 0.37
   - Higher accuracy, ensemble approach

### Model Performance

Both models were evaluated on a test set (80-20 split, random_state=45) with precision, recall, and F1-score metrics.

## 🚀 Installation

### Prerequisites

- Python 3.11+
- pip or conda

### Local Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/ItsNikhil123/Liverappolo.git
   cd Liverappolo

2. **Create virutal environment**

python -m venv .venv
source .venv/Scripts/activate  # On Windows
# or
source .venv/bin/activate      # On macOS/Linux

3. **Install dependencies**

pip install -r requirements.txt

4. **Run the application**

python app.py

5. **Docker setup**

docker build -t liverappolo: latest # for building image from Dockerfile

docker run -p 8000:8000 liverappolo: latest

## 📡 API Documentation

### Endpoints

#### 1. Health Check
- **URL**: `/health`
- **Method**: GET
- **Response**:
  ```json
  {
    "status": "healthy",
    "model_loaded": true,
    "scaler_loaded": true
  }
  ```

#### 2. Web Interface
- **URL**: `/`
- **Method**: GET
- **Returns**: HTML interface for predictions

#### 3. Make Prediction
- **URL**: `/predict`
- **Method**: POST
- **Request Body**:
  ```json
  {
    "data": {
      "age": 45.0,
      "gender": 1,
      "tbilirubin": 0.8,
      "dbilirubin": 0.2,
      "alp": 76.0,
      "alt": 32.0,
      "ast": 24.0,
      "tpro": 7.0,
      "albumin": 3.5,
      "agratio": 1.0
    }
  }
  ```

- **Response**:
  ```json
  {
    "prediction": 0,
    "probability": 0.15,
    "message": "Negative - No disease detected"
  }
  ```

## 📁 Project Structure

```
Liverappolo/
├── app.py                          # Main FastAPI application
├── Dockerfile                      # Docker configuration
├── requirements.txt                # Python dependencies
├── pyproject.toml                  # Project metadata
├── render.yaml                     # Render deployment config
├── README.md                       # Project documentation
├── .github/
│   └── workflows/
│       └── main.yaml              # GitHub Actions CI/CD pipeline
├── data/
│   └── cleaned_data.csv           # Processed dataset
├── models/
│   ├── scaler.pkl                 # StandardScaler model
│   └── liverappolo.pkl            # Trained prediction model
├── notebooks/
│   └── liverpred.ipynb            # Model training & analysis
└── templates/
    └── liverappolo.html           # Web interface
```

## 🔧 Configuration

### Environment Variables

- `PORT`: Server port (default: 8000)

### Model Files

Ensure the following files are present in the models directory:
- `scaler.pkl` - Feature scaler
- `liverappolo.pkl` - Trained model

## 🚢 Deployment

### Render Deployment

1. Connect your GitHub repository to Render
2. Create a new Web Service
3. Deploy from the `main` branch
4. Set `PORT` environment variable if needed

### GitHub Actions CI/CD

The repository includes automated workflows that:
- ✅ Run linting (flake8)
- ✅ Execute tests (pytest)
- ✅ Build Docker image
- ✅ Deploy to Render
- 📊 Upload coverage reports

**Note**: To enable automated deployment, add GitHub Secrets:
- `RENDER_SERVICE_ID`: Your Render service ID
- `RENDER_API_KEY`: Your Render API key

## 📦 Dependencies

Core dependencies:
- **fastapi**: Web framework
- **uvicorn**: ASGI server
- **pandas**: Data manipulation
- **numpy**: Numerical computing
- **scikit-learn**: Machine learning
- **joblib**: Model serialization
- **imblearn**: Data balancing (SMOTE)

See requirements.txt for complete list.

## 🧪 Testing

Run tests with pytest:
```bash
pytest --cov=. --cov-report=xml
```

Check code quality:
```bash
flake8 . --max-complexity=10
```

## 📈 Model Training

To retrain the model:

1. Update dataset in cleaned_data.csv
2. Run the Jupyter notebook: liverpred.ipynb
3. Models will be saved to models directory
4. Commit and push changes to trigger CI/CD pipeline

## ⚠️ Disclaimer

This tool is for informational purposes only and should not be used as a substitute for professional medical advice. Always consult with qualified healthcare professionals for medical decisions.

## 🤝 Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/improvement`)
3. Commit your changes (`git commit -am 'Add improvement'`)
4. Push to the branch (`git push origin feature/improvement`)
5. Create a Pull Request

## 📝 License

This project is licensed under the MIT License - see LICENSE file for details.

## 👤 Author

**Nikhil** - [GitHub Profile](https://github.com/ItsNikhil123)

## 📞 Support

For issues, questions, or suggestions, please open an issue on GitHub.

---

**Last Updated**: June 2024
**Status**: Active Development
```

You can copy this markdown and paste it directly into your `README.md` file. Feel free to customize sections like the author name, contact info, or add additional sections as needed!You can copy this markdown and paste it directly into your `README.md` file. Feel free to customize sections like the author name, contact info, or add additional sections as needed!
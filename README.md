# 📞 Telco Customer Churn Predictor

A machine learning classification model that predicts whether a telecom customer is likely to churn (leave the company). Built with scikit-learn and deployed as an interactive Streamlit web application.

**[View Live Demo](#deployment)** | **[Project Structure](#project-structure)** | **[How to Use](#how-to-use)**

---

## 🎯 Overview

Customer churn is one of the biggest challenges for telecom companies. This project develops a predictive model that identifies high-risk customers before they leave, enabling proactive retention strategies.

The model is trained on customer demographics, account information, and service usage patterns to predict churn probability with high accuracy.

---

## 🌐 Deployment

### Live Demo
This app is deployed on [**Streamlit Community Cloud**](https://telco-churn-predictor-12.streamlit.app/):
```
https://telco-churn-predictor-12.streamlit.app/
```

---

## ✨ Features

- **Binary Classification Model**: Predicts churn vs. non-churn using scikit-learn
- **Data Preprocessing**: Handles missing values, categorical encoding, and feature scaling
- **Interactive UI**: Streamlit web app for real-time predictions on new customers
- **Model Pipeline**: Scikit-learn pipeline with preprocessor + classifier
- **Production-Ready**: Serialized model (`.pkl`) for deployment and inference

---

## 🛠️ Tech Stack

| Component | Technology |
|-----------|------------|
| **ML Framework** | scikit-learn 1.6.1 |
| **Data Processing** | pandas, NumPy |
| **Web App** | Streamlit |
| **Serialization** | joblib |
| **Python Version** | 3.8+ |

---

## 📊 Dataset

The model is trained on the **Telco Customer Churn dataset** containing:
- **7,043 customer records**
- **21 features**: demographics, account info, service subscriptions, usage patterns
- **Target variable**: Churn (Yes/No)

### Key Features
- Customer demographics (age, gender, tenure)
- Account type and contract length
- Internet and phone services subscribed
- Monthly charges and total spending
- Customer support interactions

---

## 🚀 Getting Started

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Git

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/YOUR_USERNAME/telco-churn-predictor.git
cd telco-churn-predictor
```

2. **Create a virtual environment** (recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

---

## 💻 How to Use

### Run Locally

```bash
streamlit run app.py
```

The app will open at `http://localhost:8501` in your browser.

<<<<<<< HEAD
### Using the App

1. **Enter customer details** in the sidebar:
   - Demographics (age, gender, tenure)
   - Services subscribed (internet, phone, security, etc.)
   - Account details (contract type, payment method)
   - Monthly and total charges

2. **Click Predict** to get the churn probability

3. **View results** with confidence score and risk assessment

---

## 🧠 Model Details

### Approach
- **Algorithm**: Trained multiple classifiers and selected the best performer
- **Validation**: Train-test split with cross-validation
- **Preprocessing**: 
  - Missing data imputation (attribute mean / class mean)
  - Categorical encoding (one-hot encoding)
  - Feature scaling (StandardScaler)
  
### Performance
The final model achieves strong predictive performance on the test set with balanced precision-recall across churn and non-churn classes.

### Model Pipeline
```
Input Features → Preprocessing → Feature Scaling → Classifier → Churn Probability
```

The pipeline is saved as `best_churn_model.pkl` for production inference.

---

## 📁 Project Structure

```
telco-churn-predictor/
├── app.py                              # Streamlit web app
├── best_churn_model.pkl               # Trained ML model (scikit-learn pipeline)
├── customer_churn_prediction.ipynb    # Jupyter notebook with analysis & training
├── requirements.txt                    # Python dependencies
└── README.md                          # This file
```

### Files Description

- **`app.py`**: Streamlit application that loads the model and provides an interactive UI for predictions
- **`best_churn_model.pkl`**: Serialized scikit-learn pipeline (preprocessor + classifier)
- **`customer_churn_prediction.ipynb`**: Full analysis notebook including EDA, feature engineering, model training, and evaluation
- **`requirements.txt`**: List of Python packages with versions

---

## 📈 Development Process

### Data Science Workflow
1. **Exploratory Data Analysis (EDA)** - Understand distributions, correlations, missing values
2. **Data Preprocessing** - Handle missing data, encode categorical variables, scale features
3. **Feature Engineering** - Create meaningful features from raw data
4. **Model Training** - Train multiple classifiers (Logistic Regression, Random Forest, etc.)
5. **Model Evaluation** - Compare performance using accuracy, precision, recall, F1-score
6. **Hyperparameter Tuning** - Optimize the best model
7. **Serialization** - Save the final pipeline as `.pkl`
8. **Deployment** - Create Streamlit UI and deploy to cloud

### Key Decisions
- **Missing Value Strategy**: Attribute mean for numerical, class mean for categorical (learned from SWE-302 coursework)
- **Feature Scaling**: Applied to normalize feature ranges for algorithms sensitive to scale
- **Model Selection**: Chose the classifier with best cross-validation performance

---

## 📚 References & Learning

This project demonstrates:
- **Data Science**: ML pipeline, preprocessing, model selection
- **Software Engineering**: Clean code, serialization, deployment 
- **Statistics**: Handling missing data imputation strategies 

---

## 👤 Author

**Areeb ul Hassan** | Sukkur IBA University  
Software Engineer

---

## 📄 License

This project is provided as-is for educational and demonstration purposes.

---

## 🤝 Contributing

Suggestions and improvements welcome! Feel free to:
- Report bugs or issues
- Suggest new features
- Improve documentation

---

## 📞 Contact & Support

- GitHub: [@areebarifshaikh](https://github.com/areebarifshaikh)
- Project Issues: [Open an issue](https://github.com/areebarifshaikh/telco-churn-predictor/issues)

---

## 🙏 Acknowledgments

- Telco Customer Churn dataset (publicly available)
- Streamlit for the excellent web framework
- Scikit-learn for machine learning tools

---
=======
## GUI
<img width="548" height="732" alt="image" src="https://github.com/user-attachments/assets/785080a7-e98c-4573-b07d-02a52f481a24" />
>>>>>>> 0b2a6637a20e6976a8829ae7ef16a7311242b1d2

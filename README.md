# DTP_Data_Duo_project
# 💳 Data-Duo: Credit Card Fraud Detection

A machine learning-powered fraud detection system designed to identify fraudulent transactions from anonymized credit card data. Built during the DTP Hackathon Rwanda 2025.

---

## 🚀 Inspiration

With the rise in digital transactions, financial fraud has become a critical issue globally. We were inspired to build an intelligent system that helps financial institutions detect fraud early and protect consumers. We chose the Kaggle Credit Card Fraud dataset to explore real-world fraud patterns and tackle the class imbalance challenge.

---

## 🧠 What It Does

Our project builds a **binary classification model** that predicts whether a given transaction is legitimate or fraudulent using machine learning. It provides:

- Model training and evaluation pipeline
- SMOTE oversampling for imbalanced data
- Performance metrics (Precision, Recall, F1-score, AUC)
- Streamlit-powered interactive prediction dashboard

---

## 🛠️ How We Built It

We followed these steps:

1. **Data Cleaning**: Loaded and analyzed the dataset
2. **Feature Engineering**: Used PCA features (V1–V28), `Time`, and `Amount`
3. **Preprocessing**: Scaled features and handled imbalanced data using **SMOTE**
4. **Modeling**: Trained a **Logistic Regression** model (others like Random Forest & XGBoost tested)
5. **Evaluation**: Assessed performance using ROC AUC and Precision-Recall AUC
6. **Deployment**: Built a Streamlit dashboard for user interaction and predictions

---

## 💥 Challenges We Ran Into

- Severe **class imbalance** (only ~0.17% fraud cases)
- Interpreting **anonymized PCA features**
- Managing **model generalization** to avoid overfitting
- Hyperparameter tuning took time and computational power

---

## 🏆 Accomplishments We’re Proud Of

- Achieved **ROC AUC of 0.96** and **PR AUC of 0.74**
- Developed a working prototype with a **live prediction dashboard**
- Learned how to handle class imbalance effectively
- Collaborated effectively as a team under pressure

---

## 📚 What We Learned

- Real-world fraud data is sparse and complex
- SMOTE can significantly improve minority class detection
- Streamlit is a great tool for building quick ML apps
- Deployment is just as important as model training

---

## 🔮 What’s Next

- Integrate real-time APIs for live transaction input
- Add **explainability** (e.g., SHAP or LIME) for model decisions
- Explore **deep learning approaches** for better fraud detection
- Deploy on the web using **Render**, **Heroku**, or **AWS**

---

## 🧰 Built With

| Tech | Description |
|------|-------------|
| Python | Main language |
| scikit-learn | ML models and metrics |
| imbalanced-learn | SMOTE for oversampling |
| pandas, numpy | Data manipulation |
| matplotlib, seaborn | Data visualization |
| Streamlit | Web dashboard |
| joblib | Model saving/loading |
| GitHub | Version control & collaboration |

---



---

## 📌 Dataset Source

[Kaggle: Credit Card Fraud Detection](https://www.kaggle.com/datasets/mlg-ulb/creditcardfra)

---

---

## 🧪 How to Run

```bash
# Clone the repo
git clone https://github.com/Kali-AI02/DTP_Data_Duo_project.git
cd DTP_Data_Duo_project

# Install dependencies
pip install -r requirements.txt

# Launch Streamlit app
streamlit run app.py

you can access the app directly here
https://ddddddtpdataduoproject-kduvqwuzrrt7rtmz8iyxgr.streamlit.app/ 




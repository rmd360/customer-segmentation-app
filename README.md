# 🧠 Customer Segmentation App

This is an interactive Streamlit web app for performing customer segmentation using **KMeans clustering** and visualizing the results with **PCA and Plotly**.

You can upload your own dataset (CSV), choose the features to cluster, and explore customer segments for targeted marketing and revenue optimization.


## 🚀 Live Demo

👉 [Click here to open the app](https://customer-segmentation-app-5i3vrjnlvitujfragkoquf.streamlit.app/)

---

## 🔍 Features

- Upload your own customer CSV
- Select custom features for clustering (e.g., Income, Spending Score)
- Interactive slider for number of clusters (K)
- 2D visualization using PCA + Plotly
- Segment-wise estimated revenue calculation

---

## 🛠️ Technologies Used

- Python
- Streamlit
- Pandas
- Scikit-learn
- Plotly

---

## 📦 Setup Locally

```bash
git clone https://github.com/rmd360/customer-segmentation-app.git
cd customer-segmentation-app
pip install -r requirements.txt
streamlit run customer_segmentation_app.py

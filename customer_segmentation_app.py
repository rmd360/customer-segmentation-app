import streamlit as st
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
import plotly.express as px

st.set_page_config(page_title="Customer Segmentation App", layout="wide")

st.title("🧠 Customer Segmentation Dashboard")
st.markdown("Upload your customer dataset and explore automatic KMeans-based segmentation!")

# Upload CSV
uploaded_file = st.file_uploader("📂 Upload CSV", type=["csv"])
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    
    st.subheader("🔍 Raw Data Preview")
    st.dataframe(df.head())

    # Feature selection
    st.subheader("⚙️ Select Features for Clustering")
    numeric_cols = df.select_dtypes(include='number').columns.tolist()
    default_cols = [col for col in ["Annual Income", "Spending Score", "Age"] if col in numeric_cols]

    selected_features = st.multiselect("Choose columns:", numeric_cols, default=default_cols)

    if len(selected_features) >= 2:
        # Choose number of clusters
        k = st.slider("🔢 Number of Clusters (K)", 2, 10, 5)

        # Run KMeans
        model = KMeans(n_clusters=k, random_state=42)
        df['Segment'] = model.fit_predict(df[selected_features])

        # PCA for visualization
        pca = PCA(n_components=2)
        pca_result = pca.fit_transform(df[selected_features])
        df['PCA1'], df['PCA2'] = pca_result[:, 0], pca_result[:, 1]

        # Plot
        st.subheader("📊 PCA Cluster Visualization")
        fig = px.scatter(
            df, x='PCA1', y='PCA2', color=df['Segment'].astype(str),
            hover_data=selected_features,
            title="Customer Segments by PCA",
            color_discrete_sequence=px.colors.qualitative.Set1
        )
        st.plotly_chart(fig, use_container_width=True)

        # Revenue estimate (optional)
        if "Spending Score" in selected_features:
            st.subheader("💰 Estimated Revenue by Segment")
            revenue = df.groupby('Segment')['Spending Score'].mean() * df['Segment'].value_counts()
            st.dataframe(revenue.round(2).reset_index(name="Estimated Revenue"))
    else:
        st.warning("Please select at least two numeric features for clustering.")

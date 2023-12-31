import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsRegressor


st.sidebar.title('KNN Regressor Visualization')
# st.set_page_config(page_title="KNN Regressor Visualization", page_icon="📈")

# Generating a non-linear dataset
n_samples = 200
x = np.linspace(-3, 3, n_samples).reshape(-1, 1)
y = np.sin(x).ravel() + np.random.randn(n_samples) * 0.5

# Sidebar controls
k_neighbors = st.sidebar.slider('Number of Neighbors (k)', 1, 50, 5)

# KNN model
knn_model = KNeighborsRegressor(n_neighbors=k_neighbors)
knn_model.fit(x, y)
y_pred = knn_model.predict(x)

# Plotting
if st.sidebar.button('predict'):
    fig, ax = plt.subplots()
    ax.scatter(x, y, label='Data Points', color='green')
    ax.plot(x, y_pred, label=f'Prediction (k={k_neighbors})', color='red')
    ax.set_title('KNN Regressor Visualization')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.legend()

    st.pyplot(fig)

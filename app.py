import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title('CSV Analyzer & Plotter')

uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("Data Preview", df.head(5))

    st.write('Shape of CSV file', df.shape, '(rows, columns)')
    
    analysis_type = st.selectbox('Select Analysis Type', ['Univariate', 'Bivariate', 'Multivariate'])

    if analysis_type == 'Univariate':
        column = st.selectbox('Select Column for Univariate Analysis', df.columns)
        plot_type_uni = st.selectbox('Select Univariate Plot Type', ['Histogram(Numerical)', 'Count Plot(Categorical)', 'Pie Chart(Categorical)'])

        if st.button('Plot Univariate Graph'):
            fig, ax = plt.subplots()
            if plot_type_uni == 'Histogram(Numerical)':
                sns.histplot(df[column], ax=ax, kde=True)
            elif plot_type_uni == 'Count Plot(Categorical)':
                sns.countplot(x=df[column], ax=ax)
            elif plot_type_uni == 'Pie Chart(Categorical)':
                df[column].value_counts().plot(kind='pie', autopct='%.2f')

            ax.set_title(f'{plot_type_uni} of {column}')
            st.pyplot(fig)

    elif analysis_type == 'Bivariate':
        x_axis = st.selectbox('Select X-axis for Bivariate Analysis(Categorical/Numerical)', df.columns)
        y_axis = st.selectbox('Select Y-axis for Bivariate Analysis(Numerical)', df.columns)
        plot_type_bi = st.selectbox('Select Bivariate Plot Type', ['Bar', 'Line', 'Scatter'])

        if st.button('Plot Bivariate Graph'):
            fig, ax = plt.subplots()
            if plot_type_bi == 'Scatter':
                sns.scatterplot(x=df[x_axis], y=df[y_axis], ax=ax)
            elif plot_type_bi == 'Line':
                sns.lineplot(x=df[x_axis], y=df[y_axis], ax=ax)
            elif plot_type_bi == 'Bar':
                sns.barplot(x=df[x_axis], y=df[y_axis], ax=ax)

            ax.set_title(f'{x_axis} vs {y_axis} ({plot_type_bi} Plot)')
            st.pyplot(fig)

    elif analysis_type == 'Multivariate':
        x_axis = st.selectbox('Select X-axis for Multivariate Analysis', df.columns)
        y_axis = st.selectbox('Select Y-axis for Multivariate Analysis', df.columns)
        hue = st.selectbox('Select Hue for Multivariate Analysis', df.columns)
        plot_type_multi = st.selectbox('Select Multivariate Plot Type', ['Scatter', 'Line'])

        if st.button('Plot Multivariate Graph'):
            fig, ax = plt.subplots()
            if plot_type_multi == 'Scatter':
                sns.scatterplot(x=df[x_axis], y=df[y_axis], hue=df[hue], ax=ax)
            elif plot_type_multi == 'Line':
                sns.lineplot(x=df[x_axis], y=df[y_axis], hue=df[hue], ax=ax)

            ax.set_title(f'{x_axis} vs {y_axis} by {hue} ({plot_type_multi} Plot)')
            st.pyplot(fig)


import streamlit as st 
import plotly.express as px
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 



st.subheader("Data Exploration")
data = st.file_uploader("Upload a Dataset", type=["csv", "txt"])

if data is not None:
    d = pd.read_csv(data)
    df=d.dropna()
    st.dataframe(df.head())
    
    cols=df.columns.to_list()    
    if st.button("show shape"):
        st.write(df.shape)

    if st.button("summary"):
        st.write(df.describe())
    if st.button("show columns names"):
        st.write(cols)
    if st.button("value counts"):
        st.write(df.iloc[:,-1].value_counts())
    
    
    st.subheader("Data Visualization")
    type_of_plot = st.selectbox("Select Type of Plot",["scatter","bar","line","hist","box"])
    selected_columns_names = st.multiselect("Select Columns To Plot",cols)
    if st.button("Generate Plot"):
        st.success("Generating Customizable Plot of {} for {}".format(type_of_plot,selected_columns_names))
        if type_of_plot == 'scatter':
            new_df=df[selected_columns_names]
            fig=px.scatter(new_df)
            st.plotly_chart(fig)
        elif type_of_plot == 'bar':
            new_df=df[selected_columns_names]
            fig=px.bar(new_df)
            st.plotly_chart(fig)
        elif type_of_plot == 'line':
            new_df=df[selected_columns_names]
            fig = px.line(new_df)
            st.plotly_chart(fig)
        elif type_of_plot == 'hist':
            new_df=df[selected_columns_names]
            fig=px.histogram(new_df)
            st.plotly_chart(fig)
        elif type_of_plot == 'box':
            new_df=df[selected_columns_names]
            fig=px.box(new_df)
            st.plotly_chart(fig)
        
            
            
            
            
            
            
            
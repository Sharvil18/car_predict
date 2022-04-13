# S1.1: Design the "Visualise Data" page of the multipage app.
# Import necessary modules 
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
# Define a function 'app()' which accepts 'car_df' as an input.
def app(car_df):
  st.header('Visualize Data')
  st.set_option('deprecation.showPyplotGlobalUse',False)
  st.subheader('Scatter Plot')
  features_list = st.multiselect('Select the x-axis value :',('carwidth','enginesize','horsepower','drivewheel_fwd','car_company_buick'))
  for feature in features_list:
    st.subheader(f'Scatter Plot between {feature} and price')
    plt.figure(figsize=(16,7))
    sns.scatterplot(x=feature,y='price',data=car_df)
    st.pyplot()
  st.subheader('Visalization Sector')
  plot_types = st.selectbox('Select chart or plot:',('Boxplot','Correlation Heatmap','Histogram'))
  if 'Histogram' in plot_types:
    st.subheader('Histogram')
    col = st.selectbox('Select column for histogram',('enginesize','carwidth','horsepower'))
    plt.figure(figsize=(16,7),dpi=96)
    plt.title(f'Histogram for {col}')
    plt.hist(car_df[col],bins='sturges',edgecolor='black')
    st.pyplot()
  if 'Correlation Heatmap' in plot_types:
    st.subheader('Correlation Heatmap')
    col = st.selectbox('Select column for heatmap',('enginesize','carwidth','horsepower'))
    plt.figure(figsize=(16,7),dpi=96)
    plt.title(f'Correlation Heatmap for {col}')
    ax = sns.heatmap(car_df.corr(),annot=True)
    bottom,top = ax.get_ylim()
    ax.set_ylim(bottom+0.5,top-0.5)
    st.pyplot()
  if 'Boxplot' in plot_types:
    st.subheader('Boxplot')
    col = st.selectbox('Select column for boxplot',('enginesize','carwidth','horsepower'))
    plt.figure(figsize=(16,7),dpi=96)
    plt.title(f'Boxplot for {col}')
    sns.boxplot(car_df[col])
    st.pyplot()
import pandas as pd
import numpy as np
import streamlit as st
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score,mean_absolute_error,mean_squared_log_error,mean_squared_error
from sklearn.linear_model import LinearRegression
# Define the 'prediction()' function.
def prediction(car_df,car_width,engine_size,horse_power,drive_wheel_fwd,car_comp_buick):
  X = car_df.iloc[:,:-1]
  y = car_df['price']
  X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.3,random_state=42)
  lin_reg = LinearRegression()
  lin_reg.fit(X_train,y_train)
  score = lin_reg.score(X_train,y_train)
  price = lin_reg.predict([[car_width,engine_size,horse_power,drive_wheel_fwd,car_comp_buick]])
  price = price[0]
  y_test_pred = lin_reg.predict(X_test)
  test_r2_score = r2_score(y_test,y_test_pred)
  test_mae = mean_absolute_error(y_test,y_test_pred)
  test_mslr = mean_squared_log_error(y_test,y_test_pred)
  test_rmse = np.sqrt(mean_squared_error(y_test,y_test_pred))
  return price,score,test_r2_score,test_mae,test_mslr,test_rmse


def app(car_df):
  st.markdown('<p style="color:blue;font-size:25px">This app uses <b>Linear regression</b> to predict the price of a car based on your inputs.',unsafe_allow_html=True)
  st.subheader('Select the values')
  car_wid = st.slider('Car width:',float(car_df['carwidth'].min()),float(car_df['carwidth'].max()))
  eng_siz = st.slider('Engine Size: ',int(car_df['enginesize'].min()),int(car_df['enginesize'].max()))
  hor_pow = st.slider('Horse Power: ',int(car_df['horsepower'].min()),int(car_df['horsepower'].max()))
  drw_fwd = st.radio('Is it a forward drive wheel car?',('Yes','No'))
  if drw_fwd == 'Yes':
    drw_fwd = 1
  else:
    drw_fwd = 0
  com_bui = st.radio('Is the car manufactured by Buick?',('Yes','No'))
  if com_bui == 'Yes':
    com_bui = 1
  else:
    com_bui = 0
  if st.button('Predict'):
    price,score,car_r2,car_mae,car_msle,car_rmse = prediction(car_df,car_wid,eng_siz,hor_pow,drw_fwd,com_bui)
    st.success('The predicted price of the car is : ${:,}'.format(int(price)))
    st.info('Accuracy score of this model is : ${:2.2%}'.format(score))
    st.info(f'R-squared score of this model is : {car_r2:.3f}')
    st.info(f'Mean Abosulute error of this model is : {car_mae:.3f}')
    st.info(f'Mean squared log error of this model is : {car_msle:.3f}')
    st.info(f'Root mean squared error of this model is : {car_rmse:.3f}')
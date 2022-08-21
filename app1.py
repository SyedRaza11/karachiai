# -*- coding: utf-8 -*-
"""
Created on Sat Aug 20 03:09:39 2022

@author: hp
"""

path = 'AirPassengers.csv'
import streamlit as st
import pandas as pd
def main():
     #path = r'C:/Users/hp/.spyder-py3/AirPassengers.csv'
     df=pd.read_csv('AirPassengers.csv')
     data = df
     data['year'] = data['Month'].apply(lambda x: x.split('-')[0])
     year = st.selectbox('Select year', data['year'].unique())
     button = st.button('show results')
     if button :
        subset = data [data['year']==year]
        st.table(subset)
     
     
     
if __name__=='__main__':
    main()
    
    
    
     
     
     
     
     
     
     
     
     

    
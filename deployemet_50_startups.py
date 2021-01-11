# -*- coding: utf-8 -*-
"""
Created on Sun Jan 10 20:16:19 2021

@author: PawanK
"""

import pandas as pd
import streamlit as st
from pickle import load


st.title('Model deployment : Profit Prediciton')

st.sidebar.header('User Input Parameter')
    
loaded_model = load(open('multiple_linear_model_50_startups.sav','rb'))

def user_input_parameter(RNDspend,Administration,MarketingSpend,State_Florida,State_New_York):
    RNDspend = float(RNDspend)
    Administration = float(Administration)
    MarketingSpend 	= float(MarketingSpend)
    State_Florida = int(State_Florida)
    State_New_York = int(State_New_York)
    data = {"RDSpend":RNDspend,
            "Administration":Administration,
            "MarketingSpend":MarketingSpend,
            "State_Florida":State_Florida,
            "State_New_York":State_New_York}
    global features
    features = pd.DataFrame(data,index = [0])
    
    final_predict=loaded_model.predict(features).round(2)
    return (final_predict).values


def main():
    
    st.title('Profit prediction')
    
    RNDspend = st.sidebar.number_input("R&D Spend")
    Administration = st.sidebar.number_input("Administration")
    MarketingSpend 	= st.sidebar.number_input("MarketingSpend")
    State_Florida = st.sidebar.selectbox('State_Florida',('0','1'))
    State_New_York = st.sidebar.selectbox('State_New_York',('0','1'))
    st.sidebar.selectbox('State_California',('0','1'))

    if st.button('Predict'):
        result = user_input_parameter(RNDspend,Administration,MarketingSpend,State_Florida,State_New_York)
        
        st.success('Predicted profit is {}'.format(result))


if __name__=='__main__':
        main()


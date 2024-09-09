import streamlit as lit
import pandas as pd
import numpy as np

lit.title("Phone evolution")

dat = pd.DataFrame({
    'Phone' : ['Nokia','Samsung','Apple'],
    'Year' : ['1998','2001','2003']
})

dat

if lit.checkbox('Click to see Map data'):
    map_dat = pd.DataFrame(
    np.random.randn(1000,2)/[70,30]+[11.323,80.234],
    columns=['lat','lon'],
    )
    lit.map(map_dat)

option = lit.selectbox(
    'Select any Mobile you wanna see',
    dat['Phone'])


'you select:',option

left_column,right_column = lit.columns(2)
pressed = left_column.button('Cick to see the latest updates')
if pressed:
    right_column.write("we'll launch a new phone updates will be on new year eve")

expander = lit.expander("FAQ")
expander.write("Ask us anything briefly")

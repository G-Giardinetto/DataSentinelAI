import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from textExtractor import extract
import GenerazioneTesto

DATE_COLUMN = 'date/time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
         'streamlit-demo-data/uber-raw-data-sep14.csv.gz')

st.title('Analyze your data')

file = st.file_uploader("Upload your file to get you report", type=['pdf', 'docx', 'txt'], accept_multiple_files=False)

if file is not None:
    testo = extract(file)
    report = GenerazioneTesto.generate(testo)
    with st.chat_message("assistant"):
        with st.status('Analizzando...'):
            st.write(f"Ecco il tuo report:\n{report}")
    # st.text(file._file_urls)
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from textExtractor import extract
import GenerazioneTesto

st.title('Analyze your data')

file = st.file_uploader("Upload your file to get you report", type=['pdf', 'docx', 'txt'], accept_multiple_files=False)

if file is not None:
    testo = extract(file)

    with st.chat_message("assistant"):
        with st.status('Analizzando...') as status:
            report = GenerazioneTesto.generate(testo)
            status.update(
                label="Analisi completa!", state="complete", expanded=True)
            st.write(f"Ecco il tuo report:\n{report}")
    # st.text(file._file_urls)
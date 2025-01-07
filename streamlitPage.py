import streamlit as st
from textExtractor import extract, writeFile
from textExtractor import findExtension
import GenerazioneTesto

st.title('Analyze your data')

file = st.file_uploader("Upload your file to get you report", type=['pdf', 'docx', 'txt'], accept_multiple_files=False)
testo=""
flag=False
if file is not None:
    st.session_state['fileExtension'] = findExtension(file)
    testo = extract(file)
    if st.button("Genera report", type="primary"):
        flag=True
        with st.chat_message("assistant"):
            with st.status('Analizzando...') as status:
                report = GenerazioneTesto.generateReport(testo)
                status.update(
                    label="Analisi completa!", state="complete", expanded=True)
                st.markdown(f"Ecco il tuo report:\n\n {report}")
                st.session_state['report'] = report
                st.session_state['button'] = False

if flag:
    st.write("Modificare il file secondo le indicazioni?")
    button = st.button("Modifica", type="secondary", disabled=False)
else:
    button = st.button("Modifica", type="secondary", disabled=True)

buttonFlag= st.session_state['button'] if not None else False

if button | buttonFlag:
    st.session_state['button']=True
    report=st.session_state['report']
    with st.status('Modificando...') as status:
        left, right = st.columns(2)
        edited = GenerazioneTesto.editDocument(testo, report)
        status.update(
            label="Modifica completata!", state="complete", expanded=True)
        left.markdown(f"File modificato:\n\n{edited}")
        right.markdown(f"File originale:\n\n{testo}")
    extension = st.session_state['fileExtension']
    st.download_button(label="Scarica file modificato", data=writeFile(edited, extension),
                       file_name='edited' + extension)
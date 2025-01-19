import streamlit as st

from GenerazioneTesto import sensitiveInformations
from textExtractor import extract, writeFile
from textExtractor import findExtension
import GenerazioneTesto

containerHeight=500

st.set_page_config(page_title="Analizza il tuo documento",layout="wide")
first,center,last = st.columns([0.15,0.7,0.15])
_,ccenter,_ = center.columns(3)
ccenter.title('Analyze your data')
file = center.file_uploader("Upload your file to get you report", type=['pdf', 'docx', 'txt'], accept_multiple_files=False)
testo=""
flag=False
if file is not None:
    st.session_state['fileExtension'] = findExtension(file)
    testo = extract(file)
    if center.button("Genera report", type="primary", use_container_width=True):
        flag=True
        with center.chat_message("assistant"):
            with center.status('**Analizzando...**', expanded=True) as status:
                report = GenerazioneTesto.generateReport(testo)
                status.update(
                    label="**Analisi completa!**", state="complete", expanded=True)
                st.markdown(f"# Ecco il tuo report:\n\n {report}")
                st.session_state['report'] = report

if flag:
    center.write("Modificare il file secondo le indicazioni?")
    button = center.button("Modifica", type="secondary", disabled=False, use_container_width=True)
else:
    button = center.button("Modifica", type="secondary", disabled=True, use_container_width=True)


if button:
    report=st.session_state['report']
    with center.status('**Modificando...**') as status:
        left, centerr, right = center.columns(3)
        edited = GenerazioneTesto.editDocument(testo, report)
        nerEdited = GenerazioneTesto.extractEntities(testo)
        status.update(
            label="**Modifica completata!**", state="complete", expanded=True)
        leftContainer = left.container(height=containerHeight)
        centerContainer = centerr.container(height=containerHeight)
        rightContainer= right.container(height=containerHeight)

        leftContainer.markdown(f"## File modificato:\n\n{edited}")
        centerContainer.markdown(f"## Entità riconosciute:\n\n{nerEdited}")
        rightContainer.markdown(f"## File originale:\n\n{testo}")
    extension = st.session_state['fileExtension']
    left.download_button(label="**Scarica file modificato**", data=writeFile(edited, extension),
                       file_name='edited' + extension)
    centerr.download_button(label="**Scarica entità riconosciute**", data=writeFile(nerEdited, ".txt"),
                         file_name='recognized' + ".txt")
    center.download_button(label="**Scarica file modificato\n ed entità riconosciute**", data=writeFile(testo+"\n\n"+'-'*30+"Entità riconosciute:"+'-'*30+"\n\n"+nerEdited, extension), file_name="Bundle"+extension)
    firstContainer = first.container()
    firstContainerr = firstContainer.container(height=containerHeight%2)
    firstContainerr.markdown(f"## Contesti in cui le entità possono essere sensibili:\n\n{sensitiveInformations(report)}")

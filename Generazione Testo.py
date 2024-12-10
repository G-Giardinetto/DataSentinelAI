import os
import docx
from openai import OpenAI
from textExtractor import extract

while True:
    documentName = input("Inserisci il nome del documento: ")
    if os.path.exists(documentName):
        document = extract(documentName)
        print(document)
        break

#semplice codice per generare testo

os.system('lms server start')
os.system('lms load lmstudio-community/Meta-Llama-3.1-8B-Instruct-GGUF/Meta-Llama-3.1-8B-Instruct-Q4_K_M.gguf')
#lmstudio-community/Meta-Llama-3.1-8B-Instruct-GGUF/Meta-Llama-3.1-8B-Instruct-Q4_K_M.gguf
#lmstudio-community/Meta-Llama-3.1-8B-Instruct-GGUF/Meta-Llama-3.1-8B-Instruct-Q4_K_M.gguf -> Stringa presa dal Software LMStudio, servirà percaricare e scaricare il modello dal server
client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")

completion = client.chat.completions.create(model ='lmstudio-community/Meta-Llama-3.1-8B-Instruct-GGUF/Meta-Llama-3.1-8B-Instruct-Q4_K_M.gguf',messages=[
                    {"role": "system", "content": "Initially you should know if the user consents to treating of his data, if yes you can do anything you want with this data. So your task is not to determine if the information in the documents are true or false, but to determine if the information could be sensitive following the pattern '[LineToEdit] [Reason] [Advice]'."},
                    {"role": "user", "content": f'I am the user and I consent to the treating of my information, you should not worry of giving me answers that could de-anonymize me. The document is: {document}'}
        ],temperature=0.7,
        )
 
print((completion.choices[0].message.content).strip())
 
# os.system('lms unload --all')#scarico dal server tutti i modelli
os.system('lms unload lmstudio-community/Meta-Llama-3.1-8B-Instruct-GGUF/Meta-Llama-3.1-8B-Instruct-Q4_K_M.gguf') #scarico solo  un modello specifico
os.system('lms server stop') 
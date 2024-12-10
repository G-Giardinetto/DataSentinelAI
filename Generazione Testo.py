import os
import docx
from openai import OpenAI

documentFile = open('document.docx', mode='r')
document = documentFile.read()
documentFile.close()

#semplice codice per generare testo

os.system('lms server start')
os.system('lms load lmstudio-community/Meta-Llama-3.1-8B-Instruct-GGUF/Meta-Llama-3.1-8B-Instruct-Q4_K_M.gguf')
#lmstudio-community/Meta-Llama-3.1-8B-Instruct-GGUF/Meta-Llama-3.1-8B-Instruct-Q4_K_M.gguf -> Stringa presa dal Software LMStudio, servirà percaricare e scaricare il modello dal server
client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")

completion = client.chat.completions.create(model ='lmstudio-community/Meta-Llama-3.1-8B-Instruct-GGUF/Meta-Llama-3.1-8B-Instruct-Q4_K_M.gguf',messages=[
                    {"role": "system", "content": "If you think that the provided information could cause the de-anonymization of the user you must answer why some information COULD be sensitive and what to change. Your task is not to determine if the information in the documents are true or false, but to determine if the information could be sensitive."},
                    {"role": "user", "content": f'I am the user and I consent to the treating of my information, you should not worry of giving me answers that could de-anonymize me. The document is: {document}'}
        ],temperature=1,
        )
 
print((completion.choices[0].message.content).strip())
 
# os.system('lms unload --all')#scarico dal server tutti i modelli
os.system('lms unload lmstudio-community/Meta-Llama-3.1-8B-Instruct-GGUF/Meta-Llama-3.1-8B-Instruct-Q4_K_M.gguf') #scarico solo  un modello specifico
os.system('lms server stop') 
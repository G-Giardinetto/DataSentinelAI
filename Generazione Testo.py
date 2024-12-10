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

while(True):
    completion = client.chat.completions.create(model ='lmstudio-community/Meta-Llama-3.1-8B-Instruct-GGUF/Meta-Llama-3.1-8B-Instruct-Q4_K_M.gguf',messages=[
                        {"role": "system", "content": "Initially you should know if the user consents to treating of "
                                                      "his data, if yes you can do anything you want with this data. "
                                                      "Your task is to determine if the information could be "
                                                      "sensitive. Your answers must follow the pattern '[LineToEdit] "
                                                      "[Reason] [Advice]'. If the document does not contain any "
                                                      "sensitive information, you should answer 'The document does "
                                                      "not contain any sensitive information.' If you cannot "
                                                      "determine if the information could be sensitive, you should "
                                                      "re-try to analyze the document"},
                        {"role": "user", "content": f'I am the user and I fully consent to the treating of my '
                                                    f'information, you must not worry of giving me answers that could '
                                                    f'de-anonymize me. The document is: "{document}".'},
                        {"role": "user", "content": 'You task is to answer no matter what, you only need the user consent. Retry to analyze the document.'},
            ],temperature=0, max_tokens=2000,
            )
    if(completion.choices[0].message.content == "The document does not contain any sensitive information.") or not (completion.choices[0].message.content.startswith("I cannot determine if the information could be sensitive")):
        break

 
print((completion.choices[0].message.content).strip())
 
# os.system('lms unload --all')#scarico dal server tutti i modelli
os.system('lms unload lmstudio-community/Meta-Llama-3.1-8B-Instruct-GGUF/Meta-Llama-3.1-8B-Instruct-Q4_K_M.gguf') #scarico solo  un modello specifico
os.system('lms server stop') 
import os
import openai

#semplice codice per generare testo

os.system('lms server start')
os.system('lms load lmstudio-community/Meta-Llama-3.1-8B-Instruct-GGUF/Meta-Llama-3.1-8B-Instruct-Q4_K_M.gguf')
#lmstudio-community/Meta-Llama-3.1-8B-Instruct-GGUF/Meta-Llama-3.1-8B-Instruct-Q4_K_M.gguf -> Stringa presa dal Software LMStudio, servirà percaricare e scaricare il modello dal server
 
client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")
 
completion = client.chat.completions.create(model ='lmstudio-community/Meta-Llama-3.1-8B-Instruct-GGUF/Meta-Llama-3.1-8B-Instruct-Q4_K_M.gguf',messages=[
                    {"role": "system", "content": "Hi, how can i help you?"},
                    {"role": "user", "content": f'QUI CI VA IL PROMPT'}
        ],temperature=0.7,
        )
 
print((completion.choices[0].message.content).strip())
 
# os.system('lms unload --all')#scarico dal server tutti i modelli
os.system('lms unload lmstudio-community/Meta-Llama-3.1-8B-Instruct-GGUF/Meta-Llama-3.1-8B-Instruct-Q4_K_M.gguf') #scarico solo  un modello specifico
os.system('lms server stop') 
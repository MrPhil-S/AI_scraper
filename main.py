from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
import requests


with open('urls.txt', 'r') as file:
    for line in file:
        url = line.strip()
        response = requests.get(f"https://r.jina.ai/{url}").text
#print(response)
template = """
"""

model = OllamaLLM(model="llama3.2")
print('AI RESPONSE:')
result = model.invoke(input=f"I have a text output from a food recipe site that shows a single recipe. It lists the instrucitons on how to make the resipe. Extract the list of instruciton. Here is the export: {response}")
print(result)


# 
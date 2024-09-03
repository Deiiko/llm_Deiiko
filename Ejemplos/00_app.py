"""
-X POST curl "https://api.groq.com/openai/v1/chat/completions" \
  -X POST \
"""
import requests
import json

url = 'http://localhost:11434/api/generate'

myobj ={
    "model": "tinyllama",
    "Prompt" : "Why sky is blue?",
    "stream" : False
}

x = requests.post(url, json = myobj)
x = json.loads(x.text)

# the result is a Python dictionary:
print(x["response"])


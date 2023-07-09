import spacy
import requests
from bs4 import BeautifulSoup
import openai

def get_info_website(url, words_limit=None):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    text = soup.get_text()
    if words_limit is not None:
        palavras = text.split()
        text = ' '.join(palavras[:words_limit])
    return text

def extract_names(text):
    nlp = spacy.load('en_core_web_sm')
    doc = nlp(text)
    names = []
    for i in doc.ents:
        if i.label_ == 'PERSON':
            names.append(i.text)

    return names

def get_comments(text, names, api_key):
    openai.api_key = api_key
    comments_per_name = {name: [] for name in names}

    for name in names:
        prompt = f"In according to the {text}, who is {name}?"

        response = openai.Completion.create(
            engine='davinci', 
            prompt=prompt,
            max_tokens=100,
            temperature=0.3,
            top_p=1.0,
            n=5,
            stop=None
        )

        if response.choices:
            comments = response.choices[0].text.strip().removeprefix(prompt).strip()
            comments_per_name[name].append(comments)

    return comments_per_name

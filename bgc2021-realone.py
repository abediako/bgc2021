'''
loads the text from the website of a fashion brand 
Then queries the classifications from the IBM Cloud Natural Language Classifier
Determines if any brand is ethical or unethical based on the wording of its website
'''

import json
import nltk
import re
import requests
import sys
from bs4 import BeautifulSoup
from ibm_watson import NaturalLanguageClassifierV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

apikey = sys.argv[1] 

url = 'https://www.converse.com/'
resp = requests.get(url)
soup = BeautifulSoup(resp.text, 'html.parser')
text = soup.get_text().lower()
list_of_words = nltk.tokenize.casual_tokenize(text)
string_of_words = " ".join(list_of_words)
alnum_only = re.sub(r'[^a-zA-Z ]', '', string_of_words)
feature_text = alnum_only[:1024]

authenticator = IAMAuthenticator(apikey)
natural_language_classifier = NaturalLanguageClassifierV1(
    authenticator=authenticator
)

natural_language_classifier.set_service_url('https://api.us-east.natural-language-classifier.watson.cloud.ibm.com/instances/5d3ee9bb-3a90-440f-8196-e0f26cf636a1/v1/classifiers/f1985cx420-nlc-42')
classes = natural_language_classifier.classify(
    'f1985cx420-nlc-42',
    feature_text).get_result()
print(json.dumps(classes, indent=2))
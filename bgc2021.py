import json
from ibm_watson import NaturalLanguageClassifierV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator('SLl2P-MG2kXAlI6H8kbOS3mRh4qMGyfW1kNKOBmqA6Qp')
natural_language_classifier = NaturalLanguageClassifierV1(
    authenticator=authenticator
)

natural_language_classifier.set_service_url('https://api.us-east.natural-language-classifier.watson.cloud.ibm.com/instances/5d3ee9bb-3a90-440f-8196-e0f26cf636a1')
classes = natural_language_classifier.classify(
    'f1985cx420-nlc-42',
    'sale').get_result()
print(json.dumps(classes, indent=2))

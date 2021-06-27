# fashionably late
Black Girls Code Team 12 Submission

The query is in the bgc2021-realone.py file. 

The information used for the IBM Natural Language Classifier is in this file: https://github.com/IBM-CfC-BGC-2021-Team12/ethical-fashion-classifier .

# Description of fashionably late:
Fast fashion is a phenomenon that has taken consumerism by storm these past few years and its effects on the Earth have been catastrophic. Even though some consumers may be aware of the effects of their cheap consumerism, they do not have the resources to make better decisions that will benefit them. Our intended users are consumers that are young, targeted by fast fashion, care about the environment, and can’t afford good quality clothes for their price range.

Our solution was to develop an app that provides information about fast fashion, what consumers can do to stop contributing to it, and alternatives to fast fashion. Our main feature is a scanner that utilizes an IBM Natural Language Classifier to allow consumers to know if the brands they are buying from are ethical or unethical.

We decided to go with the IBM Natural Language Classifier because we wanted a feature where consumers would be able to scan the tag of clothes and be able to easily access the needed information. Once the scanner recognizes the brand name, the app will find the brand's web site, extract text from the brand's home page, and send that text to the IBM Cloud Natural Language classifier, which returns a prediction of the ethical status of the brand based on the text.

# Refer to API : https://googleapis.github.io/google-cloud-python/latest/language/usage.html
# https://cloud.google.com/natural-language/docs/reference/rest/v1/documents/classifyText

# Imports the Google Cloud client library
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types

def analyzeclass(tweettext): 
    client = language.LanguageServiceClient()
    print('************************Classify Testing Start**************************************************')
    # The text to analyze
    # text = u'i feel so happy and joyful!'
    text6 = tweettext
    document6 = types.Document(
        content=text6,
        language = 'en_US',
        type=enums.Document.Type.PLAIN_TEXT)
        # Detects the sentiment of the text
    # if there's any error , just retrun false back 
    try: 
        response6 = client.classify_text(document=document6)
    except: 
        return False 
    
    # if there's no exception, it continues to check the response value from GCP NLP
    # if the response is empty, return false, otherwise return the category 

    classind = False 
    for entity in response6.categories:
        print('=' * 20)
        classind = True 
        print('categories: {0}'.format(entity))
        a  = entity 
        print ('a value is',type(a),a.name,a.confidence)
    if classind == True :
        return a
    return False 
    print('************************Classify Testing End**************************************************')

#tweettext ='Google, headquartered in Mountain View (1600 Amphitheatre Pkwy, Mountain View, CA 940430), unveiled the new Android phone for $799 at the Consumer Electronic Show. Sundar Pichai said in his keynote that users love their new Android phones.'
#analyzeclass(tweettext)

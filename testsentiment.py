# Refer to API : https://googleapis.github.io/google-cloud-python/latest/language/usage.html
# https://cloud.google.com/natural-language/docs/reference/rest/v1/documents/classifyText

# Imports the Google Cloud client library
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types


def analyzesentiment(tweettext): 
    # Instantiates a client
    client = language.LanguageServiceClient()
    print('************************1.Sentiment Testing Start **************************************************')
    # The text to analyze
    #text = u'i feel so happy and joyful!'
    text = tweettext
    #text = u'Google, headquartered in Mountain View (1600 Amphitheatre Pkwy, Mountain View, CA 940430), unveiled the new Android phone for $799 at the Consumer Electronic Show. Sundar Pichai said in his keynote that users love their new Android phones.'
    document = types.Document(
        content=text,
        type=enums.Document.Type.PLAIN_TEXT)

    # Detects the sentiment of the text
    try: 
        sentiment = client.analyze_sentiment(document=document).document_sentiment
    except:
        return False 
    print('Text: {}'.format(text))
    print('Sentiment(score,magnitude): {}, {}'.format(sentiment.score, sentiment.magnitude))
    print(type(sentiment.score),sentiment.score)
    print(type(sentiment.magnitude),sentiment.magnitude)
    print('************************1.Sentiment Testing End**************************************************')
    return sentiment 
#analyzeclass('I feel so happy and joyful. So I love this world!')
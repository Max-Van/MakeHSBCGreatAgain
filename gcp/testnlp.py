# Refer to API : https://googleapis.github.io/google-cloud-python/latest/language/usage.html
# https://cloud.google.com/natural-language/docs/reference/rest/v1/documents/classifyText

# Imports the Google Cloud client library
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types



# Instantiates a client
client = language.LanguageServiceClient()

print('************************1.Sentiment Testing Start **************************************************')
# The text to analyze
#text = u'i feel so happy and joyful!'
text = 'I feel so happy and joyful. So I love this world!'
#text = u'Google, headquartered in Mountain View (1600 Amphitheatre Pkwy, Mountain View, CA 940430), unveiled the new Android phone for $799 at the Consumer Electronic Show. Sundar Pichai said in his keynote that users love their new Android phones.'
document = types.Document(
    content=text,
    type=enums.Document.Type.PLAIN_TEXT)

# Detects the sentiment of the text
sentiment = client.analyze_sentiment(document=document).document_sentiment

print('Text: {}'.format(text))
print('Sentiment(score,magnitude): {}, {}'.format(sentiment.score, sentiment.magnitude))


# The text to analyze(Chinese)
#text = u'i feel so happy and joyful!'
text2 = '人生如此艰难，生活对我如此不公，我真的非常讨厌这个世界。'
#text = u'Google, headquartered in Mountain View (1600 Amphitheatre Pkwy, Mountain View, CA 940430), unveiled the new Android phone for $799 at the Consumer Electronic Show. Sundar Pichai said in his keynote that users love their new Android phones.'
document2 = types.Document(
    content=text2,
    language = 'zh_CN',
    type=enums.Document.Type.PLAIN_TEXT)

# Detects the sentiment of the text
sentiment2 = client.analyze_sentiment(document=document2).document_sentiment

print('Text: {}'.format(text2))
print('Sentiment(score,magnitude): {}, {}'.format(sentiment2.score, sentiment2.magnitude))

print('************************1.Sentiment Testing End**************************************************')


print('************************2.Entities Testing Start**************************************************')


# The text to analyze
#text = u'i feel so happy and joyful!'
text3 = 'President Lincoln delivered the 272 word Gettysburg Address on November 19, 1863 on the battlefield near Gettysburg, Pennsylvania.'
#text = u'Google, headquartered in Mountain View (1600 Amphitheatre Pkwy, Mountain View, CA 940430), unveiled the new Android phone for $799 at the Consumer Electronic Show. Sundar Pichai said in his keynote that users love their new Android phones.'
document3 = types.Document(
    content=text3,
    type=enums.Document.Type.PLAIN_TEXT)

# Detects the sentiment of the text
response = client.analyze_entities(document=document3)

for entity in response.entities:
    print('=' * 20)
    print('         name: {0}'.format(entity.name))
    print('         type: {0}'.format(entity.type))
    print('     metadata: {0}'.format(entity.metadata))
    print('     salience: {0}'.format(entity.salience))


# The text to analyze
#text = u'i feel so happy and joyful!'
text4 = '我爱北京天安门，天安门上太阳升。伟大领袖毛泽东，指引我们向前进。'
#text = u'Google, headquartered in Mountain View (1600 Amphitheatre Pkwy, Mountain View, CA 940430), unveiled the new Android phone for $799 at the Consumer Electronic Show. Sundar Pichai said in his keynote that users love their new Android phones.'
document4 = types.Document(
    content=text4,
    type=enums.Document.Type.PLAIN_TEXT)

# Detects the sentiment of the text
response4 = client.analyze_entities(document=document4)

for entity in response4.entities:
    print('=' * 20)
    print('         name: {0}'.format(entity.name))
    print('         type: {0}'.format(entity.type))
    print('     metadata: {0}'.format(entity.metadata))
    print('     salience: {0}'.format(entity.salience))

print('************************2.Entities Testing End**************************************************')

print('************************3.Entitity-Sentiment Testing Start**************************************************')


# The text to analyze
#text = u'i feel so happy and joyful!'
text5 = 'Mona said that jogging is very fun.'
#text = u'Google, headquartered in Mountain View (1600 Amphitheatre Pkwy, Mountain View, CA 940430), unveiled the new Android phone for $799 at the Consumer Electronic Show. Sundar Pichai said in his keynote that users love their new Android phones.'
document5 = types.Document(
    content=text5,
    language = 'en_US',
    type=enums.Document.Type.PLAIN_TEXT)

# Detects the sentiment of the text
response5 = client.analyze_entity_sentiment(document=document5)

for entity in response5.entities:
    print('=' * 20)
    print('         name: {0}'.format(entity.name))
    print('         sentiment.magnitude: {0}'.format(entity.sentiment.magnitude))
    print('     sentiment.score: {0}'.format(entity.sentiment.score))


print('************************3.Entitity-Sentiment Testing End**************************************************')

print('************************4.Classify Testing Start**************************************************')



# The text to analyze
#text = u'i feel so happy and joyful!'
text6 = 'Google, headquartered in Mountain View (1600 Amphitheatre Pkwy, Mountain View, CA 940430), unveiled the new Android phone for $799 at the Consumer Electronic Show. Sundar Pichai said in his keynote that users love their new Android phones.'
#text = u'Google, headquartered in Mountain View (1600 Amphitheatre Pkwy, Mountain View, CA 940430), unveiled the new Android phone for $799 at the Consumer Electronic Show. Sundar Pichai said in his keynote that users love their new Android phones.'
document6 = types.Document(
    content=text6,
    language = 'en_US',
    type=enums.Document.Type.PLAIN_TEXT)

# Detects the sentiment of the text
response6 = client.classify_text(document=document6)

for entity in response6.categories:
    print('=' * 20)
    print('         categories: {0}'.format(entity))

print('************************4.Classify Testing End**************************************************')


print('************************5.Bulk-Process Testing Start**************************************************')

#  document = {"gcs_content_uri": gcs_content_uri, "type": type_, "language": language}

# document7 = types.Document(
#     gcs_content_uri='https://storage.googleapis.com/maxtweettst/trump-tw.txt',
#     type=enums.Document.Type.PLAIN_TEXT)



# # Detects the sentiment of the text
# sentiment7 = client.analyze_sentiment(document=document7).document_sentiment

# print('Text: {}'.format(text))
# print('Sentiment(score,magnitude): {}, {}'.format(sentiment7.score, sentiment7.magnitude))

print('************************Bulk-Process Testing End**************************************************')













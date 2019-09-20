import json
from ibm_watson import ToneAnalyzerV3

def testtone(tweettext):
    tone_analyzer = ToneAnalyzerV3(
    version='2017-09-21',
    iam_apikey='N07MuzLARtF0AVKnRv19KfBABJusMoRRoo1ePVnKeQkY',
    url='https://gateway.watsonplatform.net/tone-analyzer/api'
    )

# text = 'Team, I know that times are tough! Product '\
#     'sales have been disappointing for the past three '\
#     'quarters. We have a competitive product, but we '\
#     'need to do a better job of selling it!'
    text = tweettext
    try:
        tone_analysis = tone_analyzer.tone(
            {'text': text},
            content_type='application/json'
            ).get_result()
        print('*************tone analysis successful*******************')
        print(json.dumps(tone_analysis, indent=2))
        print(tone_analysis['document_tone']['tones'])
        if len(tone_analysis['document_tone']['tones']) == 0 :
            print('result is empty!')
            return False 
        else :
            print(json.dumps(tone_analysis, indent=2))
            return tone_analysis['document_tone']['tones']
    except ApiException as ex:
        print ('Method failed with status code ' + str(ex.code) + ': ' + ex.message)
        return False 

b=testtone('i hate you')

if b == False :
    print ('analysis result is empty ')
else :
    print (b)
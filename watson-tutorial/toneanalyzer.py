import json
from ibm_watson import ToneAnalyzerV3

tone_analyzer = ToneAnalyzerV3(
    version='2017-09-21',
    iam_apikey='N07MuzLARtF0AVKnRv19KfBABJusMoRRoo1ePVnKeQkY',
    url='https://gateway.watsonplatform.net/tone-analyzer/api'
)

# text = 'Team, I know that times are tough! Product '\
#     'sales have been disappointing for the past three '\
#     'quarters. We have a competitive product, but we '\
#     'need to do a better job of selling it!'
text = 'you'

tone_analysis = tone_analyzer.tone(
    {'text': text},
    content_type='application/json'
).get_result()
print(json.dumps(tone_analysis, indent=2))
print(tone_analysis)
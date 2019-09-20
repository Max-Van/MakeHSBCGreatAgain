IBM Watson NLP Investigation 
============

## Two Testings

* Tone Analyzer
* NLP(Analyse Twitter) with IBM Cloud


### Tone Analyzer  

* General tone analyzer 
* Customer-Engagement tone(it's used for chatbot)

According to [API Doc](https://cloud.ibm.com/apidocs/tone-analyzer?code=python)

it can analyze follwoing **tone id** : 
anger, fear, joy, and sadness (emotional tones); analytical, confident, and tentative

and **tone score** : 
The score that is returned lies in the range of 0.5 to 1. A score greater than 0.75 indicates a high likelihood that the tone is perceived in the content.

Find one sample : 

~~~python
text = 'Team, I know that times are tough! Product '\
    'sales have been disappointing for the past three '\
    'quarters. We have a competitive product, but we '\
    'need to do a better job of selling it!'

tone_analysis = tone_analyzer.tone(
    {'text': text},
    content_type='application/json'
).get_result()
print(json.dumps(tone_analysis, indent=2))
~~~

Result :
~~~json
{
  "document_tone": {
    "tones": [
      {
        "score": 0.6165,
        "tone_id": "sadness",
        "tone_name": "Sadness"
      },
      {
        "score": 0.829888,
        "tone_id": "analytical",
        "tone_name": "Analytical"
      }
    ]
  },
  "sentences_tone": [
    {
      "sentence_id": 0,
      "text": "Team, I know that times are tough!",
      "tones": [
        {
          "score": 0.801827,
          "tone_id": "analytical",
          "tone_name": "Analytical"
        }
      ]
    },
    {
      "sentence_id": 1,
      "text": "Product sales have been disappointing for the past three quarters.",
      "tones": [
        {
          "score": 0.771241,
          "tone_id": "sadness",
          "tone_name": "Sadness"
        },
        {
          "score": 0.687768,
          "tone_id": "analytical",
          "tone_name": "Analytical"
        }
      ]
    },
    {
      "sentence_id": 2,
      "text": "We have a competitive product, but we need to do a better job of selling it!",
      "tones": [
        {
          "score": 0.506763,
          "tone_id": "analytical",
          "tone_name": "Analytical"
        }
      ]
    }
  ]
}
~~~

It can do following four analysis :

* [Analyzing Sentiment](https://cloud.google.com/natural-language/docs/analyzing-sentiment)
* [Analyzing Entities](https://cloud.google.com/natural-language/docs/analyzing-entities)
* [Analyzing Syntax](https://cloud.google.com/natural-language/docs/analyzing-syntax)
* [Classifying Content](https://cloud.google.com/natural-language/docs/classifying-text)


#### analyze-entities

~~~bash
gcloud ml language analyze-entities --content="Michelangelo Caravaggio, Italian painter, is known for 'The Calling of Saint Matthew'."
~~~

The result is 

~~~json
{
  "entities": [
    {
      "mentions": [
        {
          "text": {
            "beginOffset": 0,
            "content": "Michelangelo Caravaggio"
          },
          "type": "PROPER"
        },
        {
          "text": {
            "beginOffset": 33,
            "content": "painter"
          },
          "type": "COMMON"
        }
      ],
      "metadata": {
        "mid": "/m/020bg",
        "wikipedia_url": "https://en.wikipedia.org/wiki/Caravaggio"
      },
      "name": "Michelangelo Caravaggio",
      "salience": 0.82904786,
      "type": "PERSON"
    },
    {
      "mentions": [
        {
          "text": {
            "beginOffset": 25,
            "content": "Italian"
          },
          "type": "PROPER"
        }
      ],
      "metadata": {},
      "name": "Italian",
      "salience": 0.13981608,
      "type": "LOCATION"
    },
    {
      "mentions": [
        {
          "text": {
            "beginOffset": 56,
            "content": "The Calling of Saint Matthew"
          },
          "type": "PROPER"
        }
      ],
      "metadata": {
        "mid": "/m/085_p7",
        "wikipedia_url": "https://en.wikipedia.org/wiki/The_Calling_of_St_Matthew_(Caravaggio)"
      },
      "name": "The Calling of Saint Matthew",
      "salience": 0.031136045,
      "type": "EVENT"
    }
  ],
  "language": "en"
}
~~~


#### analyze-entity-sentiment

~~~bash
gcloud ml language analyze-entity-sentiment --content="Michelangelo Caravaggio, Italian painter, is known for 'The Calling of Saint Matthew'."
~~~

The result is 

~~~json
{
  "entities": [
    {
      "mentions": [
        {
          "sentiment": {
            "magnitude": 0.2,
            "score": -0.2
          },
          "text": {
            "beginOffset": 0,
            "content": "Michelangelo Caravaggio"
          },
          "type": "PROPER"
        },
        {
          "sentiment": {
            "magnitude": 0.0,
            "score": 0.0
          },
          "text": {
            "beginOffset": 33,
            "content": "painter"
          },
          "type": "COMMON"
        }
      ],
      "metadata": {
        "mid": "/m/020bg",
        "wikipedia_url": "https://en.wikipedia.org/wiki/Caravaggio"
      },
      "name": "Michelangelo Caravaggio",
      "salience": 0.82904786,
      "sentiment": {
        "magnitude": 0.2,
        "score": -0.1
      },
      "type": "PERSON"
    },
    {
      "mentions": [
        {
          "sentiment": {
            "magnitude": 0.0,
            "score": 0.0
          },
          "text": {
            "beginOffset": 25,
            "content": "Italian"
          },
          "type": "PROPER"
        }
      ],
      "metadata": {},
      "name": "Italian",
      "salience": 0.13981608,
      "sentiment": {
        "magnitude": 0.0,
        "score": 0.0
      },
      "type": "LOCATION"
    },
    {
      "mentions": [
        {
          "sentiment": {
            "magnitude": 0.0,
            "score": 0.0
          },
          "text": {
            "beginOffset": 56,
            "content": "The Calling of Saint Matthew"
          },
          "type": "PROPER"
        }
      ],
      "metadata": {
        "mid": "/m/085_p7",
        "wikipedia_url": "https://en.wikipedia.org/wiki/The_Calling_of_St_Matthew_(Caravaggio)"
      },
      "name": "The Calling of Saint Matthew",
      "salience": 0.031136045,
      "sentiment": {
        "magnitude": 0.0,
        "score": 0.0
      },
      "type": "EVENT"
    }
  ],
  "language": "en"
}
~~~



#### analyze-sentiment

~~~bash
gcloud ml language analyze-sentiment --content="I feel so happy and joyful. So I love this world so much."
~~~

The result is 

~~~json
{
  "documentSentiment": {
    "magnitude": 1.8,
    "score": 0.9
  },
  "language": "en",
  "sentences": [
    {
      "sentiment": {
        "magnitude": 0.9,
        "score": 0.9
      },
      "text": {
        "beginOffset": 0,
        "content": "I feel so happy and joyful."
      }
    },
    {
      "sentiment": {
        "magnitude": 0.8,
        "score": 0.8
      },
      "text": {
        "beginOffset": 28,
        "content": "So I love this world so much."
      }
    }
  ]
}
~~~



#### analyze-syntax

~~~bash
gcloud ml language analyze-syntax --content="Fourscore and seven years ago our fathers brought forth, on this continent, a new nation, conceived in liberty, and dedicated to the proposition that all men are created equal."
~~~


#### classify-text


~~~bash
gcloud ml language classify-text --content="Google, headquartered in Mountain View (1600 Amphitheatre Pkwy, Mountain View, CA 940430), unveiled the new Android phone for $799 at the Consumer Electronic Show. Sundar Pichai said in his keynote that users love their new Android phones."
~~~


The result is 

~~~json
{
  "categories": [
    {
      "confidence": 0.52,
      "name": "/Internet & Telecom/Mobile & Wireless"
    }
  ]
}
~~~


### NLP With IBM Watson  


According to [Guideline](https://github.com/IBM/cognitive-social-crm?cm_sp=Developer-_-analyze-twitter-handles-and-hashtags-for-sentiment-and-content-_-Get-the-Code)

It can analyze any twitter(I set it as realDonaldTrump now, it can be changed to any twitter handle or hashtag). 
i follow the guideline and it's working 
![IBM Cloud](https://cdn-std.droplr.net/files/acc_136293/l4O7n1)

your guys can visit [it here](https://cognitive-social-crm-noisy-kudu.mybluemix.net)

![Twitter Analysis](https://cdn-std.droplr.net/files/acc_136293/H6BiBn)


Max

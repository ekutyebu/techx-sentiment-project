from textblob import TextBlob

# --GETS SENTIMENT --
def get_sentiment(text):
    # -- CHECKS IF INPUT IS VALID --
    if not isinstance(text, str):
        print(f'\nInvalid : ${text} - is not a string\n')
    if not text.strip():
        print("Invalid : Empty imput\n")

    
    # -- ANALIZING SSENTIMENT --
    word = TextBlob(text)
    wordPolarity = word.sentiment.polarity #type:ignore

    if wordPolarity > 0.1:
        return 'Positive'
    elif wordPolarity < -0.1:
        return 'Negative'
    else:
        return 'Neutral'

# -- SHOW SENTIMENT AND SENTENCE --
sentence = input("\nEnter a sentence: ")
print(f'{sentence} has a {get_sentiment(sentence)} sentiment.')
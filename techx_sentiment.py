from textblob import TextBlob
import ast

# --GETS SENTIMENT --
def get_sentiment(text):
    # -- CHECKS IF INPUT IS VALID --
    if not isinstance(text, str):
        return f'\nInvalid : {text} - is not a string\n'
    if not text.strip():
        return "Invalid : Empty input\n"

    
    # -- ANALYZING SENTIMENT --
    word = TextBlob(text)
    wordPolarity = word.sentiment.polarity #type:ignore

    if wordPolarity > 0.1:
        return 'Positive'
    elif wordPolarity < -0.1:
        return 'Negative'
    else:
        return 'Neutral'

# -- SHOW SENTIMENT AND SENTENCE --
user_input = input("\nEnter a sentence: ")

# -- ENSURE INPUT DATATYPE DON'T CHANGE --
try:
    sentence = ast.literal_eval(user_input)
except (ValueError, SyntaxError):
    
    sentence = user_input

print(f"\n'{sentence}' has a {get_sentiment(sentence)} sentiment\n")
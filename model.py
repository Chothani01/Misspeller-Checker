from textblob import TextBlob

def process(text): 
    text = text.split()
    new_text = []
    errors = []
    for word in text:
        new_word = str(TextBlob(word).correct())
        new_text.append(new_word)
        if word != new_word:
            errors.append(word)
    
    errors.append(len(errors))
    return " ".join(new_text), errors

    
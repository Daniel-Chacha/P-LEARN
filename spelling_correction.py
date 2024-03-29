from textblob import TextBlob

text=TextBlob('I have a guud idea about yuo')

new_text=text.correct()

print(text)
print(new_text)
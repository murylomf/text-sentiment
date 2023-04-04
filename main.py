from textblob import TextBlob

text = input("Digite seu texto: ")
blob = TextBlob(text)

polarity = blob.sentiment.polarity
print(polarity)
print(blob.json)
if polarity > 0:
    print("O texto expressa um sentimento positivo.")
elif polarity == 0:
    print("O texto expressa um sentimento neutro.")
else:
    print("O texto expressa um sentimento negativo.")
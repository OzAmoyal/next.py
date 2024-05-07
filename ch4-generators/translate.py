def translate(sentence):
    words = {'esta': 'is', 'la': 'the', 'en': 'in', 'gato': 'cat', 'casa': 'house', 'el': 'the'}
    divide = (word for word in sentence.split())
    gen_translate = (words[word] for word in divide)
    string = ""
    for translate in gen_translate:
        string +=translate +" "
    return string

print(translate("el gato esta en la casa"))


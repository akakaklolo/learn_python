def pig_latin(text):
    say = ""
    # Separate the text into words
    words = text.split()
    new_words = []
    for word in words:
        # Create the pig latin word and add it to the list
        new_word = word[1:] + word[0] + "ay"
        new_words.append(new_word)
    # Turn the list back into a phrase
    say = ' '.join(new_words)
    return say

print(pig_latin("hello how are you")) # "ellohay owhay reaay ouyay"
print(pig_latin("programming in python is fun")) # "rogrammingpay niay ythonpay siay unfay"

def pig_latin(phrase):
    """Turn a phrase into pig latin.

    There will be no uppercase letters or punctuation in the phrase.

        >>> pig_latin('hello awesome programmer')
        'ellohay awesomeyay rogrammerpay'
    """

    words = phrase.split()
    pig_latin = []
    for word in words:
        if word[0] in ['a', 'e','i', 'o', 'u']:
            word = word + 'yay'
        else:
            word = word + word[0]
            word = word[1:] + 'ay'
        pig_latin.append(word)

    pig_latin_phrase = " ".join(pig_latin)

    return pig_latin_phrase

print pig_latin("hello awesome programmer")
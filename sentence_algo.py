sentence = "policemen wear   blue  especially on  Thursdays."


def sentence_reverse(any_string):
    """Given a string with any number of spaces and words, returns the sentence reversed.

    >>> sentence_reverse("policemen wear   blue  especially on  Thursdays.")
    'Thursdays.  on especially  blue   wear policemen'
    """

    sent_list = diff_sentence.split(" ")
    sent_list.reverse()

    reversed_sentence = " ".join(sent_list)
    return reversed_sentence


print sentence_reverse(sentence)
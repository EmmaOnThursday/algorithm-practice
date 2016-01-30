sentence = "policemen wear   blue  especially on  Thursdays."

# replace spaces with another character + space
# split on other character & append all to list
# reverse list
# join reversed list


def sentence_reverse(any_string):
    """Given a string with any number of spaces and words, returns the sentence reversed.

    >>> sentence_reverse("policemen wear   blue  especially on  Thursdays.")
    ' Thursdays.  on especially  blue   wearpolicemen'
    """
    diff_sentence = sentence.replace(" ", "# ")
    sent_list = diff_sentence.split("#")
    sent_list.reverse()

    reversed_sentence = "".join(sent_list)
    return reversed_sentence

""" Word Search: given a 2-d array, figure out if a word exists in the array. 
Word can be vertical or horizontal.

EX:
[ [g, h, t, y, a],
  [k, j, r, s, p],
  [b, h, t, q, p],
  [l, h, e, c, l],
  [b, k, o, i, e] ]

word: apple

GIVEN: no blanks; all arrays are the same length

"""

def word_search(array, apple):

    for lst in array:
        if word in "".join(lst):
            return True

    # make as many new lists as there are items in each list
    # unpack list items in order into those new lists

    for lst in array:


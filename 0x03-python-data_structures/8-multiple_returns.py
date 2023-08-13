#!/usr/bin/python3
def multiple_returns(sentence):

    str_len = len(sentence)
    if str_len == 0:
        first_letter = None
    else:
        first_letter = sentence[0]

    return str_len, first_letter

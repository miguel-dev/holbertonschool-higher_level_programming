#!/usr/bin/python3


def multiple_returns(sentence):
    if not sentence:
        return None
    elif sentence == "":
        return 0, None
    else:
        return len(sentence), sentence[0]

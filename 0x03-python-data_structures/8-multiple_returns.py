#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence is None:
        return (None, 0)

    return (len(sentence), sentence[0])

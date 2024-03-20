#!/usr/bin/python3


def best_score(a_dictionary):
    student = []
    score = []

    if a_dictionary is None or len(a_dictionary) == 0:
        return None

    for key, value in a_dictionary.items():
        student.append(key)
        score.append(value)

    best = max(score)
    index = score.index(best)

    return student[index]

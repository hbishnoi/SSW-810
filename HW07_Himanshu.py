'''wroking with different type of methods to use dictionaries, tuples, list and set'''
from collections import defaultdict, Counter    
from typing import DefaultDict, Counter, List, Tuple


def anagrams_lst(str1: str, str2: str) -> bool:
    '''checking if two given strings are anagrams or not'''
    return sorted(str1.lower()) == sorted(str2.lower())


def anagrams_dd(str1: str, str2: str) -> bool:
    '''checking if two given strings are anagrams or not by method defaultdict'''
    dd: DefaultDict[str, int] = defaultdict(int)
    for i in str1.lower():
        dd[i] += 1

    for c in str2.lower():
        dd[c] -= 1

    return not any(dd.values())


def anagrams_cntr(str1: str, str2: str) -> bool:
    '''checking if two given strings are anagrams or not by method Counter'''
    return Counter(str1.lower()) == Counter(str2.lower())


def covers_alphabet(sentence: str) -> bool:
    '''determine if input string contains all the alphabets'''
    return set('abcdefghijklmnopqrstuvwxyz') <= set(sentence.lower())                                                   # method 1

    # return sorted('abcdefghijklmnopqrstuvwxyz') == sorted(set((''.join(e for e in sentence if e.isalpha())).lower())) # method 2

    # return set("abcdefghijklmnopqrstuvwxyz").issubset(set(sentence.lower()))                                          # method 3



def web_analyzer(weblogs: List[Tuple[str, str]]) -> List[Tuple[str, List[str]]]:
    '''using defaultdict to determine which website is used by which person'''
    dd_wa: DefaultDict[Tuple[str, List[str]]] = defaultdict(set)
    for first, second in weblogs:
        dd_wa[second] = dd_wa[second].union({first})                                # method 1

        # dd_wa[second].add(first)                                                  # method 2
    return sorted([tuple([key, sorted(value)]) for key, value in dd_wa.items()])

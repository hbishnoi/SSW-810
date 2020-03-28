'''working on generators in this assignment'''

from typing import Sequence, Optional, Any, Iterator, Tuple

def count_vowels(s: str) -> int:
    '''count vowels in a string'''
    count: int = 0
    try:
        s: str = s.lower()
        for i in s:
            if i in ['a','e','i','o','u']:
                count += 1
        return count
    except:
        raise ValueError('input is not string')
        # return None

def last_occurrence(target: Any, sequence: Sequence[Any]) -> Optional[int]:
    '''last occurence of the target value in a sequence'''
    last: Optional[int] = None
    for offset, i in enumerate(sequence):
        if i == target:
            last = offset
    return last

# def my_enumerate(seq: Sequence[Any]) -> Iterator[Any]:
def my_enumerate(seq: Sequence[Any]) -> Iterator[Tuple[int, Any]]:
    '''creating enumerate in built function'''
    # len_seq: int = len(seq)
    for i in range(len(seq)):
        yield i, seq[i]

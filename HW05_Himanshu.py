'''working with strings'''
from typing import IO, Iterator

# def reverse_string(inp: str) -> str:
#     new_str = ''
#     # char = inp[::-1]:
#     if inp == '':
#         raise ValueError('empty string')
#     else:
#         for char in inp:
#             new_str = char + new_str
            
#             # print(char)
#         return new_str

def reverse_string(inp: str) -> str:
    '''reversing the input string'''
    new_str: str = ''
    try:
        for i in range(len(inp)-1,-1,-1):
            new_str += inp[i]
        return new_str
    except:
        raise ValueError('input is not a string')


def sub_string(target: str, main_string: str) -> int:
    '''checking if target substring is in main string and where it is'''
    
    # if main_string and target and target in main_string: # if main_string and target are not empty and target is in main_string
    #     count: int = 0
    #     for offset, char in enumerate(main_string):
    #         if target[0] == char:
    #             new_string: str = main_string[offset : offset + len(target)]
    #             if target ==  new_string:
    #                 count: int = offset
    #         return count
    # else:
    #     return -1

    # for i in range(len(main_string) - len(target) + 1):
    #     if main_string[i:i+len(target)] == target:
    #         return i
    # return -1

    return main_string.find(target, main_string.find(target) + 1)

print(sub_string('he', 'hello'))

def find_second(target: str, string: str) -> int:
    '''checking if target substring is in main string twice or more and return the positon of the second'''

    count: int = string.find(target, 0)
    if target in string[count + 1: ]:
        new_count: int = string.find(target, count + 1)
        return new_count
    else:
        return -1


def get_lines(path: str) -> Iterator[str]:
    '''open file and reading lines step by step'''
    try:
        fp: IO = open(path, 'r', encoding='utf-8')
    except FileNotFoundError:
        raise FileNotFoundError(f"Can not open {path}")
        # print (f"Can not open {path}")
    else:
        with fp:
            for line in fp:
                # line: str = line.strip('\n')
                line: str = line.rstrip('\n')
                # line: str = line.strip()

                while line.endswith("\\"):
                    # line: str = line.strip("\\\n") + fp.readline().strip("\n")
                    # line: str = line.strip("\\\n") + fp.readline().rstrip("\n")
                    line: str = line[:-1] + next(fp).rstrip("\n") # strip the trailing  \ and join with the next line


                # if line == '':
                #     continue

                # here, lines have been combined so look for a comment

                if not line.startswith('#'):
                    yield line.split('#')[0] # split returns a list with everything before the #
                    
                # if '#' in line:
                #     if line.startswith('#'):
                #         continue
                #     else:
                #         line: str = line.split('#', maxsplit=1)[0]
                # yield line

# print(list(get_lines('test1.txt')))
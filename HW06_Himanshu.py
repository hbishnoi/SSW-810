from typing import Any, List, Optional

'''making several list functions'''

def list_copy(l: List[Any]) -> List[Any]:
    '''copying list to new list'''
    return [element for element in l]


def list_intersect(l1: List[Any], l2: List[Any]) -> List[Any]:
    '''picking up common elements in two lists'''
    return [element1 for element1 in l1 if element1 in l2]


def list_difference(l1: List[Any], l2: List[Any]) -> List[Any]:
    '''picking up unique element in list 1 from list 2'''
    return [element1 for element1 in l1 if element1 not in l2]


def remove_vowels(string: str) -> str:
    '''removing words which starts with vowels from string'''
    return ' '.join([element for element in string.split() if not element.lower().startswith(('a', 'e', 'i', 'o', 'u'))])


def check_pwd(password: str) -> bool:
    '''checking password string if it contains one lowercase letter, two upper case letter and starts with a digit'''
    # return len([upper_l for upper_l in password if upper_l.isupper()])>=2 \
    #         and len([lower_l for lower_l in password if lower_l.islower()]) >= 1 \
    #         and password[0].isdigit()
    return len(password) >= 4 \
           and sum([1 for c in password if c.isupper()]) >= 2 \
           and sum([1 for c in password if c.islower()]) >= 1 \
           and password[0].isdigit()


class DonutQueue:
    '''class for donut queue problem'''
    def __init__(self) -> None:
        self.queue_normal: List[str] = list()
        self.queue_priority: List[str] = list()

    def arrive(self, name: str, vip: bool) -> None:
        '''checking if the person is vip or not'''
        if vip is True:
            self.queue_priority.append(name)
            # return self.queue_priority
        else:
            self.queue_normal.append(name)
            # return self.queue_normal

    def next_customer(self) -> Optional[str]:
        '''calling for the next customer depending on the status of that person'''
        if len(self.queue_priority) > 0:
            return self.queue_priority.pop(0)
        elif len(self.queue_normal) > 0 and len(self.queue_priority) == 0:
            return self.queue_normal.pop(0)
        else:
            return None

    def waiting(self) -> Optional[str]:
        '''checking who is waiting in line to be served'''
        wait_list: List[str] = self.queue_priority + self.queue_normal
        if len(wait_list) > 0:
            return ", ".join(wait_list)
        else:
            return None
        # temp: List[str] = list()
        # if self.queue_priority or self.queue_normal:
        #     temp.extend(self.queue_priority)
        #     temp.extend(self.queue_normal)
        # return ", ".join(temp)

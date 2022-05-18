# Merge two sorted lists.
# We will take as an assumption that both lists have same len

from os import lseek


TST_LST_1 = [4, 8, 15, 19]
TST_LST_2 = [7, 9, 10, 16]


def merge_lists(lst1: list, lst2: list) -> list:
    i = 0
    merged_list = list()
    while i < len(lst1):
        if lst1[i] <= lst2[i]:
            merged_list.append(lst1[i])
            merged_list.append(lst2[i])
        else:
            merged_list.append(lst2[i])
            merged_list.append(lst1[i])
        i += 1
    return merged_list


# ans = merge_lists(TST_LST_1, TST_LST_2)
# print(ans)

# Merge two lists using linked lists

from collections import deque


def merge_linked_list(lnkd1: list, lnkd2: list) -> list:
    if lnkd1 is None:
        return lnkd2
    if lnkd2 is None:
        return lnkd1


l = deque([1, 2, 3, 4, 5])

print(l.appendleft(6))
print(l)

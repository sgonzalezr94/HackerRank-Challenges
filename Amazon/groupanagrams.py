from cgi import test
from typing import List

# Slow approach O((n^2)*n-1)
# def isAnagram(str1: str, str2: str) -> bool:
#     return sorted(str1) == sorted(str2)


# def groupAnagrams(strs: List[str]) -> List[List[str]]:
#     anagrams_list = list()
#     for word in strs:
#         if len(strs) == 1:
#             anagrams_list.append(strs)
#             break
#         sub_list = [word]
#         strs.remove(word)
#         for word2 in strs:
#             if isAnagram(word, word2):
#                 sub_list.append(word2)
#                 strs.remove(word2)
#         anagrams_list.append(sub_list)

#     return anagrams_list


def create_count_dict(str: str) -> dict:
    str_dict = dict()
    for character in str:
        if character not in str_dict:
            str_dict[character] = 1
        else:
            str_dict[character] += 1
    return str_dict


def groupAnagrams(strs: List[str]) -> List[List[str]]:
    count_dict = dict()
    for str_in in strs:
        sorted_str = str(sorted(str_in))
        if sorted_str not in count_dict:
            count_dict[sorted_str] = [create_count_dict(sorted_str), [str_in]]
        else:
            count_dict[sorted_str][1].append(str_in)
    return [strs[1] for strs in count_dict.values()]


test_strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
tst2 = ["", "", ""]
# print(isAnagram(test_strs[0], test_strs[1]))
res = groupAnagrams(test_strs)
print(res)

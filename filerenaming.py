import re


def renameFile(newName, oldName):
    count = 0
    for i in range(0, len(oldName)):
        if oldName[i:].startswith(newName):
            count += 1
    return count


def renameFile(newName, oldName):
    newcount = re.findall('(?='+newName+')', oldName)
    return len(newcount)


teststr = 'cccc'
tstsub = 'ccc'

print(renameFile(tstsub, teststr))

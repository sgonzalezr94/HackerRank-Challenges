

def maxPairs(skillLevel, minDiff):
    skillset = set(skillLevel)
    skillLevel = list(skillset)
    i = 0
    count = 0
    while(i < len(skillLevel)):
        j = i+1
        while(j < len(skillLevel)):
            if abs(skillLevel[i]-skillLevel[j]) == minDiff:
                print(skillLevel[i], skillLevel[j])
                count += 1
            j += 1
        i += 1
    return count

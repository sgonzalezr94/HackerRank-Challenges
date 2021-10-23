

# we can take as an asummption that the first game sets the high and low score.

def breakingRecords(scores):
    maxrecord = minrecord = scores[0]
    maxcount = mincount = 0
    for score in scores:
        if score > maxrecord:
            maxrecord = score
            maxcount += 1
        if score < minrecord:
            minrecord = score
            mincount += 1
    return maxcount, mincount


testScores = [3, 4, 21, 36, 10, 28, 35, 5, 24, 42]


breakingRecords(testScores)

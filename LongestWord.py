import re

pattern = re.compile(r'\W')


def LongestWord(sen):

    x = pattern.split(sen)

    return max(x, key=len)


print(LongestWord(input()))

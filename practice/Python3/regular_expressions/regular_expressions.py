import re


# match whole string
data1 = "aaab"
data2 = "aaaba"
pattern = r"\Aa+b\Z"

match1 = re.match(pattern, data1)
print(match1)
match2 = re.match(pattern, data2)
print(match2)

# regular expression options

data = "AaaA\n\raaaA"
pattern = r"^(a+)$"
match = re.match(pattern, data, re.I | re.M)
print(match)
print(match.group())

# search all matches
data = "Pi = 3.14, exponent = 2.718"
pattern = r"(\d+\.\d+)"
matches = re.findall(pattern, data)
print(matches)

# replacement of the match(with catch group)

data = re.sub(pattern, r'<f>\1</f>', data)
print(data)

# search for a match
match = re.search(pattern, data)
if match:
    print(match.group())
    print(float(match.group()))

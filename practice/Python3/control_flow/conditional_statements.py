# Ternary operator
n = -42
classify = "positive" if n > 0 else "negative"
print(classify)

# complex conditions
A = 3
B = 5
C = 7

if C >= A and C >= B:
    print("C is the biggest")

if not (A >= B or A >= C):
    print("A is the smallest")


# Switch Case
str = ""
monitorSize = 24

str = {
    monitorSize == 15: "too small",
    16 <= monitorSize <= 18: "good for the past decade",
    19 <= monitorSize <= 23: "for office work",
    24 <= monitorSize <= 27: "great choice",
    15 > monitorSize > 18: "",
}[True]
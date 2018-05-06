# append text to file

file_name = "file.txt"
text = "Line1\nLine2\n"
with open(file_name, 'a') as wf:
    wf.write(text)

# read file line by line
with open(file_name, 'r') as rf:
    for line in rf:
        print(line)

# read from a file
with open(file_name, 'r') as rf:
    text = rf.read()
    print(text)

# write to a file
with open(file_name, 'a') as wf:
    print(text, file=wf)

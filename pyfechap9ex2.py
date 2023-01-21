import string

user_file = input("Enter the name of the file: ")
fhand = open(user_file)

try:
    fhand = open(user_file)

except:
    print("File cannot be opened!", fhand)
    exit()

counts = dict()

for line in fhand:
    line.rstrip()
    line.translate(line.maketrans('','',string.punctuation))

    if "From" not in line:
        continue
    elif "From:" in line:
        continue
    else:
        words = line.split()
        words = words[2]

        if words == "Sat" or words == "Fri" or words == "Thu":
            counts[words] = counts.get(words, 0) + 1
            
print(counts)
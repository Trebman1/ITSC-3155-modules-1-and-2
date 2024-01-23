string1 = input("Enter A String: ")
list1 = []
for x in string1:
    if x != " ":
        if x.islower():
            list1.append(x)
for x in string1:
    if x != " ":
        if x.isupper():
            list1.append(x)
print("".join(list1))
# print("Hello World!")

A = ["a", "b", "c"]
B = ["s", "j", "h", "b", "v", "l", "a", "i",
     "s", "u", "b", "v", "u", "i", "a", "s", 
     "b", "v", "l", "i", "v", "n", "l", "a", "k"]

for i in A:
    count = 0

    for j in B:
        if i == j:
            count += 1

    print(f"{i} has occured {count} times")
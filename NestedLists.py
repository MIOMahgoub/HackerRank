if __name__ == '__main__':
    # Added empty list to append name and score to
    lst = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        # Added append to for loop
        lst.append([name, score])

# Sort list by score primarily and name secondarily  
organized = sorted(lst, key=lambda x: (x[1], x[0]))

# identify lowest score in nested list and initialize target 
check = organized[0][1]
target = 0

# create loop to identify second lowest score and then 
# printed each name in order that achieved the second lowest score
for name, score in organized:
    if score != check:
        target = score
        for name, score in organized:
            if score == target:
                print(name)
        break
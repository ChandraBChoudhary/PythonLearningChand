count = 0
with open("captains.pdf") as FH :
    headers = next(FH)
    for line in FH:
        if count == 0:
            continue
            count += 1
        name = line.split(",")[0]
        count += 1

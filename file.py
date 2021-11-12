'''Read a file '''
counter=0
with open("captains.txt") as FH:
    for line in FH:
        if counter == 0 :
            counter += 1
            continue 
        elif counter < 6 :
            #print(line.split(",")[0],end="\n")
            print(line)
        else :
            break
        counter += 1

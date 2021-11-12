booked = [ 1, 3, 9, 12, 13, 18, 26, 27, 28, 29 ]
travel = [ 4, 5, 15, 16, 21, 22 ]
month = range(1,31)
busy = booked + travel

study = list()
for date in month:
    if date not in busy:
        study.append(date)
for date in study:
    print(date)

LN = 9
user_i = input("Please guess the lucky number by entering a number from 0-25 : ")
user_io = int(user_i)
if(user_io < LN -3 ):
    print("Too Low")
elif(user_io > LN +3):
    print("Too High")
elif user_io == LN:
    print("You are the winner")
else :
    print("Almost there")

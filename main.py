# Brianna Gregory
# 9/2/21
# All about the function
# Doing the all about the function program
def myCountfun(Mystr):
    ucount1 = 0
    lcount1 = 0
    print(Mystr)
    for c in Mystr:

        if c.isupper():
            ucount1 += 1
        else:
            lcount1 += 1

    return ucount1,lcount1

answer = input("Please enter a string: ")

letter = answer.replace(" ", "")
if letter.isalpha():
    ucount,lcount = myCountfun(answer)
    print(f"Your upper count was: {ucount} and your lower count was {lcount}")
else:
    print("Please only enter letters, no numbers!")










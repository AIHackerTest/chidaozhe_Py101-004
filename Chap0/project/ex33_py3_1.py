i = 0
numbers = []

def cycle():
    global i
    print ("At the top i is %d" % i)
    numbers.append(i)
    print ("Numbers now:", numbers)
    i = i + 1
    print ("At the bottom i is %d" % i)

def other():
    print ("The numbers:")
    for num in numbers:
	    print (num)

while i < 6:
    cycle()

other()

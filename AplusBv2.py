# not as elegant as the coursera solution (mapping is cool), 
# but better readable
# (even though the waiting for the second input is slightly pedestrian)
if __name__ == '__main__':
    def add2(a, b):
        return (a + b)
    
    firstvar    = int(input("first number to add: "))
    secondvar   = int(input("second number to add: "))
    
    print( add2(firstvar, secondvar))


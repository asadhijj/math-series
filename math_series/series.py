def fibonacci (n):
    '''The function should return the nth value in the fibonacci series'''
    if type(n) !=int :
        return "Please enter an integer"
    if n<0 :
        return "please enter a positive integer!!"
    sequence = []
    if n == 0:
        sequence = [0]
    else:
        sequence = [0,1]
        for i in range(1, n):
            sequence.append(sequence[i-1] + sequence[i])
    return sequence[n]



def lucas(n):
    '''returns the nth value in the lucas numbers'''
    if type(n) !=int :
        return "Please enter an integer"
    if n<0 :
        return "please enter a positive integer!!"
    sequence = []
    if n == 0:
        sequence = [2]
    else:
        sequence = [2,1]
        for i in range(2,n+1):
            sequence.append(sequence[i-2] + sequence[i-1])
    return sequence[n]


def sum (n, x=0,y=1):
    '''
    Calling this function with no optional parameters will produce numbers from the fibonacci series.
    Calling it with the optional arguments 2 and 1 will produce values from the lucas numbers.
     Other values for the optional parameters will produce other series.
     '''
    if type(n) !=int :
        return "Please enter an integer"
    
    if n<0 :
        return "please enter a positive integer!!"
    sequence=[]
    if n==0:
        sequence=[x]
    else :
        sequence=[x,y]
    
    if x==2 and y==1:
        sequence = [x,y]
        for i in range(2,n+1):
            sequence.append(sequence[i-2] + sequence[i-1])
    elif x==0 and y==1 :
        sequence = [0,1]
        for i in range(1, n):
            sequence.append(sequence[i-1] + sequence[i])
    else :
        sequence=[x,y]
        for i in range(1, n):
            sequence.append(sequence[i-1] + sequence[i])
    
    return sequence[n]


        








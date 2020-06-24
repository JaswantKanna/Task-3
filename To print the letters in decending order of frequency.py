# Task 3
Input :
import operator

def arrange ():

    str = input("Enter character or number in String :\n")
    output = {}

    for x in str:
        output [x] = str.count(x)
        
    Descending = sorted (output.items(), key = operator.itemgetter(1), reverse = True)

    print ("\nThe frequency of the given string :\n", Descending)


    print ("\n Frequency of the given string in Descending order :\n")
    for x in Descending:
        print (f"{x[0]}={x[1]}")

arrange ()

Output :
Enter character or number in String :
MISSISSIPPI

The frequency of the given string :
 [('I', 4), ('S', 4), ('P', 2), ('M', 1)]

 Frequency of the given string in Descending order :

I=4
S=4
P=2
M=1

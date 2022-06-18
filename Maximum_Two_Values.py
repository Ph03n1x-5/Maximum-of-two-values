def main() :
    filename = "Ryan_Jessica_Maximum_Two_Values.txt"
    outFile = open(filename, "w")
    print("Enter a positive whole integer for number 1:")
    num1 = checkIntDataType()
    print("Enter a positive whole integer for number 2:")
    num2 = checkIntDataType()
    result(num1, num2, outFile)
    outFile.close()
    
def findMax(a,b) :
    if(a>b) :
        return a
    else :
        return b
    
    
def checkIntDataType() :
    while True :
        try :
            IntDataType = int(input())
        except ValueError :
            print("Wrong data type entered - RE-ENTER A POSITIVE VALUE")
            continue
        else :

            if (IntDataType < 0) :
                print("You entered a negative value -RE-ENTER A POSITIVE VALUE")
                continue
            else :

                break
    return IntDataType

def result(a, b, f) :

    f.write("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    f.write("             MAXIMUM OF TWO VALUES\n")
    f.write("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    f.write("      The maximum of"+ format(a,"2d")+" and "+ format (b,"2d")+ " is " + format(findMax (a,b),"2d")+"\n")
    f.write("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    
main()
    

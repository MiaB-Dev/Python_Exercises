from math import sqrt



def main():
    
    n1 = read_num()

    op = input("Choose an operator: + - * / ^ √ ")

        
    match op:
        case "+":
            n2 = read_num()
            result = n1 + n2
        
        case "-":
            n2 = read_num()
            result = n1 - n2
        
        case "*":
            n2 = read_num()
            result = n1 * n2
        
        case "/":
            n2 = read_num()
            if (n2 == 0):
                print ("not possible to divide by 0!")
                result = "ERROR"
            else:
                result = n1 / n2
                
        case "^":
            n2 = read_num()
            result = pow(n1, n2)

        case "√":
            result = sqrt(n1)

        case _:
            print("invalid operator")
    
    
    print (result)

def read_num():
    n = input("Insert a number: ")
    if n.isdigit():
        n = int(n)
    else:
        n = float(n)
    
    return n

    

if __name__ == "__main__":
    main()

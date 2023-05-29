def main():
    
    n1 = input("Insert a number: ")
    if n1.isdigit():
        n1 = int(n1)
    else:
        n1 = float(n1)

    op = input("Choose an operator: + - * /: ")
    
    n2 = input("Insert a number: ")
    if n2.isdigit():
        n2 = int(n2)
    else:
        n2 = float(n2)
        
    match op:
        case "+":
            result = n1 + n2
        
        case "-":
            result = n1 - n2
        
        case "*":
            result = n1 * n2
        
        case "/":
            if (n2 == 0):
                print ("not possible to divide by 0!")
                result = "ERROR"
            else:
                result = n1 / n2
                
        case _:
            print("invalid operator")
    
    
    print (result)
    

if __name__ == "__main__":
    main()

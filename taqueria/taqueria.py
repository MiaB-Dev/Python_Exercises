def main():
    taqueria()

def taqueria():
    menu={
        "Baja Taco": 4.00,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }

    sum = 0
    while True:
        try:
            item = input('Item: ').title()
            val = menu[item]
        except KeyError:
            pass
        except (EOFError, KeyboardInterrupt) as e:
            break
        else:
            sum = sum + val
            print(sum)



main()
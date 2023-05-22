def main():
    tweet = input("Say a string: ")
    str=shorten(tweet)
    #str=shorten()
    print(str)

def shorten(word="world"):
    a=""
    for character in word:
        if character.upper() not in ['A', 'E', 'I', 'O', 'U']:
            a+=character
            ##print(character, end="")
    return a

if __name__ == "__main__":
    main()
    

# ? Check whether a character is a vowel or a consonant.

character = input("Enter your character from the keyboard : ")

vowels = "aeiouAEIOU"
if character.isalpha() and len(character) == 1:
    
    if character in vowels:
        print("It is belong to vowel")
    else:
        print("It is consonant")
else:
    print("please Enter only single character")

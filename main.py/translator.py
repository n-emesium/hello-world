#The 'E' language. 

def translator(phrase):
    translation = ""
    for x in phrase:
        if x.lower() in "aeiou":
            if x.isupper():
                translation = translation + "G"
            else:
                translation = translation + "g"
        else:
            translation = translation + x
            
    return translation

print(translator(input("Please type in what you want to translate. ")))
    
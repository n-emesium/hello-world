#Karan'ın şifresi :)

def encryptor(pw):
    char_list = "aeiou"
    translation = ""
    for x in pw:
        if x.lower() not in char_list:
            if x.isupper():
                translation = translation + x + "E"
            else:
                translation = translation + x + "e"
        else:
            translation = translation + x
    return translation

print(encryptor(input("Please choose what you'd like to encrypt. ")))
                 
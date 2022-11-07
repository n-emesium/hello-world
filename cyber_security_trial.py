#amateur translation program

hi = "Hello. "
user_input = ""

translatable_words = [
    ["nihao", "merhaba", "konnichiwa"],
    ["salam", "hallo", "bonjour"],
    ["bonjour", "hola", "privyet"],
    ["anyoung haseyo"],


]
print("\n",translatable_words[0],"\n",translatable_words[1],"\n",translatable_words[2],"\n",translatable_words[3])

translator = {
    "nihao": hi,
    "merhaba": hi,
    "konnichiwa": hi,
    "salam": hi,
    "hallo": hi,
    "bonjour": hi,
    "hola": hi,
    "privyet": hi,
    "anyoung haseyo": hi,
}

def translation_device():
        user_input = input("What do you want to translate? ")
        print(translator.get(user_input.lower()))
        print("Translation succesful. ")
        if not user_input.lower() in translator:
            print("Invalid word. ")





translation_device()


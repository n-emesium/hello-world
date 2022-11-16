from camelcase import CamelCase

def camel_case():
    c = CamelCase()
    txt = input("Please enter a sentence. ")
    print(c.hump(txt))

camel_case()
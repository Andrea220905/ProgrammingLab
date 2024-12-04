def conta_parole (file, word):
    c=0
    with open ("file" ,"r") as file:
        contenuto= file.read()
        c += contenuto.count(word)
    print (c)
    return c
palavra = input(str("Digite a palavra: "))
palavra_invertida = palavra[::-1]
if palavra == palavra_invertida:
    print("A palavra é palíndroma!!")
else:
    print("A palavra não é palíndroma!")
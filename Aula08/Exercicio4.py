frase = input(str("Digite a sua frase: "))
contador = 0
vogais = "aeiouAEIOU"
for letra in frase:
    if letra in vogais:
        contador+=1
print(f"A frase digitada possui: {contador} vogais!")
A = frase.count('a')
print(A)

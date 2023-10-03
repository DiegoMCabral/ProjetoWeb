while True:
    valor = input(str('Digite um número com 9 caracteres: '))
    if valor.isdigit() and len(valor) == 9:
        break
    if len(valor) !=9:
        print("Tem que ter 9 digítos")
    else:
        print("Digite apenas números!!")
        
novo_valor = valor[0] + "." + valor[1:4] + "." + valor[4:7] + "," + valor[7:9]
print(novo_valor)
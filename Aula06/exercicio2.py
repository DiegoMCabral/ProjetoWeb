valor = float(input("Digite o valor: R$ "))
desconto1 = valor*0.1
desconto2 = valor*0.2
desconto3 = valor*0.3

if valor<1000:
    print("O valor do desconto é de: R$ ",desconto1)

elif valor>5000:
    print("O valor do desconto é de: R$  ",desconto3)
    
else:
    print("O valor do desconto é de: R$ ",desconto2)
    
    
    



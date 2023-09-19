largura = float(input("Adicione a largura do local: "))
comprimento = float(input("Adicione o comprimento do local: "))
material = str(input("Qual será o material utilizado: "))
lata = 18
galao=3.6
litro = 1
pe_direito = 2.80
areaparede = ((pe_direito * largura) * 2) + ((pe_direito * comprimento) * 2)
areaporta = 2.10 * 0.80
rendimentolitro = 3
quantidadelitro = ((areaparede - areaporta) / rendimentolitro) 

import math   
lata18 = (quantidadelitro/18)
lata18_arredondado = math.ceil(lata18)
galao36 = (quantidadelitro/3.6)
galao36_arredondado = math.ceil (galao36)
litrotinta = math.ceil (quantidadelitro)

if material == "lata":
    print(f"Será necessário {lata18_arredondado} latas de 18L para pintar o cômodo") 
elif material == "galao":
    print(f"Será necessário {galao36_arredondado} galõees de 3,6 Lpara pintar o cômodo") 
else:
    print(f"Será necessário {litrotinta} litros para realizar a pintura do cômodo")  
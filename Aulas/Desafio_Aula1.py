CONSTANTE_BONUS = 1000
nome_usuario = input("Digite seu nome aqui: ")
salario_usuario = float(input("Digite o valor do seu salário: "))
bonus_usuario = float(input("Digite o valor do seu bônus: "))

calculo = CONSTANTE_BONUS + salario_usuario * bonus_usuario 
print(f"O usuario {nome_usuario} possui o bonus de {calculo}")
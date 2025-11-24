# #### INTEIROS (`int`)

# 1. Escreva um programa que soma dois números inteiros inseridos pelo usuário.
#numero_01 = int(input("Insira o primeiro número: "))
#numero_02 = int(input("Insira o segundo número: "))
#resultado = numero_01 + numero_02
#print(f"O seu resultado é de: {resultado}")

# 2. Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.
#numerador = float(input("Digite o seu numerador: "))
#denominador = float(input("Digite o seu denominador: "))
#resto = int(numerador % denominador)
#print(f"O resto de {int(numerador)} / {int(denominador)} é {resto}")

# 3. Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.
#multiplicando = float(input("Digite o seu multiplicando: "))
#multiplicador = float(input("Digite o seu multiplicador: "))
#multiplicacao = float(multiplicando * multiplicador)
#print(f"O resultado de {multiplicando} por {multiplicador}, é de {multiplicacao}")

# 4. Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.
#numero_01 = int(input("Inserir um numero inteiro: "))
#numero_02 = int(input("Inserir outro numero inteiro: "))
#resultado = numero_01 // numero_02
#print(resultado)

# 5. Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.
#numero_quadrado = int(input("Digite o número que quer saber o quadrado dele: "))
#resultado_quadrado = numero_quadrado ** 2 #Ou numero_quadrado * numero_quadrado
#print(f"Seu número ao quadrado é {resultado_quadrado}")

# #### NÚMEROS DE PONTO FLUTUANTE (`float`)

# 6. Escreva um programa que receba dois números flutuantes e realize sua adição.
#numero01 = float(input("Digite seu primeiro número: "))
#numero02 = float(input("Digite seu próximo número: "))
#adicao = numero01 + numero02
#print(f"Seu resultado da adição de {numero01} + {numero02} é de: {adicao}.")

# 7. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.
#numero01 = float(input("Digite seu primeiro número: "))
#numero02 = float(input("Digite seu próximo número: "))
#media = (numero01 + numero02)/ 2
#print(f"Seu resultado da adição de {numero01} + {numero02} é de: {media}.")

# 8. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).
#base = float(input("Digite a base: "))
#expoente = float(input("Digite a expoente: "))
#potência = base ** expoente
#print(f"O resultado da potência entre a base {base} pelo expoente {expoente} é de:  {potência}")

# 9. Faça um programa que converta a temperatura de Celsius para Fahrenheit.
#Celsius = int(input("Digite quantos graus celsius quer converter para Fahrenheit: "))
#Fahrenheit = int((Celsius * 9/5) + 32)
#print(f"A conversão de {Celsius}° para Fahrenheit é de: {Fahrenheit}°F")

# 10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.
#import math
#raio_do_circulo = float(input("Digite o raio"))
#area_do_circulo = math.pi * raio_do_circulo ** 2
#print(f"{area_do_circulo}")

# #### STRINGS (`str`)

# 11. Escreva um programa que receba uma string do usuário e a converta para maiúsculas.
#nome = input("Digite seu nome: ").upper()
## nome_maiusculo = nome.upper() segunda opção
#print(f"Seu nome é: {nome}")

# 12. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.
#nome = input("Digite seu nome: ").lower()
## nome_maiusculo = nome.upper() segunda opção
#print(f"Seu nome é: {nome}")

# 13. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.
#frase = input("Digite uma frase: ")
#print(f"SUA FRASE É: {frase}")

# 14. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.
#data = input("Digite sua data no formato dd/mm/aaaa: ")
#if data.count('/') == 2:
#    dia , mes, ano = data.split('/')
#    print(f"Dia: {dia}")
#    print(f"mês: {mes}")
#    print(f"ano: {ano}")
#else:
#    print("Formato inválido! Use dd/mm/aaaa.")

# 15. Escreva um programa que concatene duas strings fornecidas pelo usuário.
#data_do_usuario = input("Insira uma data no formato dd/mm/aaaa: ")
#lista_de_dia_mes_ano = data_do_usuario.split("/")
#print(f"O elemento 1 e 0: {lista_de_dia_mes_ano[0]}")
#print(f"O elemento 2 e 0: {lista_de_dia_mes_ano[1]}")
#print(f"O elemento 3 e 0: {lista_de_dia_mes_ano[2]}")

# #### BOOLEANOS (`bool`)

# 16. Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.
# Exemplo de entrada
valor1 = True
valor2 = False
resultado_and = valor1 and valor2
print("Resultado do AND lógico:", resultado_and)

# 17. Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.
# Exemplo de entrada
resultado_or = valor1 or valor2
print("Resultado do OR lógico:", resultado_or)

# 18. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.
# Exemplo de entrada
resultado_not = not valor1
print("Resultado do NOT lógico:", resultado_not)

# 19. Faça um programa que compare se dois números fornecidos pelo usuário são iguais.
# Exemplo de entrada
num1 = 5
num2 = 5
resultado_igualdade = (num1 == num2)
print("Resultado da igualdade:", resultado_igualdade)

# 20. Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.
# Exemplo de entrada
resultado_diferenca = (num1 != num2)
print("Resultado da diferença:", resultado_diferenca)

# #### TRY-EXCEPT E IF

# 21: Conversor de Temperatura
# 22: Verificador de Palíndromo
# 23: Calculadora Simples
# 24: Classificador de Números
# 25: Conversão de Tipo com Validação
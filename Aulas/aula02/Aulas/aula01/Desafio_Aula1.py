#CONSTANTE_BONUS = 1000

# 1) Solicita ao usuário que digite seu nome
#nome_usuario = input("Digite seu nome aqui: ")

# 2) Solicita ao usuário que digite o valor do seu salário
# Converte a entrada para um número de ponto flutuando (casa decimal)
#salario_usuario = float(input("Digite o valor do seu salário: "))

# 3) Solicita ao usuário que digite o valor do seu bônus recebido
# Converte a entrada para um número de ponto flutuando (casa decimal)
#bonus_usuario = float(input("Digite o valor do seu bônus: "))

# 4) Calcula o valor do bônus final
#calculo = CONSTANTE_BONUS + salario_usuario * bonus_usuario 

# 5) Imprime a mensagem personalizada incluindo o nome do usuário e o valor
#print(f"O usuario {nome_usuario} possui o bonus de {calculo}")



# Quais bugs e risco consigo identificar nesse programa ?
# Texto no lugar de número e número no lugar de texto
# Digitos negativos
# Bônus colocar com virgula ao invés de ponto

# Novo Código ajudado pelo Deepseek

CONSTANTE_BONUS = 1000

# 1) Nome do usuário - repete até ser válido
while True:
    nome_usuario = input("Digite seu nome aqui: ")
    
    # Verifica se nome é válido
    if nome_usuario and nome_usuario.replace(" ", "").isalpha():
        break  # Sai do loop se nome for válido
    else:
        print("Erro: Nome inválido! Digite apenas letras. Tente novamente.\n")

# 2) Salário - repete até ser válido
while True:
    try:
        salario_input = input("Digite o valor do seu salário: ")
        salario_usuario = float(salario_input.replace(",", "."))
        
        # Verifica se salário é positivo
        if salario_usuario >= 0:
            break  # Sai do loop se salário for válido
        else:
            print("Erro: Salário não pode ser negativo! Tente novamente.\n")
    except ValueError:
        print("Erro: Digite apenas números para o salário! Use ponto ou vírgula para decimais.\n")

# 3) Bônus - repete até ser válido
while True:
    try:
        bonus_input = input("Digite o valor do seu bônus: ")
        # Substitui vírgula por ponto
        bonus_input = bonus_input.replace(",", ".")
        bonus_usuario = float(bonus_input)
        
        # Verifica se bônus é positivo
        if bonus_usuario >= 0:
            break  # Sai do loop se bônus for válido
        else:
            print("Erro: Bônus não pode ser negativo! Tente novamente.\n")
    except ValueError:
        print("Erro: Digite apenas números para o bônus! Use ponto ou vírgula para decimais.\n")

# 4) Cálculo do bônus final
calculo = CONSTANTE_BONUS + salario_usuario * bonus_usuario 

# 5) Mensagem final
print(f"\nO usuário {nome_usuario} possui o bônus final de R$ {calculo:.2f}")
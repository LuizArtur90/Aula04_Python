nome_valido:bool = False
salario_valido:bool = False
bonus_valido:bool = False

#Entre com o nome do usuário
user:str = input("Digite seu nome:")
#Retorna msg caso user digitar um numero.
while not nome_valido:
    if user.isdigit():
        print("Você digitou o nome errado!")
    #Retorna msg caso user digitar espaço.
    elif user.isspace():
        print("Verifique se seu nome foi digitado corretamente.")
    #Retorna msg caso user não digitar algo.
    elif len(user) == 0:
        print("Verifique se seu nome foi digitado corretamente.")
    else:
        print("Nome válido:",user)
        nome_valido = True
while not salario_valido:
    try:
        #Entre com o salário do usuário
        salario:float = float(input("Digite seu salário somente em números:"))
        if salario <= 0:
            print("Por favor, digite um valor positivo para o salário.")
        else:
            salario_valido = True
            print ("Salário válido:",salario)
    except ValueError:
        print("Entrada inválida para o salário. Por favor, digite um número.")
while not bonus_valido:
    try:
        #Entre com o bonus do usuário
        bonus_user:float = float(input("Digite sue bônus:"))
        if bonus_user <= 0:
            print("Por favor, digite um valor positivo para o bônus.")
        else:
            print("Bônus válido:",bonus_user)
            bonus_valido = True
    except ValueError:
        print("Entrada inválida para o bônus. Por favor, digite um número.")
#Variável que será alterado anualmente.
percent:int = 1000
try:
    if percent <= 0:
        print("Atenção, o valor da variável anual PERCENT deve ser maior que 0")
        
except ValueError:
        print("Atenção, o valor da variável anual PERCENT um numero")
            
#Cálculo do KPI final
bonus_final = percent + salario*bonus_user
#Mensagem final
print(f"Olá {user}, o seu salário é {salario} e seu bônus anual foi de {bonus_final}.")
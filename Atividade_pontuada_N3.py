import os
os.system("cls || clear")

login_cadastrado ="miguel"
senha_cadastrada = "1234"
vl_trans=""
login=str(input("digite o usuario: "))
senha=str(input("digite a senha: "))
os.system("cls || clear")
if login_cadastrado == login and senha_cadastrada == senha:
    salarioBase=float(input("digite o seu salario: "))
    os.system("cls || clear")
    dependentes= int(input("quantos dependentes á em sua casa (exceto de você): "))
    planoDeSaude= 150*dependentes
    os.system("cls || clear")
    valeRefeicao=int(input("digite o valor do seu vale refeição da empresa: "))
    os.system("cls || clear")
    while True:
     opcao = str(input("possui vale transposte?: ")).lower()
     if opcao == "s" or opcao == "sim":
        vl_trans == "possui vale transporte"
        descValeTransporte= salarioBase*0.06
        break
     elif opcao == "n" or opcao == "nao":
        vl_trans == "possui vale transporte"
        break
     else:
        os.system("cls || clear")
    

    def inss(salarioA):

     if salarioA <=1518.00:
        return salarioA * 0.075
       
     elif salarioA <=2793.88:
        return salarioA*0.09-113.85
        
       
     elif salarioA <=4190.83:
        return salarioA*0.12-189.54
        
       
     elif salarioA <=8157.41:
        return salarioA*0.14-318.38
     
     else:
        return 1142.04

    salario_inss=inss

       

# def calcular_inss(salario):
#     if salario <= 1518.00:
#         return salario * 0.075
#     elif salario <= 2793.88:
#         return salario * 0.09 - 113.85
#     elif salario <= 4190.83:
#         return salario * 0.12 - 189.54
#     elif salario <= :
#         return salario * 0.14 - 318.38
#     else:
#           # Teto de contribuição

# def calcular_irrf(salario, dependentes):
#     deducao_dependente = 189.59 * dependentes
#     base_calculo = salario - deducao_dependente
#     if base_calculo <= 2259.20:
#         return 0
#     elif base_calculo <= 2826.65:
#         return base_calculo * 0.075 - 169.44
#     elif base_calculo <= 3751.05:
#         return base_calculo * 0.15 - 381.44
#     elif base_calculo <= 4664.68:
#         return base_calculo * 0.225 - 662.77
#     else:
#         return base_calculo * 0.275 - 896.00

# def calcular_folha_pagamento():
#     print("=== Sistema de Folha de Pagamento ===")
    
#     matricula = input("Informe a matrícula do funcionário: ")
#     senha = input("Informe a senha: ")  # Simples verificação, não implementa autenticação real
    
#     try:
#         salario_base = float(input("Informe o salário base (R$): "))
#         vale_transporte = input("Deseja receber vale transporte? (s/n): ").strip().lower()
#         valor_vale_refeicao = float(input("Informe o valor do vale refeição fornecido pela empresa (R$): "))
#         dependentes = int(input("Informe a quantidade de dependentes: "))
#     except ValueError:
#         print("Erro: Entrada inválida. Certifique-se de digitar os valores corretamente.")
#         return

#     # Cálculos
#     desconto_inss = calcular_inss(salario_base)
#     desconto_irrf = calcular_irrf(salario_base, dependentes)
#     desconto_vale_transporte = salario_base * 0.06 if vale_transporte == 's' else 0
#     desconto_vale_refeicao = valor_vale_refeicao * 0.20
#     desconto_plano_saude = dependentes * 150.00

#     total_descontos = desconto_inss + desconto_irrf + desconto_vale_transporte + desconto_vale_refeicao + desconto_plano_saude
#     salario_liquido = salario_base - total_descontos

#     print("\n--- Demonstrativo de Pagamento ---")
#     print(f"Matrícula: {matricula}")
#     print(f"Salário Base: R$ {salario_base:.2f}")
#     print(f"Desconto INSS: R$ {desconto_inss:.2f}")
#     print(f"Desconto IRRF: R$ {desconto_irrf:.2f}")
#     print(f"Desconto Vale Transporte: R$ {desconto_vale_transporte:.2f}")
#     print(f"Desconto Vale Refeição: R$ {desconto_vale_refeicao:.2f}")
#     print(f"Desconto Plano de Saúde: R$ {desconto_plano_saude:.2f}")
#     print(f"Total de Descontos: R$ {total_descontos:.2f}")
#     print(f"Salário Líquido: R$ {salario_liquido:.2f}")

# # Executar o programa
# calcular_folha_pagamento()






else:
    print("login ou senha incorreto")
        
#     Até R$ 1.518,00	7,5%	—
# De R$ 1.518,01 até R$ 2.793,88	9%	113,85
# De R$ 2.793,89 até R$ 4.190,83	12%	189,54
# De R$ 4.190,84 até R$ 8.157,41	14%	318,38
import os
import time
os.system("cls || clear")

login_cadastrado ="miguel"
senha_cadastrada = "1234"
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
        opcao = "possui vale transporte"
        descValeTransporte= salarioBase*0.06
        break
     elif opcao == "n" or opcao == "nao":
        opcao = " não possui vale transporte"
        break
     else:
        print("Opção Invalida \nEspere 2 segundos")
        time.sleep(2)
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

    salario_inss=inss(salarioBase)

    def IRRF(salarioBase, dependentes):
     deducao_dependente = 189.59 * dependentes
     base_calculo = salarioBase - deducao_dependente
     if base_calculo <= 2259.20:
        return 0
     elif base_calculo <= 2826.65:
        return base_calculo * 0.075 - 169.44
     elif base_calculo <= 3751.05:
        return base_calculo * 0.15 - 381.44
     elif base_calculo <= 4664.68:
        return base_calculo * 0.225 - 662.77
     else:
        return base_calculo * 0.275 - 896.00
     
    salario_irrf=IRRF(salarioBase, dependentes)
    desconto_vale_transporte = salarioBase * 0.06 if opcao == 's' or opcao == "sim" else 0
    desconto_vale_refeicao = valeRefeicao * 0.20
    descontoTotal= descValeTransporte + desconto_vale_refeicao + salario_inss + salario_irrf + planoDeSaude
    SalarioLiquido= salarioBase - descontoTotal


    print("\t--- FOLHA DE PAGAMENTO ---\n")
    print(f"Usuario: {login}")
    print(f"Salário Base: R$ {salarioBase}")
    print(f"Desconto INSS: R$ {salario_inss:.2f}")
    print(f"Desconto IRRF: R$ {salario_irrf:.2f}")
    print(f"status do vale transporte: {opcao}")
    print(f"Desconto Vale Transporte: R$ {descValeTransporte:.2f}")
    print(f"Desconto Vale Refeição: R$ {desconto_vale_refeicao:.2f}")
    print(f"Desconto Plano de Saúde: R$ {planoDeSaude:.2f}")
    print(f"Total de Descontos: R$ {descontoTotal:.2f}")
    print(f"Salário Líquido: R$ {SalarioLiquido:.2f}\n")
    

else:
    print("login ou senha incorretos")
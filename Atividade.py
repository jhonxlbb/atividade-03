# João Filipe Sampaio de oliveira
# Turma: G93313
import os

# Função sem retorno.
def logoSenai():
    os.system("cls || clear")
    print("=== SENAI === ")

def calcular_imc(pesos, alturas):
    lista_resultados_calculo = []
    for peso in pesos:
        for altura in alturas:
            calculo = peso / (altura ** 2)
            lista_resultados_calculo.append(calculo)
    return lista_resultados_calculo

def verificar_classificacao(a):
    lista_classificacao_imc = []
    for imc in a:
        if imc < 18.5:
            lista_classificacao_imc.append("Abaixo do peso")
        elif imc < 25:
            lista_classificacao_imc.append("Peso normal")
        elif imc < 30:
            lista_classificacao_imc.append("Sobrepeso")
        elif imc < 35:
            lista_classificacao_imc.append("Obesidade grau I")
        elif imc < 40:
            lista_classificacao_imc.append("Obesidade grau II")
        elif imc >= 40:
            lista_classificacao_imc.append("Obesidade grau III")
    return lista_classificacao_imc
        
    
# Definindo listas vazias para armazenar os dados dos usuários
nomes = []
sobrenomes = []
idades = []
alturas = []
pesos = []

# Solicitando os dados dos usuários em um loop
while True:
    logoSenai()
    nome = input("Digite o nome do usuário (ou digite 'sair' para encerrar): ")
    
    # Verificando se o usuário quer sair
    if nome.lower() == 'sair':
        break
    
    idade = int(input("Digite a idade do usuário: "))
    altura = float(input("Digite a altura do usuário (em metros): "))
    peso = float(input("Digite o peso do usuário (em quilogramas): "))
    

    # Adicionando os dados às listas
    nomes.append(nome)
    sobrenomes.append(sobrenomes)
    idades.append(idade)
    alturas.append(altura)
    pesos.append(peso)

lista_resultados_calculos = calcular_imc(pesos, alturas)
lista_classificacao_imc = verificar_classificacao(lista_resultados_calculos)

# Exibindo os dados armazenados
logoSenai()
print("\nDados dos usuários:")
for i in range(len(nomes)):
    print(f"Usuário {i+1}:")
    print("Nome completo:", nomes[i])
    print("Idade:", idades[i])
    print("Altura:", alturas[i], "metros")
    print("Peso:", pesos[i], "quilogramas")
    print(f"IMC:", round(lista_resultados_calculos[i],2))
    print(f"Classificação:", lista_classificacao_imc[i])

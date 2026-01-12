print("-.-.- NOMEAÇÃO DE VARIÁVEIS -.-.-\n")

print("DISPONÍVEL\n")
# Colocando um valor distinto para cada variável.
laranja, melao, limao = 32, 22, 67
print(
    f" Quantidade de laranjas: {laranja}\n Quantidade de Melões: {melao}\n Quantidade de Limões: {limao}\n"
)

print("VALORES(R$/KG)\n")
# Colocando o mesmo valor para variáveis diferentes.
morango = mamao = banana = 5.50
print(
    " Morango(R$/KG): {}\n Mamão(R$/KG): {}\n Banana(R$/KG): {}\n".format(
        morango, mamao, banana
    )
)

print("VALORES POR LISTAS\n")

# Criamos uma lista e atribuímos 5 valores.
lista_carros01 = [
    "VW",
    "FORD",
    "CITROEN",
    "FIAT",
    "CHEVROLET",
]

# Atribuímos às 5 variáveis os valores da lista criada.
marca01, marca02, marca03, marca04, marca05 = lista_carros01

# Nós chamamos a lista de acordo com a marca disponível.
print(
    "Concessionária Boa Viagem (Disponibilidade): ", marca01, marca02, marca03, marca04
)
print("Concessionária Paulista (Disponibilidade): ", marca04, marca05)

print("\nVALORES COMBINADOS DE VARIÁVEIS\n")

proprietario = "William"
sobrenome = "Morais"
idade = str(28)  # Precisa ser convertido para str para mostrar
nome_completo = proprietario + " " + sobrenome

print("Proprietário da Concessionária: ", nome_completo + ", " + idade)

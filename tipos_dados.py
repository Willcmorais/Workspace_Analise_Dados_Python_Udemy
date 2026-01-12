print("=.=.=. TIPOS DE DADOS .=.=.=\n")

# Armazenamento de sequência de dados.
lista_ex01 = [0, 1, 2, 3, 4, 5, 6, 7, 8]
lista_02 = ["Matheus", "júnior", "Adalberto", "Mariá", "Antônia"]
lista_03 = [
    "Jorge Aragão Neto",
    19,
    "Brasileiro",
    ["Maringá", "Itapissuma", "Guaratinguetá"],
    "Solteiro",
    1555.48,
    True,
]

print("- MOSTRANDO AS LISTAS:\n")

print("Lista 01:", lista_ex01, "\n")
print("Lista 02: {}".format(lista_02), "\n")
print(
    "Lista 03:\n Nome: {}\n Idade: {}\n Nacionalidade: {}\n Residiu em: {}\n Estado Civil: {}\n Salário: {}\n Pagamento: {}\n".format(
        lista_03[0],
        lista_03[1],
        lista_03[2],
        lista_03[3],
        lista_03[4],
        lista_03[5],
        lista_03[6],
    )
)

print("- MOSTRANDO AS TUPLAS (TUPLAS SÃO IMUTÁVEIS!!):\n")

# Após criadas não podem ser mudadas
tupla_ex01 = (
    "João Goulart da Silva",
    38,
    "Brasileiro",
    ("Boa vista", "Itapissuma", "Goiania"),
    "Casado",
    9800,
    False,
)

print(
    "Tupla 01:\n Nome: {}\n Idade: {}\n Nacionalidade: {}\n Residiu em: {}\n Estado Civil: {}\n Salário: {}\n Pagamento: {}\n".format(
        tupla_ex01[0],
        tupla_ex01[1],
        tupla_ex01[2],
        tupla_ex01[3],
        tupla_ex01[4],
        tupla_ex01[5],
        tupla_ex01[6],
    )
)

print("- MOSTRANDO OS DICIONÁRIOS:\n")

dicionario_ex01 = {
    "index": "valor",
    "id": 1,
    "nome": "Matheus",
    "lista": lista_03,
    "tupla": tupla_ex01,
}

print(
    "Index: {}\n Id: {}\n Nome: {}\n Lista: {}\n Tupla: {}\n".format(
        dicionario_ex01["index"],
        dicionario_ex01["id"],
        dicionario_ex01["nome"],
        dicionario_ex01["lista"],
        dicionario_ex01["tupla"],
    )
)

print("==== VARIÁVEIS ====\n")

var_texto = "Qualquer coisa"
var_int = str(
    2576
)  # o str é utilizado para que forcemos o que aparecer a ser do tipo string. Útil para quando queremos juntar números a textos.
var_int1 = int(2222)
var_float = float(2.5)
var_bool = False
var_bool2 = True

print("Tipo da variável var_texto é livre e no momento é uma ", type(var_texto))
print(
    "O valor {} está sendo atribuído à variável var_int. E está sendo forçada a ser uma {} mesmo sendo um número inteiro.".format(
        var_int, type(var_int)
    )
)
print(f"A variável {var_int1} é do tipo {type(var_int1)}")
print(
    f"A variável float tem o valor {var_float}. Ela é do tipo {type(var_float)}, já anteriormente especificada."
)
print(f"O usuário pagou a conta? {var_bool}")
print(f"O usuário pagou a conta? {var_bool2}")   



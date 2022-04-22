# Gerar senhas cripto

chave = input("Informe sua senha: ")

senha = ""
for letra in chave:
    if letra in "Aa":
        senha = senha + "'"
    elif letra in "Bb":
        senha = senha + "3"
    elif letra in "Cc":
        senha = senha + "6"
    elif letra in "Dd":
        senha = senha + "!"
    elif letra in "Ee":
        senha = senha + "4"
    elif letra in "Ff":
        senha = senha + "5"
    elif letra in "Rr":
        senha = senha + "#"
    elif letra in "Ss":
        senha = senha + "%"
    elif letra in "Mm":
        senha = senha + "$"
    elif letra in "Gg":
        senha = senha + "6"
    elif letra in "Hh":
        senha = senha + "*"
    elif letra in "Ii":
        senha = senha + "&"
    elif letra in "Oo":
        senha = senha + "@"
    else:
        senha = senha + letra
print(senha)


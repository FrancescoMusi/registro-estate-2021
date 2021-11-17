l = [
    {
        "matricola": 1,
        "cognome": "Musi",
        "nome": "Francesco"
    }
]

dic = {}


n = int(input("Inserisci il numero di matricole da inserire: "))
print()

for i in range(n):
    nome = input("inserisci il nome: ")
    cognome = input("inserisci il cognome: ")
    matricola = input("inserisci matricola: ")
    print()

    dic = {
        "matricola": matricola,
        "cognome": cognome,
        "nome": nome
    }

    l.append(dict(dic))



print("\nRecodrds")

for d in l:
    print('''
    - matricola: {}
    - cognome: {}
    - nome: {}'''.format(d["matricola"], d["cognome"], d["nome"]))
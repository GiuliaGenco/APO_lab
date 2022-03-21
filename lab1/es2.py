# Esercizio 2
# Scrivete un programma che chieda all’utente di fornire due stringhe, per poi visualizzare
# (evitando ripetizioni di caratteri nella stampa):
#
# i caratteri che compaiono in entrambe le stringhe;
# i caratteri che compaiono in una stringa ma non nell’altra;
# le lettere che non compaiono in nessuna delle due stringhe.
# Suggerimento: trasformare una o più stringhe in un insieme (set) di caratteri

str1 = input("Inserire prima stringa: ").lower()
str2 = input("Inserire seconda stringa: ").lower()
insieme = str1 + str2

conto1 = len(str1)
conto2 = len(str2)

comuni = []
diverse = []

for lettera1 in range(conto1):
    for lettera2 in range(conto2):
        if str1[lettera1] == str2[lettera2]:
            flag = 0
            for i in range(len(comuni)):
                if str1[lettera1] == comuni[i]:
                    flag = 1
            if flag == 0:
                comuni.append(str1[lettera1])

print(comuni)  # caratteri che compaiono in entrambe le stringhe

for lett1 in range(len(insieme)):
    for lett2 in range(len(comuni)):
        if insieme[lett1] != comuni[lett2]:
            flag1 = 0
            for j in range(len(diverse)):
                if insieme[lett1] == diverse[j]:
                    flag1 = 1
            if flag1 == 0:
                diverse.append(insieme[lett1])

print(diverse)  # i caratteri che compaiono in una stringa ma non nell’altra;
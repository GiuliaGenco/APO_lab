# Scrivete un programma che legga tutte le righe di un file di testo (input.txt),
# le stampi su console, ne inverta l’ordine e le scriva in un altro file (output.txt).

file = open("D:\POLITO\II anno\Algoritmi e Programmazione ad oggetti\Git\APO_lab\lab1\data\input.txt", "r")
for i in len(file.readline()):
    linee = file.readline()
if linee != "":
    print(linee)


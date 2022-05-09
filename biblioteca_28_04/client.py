from biblioteca import Biblioteca

b = Biblioteca()
b.add_libro("Zanna Bianca", "Jack London", 3, 5)
b.add_libro("Harry Potter", "J.K. Rowling", 3, 5)
b.add_libro("Orlando", "Virginia Wolf", 4, 2)
print(b.get_collocazione("Zanna Bianca", "Jack London"))
print(b.get_libri_scaffale(3, 5))
print(b.get_libri_scaffale(4, 2))

b.add_utente("Mario Rossi", 1)
b.prestito(1, "Zanna Bianca", "Jack London")
b.restituisci("Zanna Bianca", "Jack London")

b.add_utente("Maria Rossi", 2)
b.prestito(2, "Zanna Bianca", "Jack London")

print(b.get_libri_utente(1))
print(b.get_libri_utente(2))

print()
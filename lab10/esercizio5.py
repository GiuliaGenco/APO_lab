# Scrivere due decoratori per funzioni con argomenti sconosciuti (*args, **kwargs). Il primo decoratore,
# repeat_ten_times(f), fa in modo che la funzione decorata sia invocata 10 volte.
# Il secondo decoratore, time_execution(f), stampa il tempo di esecuzione della funzione decorata,
# espresso in nanosecondi, dopo averla invocata.
#
# Decoratore i due metodi con entrambi i decoratori, usandoli in ordine opposto. Scrivere un main che testi i due
# metodi e notare le differenze dovute all'ordine dei decoratori.
import time


def repeat_ten_times(f):
    def decor1(*args, **kwargs):
        f(*args, **kwargs)
        f(*args, **kwargs)
        f(*args, **kwargs)
        f(*args, **kwargs)
        f(*args, **kwargs)
        f(*args, **kwargs)
        f(*args, **kwargs)
        f(*args, **kwargs)
        f(*args, **kwargs)
        f(*args, **kwargs)
    return decor1


def time_execution(f):
    def decoratore2(*args, **kwargs):
        # SUGGERIMENTO: per calcolare il tempo di esecuzione di una funzione, chiamare time.perf_counter_ns()
        # prima e dopo averla invocata. La differenza dei valori restituiti da time.perf_counter_ns() è il tempo di
        # esecuzione in nanosecondi.
        t1 = time.perf_counter_ns()
        f(*args, **kwargs)
        t2 = time.perf_counter_ns()
        tempo = t2 - t1
        print("Tempo di esecuzione: ", tempo)
    return decoratore2


class Greet:
    def __init__(self, nome):
        self._nome = nome

    # Sviluppare la classe Greet, il cui costruttore accetti come parametro il nome della persona da salutare.
    # Il metodo say_hello(self) -> None stampa a schermo la scritta "Hello" seguita dal nome della persona
    # (ad es., "Hello Pietro")
    def say_hello(self) -> None:
        print("Hello", self._nome)

    # Il metodo say_good(self, time_of_day: str) -> None accetta come parametro un stringa contente il periodo della
    # giornata (ad es., "morning", "afternoon", ecc...), e stampa a schermo la scritta "Good" seguita dal periodo della
    # giornata e il nome della persona (ad es., "Good evening Pietro").
    def say_good(self, time_of_day: str) -> None:
        print("Good", time_of_day, self._nome)


def main():
    g1 = Greet("Giulia")
    g1.say_hello = repeat_ten_times(g1.say_hello)
    g1.say_hello()
    g1.say_good = repeat_ten_times(g1.say_good)
    g1.say_good("Morning")

    g2 = Greet("Paolo")
    g2.say_hello = time_execution(g2.say_hello)
    g2.say_hello()  # 7100
    g2.say_good = time_execution(g2.say_good)
    g2.say_good("Evening")  # 9100

    g3 = Greet("Cami")
    g3.say_hello = time_execution(repeat_ten_times(g3.say_hello))
    g3.say_hello()  # 85400
    g3.say_good = time_execution(repeat_ten_times(g3.say_good))
    g3.say_good("Afternoon")  # 133200


main()

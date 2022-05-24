# Sviluppare la classe Thermostat rappresentate un termostato. Il costruttore accetta come parametri la temperatura
# target da mantenere e un valore booleano che esprime se l'utente vuole usare gradi Celsius o Fahrenheit.


class Thermostat:
    def __init__(self):
        self._target = 0
        self._tipo = False  # False = Celsius   True = Fahrenheit

    @staticmethod  # La classe presenta due metodi statici (staticmethod) che trasformano gradi Celsius in Fahrenheit.
    def daFahrenheit(temp):
        return (temp - 32) * 5 / 9

    @staticmethod
    def daCelsius(temp):
        return (temp * 9 / 5) + 32

    @classmethod
    # Sviluppare un metodo di classe (classmethod) che restituisce una nuova istanza della classe Thermostat, copia di
    # quella passata come parametro (questo è similare al costruttore di copia trovato in altri linguaggi).
    def new_istance(cls):
        return cls

    # Sia la temperatura target che il valore booleano devono essere ottenibili e settabili tramite properties (usare
    # appositi decoratori). Se la temperatura impostata supera i 30 Celsius (o equivalente Fahrenheit) limitarla a
    # 30 Celsius (o equivalente Fahrenheit).
    @property
    def target(self):
        return self._target

    @property
    def tipo(self):
        return self._tipo

    @target.setter
    def target(self, temperatura):
        tipo = self._tipo
        if tipo is True:  # Se Fahr
            if temperatura > 86:
                temp = 86
            else:
                temp = temperatura
        else:  # Se Celsius
            if temperatura > 30:
                temp = 30
            else:
                temp = temperatura
        self._target = temp

    @tipo.setter
    def tipo(self, tipo):
        self._tipo = tipo


t = Thermostat()
t.tipo = True  # Fahrenheit
print("Tipo inserito: ", t.tipo)
t.target = 40
print(t.target)  # OK

t2 = Thermostat()
t2.tipo = False  # Celsius
t2.target = 65
print(t2.target)  # Ok

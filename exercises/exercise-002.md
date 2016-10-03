# Aufgabe 2

![corgi running practise](https://uproxx.files.wordpress.com/2011/08/corgi-treadmill.gif)


Ein Corgi hat einen Namen, ein Gewicht und (genau) einen Diener. Ein Diener hat einen Namen
und kann die Eigenschaft haben gehorsam zu sein. Ein Diener kann mehreren Corgis dienen.

Dies kann man folgendermaßen modellieren:

```python
class Corgi
  def __init__(self, name, weight):
    self.name = name
    self.weight = weight

class Servant
  def __init__(self, name, obedient, corgis):
    self.name = name
    self.obedient = obedient
    self.corgis = corgis
```

Gegeben seien die folgenden Corgis
```
Pancake, 23kg
Truffle, 14kg
Iceberg, 28kg
Fruitloops, 13kg
Darth Corgi, 27kg
Leia, 10kg
Breadcrump, 8kg
Mona Lisa, 3kg
Warrior King, 19kg

```

und die folgenden Diener:
```
Michael (gehorsam) dient Warrior King
Friedgard (gehorsam) dient Breadcrump und Mona Lisa
Miggi (ungehorsam) dient Fruitloops, Darth Corgy und Leia
Inga (ungehorsam) dient Truffle und Iceberg
Ulli (gehorsam) dient Pancake
```

* Schreibe eine Funktion, die die Namen aller gehorsamen Diener zurück liefert.
* Schreibe eine Funktion, die die Namen aller ungehorsamen Corgis zurück liefert. Ein Corgi ist ungehorsam genau dann, wenn er einen gehorsamen Diener hat.
* Schreibe eine Funktion, die die Namen aller Diener zurückliefert, die einen übergewichtigen Corgi haben (>= 27 kg).
* Erweitere die Klasse `Servant` um eine Methode `callCorgies`, mit der alle zugehörigen Corgis gerufen werden (Ausgabe des Namens mittles `println`)
* Erweitere die Klasse `Servant` um eine Methode `canCarryCorgis`, die `true` zurück liefert, wenn der jeweilige Diener alle seine Corgis tragen kann und `false` wenn nicht. Ein Diener kann seine Corgis tragen, wenn die Anzahl 2 und das Gesamtgewicht 15 kg nicht überschreitet.
* Schreibe eine Funktion, die die Namen aller Diener zurück liefert, die ihre Corgis tragen können.

**Bestätige die Korrektheit aller Funktionen & Methoden durch Unit Tests!**

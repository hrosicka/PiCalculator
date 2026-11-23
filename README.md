<div align="center">

# 🥧 PiCalculator

**Four ways to explore π — one Python project.**  
**Čtyři způsoby, jak prozkoumat π — jeden Python projekt.**

[🇬🇧 English](#-english) · [🇨🇿 Čeština](#-čeština)

[![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Tkinter](https://img.shields.io/badge/Tkinter-GUI-4B8BBE)](https://docs.python.org/3/library/tkinter.html)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

</div>

---

<a id="-english"></a>

# 🇬🇧 English

## About

**PiCalculator** is a lightweight Python project for approximating the mathematical constant **π** using four different methods:

- **Leibniz series** — an alternating infinite series.
- **Nilakantha series** — a quickly converging series based on fractions.
- **Monte Carlo method** — a probabilistic estimate using random points.
- **Machin formula** — an inverse-tangent formula known for its precision.

The project includes a reusable `PiCalculator` class, a command-line example, and a small Tkinter graphical interface.

## ✨ Features

- Four independent π approximation methods
- Simple object-oriented Python API
- Interactive desktop GUI
- Unit tests with `unittest`
- MIT licensed

## 🚀 Quick start

### Requirements

- Python 3
- Standard-library modules
- `customtkinter` only if you modify or extend the GUI import

> `customtkinter` is imported by `PiCalculatorGUI.py`, but the current GUI implementation uses Tkinter widgets.

### Run the console version

```bash
python PiCalculator.py
```

Example output:

```text
Pi (Leibniz): 3.141591...
Pi (Nilakantha): 3.141592...
Pi (Monte Carlo): 3.14...
Pi (Machin): 3.141592653589793
Pi (math.pi): 3.141592653589793
```

Monte Carlo results vary because they use random sampling.

### Launch the GUI

```bash
python PiCalculatorGUI.py
```

Enter:

- the number of terms for the Leibniz and Nilakantha series;
- the number of random points for the Monte Carlo estimate;
- then click **Calculate**.

## 🧮 Methods at a glance

| Method | Approach | Trade-off |
|---|---|---|
| Leibniz | Alternating series | Easy to understand; slow convergence |
| Nilakantha | Infinite series | Much faster convergence than Leibniz |
| Monte Carlo | Random sampling | Simple and visual; accuracy depends on point count |
| Machin | Inverse trigonometric formula | Fast, compact, and highly accurate |

## 🧪 Run tests

Run the test suite from the repository root:

```bash
python -m unittest discover -s Tests -p "test*.py"
```

The tests cover all four approximation methods. The Monte Carlo test allows a broader tolerance because of randomness.

## 📂 Project structure

```text
PiCalculator/
├── PiCalculator.py          # Calculation methods and console entry point
├── PiCalculatorGUI.py       # Tkinter graphical interface
├── Tests/
│   └── test_pi_calculator.py
└── LICENSE
```

## 💻 Example API usage

```python
from PiCalculator import PiCalculator

calculator = PiCalculator()

print(calculator.calculate_pi_leibniz(100000))
print(calculator.calculate_pi_nilakantha(1000))
print(calculator.calculate_pi_monte_carlo(100000))
print(calculator.calculate_pi_machin())
```

## 🤝 Contributing

Contributions are welcome:

1. Fork the repository.
2. Create a focused feature or fix branch.
3. Add or update unit tests.
4. Open a pull request.

Ideas for improvement: improve input validation, show all four GUI results, add progress feedback, or make the GUI layout responsive.

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

<a id="-čeština"></a>

# 🇨🇿 Čeština

## O projektu

**PiCalculator** je jednoduchý Python projekt pro aproximaci matematické konstanty **π** pomocí čtyř různých metod:

- **Leibnizova řada** — střídavá nekonečná řada.
- **Nílakanthova řada** — rychleji konvergující řada založená na zlomcích.
- **Metoda Monte Carlo** — pravděpodobnostní odhad pomocí náhodných bodů.
- **Machinův vzorec** — vzorec s arkustangensy, známý svou přesností.

Projekt obsahuje znovupoužitelnou třídu `PiCalculator`, ukázku pro příkazovou řádku a malé grafické rozhraní Tkinter.

## ✨ Funkce

- Čtyři nezávislé metody aproximace π
- Jednoduché objektově orientované Python API
- Interaktivní desktopové grafické rozhraní
- Unit testy pomocí `unittest`
- Licence MIT

## 🚀 Rychlý start

### Požadavky

- Python 3
- Moduly ze standardní knihovny
- `customtkinter` jen při úpravách nebo rozšiřování GUI

> Soubor `PiCalculatorGUI.py` importuje `customtkinter`, ale aktuální rozhraní používá widgety Tkinter.

### Spuštění konzolové verze

```bash
python PiCalculator.py
```

Ukázkový výstup:

```text
Pi (Leibniz): 3.141591...
Pi (Nilakantha): 3.141592...
Pi (Monte Carlo): 3.14...
Pi (Machin): 3.141592653589793
Pi (math.pi): 3.141592653589793
```

Výsledky metody Monte Carlo se mohou lišit, protože používají náhodný výběr.

### Spuštění GUI

```bash
python PiCalculatorGUI.py
```

Zadejte:

- počet členů řad Leibniz a Nílakantha;
- počet náhodných bodů pro odhad Monte Carlo;
- poté klikněte na **Calculate**.

## 🧮 Metody v přehledu

| Metoda | Princip | Výhody a omezení |
|---|---|---|
| Leibniz | Střídavá řada | Snadno pochopitelná; pomalá konvergence |
| Nílakantha | Nekonečna řada | Mnohem rychlejší konvergence než Leibniz |
| Monte Carlo | Náhodný výběr | Jednoduchá a názorná; přesnost závisí na počtu bodů |
| Machin | Inverzní goniometrický vzorec | Rychlá, kompaktní a velmi přesná metoda |

## 🧪 Spuštění testů

Spusťte testy z kořenového adresáře repozitáře:

```bash
python -m unittest discover -s Tests -p "test*.py"
```

Testy pokrývají všechny čtyři aproximační metody. Monte Carlo test umožňuje širší toleranci kvůli náhodnosti.

## 📂 Struktura projektu

```text
PiCalculator/
├── PiCalculator.py          # Výpočtové metody a konzolový vstup
├── PiCalculatorGUI.py       # Grafické rozhraní Tkinter
├── Tests/
│   └── test_pi_calculator.py
└── LICENSE
```

## 💻 Ukázka použití API

```python
from PiCalculator import PiCalculator

calculator = PiCalculator()

print(calculator.calculate_pi_leibniz(100000))
print(calculator.calculate_pi_nilakantha(1000))
print(calculator.calculate_pi_monte_carlo(100000))
print(calculator.calculate_pi_machin())
```

## 🤝 Přispívání

Příspěvky jsou vítány:

1. Forkněte repozitář.
2. Vytvořte samostatnou větev pro funkci nebo opravu.
3. Přidejte nebo upravte unit testy.
4. Otevřete pull request.

Nápady na vylepšení: lepší ověřování vstupu, zobrazení všech čtyř výsledků v GUI, indikace průběhu nebo responzivnější rozložení rozhraní.

## 📄 Licence

Projekt je licencovaný pod [licencí MIT](LICENSE).

<div align="right"><a href="#-english">🇬🇧 Back to English</a></div>

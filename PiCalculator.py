import math
import random

class PiCalculator:
    """A class for approximating the value of pi using various methods."""

    def __init__(self):
        """Initializes an instance of the class."""
        pass

    def calculate_pi_leibniz(self, terms):
        """Calculates an approximation of pi using the Leibniz series.

        Args:
            terms: The number of terms in the series to use for calculation.

        Returns:
            An approximation of pi calculated using the Leibniz series.
        """
        pi = 0
        for i in range(terms):
            pi += (-1)**i / (2*i + 1)
        return 4 * pi

    def calculate_pi_nilakantha(self, terms):
        """Calculates an approximation of pi using the Nilakantha series.

        Args:
            terms: The number of terms in the series to use for calculation.

        Returns:
            An approximation of pi calculated using the Nilakantha series.
        """
        pi = 3
        sign = 1
        for i in range(1, terms + 1):
            pi += sign * 4 / ((2 * i) * (2 * i + 1) * (2 * i + 2))
            sign *= -1
        return pi

    def calculate_pi_monte_carlo(self, points):
        """Calculates an approximation of pi using the Monte Carlo method.

        Args:
            points: The number of random points to use for the simulation.

        Returns:
            An approximation of pi calculated using the Monte Carlo method.
        """
        inside_circle = 0
        total_points = points
        for _ in range(points):
            x = random.uniform(0, 1)
            y = random.uniform(0, 1)
            if x**2 + y**2 <= 1:
                inside_circle += 1
        return 4 * inside_circle / total_points
    
    def calculate_pi_machin(self):
            """Vypočítá aproximaci čísla π pomocí Machinovy formule.

            Returns:
                Aproximace čísla π vypočítaná pomocí Machinovy formule.
            """
            pi_4 = 4 * math.atan(1/5) - math.atan(1/239)
            return 4 * pi_4

calculator = PiCalculator()

# Výpočet π různými metodami
terms = 1000000  # Počet členů řady
points = 1000000  # Počet bodů pro Monte Carlo metodu

pi_leibniz = calculator.calculate_pi_leibniz(terms)
pi_nilakantha = calculator.calculate_pi_nilakantha(terms)
pi_monte_carlo = calculator.calculate_pi_monte_carlo(points)
pi_machin = calculator.calculate_pi_machin()

print("Pi (Leibniz):", pi_leibniz)
print("Pi (Nilakantha):", pi_nilakantha)
print("Pi (Monte Carlo):", pi_monte_carlo)
print("Pi (Machin):", pi_machin)
print("Pi (math.pi):", math.pi)

import tkinter as tk
import customtkinter

from PiCalculator import PiCalculator

class PiCalculatorGUI:
    """
    This class creates the graphical user interface (GUI) for calculating Pi.

    Attributes:
        root (tk.Tk): The main application window.
        input_frame (tk.Frame): The frame containing input widgets.
        button_frame (tk.Frame): The frame containing the calculate button.
        output_frame (tk.Frame): The frame containing the calculation results.
        label_terms (tk.Label): Label for the number of terms input.
        entry_terms (tk.Entry): Entry field for the number of terms.
        label_points (tk.Label): Label for the number of points for Monte Carlo.
        entry_points (tk.Entry): Entry field for the number of points.
        button_calculate (tk.Button): The button to trigger the calculation.
        label_result_leibniz (tk.Label): Label to display the Leibniz series result.
        label_result_nilakantha (tk.Label): Label to display the Nilakantha series result.
    """

    def __init__(self):
        """
        Initializes the GUI window, frames, and widgets.
        """

        # Create the main application window
        self.root = tk.Tk()
        self.root.title("π Calculator")
        self.root.resizable(False, False)       # Prevent window resizing
        self.root.geometry("400x200")           # Set window size


        # Create frames for organizing widgets
        self.input_frame = tk.Frame(self.root)
        self.input_frame.pack(side=tk.LEFT, fill="both", padx=10, pady=10)
        self.button_frame = tk.Frame(self.root)
        self.button_frame.pack(side=tk.RIGHT, fill="both", padx=10, pady=10)
        self.output_frame = tk.Frame(self.root)
        self.output_frame.pack(side=tk.BOTTOM, fill="x", pady=10)

        # Create and place widgets in the input frame
        self.label_terms = tk.Label(self.input_frame, text="Number of terms:")
        self.label_terms.pack()
        self.entry_terms = tk.Entry(self.input_frame)
        self.entry_terms.pack()

        self.label_points = tk.Label(self.input_frame, text="Number of points for Monte Carlo:")
        self.label_points.pack()
        self.entry_points = tk.Entry(self.input_frame)
        self.entry_points.pack()

        self.button_calculate = tk.Button(self.button_frame, text="Calculate")
        self.button_calculate.config(command=self.calculate)
        self.button_calculate.pack()

        self.label_result_leibniz = tk.Label(self.output_frame, text="Leibniz:")
        self.label_result_leibniz.pack()
        self.label_result_nilakantha = tk.Label(self.output_frame, text="Nilakantha:")
        self.label_result_nilakantha.pack()
        self.label_result_monte_carlo = tk.Label(self.output_frame, text="")
        self.label_result_machin = tk.Label(self.output_frame, text="")
        self.label_result_math_pi = tk.Label(self.output_frame, text="")



    def calculate(self):
        """
        Retrieves user input, performs calculations using the PiCalculator class,
        and updates the result labels.
        """

        terms = int(self.entry_terms.get())
        points = int(self.entry_points.get())

        # Perform calculations using the PiCalculator object
        calculator = PiCalculator()
        pi_leibniz = calculator.calculate_pi_leibniz(terms)
        pi_nilakantha = calculator.calculate_pi_nilakantha(terms)
        pi_monte_carlo = calculator.calculate_pi_monte_carlo(points)
        pi_machin = calculator.calculate_pi_machin()

        # Update result
        self.label_result_leibniz.config(text=f"Leibniz: {pi_leibniz:.10f}")
        self.label_result_nilakantha.config(text=f"Nilakantha: {pi_nilakantha:.10f}")



gui = PiCalculatorGUI()
gui.root.mainloop()
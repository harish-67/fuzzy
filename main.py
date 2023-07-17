import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Create the fuzzy variables
service = ctrl.Antecedent(np.arange(0, 11, 1), 'service')
food = ctrl.Antecedent(np.arange(0, 11, 1), 'food')
tip = ctrl.Consequent(np.arange(0, 26, 1), 'tip')

# Define the membership functions for each variable
service['poor'] = fuzz.trimf(service.universe, [0, 0, 5])
service['average'] = fuzz.trimf(service.universe, [0, 5, 10])
service['excellent'] = fuzz.trimf(service.universe, [5, 10, 10])

food['poor'] = fuzz.trimf(food.universe, [0, 0, 5])
food['average'] = fuzz.trimf(food.universe, [0, 5, 10])
food['excellent'] = fuzz.trimf(food.universe, [5, 10, 10])

tip['low'] = fuzz.trimf(tip.universe, [0, 0, 13])
tip['medium'] = fuzz.trimf(tip.universe, [0, 13, 25])
tip['high'] = fuzz.trimf(tip.universe, [13, 25, 25])

# Define the fuzzy rules
rule1 = ctrl.Rule(service['poor'] | food['poor'], tip['low'])
rule2 = ctrl.Rule(service['average'], tip['medium'])
rule3 = ctrl.Rule(service['excellent'] | food['excellent'], tip['high'])

# Create the fuzzy system
tip_ctrl = ctrl.ControlSystem([rule1, rule2, rule3])
tip_amount = ctrl.ControlSystemSimulation(tip_ctrl)

# Input values to the fuzzy system
tip_amount.input['service'] = 6.5
tip_amount.input['food'] = 9.8

# Compute the result
tip_amount.compute()

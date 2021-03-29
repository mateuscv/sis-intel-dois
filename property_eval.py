import matplotlib.pyplot as plt
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Valores para teste:
construction_standard_test_value = 8
property_area_test_value = 205

# Objetos com ranges:
property_area = ctrl.Antecedent(np.arange(20, 351, 0.5), 'property_area')
construction_standard = ctrl.Antecedent(np.arange(0, 11, 0.01), 'construction_standard')
price = ctrl.Consequent(np.arange(50000, 1000001, 100), 'price')

# Funções de pertinência automática:

property_area.automf(5, names=['tiny', 'small', 'medium', 'large', 'huge'])
construction_standard.automf(5, names=['very low', 'low', 'average', 'high', 'very high'])
price.automf(5, names=['very cheap', 'cheap', 'fair', 'expensive', 'very expensive'])

# Regras:

rule1 = ctrl.Rule(property_area['tiny'] & construction_standard['very low'], price['very cheap'])
rule2 = ctrl.Rule(property_area['tiny'] & construction_standard['low'], price['very cheap'])
rule3 = ctrl.Rule(property_area['tiny'] & construction_standard['average'], price['cheap'])
rule4 = ctrl.Rule(property_area['tiny'] & construction_standard['high'], price['cheap'])
rule5 = ctrl.Rule(property_area['tiny'] & construction_standard['very high'], price['fair'])

rule6 = ctrl.Rule(property_area['small'] & construction_standard['very low'], price['very cheap'])
rule7 = ctrl.Rule(property_area['small'] & construction_standard['low'], price['cheap'])
rule8 = ctrl.Rule(property_area['small'] & construction_standard['average'], price['cheap'])
rule9 = ctrl.Rule(property_area['small'] & construction_standard['high'], price['fair'])
rule10 = ctrl.Rule(property_area['small'] & construction_standard['very high'], price['fair'])

rule11 = ctrl.Rule(property_area['medium'] & construction_standard['very low'], price['cheap'])
rule12 = ctrl.Rule(property_area['medium'] & construction_standard['low'], price['fair'])
rule13 = ctrl.Rule(property_area['medium'] & construction_standard['average'], price['fair'])
rule14 = ctrl.Rule(property_area['medium'] & construction_standard['high'], price['expensive'])
rule15 = ctrl.Rule(property_area['medium'] & construction_standard['very high'], price['expensive'])

rule16 = ctrl.Rule(property_area['large'] & construction_standard['very low'], price['fair'])
rule17 = ctrl.Rule(property_area['large'] & construction_standard['low'], price['fair'])
rule18 = ctrl.Rule(property_area['large'] & construction_standard['average'], price['expensive'])
rule19 = ctrl.Rule(property_area['large'] & construction_standard['high'], price['very expensive'])
rule20 = ctrl.Rule(property_area['large'] & construction_standard['very high'], price['very expensive'])

rule21 = ctrl.Rule(property_area['huge'] & construction_standard['very low'], price['fair'])
rule22 = ctrl.Rule(property_area['huge'] & construction_standard['low'], price['expensive'])
rule23 = ctrl.Rule(property_area['huge'] & construction_standard['average'], price['very expensive'])
rule24 = ctrl.Rule(property_area['huge'] & construction_standard['high'], price['very expensive'])
rule25 = ctrl.Rule(property_area['huge'] & construction_standard['very high'], price['very expensive'])

controller = ctrl.ControlSystem([eval("rule" + str(x)) for x in range(1,26)])
simulator = ctrl.ControlSystemSimulation(controller)

simulator.input['construction_standard'] = construction_standard_test_value
simulator.input['property_area'] = property_area_test_value

# Crunch the numbers
simulator.compute()

print(simulator.output['price'])
property_area.view()
construction_standard.view()
price.view(sim=simulator)
plt.show()
"""Program Name: National Average Annual Vehicle Emissions Data Analysis Comparison
   Developer: Terrence Lee
   Development Period: August 10,2020 - August 17,2020
   """
# Link to data source: https://afdc.energy.gov/vehicles/electric_emissions.html

"""This Python program aims to compare the national average CO2 emissions between any 2 of 4 possible different vehicle types based on user input, developed for fun.
It is based on assumptions made in the data source website, thus it computes generalized results."""

GasolineAvgEmissions = 11435
# National average annual emissions of a gasoline vehicle in pounds of CO2

HybridAvgEmissions = 6258
# National average annual emissions of a hybrid vehicle in pounds of CO2

PlugInHybridAvgEmissions = 5885
# National average annual emissions of a plug-in hybrid vehicle in pounds of CO2

ElectricAvgEmissions = 4100
# National average annual emissions of an all electric vehicle in pounds of CO2

confirm1, confirm2 = 0, 0
comparisonTimeType, quantityComparisonType = 0, 0
durationInput, quantityInput = 0, 0
adjustedInput1, adjustedInput2 = 0, 0
difference = 0
# Global variables that will be adjusted

input1 = input("Please enter a vehicle type as displayed from the list (All-Electric, Plug-in Hybrid, Hybrid, or Gasoline). \nNo space necessary after the last letter. Case sensitive: ")
def first(i1):
  global input1
  if input1 == "All-Electric":
    input1 = ElectricAvgEmissions
  elif input1 == "Plug-in Hybrid":
    input1 = PlugInHybridAvgEmissions
  elif input1 == "Hybrid":
    input1 = HybridAvgEmissions
  elif input1 == "Gasoline":
    input1 = GasolineAvgEmissions
  else:
    print("Not a valid option.")
    input1 = input("Please make sure to enter a vehicle type as displayed from the list (All-Electric, Plug-in Hybrid, Hybrid, or Gasoline). \nNo space necessary after the last letter. Case sensitive: ")
    first(input1)
  return
first(input1)

input2 = input("Please enter another vehicle type as displayed from the list that is different from the 1st selection. \nNo space necessary after the last letter. Case sensitive: ")
def second(i2):
  global input2
  if input2 == "All-Electric":
    input2 = ElectricAvgEmissions
  elif input2 == "Plug-in Hybrid":
    input2 = PlugInHybridAvgEmissions
  elif input2 == "Hybrid":
    input2 = HybridAvgEmissions
  elif input2 == "Gasoline":
    input2 = GasolineAvgEmissions
  else:
    print("Not a valid option.")
    input2 = input("Please make sure to enter another vehicle type from the list as displayed that is different from the 1st selection. \nNo space necessary after the last letter. Case sensitive: ")
    second(input2)
  return
second(input2)

def check(var1, var2):
  global input2
  global quantityComparisonType, comparisonTimeType
  if var1 == var2:
    print("Same vehicle types were selected.")
    input2 = input("Please make sure to enter another vehicle type from the list as displayed that is different from the 1st selection. \nNo space necessary after the last letter. Case sensitive: ")
    second(input2)
    check(var1, input2)
  else:
    print("Great! Vehicle types can be compared.")
    quantityComparisonType = input("Please enter a numerical quantity for the selected duration type. \nNo space necessary after the number: ")
    comparisonTimeType = input("Please enter a duration type (days, months, or years). \nNo space necessary after the duration type: ")
  return
check(input1, input2)

def double_check(num):
  global quantityInput
  try:
    quantityInput = float(num)
  except ValueError:
    print("Invalid input: A number was not entered.")
    quantityInput = input("Please make sure to enter a numerical quantity for the selected duration type. \nNo space necessary after the number: ")
    double_check(quantityInput)
  return
double_check(quantityComparisonType)

def double_check2(duration):
  global durationInput
  if duration == "days" or duration == "Days":
    durationInput = duration
  elif duration == "months" or duration == "Months":
    durationInput = duration
  elif duration == "years" or duration == "Years":
    durationInput = duration
  else:
    print("A duration type from the list was not selected.")
    durationInput = input("Please make sure to enter days/months/years for the duration type. \nNo space necessary after the duration type: ")
    double_check2(durationInput)
  return
double_check2(comparisonTimeType)

def adjust(durationType, quantity):
  global adjustedInput1, adjustedInput2
  if durationType == "days" or durationType == "Days":
    adjustedInput1 = (input1 * quantity) / 365
    adjustedInput2 = (input2 * quantity) / 365
    difference = max(adjustedInput1, adjustedInput2) - min(adjustedInput1, adjustedInput2)
    print("After " + str(quantityInput) + " day(s), the difference in average CO2 emissions between the selected vehicle types is " + str(difference) + " pounds of CO2.")
  elif durationType == "months" or durationType == "Months":
    adjustedInput1 = (input1 * quantity) / 12
    adjustedInput2 = (input2 * quantity) / 12
    difference = max(adjustedInput1, adjustedInput2) - min(adjustedInput1, adjustedInput2)
    print("After " + str(quantityInput) + " month(s), the difference in average CO2 emissions between the selected vehicle types is " + str(difference) + " pounds of CO2.")
  elif durationType == "years" or durationType == "Years":
    adjustedInput1 = (input1 * quantity)
    adjustedInput2 = (input2 * quantity)
    difference = max(adjustedInput1, adjustedInput2) - min(adjustedInput1, adjustedInput2)
    print("After " + str(quantityInput) + " year(s), the difference in average CO2 emissions between the selected vehicle types is " + str(difference) + " pounds of CO2.")
  return
adjust(durationInput, quantityInput)
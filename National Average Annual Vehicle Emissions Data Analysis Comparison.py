"""Program Name: National Average Annual Vehicle Emissions Data Analysis Comparison
   Developer: Terrence Lee
   Development Period: August 10,2020 - August 17,2020
   
   Revision 1: July 10,2021
   -Added comments and revised function names to make code more readable/intuitive
   """
# Link to data source: https://afdc.energy.gov/vehicles/electric_emissions.html

"""This Python program aims to compare the national average CO2 emissions between any 2 of 4 possible different vehicle types based on user input, developed for fun.
It is based on assumptions made in the data source website, thus it computes generalized results. Written in the Visual Studio Code editor."""

GasolineAvgEmissions = 11435
# National average annual emissions of a gasoline vehicle in pounds of CO2

HybridAvgEmissions = 6258
# National average annual emissions of a hybrid vehicle in pounds of CO2

PlugInHybridAvgEmissions = 5885
# National average annual emissions of a plug-in hybrid vehicle in pounds of CO2

ElectricAvgEmissions = 4100
# National average annual emissions of an all electric vehicle in pounds of CO2

quantity, timeType = 0, 0
durationInput, quantityInput = 0, 0
adjustedInput1, adjustedInput2 = 0, 0
difference = 0
# Global variables that will be adjusted 

input1 = input("Please enter a vehicle type as displayed from the list (All-Electric, Plug-in Hybrid, Hybrid, or Gasoline). \nNo space necessary after the last letter. Case sensitive: ")
def first_choice(i1):
  global input1
  if input1 == "All-Electric":
    input1 = ElectricAvgEmissions
  elif input1 == "Plug-in Hybrid":
    input1 = PlugInHybridAvgEmissions
  elif input1 == "Hybrid":
    input1 = HybridAvgEmissions
  elif input1 == "Gasoline":
    input1 = GasolineAvgEmissions
  else: # None of the 4 vehicle types were chosen so the user is requested to answer again until a valid selection is made.
    print("\nNot a valid option.")
    input1 = input("Please make sure to enter a vehicle type as displayed from the list (All-Electric, Plug-in Hybrid, Hybrid, or Gasoline). \nNo space necessary after the last letter. Case sensitive: ")
    first_choice(input1)
  return
first_choice(input1)

input2 = input("Please enter another vehicle type as displayed from the list that is different from the 1st selection. \nNo space necessary after the last letter. Case sensitive: ")
def second_choice(i2):
  global input2
  if input2 == "All-Electric":
    input2 = ElectricAvgEmissions
  elif input2 == "Plug-in Hybrid":
    input2 = PlugInHybridAvgEmissions
  elif input2 == "Hybrid":
    input2 = HybridAvgEmissions
  elif input2 == "Gasoline":
    input2 = GasolineAvgEmissions
  else: # None of the 4 vehicle types were chosen so the user is requested to answer again until a valid selection is made.
    print("\nNot a valid option.")
    input2 = input("Please make sure to enter another vehicle type from the list as displayed that is different from the 1st selection. \nNo space necessary after the last letter. Case sensitive: ")
    second_choice(input2)
  return
second_choice(input2)

def check_choices(var1, var2):
  global input2
  global quantity, timeType
  if var1 == var2: # Check if the user selected the same vehicle types for the 2 choices.
    print("\nSame vehicle types were selected.")
    input2 = input("Please make sure to enter another vehicle type from the list as displayed that is different from the 1st selection. \nNo space necessary after the last letter. Case sensitive: ")
    second_choice(input2) # Ask the user to select a new vehicle type that is different from the first one.
    check_choices(var1, input2) # Compare the choices again with the updated 2nd vehicle type. User will be prompted to select again if the same vehicle type is picked.
  else:
    print("\nGreat! Vehicle types can be compared.")
    quantity = input("Please enter a numerical quantity for the selected duration type. \nNo space necessary after the number: ")
    timeType = input("Please enter a duration type (days, months, or years). \nNo space necessary after the duration type: ")
  return
check_choices(input1, input2)

def check_quantity(num):
  global quantityInput
  try: # See if the user typed a numerical value for the duration.
    quantityInput = float(num)
  except ValueError: 
    print("\nInvalid input: A number was not entered.")
    quantityInput = input("Please make sure to enter a numerical quantity for the selected duration type. \nNo space necessary after the number: ")
    check_quantity(quantityInput)
  return
check_quantity(quantity)

def check_timeType(duration):
  global durationInput
  if duration == "days" or duration == "Days":
    durationInput = duration
  elif duration == "months" or duration == "Months":
    durationInput = duration
  elif duration == "years" or duration == "Years":
    durationInput = duration
  else: # User did not type a valid duration type from the list.
    print("\nA duration type from the list was not selected.")
    durationInput = input("Please make sure to enter days/months/years for the duration type. \nNo space necessary after the duration type: ")
    check_timeType(durationInput)
  return
check_timeType(timeType)

def compare_choices(durationType, quantity): # Use received user input on duration to perform dimensional analysis and compare average CO2 emissions between the selected vehicle types.
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
compare_choices(durationInput, quantityInput)

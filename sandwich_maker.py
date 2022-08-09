import pyinputplus as pyip

response = pyip.inputMenu(['wheat', 'white', 'sourdough'], prompt='Choose a bread type:\n')
response = pyip.inputMenu(['chicken', 'turkey', 'ham', 'tofu'], prompt='Choose a protein type:\n')
response = pyip.inputYesNo(prompt='Want some cheese?\n')

if response == 'yes': 
    pyip.inputMenu(['cheddar','Swiss','mozzarella'], prompt='Choose cheese type:\n')

response = pyip.inputInt(prompt='How many sandwiches you tryna cop?\n', min=1)


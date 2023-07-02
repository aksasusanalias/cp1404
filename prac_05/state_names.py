"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""

# Reformat this file so the dictionary code follows PEP 8 convention
CODE_TO_NAME = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
                "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania"}

for state_code, state_name in CODE_TO_NAME.items():
    print(f"{state_code:3s} is {state_name}")

state_code = input("Enter short state: ").upper()
while state_code != "":
    try:
        state_name = CODE_TO_NAME[state_code]
        print(f"{state_code:3s} is {state_name}")
        state_code = input("Enter short state: ").upper()
    except KeyError:
        print("Invalid short state")
        state_code = input("Enter short state: ").upper()



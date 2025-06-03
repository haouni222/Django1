import sys

def Name_syntax(name):
    return ' '.join(word.capitalize() for word in name.split())

def the_dict():
    states = {
    "Oregon" : "OR",
    "Alabama" : "AL",
    "New Jersey": "NJ",
    "Colorado" : "CO"
    }
    capital_cities = {
    "OR": "Salem",
    "AL": "Montgomery",
    "NJ": "Trenton",
    "CO": "Denver"
    }

    new_capital_cities = {capital:tag for tag, capital in capital_cities.items()}

    if len(sys.argv) != 2:
        sys.exit(1)
    
    string = sys.argv[1]
    split = string.split(',')

    for item in split:
        item = item.strip()
        syntaxed_item = Name_syntax(item)
        if syntaxed_item is None or item == "":
            continue
        if syntaxed_item in states:
            tag = states[syntaxed_item]
            capital = capital_cities[tag]
            print(f"{capital} is the capital of {syntaxed_item}")
        elif syntaxed_item in new_capital_cities:
            tag = new_capital_cities[syntaxed_item]
            state = [state for state, t in states.items() if t == tag][0]
            print(f"{syntaxed_item} is the capital of {state}")
        else:
            print(f"{syntaxed_item} is neither a capital city nor a state")

if __name__ == "__main__":
    the_dict()
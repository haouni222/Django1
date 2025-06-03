import sys

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
    new_states = {tag:state for state, tag in states.items()}

    if len(sys.argv) != 2:
        sys.exit(1)
    cap = sys.argv[1]
    cap_tag = new_capital_cities.get(cap)
    if not cap_tag:
        sys.exit(f"Unknown capital city")
    
    print(new_states.get(cap_tag))

if __name__ == "__main__":
    the_dict()
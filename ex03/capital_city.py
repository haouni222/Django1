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

    if len(sys.argv) != 2:
        sys.exit(1)
    state = sys.argv[1]
    state_tag = states.get(state)
    if not state_tag:
        sys.exit(f"Unknown state")
    
    print(capital_cities.get(state_tag))

if __name__ == "__main__":
    the_dict()
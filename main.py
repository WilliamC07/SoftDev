import random

def print_random_team(classes):
    class_names = list(classes.keys())
    class_name = class_names[random.randint(0, len(class_names) - 1)]
    members = classes[class_name]
    print(members[random.randint(0, len(members) - 1)])

if __name__ == "__main__":
    KREWES = {
            "a": ["aa", "ab", "ac"],
            "b": ["ba", "bb", "bc"],
            "c": ["ca", "cb", "cc"]
        }

    for _ in range(3):
        print_random_team(KREWES)


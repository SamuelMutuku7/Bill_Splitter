def select_dates(potential_dates):
    selected = []
    for person in potential_dates:
        if person["age"] > 30 and "art" in person["hobbies"] and person["city"] == "Berlin":
            selected.append(person["name"])
    return ", ".join(selected)
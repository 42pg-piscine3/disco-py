#!/usr/bin/env python3

class People:
    def array_of_names(self, persons_d):
        # Init empty dictionary
        caps_persons = list()
        for key in persons_d:
            caps_persons.append(f"{key.capitalize()} {persons_d[key].capitalize()}")

        return caps_persons

persons = {
        "jean": "valjean",
        "grace": "hopper",
        "xavier": "niel",
        "fifi": "brindacier"
        }

group = People()
array_of_names = group.array_of_names


print(array_of_names(persons))

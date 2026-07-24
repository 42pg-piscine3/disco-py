#!/usr/bin/env python3


def array_of_names(persons_d):
        # Init empty list
        caps_persons = list()

        for key in persons_d:
            print ("work on: ", key)
            # The Real Work needed by the question
            caps_persons.append((key.capitalize()+ ' ' + persons_d[key].capitalize()))
            print (caps_persons)

        return caps_persons

persons = {
        "jean": "valjean",
        "grace": "hopper",
        "xavier": "niel",
        "fifi": "brindacier"
        }

#group = People()
#array_of_names = group.array_of_names


print(array_of_names(persons))

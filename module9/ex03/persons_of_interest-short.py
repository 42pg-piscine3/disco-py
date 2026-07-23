#!/usr/bin/env python3

class biodata:
    def date_sort(self, date):
        pass

    def famous_births(self, persons):
        # person dictionry of {key : {value}} where its value nests another {key: value}
        # persons.values() -> has {key: value} with keys of "name" and "date_of_birth"
        # we treat the persons.values() as a dictionary
        for obdata in sorted(persons.values(), key = lambda value: value["date_of_birth"] ):
            print(obdata["name"], "is a great scientist born in", obdata["date_of_birth"])
            #note: The original dictionary is unchanged.


women = biodata()
famous_births = women.famous_births

women_scientists = {
"ada": { "name": "Ada Lovelace", "date_of_birth": "1815" },
"cecilia": { "name": "Cecila Payne", "date_of_birth": "1900" },
"lise": { "name": "Lise Meitner", "date_of_birth": "1878" },
"grace": { "name": "Grace Hopper", "date_of_birth": "1906" }
}

famous_births(women_scientists)

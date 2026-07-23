#!/usr/bin/env python3

class biodata:
    def date_sort(self, date):
        pass

    def famous_births(self, persons):
        respect = dict(sorted(persons.items(), key = lambda items: items[1]["date_of_birth"]))
        for nname, obdata in respect.items():
            print(obdata["name"], "is a great scientist born in", obdata["date_of_birth"])

women = biodata()
famous_births = women.famous_births

women_scientists = {
"ada": { "name": "Ada Lovelace", "date_of_birth": "1815" },
"cecilia": { "name": "Cecila Payne", "date_of_birth": "1900" },
"lise": { "name": "Lise Meitner", "date_of_birth": "1878" },
"grace": { "name": "Grace Hopper", "date_of_birth": "1906" }
}

famous_births(women_scientists)

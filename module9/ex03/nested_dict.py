#!/usr/bin/env python3
women_scientists = {
"ada": { "name": "Ada Lovelace", "date_of_birth": "1815" },
"cecilia": { "name": "Cecila Payne", "date_of_birth": "1900" },
"lise": { "name": "Lise Meitner", "date_of_birth": "1878" },
"grace": { "name": "Grace Hopper", "date_of_birth": "1906" }
}

def get_dob(item):
    return item[1]["date_of_birth"]


cohort = dict(sorted(women_scientists.items(), key=get_dob))


for x, obj in women_scientists.items():
    print(x)

    for y in obj:
        print(y + ':', obj[y])

print("New dictionary")
for x, obj in cohort.items():
    print(x)

    for y in obj:
        print(y + ':', obj[y])

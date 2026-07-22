#!/usr/bin/env python3

class Hair:
# your method definition here

    def redfilter(self, x):
        # print("x: ",x[0], "hair:", x[1])
        if x[1] == "red":
            return True
        else:
            return False

    def find_the_redheads(self, people):
        red_hair = dict(filter(self.redfilter, people.items()))
        return list(red_hair.keys())

family = Hair()
find_the_redheads = family.find_the_redheads

dupont_family = {
"florian": "red",
"marie": "blond",
"virginie": "brunette",
"david": "red",
"franck": "red"
}
print(find_the_redheads(dupont_family))

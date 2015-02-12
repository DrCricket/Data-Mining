from fuzzy import *


user_pref = 0.0
avg_len = 0.0

mem = flc_triangular(0,5,10)

frb = [["low","low","low"],
       ["low","mid","mid"],
       ["low","hi","mid"],
       ["mid","low","low"],
       ["mid","mid","mid"],
       ["mid","hi","hi"],
       ["hi","low","mid"],
       ["hi","mid","hi"],
       ["hi","hi","hi"]]

## Input 1: 2.4,2.5

in1 = 2.4
in2 = 2.5

val1 = mem.value(2.3)
val2 = mem.value(5.6)

val1_zone = mem.zones(val1)
val2_zone = mem.zones(val2)

print val1
print val2


for i in val1_zone:
    for j in val2_zone:
        for rule in frb:
            if i == rule[0] and j == rule[1]:
                k = min(val1[i],val2[j])
                print k,rule[2], mem.defuzz(k,rule[2])


       





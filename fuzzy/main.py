from fuzzy import *


user_pref = 0.0
avg_len = 0.0

mem = flc_triangular(0,5,10)



## Input 1: 2.4,2.5

in1 = 2.4
in2 = 5.6

val1 = mem.value(2.3)
val2 = mem.value(5.6)


val1_zone = mem.zones(in1)
val2_zone = mem.zones(in2)


for i in val1_zone:
    for j in val2_zone:
        for rule in frb:
            if i == rule[0] and j == rule[1]:
                k = min(val1[i],val2[j])
                #print k,val1[i],val2[j]
                a = mem.defuzz(k,rule[2])
                #print k,rule[2] 
                #print mem.trap_area(a[0],a[1],a[2],a[3],k)
                print mem.trap_centroid(a[0],a[1],a[2],a[3],k)





       





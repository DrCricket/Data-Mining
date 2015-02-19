import fuzzy

input = 70

mem_input = fuzzy.flc_triangular(55,67,79)
mem_output = fuzzy.flc_triangular(0,25,75)

frb = [
       ["low","mid"],
       ["mid","mid"],
       ["hi","low"]]

val_zone = mem_input.zones(input)
val = mem_input.value(input)

centroid = []

print val_zone
print val

for i in val_zone:
    for rule in frb:
        if i == rule[0]:
            a = mem_output.defuzz(val[i],rule[1])
            print a
            centroid.append(mem_input.CoG(a[0],a[1],a[2],a[3],val[i]))

print centroid
                            

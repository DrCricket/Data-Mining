import fuzzy
import file_parser

pref_sentence = 0.0
pref_word = 4.5

pref_recency = 0.0

frb = [["low","low","low"],
       ["low","mid","mid"],
       ["low","hi","mid"],
       ["mid","low","low"],
       ["mid","mid","mid"],
       ["mid","hi","hi"],
       ["hi","low","mid"],
       ["hi","mid","hi"],
       ["hi","hi","hi"]]



#p = file_parser.parser("C:\Users\Chinka\Desktop\input.txt") ## Specify path name

mem_sentence = fuzzy.flc_triangular(2,10,18)
mem_word = fuzzy.flc_triangular(3,7,12)

mem_pref_word = fuzzy.flc_triangular(3,7,12)

#mem_recency = fuzzy.flc_triangular(

##code to read avg length of sentence, avg word length , recency

#parser = file_parser.parser("C:\Users\Chinka\Desktop\input.txt")

#in_word = parser.word_avg()
#in_sentence = parser.sentence_avg()



in_word = 8.9

val1 = mem_word.value(in_word)          ## Val1 : Dictionary object with membership calue in each of the three zones
val2 = mem_pref_word.value(pref_word)


val1_zone = mem_word.zones(in_word)
val2_zone = mem_pref_word.zones(pref_word)




centroid = []

for i in val1_zone:
    for j in val2_zone:
        for rule in frb:
            if i == rule[0] and j == rule[1]:
                k = max(val1[i],val2[j])
                a = mem_pref_word.defuzz(k,rule[2])
                    #print a
                centroid.append(mem_pref_word.trap_centroid(a[0],a[1],a[2],a[3],k))

cent_x =0.0
cent_y = 0.0
    #print centroid

for i in centroid:
    cent_x += i[0]
    cent_y += i[1]
        
cent_x = cent_x/4
cent_y = cent_y/4

pref_word = cent_x

print cent_x







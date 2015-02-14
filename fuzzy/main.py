import fuzzy
import file_parser

pref_sentence = 0.0
pref_word = 0.0
pref_recency = 0.0

p = file_parser.parser("C:\Users\Chinka\Desktop\input.txt") ## Specify path name

mem_sentence = fuzzy.flc_triangular(2,10,18)
mem_word = fuzzy.flc_triangular(3,7,12)
#mem_recency = fuzzy.flc_triangular(

##code to read avg length of sentence, avg word length , recency

parser = file_parser.parser("C:\Users\Chinka\Desktop\input.txt")

in_word = parser.word_avg()
in_sentence = parser.sentence_avg()


val1 = mem_sentence.value(in1)
val2 = mem_sentence.value(pref_sentence)


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







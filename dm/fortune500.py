### Python code to extract the number of likes each of the fortune 500 company's page has on Facebook


import facebook
import json


ACCESS_TOKEN = ""
def pp(obj):
    print json.dumps(obj,indent=1)

filename_in = "C\\\\\Fortune 500.txt"
filename_out = "C\\\\output.txt"

f_in = open(filename_in,"r+")
f_out = open(filename_out,"w")

company_list = [i[:-1] for i in f_in]

g = facebook.GraphAPI(ACCESS_TOKEN)

for company in company_list[]:

    response = g.request("search",{"q":company,"type":"page","limit":5})
    response_id = response["data"]
    print response_id[0]['id']
    i = []
    
    for j in range(4):
        i.append(response_id[j]["id"])
    mx = 0
    for j in i:
        obj = g.get_object(id=j)
        if(obj['likes']>mx):
            mx = obj['likes']
    
    string = '{0} : {1} \n'.format(str(company),mx)
    f_out.write(string)

f_out.close()

#f_out.close()

#for i in response_1:
#    response_list.append(g.get_object(id=i))

#like_list = []
#temp = []

#for i in response_list:
#    print i['likes']
    
            

                     

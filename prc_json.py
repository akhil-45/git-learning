import json 
#Read a json file
'''
req_file="myjson.json"

fo=open(req_file,'r')
#print(fo.read())
print(json.load(fo))

fo.close()
'''
#Write data(dictionary data) into a json file
my_dict={'Name':'Narendra','skills':['Python','shell','yaml','AWS']}

req_file="myinfo2.json"

fo=open(req_file,'w')
json.dump(my_dict,fo,indent=5)

fo.close()

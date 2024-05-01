import requests
import re,json

global lst

lst ={}


class rapid:
    search2=[]
    def __init__(self,d):
        url="https://rapiddns.io/s/"+d+"#result"
        req=requests.get(url).text
        #print(req)
        search=[]
        search=re.findall(f"[A-Za-z0-9]+\.[A-Za-z]+\.{d}",req)
        for i in search:
            if i not in self.search2:
                self.search2.append(i)

        list(set(self.search2))
        lst["rapid_res"]=self.search2
        

class crt:
    
    def __init__(self,d):
        url="https://crt.sh/?q="+d
        req=requests.get(url).text
        #print(req)
        search=[]
        search=re.findall(f"[A-Za-z0-9]+\.[A-Za-z]+\.{d}",req)
        search2=[]
        for i in search:
            if i not in search2 and i not in rapid_dom.search2:
                search2.append(i)
        list(set(search2))
        lst["crt_res"]=search2

    def jsonquery(self,dom):
        url=f"https://crt.sh/?q={dom}&output=json"
        s2=[]
        req=requests.get(url).text
        query=json.loads(req)
        res = [ sub['common_name'] for sub in query ]
        print("crt json query result\n-------------------\n")
        print(res)

        
def Passivebase(dom):
    #dom=input("please enter domain:  ")
    print("searching rapiddns ")
    global rapid_dom
    rapid_dom = rapid(dom)
    print("searching crt.sh ")
    global crt_dom
    crt_dom=crt(dom)

    #using json query method 
    #crt_dom2=crt(dom)
    #crt_dom2.jsonquery(dom)
    print("done")

    choice=int(input("please select:\n1)print\n2)export to json\n"))
    if choice == 1:
        print(lst)
    elif choice == 2:
        with open("res.json",'w') as f:
            json.dump(lst,f, indent=4)
    else:
        print("wrong choice!\n printing ")
        print(lst)

    print("filter on live hosts only?")
    choice2=int(input("please select:\n1)yes\n2)no\n"))
    checked_list=[]
    temp_list=list(lst.values())
    if choice2 == 1:
        for i in lst["crt_res"]:  
            try:
                req=requests.get("http://"+i).status_code
                checked_list.append(i)
            except Exception as e:
                print("Host not alive found: "+i)
        for i in lst['rapid_res']:  
            try:
                req=requests.get("http://"+i).status_code
                checked_list.append(i)
            except Exception as e:
                print("Host not alive found: "+i)
        choice=int(input("please select:\n1)print\n2)Rewrite live to json\n"))

        if choice == 1:
            print(checked_list)
        elif choice == 2:
            with open("res.json",'w') as f:
                json.dump(checked_list,f, indent=4)
        else:
            print("wrong choice!\n printing ")
            print(checked_list) 
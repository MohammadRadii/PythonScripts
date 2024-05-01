import requests,re
from Task2_Radi import *
import selenium,time
from selenium.webdriver.chrome.options import Options

class subbrute:
    alive=[]
    def __init__(self,choice):
        lst= open("list.txt",'r')
        print("trying...")
        for i in range(0,500):
            try:
                print(i)
                requests.get("http://"+lst.readline(i).strip()+"."+choice).status_code
                self.alive.append("http://"+lst.readline(i).strip()+"."+choice)
            except Exception:
                pass

class crawl:
    def __init__(self,d):
        #htt="http://"
        try:
            if "http" in d:
                req=requests.get(d).text
                search=[]
                reg=r'href=["\'](.*?)["\']'
                search=re.findall(reg, req)
                #print("FOUNDD ALL ")
                #print(search)
                for i in search:
                    if i not in collected:
                        if "http" in i:
                            crawlled.append(i)
                        else:
                             crawlled.append("http://"+i)
                    
            else:
                req=requests.get("http://"+d).text
                search=[]
                reg=r'href=["\'](.*?)["\']'
                search=re.findall(reg, req)
                #print("FOUNDD ALL ")
                #print(search)
                for i in search:
                    if i not in collected:
                        if "http" in i:
                            crawlled.append(i)
                        else:
                            crawlled.append("http://"+i)
        except Exception:
            pass
        
class screenshot:
    def __init__(self,doms):
        for i in doms:
            try:
                Chrome_options = Options()
                Chrome_options.add_argument('--log-level=3')
                Chrome_options.add_argument("--headless=new")
                driver = selenium.webdriver.Chrome(options=Chrome_options)
                driver.set_page_load_timeout(30)
                driver.get('http://'+i)
                driver.save_screenshot('Screenshots/'+i+'.png')
                print(f"screenshot for {i}")
                driver.quit()
                time.sleep(1)
            except Exception as e:
                print(f"couldn't take a screenshot for {i}")
                print(e)
        print("done")  

def Activebase(d):
    #choice=input("Please enter domain (Ex: google.com): ")
    dom=subbrute(d)
    print("Print live hosts: ")
    print(dom.alive)
    global collected,crawlled
    collected=[]
    crawlled=[]
    lnk=input("please input link to crawl in the format of 'http://example.com' : ")
    crawl(lnk)
    #crawling is limited for demo 
    count=0
    for x in collected:
        count=count+1
        if count==50:
                break
        if x not in crawlled:
            count=count+1
            if count==50:
                break
            print("crawl for ",x)
            crawl(x)
    print("screenshots\n########################")        
    screenshot(crawlled)
    #screenshot(collected)
    print(collected)
    print(crawlled)
    
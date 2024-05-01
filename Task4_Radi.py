import requests,re


class azureblobs:
    baseurl=".blob.core.windows.net"
    urlfiles=[]
    def __init__(self,dom):
        d=dom
        
        perm= open('perm.txt','r')
        final= open('final.txt','w')
        final.write(str(d)+'\n')
        final.close()
        final = open('final.txt','a')
        for i in perm:
            final.write((str(d)+i))
        for i in perm:     #$word$d
            final.write(i +str(d))
        
        for i in perm:     #$word$d$word
            final.write( i +str(d)+ i )

        for i in perm:     #$word$word$d
            final.write(i+i+str(d))
        
        for i in perm:     #$d$word$word
            final.write(str(d)+i+i)
        final.close()
        final= open('final.txt','r')
        finallist=final.read().splitlines()
        final.close()
        
        alive=[]
        finalurl=[]
        wordlist= open('containers.txt','r')
        word =wordlist.read().splitlines()
        wordlist.close()
        for f in finallist:
            url="https://"+f+self.baseurl
            try:
                r=requests.get(url, timeout=None)
                alive.append(url)
                print(r.status_code)
            except Exception:
                print("failed to resolve for: "+url)
        for i in alive:
            for w in word:
                constructedurl=f"{i}/{w}?restype=container&comp=list"
                finalurl.append(constructedurl)
                #print(constructedurl)
        checkedfinal={}
        for i in finalurl:
            try:
                #print("trying: "+ i)
                r=requests.get(i, timeout=None)
                if r.status_code == 200:
                    print("found: "+i)
                    checkedfinal[i]=r.text
            except Exception:
                print("failed to resolve for: "+i)
        print("--------------------------------------------------")
        print("getting urls from Azure URLs")

        for i in checkedfinal:
            reg=r"<Url>(.*?)</Url>"
            s=re.findall(reg,checkedfinal[i])
            if s != "":
                self.urlfiles.append(s)
        print(self.urlfiles)
        perm.close

class AWSbuck():
    baseurl ='.s3.amazonaws.com'
    awsFiles=[]
    def __init__(self,dom):
        self.d=dom    
        permaw= open('perm.txt','r').readlines()
        finalaw= open('final.txt','w')
        finalaw.write(str(self.d)+'\n')
        finalaw.close()
        finalaw = open('final.txt','a')
        #print(permaw)
        for i in permaw:     
            finalaw.write(i.strip('\n') + str(self.d)+'\n')
        '''for i in permaw:     
            finalaw.write(str(self.d)+ i.strip('\n'))
        for i in permaw:     
            finalaw.write( i + str(self.d) + i)
        for i in permaw:     
            finalaw.write(i+i+str(self.d))
        for i in permaw:     
            finalaw.write(str(self.d)+i+i)'''
   
        finalaw.close()
        finalaw= open('final.txt','r')
        finallistaw=finalaw.read().splitlines()
        finalaw.close()
        aliveaw=[]
        
        for faw in finallistaw:
            url="https://"+faw+self.baseurl
            try:
                r=requests.get(url, timeout=None)
                print(" trying: "+url)
                if r.status_code == 200:
                    aliveaw.append(url)
            except Exception:
                print("failed to resolve for: "+url)

        for i in aliveaw:
            r=requests.get(i, timeout=None)
            reg=r"<Key>(.*?)</Key>"
            s=re.findall(reg,r.text)
            self.awsFiles.append(s)

        print("printing found files on AWS: ")
        print("-------------------")
        print(self.awsFiles)


class GCPbuck:
    baseurl ='https://storage.googleapis.com/'
    gcpFiles=[]
    def __init__(self,dom):
        self.d=dom    
        permgcp= open('perm.txt','r').readlines()
        finalgcp= open('final.txt','w')
        finalgcp.write(str(self.d)+'\n')
        finalgcp.close()
        finalgcp = open('final.txt','a')
        #print(permaw)
        for i in permgcp:     
            finalgcp.write(str(self.d) + '-' + i.strip('\n') + '\n')
        '''for i in permgcp:     
            finalgcp.write(i.strip('\n') + str(self.d)+'\n')
        for i in permaw:     
            finalaw.write(str(self.d)+ i.strip('\n'))
        for i in permaw:     
            finalaw.write( i + str(self.d) + i)
        for i in permaw:     
            finalaw.write(i+i+str(self.d))
        for i in permaw:     
            finalaw.write(str(self.d)+i+i)'''
   
        finalgcp.close()
        finalgcp= open('final.txt','r')
        finallistgcp=finalgcp.read().splitlines()
        finalgcp.close()
        alivegcp=[]
        
        for faw in finallistgcp:
            url=self.baseurl+faw
            try:
                r=requests.get(url, timeout=None)
                print(" trying: "+url)
                if r.status_code == 200:
                    alivegcp.append(url)
            except Exception:
                print("failed to resolve for: "+url)

        for i in alivegcp:
            r=requests.get(i, timeout=None)
            reg=r"<Key>(.*?)</Key>"
            s=re.findall(reg,r.text)
            self.gcpFiles.append(s)

        print("printing found files on GCP: ")
        print("-------------------")
        print(self.gcpFiles)


def Cloudbase(doma):
    #dom=input("please enter domain: " )
    dom=doma.split(".")[0]
    print("***************")
    print(dom)
    az=azureblobs(dom) #acmetest
    aws=AWSbuck(dom) #acme
    gcp=GCPbuck(dom) #test-cache
    print("finalized files:")
    print("azure files:  ",az.urlfiles)
    print("azure files:  ",aws.awsFiles)
    print("gcp files:  ",gcp.gcpFiles)
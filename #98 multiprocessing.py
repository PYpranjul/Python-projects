import multiprocessing
import requests
import os
def Downloadfile(url,filename):
    print(f"start: {filename}")
    response=requests.get(url)
    os.makedirs("file",exist_ok=True)
    open (f"file/{filename}.jpg","wb").write(response.content)
    print(f"Downloaded: {filename}")
if __name__=="__main__":
    baseurl= "https://picsum.photos/2000/3000"
    pro=[]
    for i in range (10):
        url=f"{baseurl}{i}"
        p=multiprocessing.Process(target=Downloadfile,args=(url,i))
        p.start()
        pro.append(p)
    for p in pro:
        p.join()
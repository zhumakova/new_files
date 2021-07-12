import time,threading,requests

start=time.time()
URL = 'https://api.github.com/repos/{name}/{repo}/commits?page=1&per_page=100'
dict1 = {
    'Zinko17':'RestProject',
    'cholponesn':'StomCentr',
    'aliyaandabekova':'THE_BEST_PRICE',
    'zhumakova':'SportBetProject',
}
result = {}

def worker(username,repository):
    url=URL.format(name=username,repo=repository)
    response=requests.get(url).json()
    length=len(response)
    result[username]=length
ts=[]

for key,value in dict1.items():
    t=threading.Thread(target=worker,args=(key,value))
    t.start()
    ts.append(t)
for thread in ts:
    thread.join()

print(time.time()-start)
print(result)
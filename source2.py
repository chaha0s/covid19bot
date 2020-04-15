import requests
url='https://api.rootnet.in/covid19-in/stats/latest'
def mAllInfo():
    data=requests.get(url)
    res=[]
    pos=0
    cur=0
    deaths=0
    data=data.json()
    pos=int(data['data']['summary']['confirmedCasesIndian'])+int(data['data']['summary']['confirmedCasesForeign'])
    cur=int(data['data']['summary']['discharged'])
    deaths=int(data['data']['summary']['deaths'])
    res.append(pos)
    res.append(cur)
    res.append(deaths)
    return res
def mStateInfo(state):
    res=[]
    data=requests.get(url)
    data=data.json()
    for elems in data['data']['regional']:
        if state in elems['loc']:
            res.append(int(elems['confirmedCasesIndian'])+int(elems['confirmedCasesForeign']))
            res.append(int(elems['discharged']))
            res.append(int(elems['deaths']))
    return res
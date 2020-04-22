import requests

# To get information from MOHFW
def mCountryInfo():
    data=requests.get('https://www.mohfw.gov.in/dashboard/data/data.json')
    pos=0
    for elems in data.json():
        pos=pos+int(elems['positive'])
    return pos
def mStateInfo(state):
    data=requests.get('https://www.mohfw.gov.in/dashboard/data/data.json')
    for elems in data.json():
        if state==elems['state_name']:
            res=int(elems['positive'])
    return res

# To get information from covid19india.org

def get_stats_total():
    total=0
    data=requests.get('https://api.covid19india.org/state_district_wise.json')
    data=data.json()
    for x,y in data.items():
        for district in y['districtData']:
            if x!='Unknown':
                Number=(data[x]['districtData'][district]['confirmed'])
                total=total+Number
    return total
def get_state_total(state):
    total=0
    data=requests.get('https://api.covid19india.org/state_district_wise.json')
    data=data.json()
    for x,y in data.items():
        for district in y['districtData']:
            if x==state:
                Number=(data[x]['districtData'][district]['confirmed'])
                total=total+Number
    return total

def get_state_total_wDistricts(state):
    total=0
    data=requests.get('https://api.covid19india.org/state_district_wise.json')
    data=data.json()
    STATE=''
    dat=[]
    for x,y in data.items():
        for district in y['districtData']:
            if x==state:
                STATE=STATE+district+" : " + str(data[x]['districtData'][district]['confirmed']) +"\n"
                Number=(data[x]['districtData'][district]['confirmed'])
                total=total+Number
    dat.append(STATE)
    dat.append(total)
    return dat
# To get information from api.rootnet.in./covid19-in

def rootnetCountry():
    url='https://api.rootnet.in/covid19-in/stats/latest'
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
def rootnetState(state):
    url='https://api.rootnet.in/covid19-in/stats/latest'
    res=[]
    data=requests.get(url)
    data=data.json()
    for elems in data['data']['regional']:
        if state in elems['loc']:
            res.append(int(elems['confirmedCasesIndian'])+int(elems['confirmedCasesForeign']))
            res.append(int(elems['discharged']))
            res.append(int(elems['deaths']))
    return res
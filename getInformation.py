import requests
def mAllInfo():
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


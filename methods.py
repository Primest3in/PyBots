
import requests

def parse(url):
    s = "https://codeforces.com/profile/"
    url = url.strip()
    temp = url
    handle = ""
    while(len(temp) and temp[-1] != '/'):
        handle += temp[-1];
        temp = temp[:-1]


    handle = handle[::-1]
    handle = handle.strip()


    return temp, handle



def getMaxRating(handle):
    api_url = f"https://codeforces.com/api/user.info?handles={handle}"
    response = requests.get(api_url)
    cnt = 20
    while(response.status_code != 200 and cnt):
        response = requests.get(api_url)
        cnt -= 1
    

    data = response.json()
    data = data['result']
    return int(data[0]['maxRating'])

def getRole(handle):
    rating = getMaxRating(handle)
    
    if(rating >= 3000):
        return 'Legendary Grandmaster'
    elif(rating >= 2600):
        return 'International Grandmaster'
    elif(rating >= 2400):
        return 'Grandmaster'
    elif(rating >= 2300):
        return 'International Master'
    elif(rating >= 2100):
        return 'Master'
    elif(rating >= 1900):
        return 'Candy master'
    elif(rating >= 1600):
        return 'Expert'
    elif(rating >= 1400):
        return 'Specialist'
    elif(rating >= 1200):
        return 'Pupil'
    else:
        return 'Newbie'



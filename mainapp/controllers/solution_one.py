import requests
import json

def getKoreanData(startDate, endDate, sido, sigungu, cityGubun, marketType, userType, ageGroup, gender):
    params = {
        'startDate' : startDate,
        'endDate' : endDate,
        'sido' : sido,
        'sigungu' : sigungu,
        'cityGubun' : cityGubun,
        'marketType' : marketType,
        'userType' : userType,
        'ageGroup' : ageGroup,
        'gender' : gender
    }

    result = requests.get('https://gw.jejudatahub.net/api/proxy/072040e53b1f11e9ab958f5bbd84cea8/3d7197d6a6b4449db197d6a6b4c49d8b', params=params)
    ret = json.loads(result.text)
    print(ret)


def getChineseData(startDate, endDate, sido, sigungu, cityGubun, marketType):
    params = {
        'startDate' : startDate,
        'endDate' : endDate,
        'sido' : sido,
        'sigungu' : sigungu,
        'cityGubun' : cityGubun,
        'marketType' : marketType
    }

    result = requests.get('https://gw.jejudatahub.net/api/proxy/94e2c32f3b1d11e9ab958f5bbd84cea8/3d7197d6a6b4449db197d6a6b4c49d8b', params=params)
    ret = json.loads(result.text)
    print(ret)


if __name__ == "__main__":
    getKoreanData("201601","201902",None,None,None,None,None,None,None)
    getChineseData("201601", "201902", None, None, None, None)
import requests
import json
import pandas as pd
import numpy as np
import time

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
		'gender' : gender,
		'limit' : 100,
		'number' : 1
	}

	collected_data = pd.DataFrame()

	time.sleep(10)

	while(True):
		try:
			result = requests.get('https://gw.jejudatahub.net/api/proxy/072040e53b1f11e9ab958f5bbd84cea8/7669ab00eb7449bba9ab00eb74e9bbd3', params=params)
			ret = json.loads(result.text)
		except Exception as E:
			print (E)
			break
		print(ret)
		if(ret['hasMore']):
			params['number'] += 1
		else:
			break

		temp_df = pd.DataFrame.from_dict(ret['data'])
		collected_data = collected_data.append(temp_df)


		print(collected_data)

	return collected_data


def getChineseData(startDate, endDate, sido, sigungu, cityGubun, marketType):
	params = {
		'startDate' : startDate,
		'endDate' : endDate,
		'sido' : sido,
		'sigungu' : sigungu,
		'cityGubun' : cityGubun,
		'marketType' : marketType,
		'limit' : 100,
		'number' : 1
	}

	collected_data = pd.DataFrame()

	while(True):
		try:
			result = requests.get('https://gw.jejudatahub.net/api/proxy/94e2c32f3b1d11e9ab958f5bbd84cea8/7669ab00eb7449bba9ab00eb74e9bbd3', params=params)
			ret = json.loads(result.text)
		except Exception as E:
			print (E)
			break
		print(ret)
		if(ret['hasMore']):
			params['number'] += 1
		else:
			break

		temp_df = pd.DataFrame.from_dict(ret['data'])
		collected_data = collected_data.append(temp_df)


		print(collected_data)

	return collected_data


if __name__ == "__main__":
	getKoreanData("200001","201911",None,None,None,None,None,None,None)
	getChineseData("200001", "201911", None, None, None, None)

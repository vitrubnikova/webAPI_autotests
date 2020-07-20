#!/usr/bin/env python3

import json
from urllib import request

def test_total_count():
	res = request.urlopen('https://regions-test.2gis.com/1.0/regions')
	body = json.loads(res.read().decode('utf-8'))
	assert body['total'] == 22
#	print (body['items'])

#for def count page
	res2 = request.urlopen('https://regions-test.2gis.com/1.0/regions?page=1')
	body2 = json.loads(res2.read().decode('utf-8'))
	assert body['items'] == body2['items']
#	print (body['items'[0:4].id])
#	print (body['items'][0]['id'])

test_total_count()

def get_all_country():
	res = request.urlopen('https://regions-test.2gis.com/1.0/regions')
	body = json.loads(res.read().decode('utf-8'))

#	for item in body['items']:
#		item = 0
	
#	print (body['items'])

#вытаскивание и засовывание значений элементов массива для def contry_code
	all_country = []
	for i in body['items']:
		all_country.append(i['country']['code'])

#	print (all_country)
#	print (len(all_country))
#	print (type(all_country))
	for i in all_country:
		assert (i == 'kz' or i == 'kg' or i == 'ua' or i == 'ru' or i == 'cz')
		print (i)

#	assert list(all_id) == [196, 167, 67, 112, 114, 25, 105, 7, 26, 32]

#получение кода ответа сервера
	response = request.urlopen('https://api.github.com')
	print (response.code)

#	i = 1
#	ids = [body['items'][0 + i]['id']]
#	while i < 10:
#		print (body['items'][0 + i]['id'])
#		i = i + 1
	
#	print (ids)	
#	ids = get_id()
#	print (get_id)
#	id_all = [body['items'][0]['id'], body['items'][1]['id']]
#	print (id_all)

get_all_country()

#def all_id():
#	ids = get_id()
#	print(ids)

#all_id()

# для сопоставления значений country_code
def country_code_value():
	res = request.urlopen('https://regions-test.2gis.com/1.0/regions?country_code=ru')
	body = json.loads(res.read().decode('utf-8'))
#	print (body['items']['country']['code'])
#	all_country = []
	for i in body['items']:
		assert (i['country']['code']) == 'ru'

country_code_value()

def id_all():
	res = request.urlopen('https://regions-test.2gis.com/1.0/regions')
	body = json.loads(res.read().decode('utf-8'))
#	print (body['items']['country']['code'])
	all_id = []
	for i in body['items']:

		all_id.append(i['id'])
	print (all_id)

id_all()

def id_all_page2():
	res = request.urlopen('https://regions-test.2gis.com/1.0/regions?page=2')
	body = json.loads(res.read().decode('utf-8'))
#	print (body['items']['country']['code'])
	all_id = []
	for i in body['items']:
  		all_id.append(i['id'])

  		print (all_id)

id_all_page2()

def id_all_page3():
	res = request.urlopen('https://regions-test.2gis.com/1.0/regions?page=3')
	body = json.loads(res.read().decode('utf-8'))
#	print (body['items']['country']['code'])
	all_id = []
	for i in body['items']:
  		all_id.append(i['id'])

  		print (all_id)


id_all_page3()
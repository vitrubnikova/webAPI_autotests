#!/usr/bin/env python3

import json
from urllib import request

#page_size for valid values

def test_items_count5():
	res = request.urlopen('https://regions-test.2gis.com/1.0/regions?page_size=5')
	body = json.loads(res.read().decode('utf-8'))
	assert body['total'] == 22
	assert len(body['items']) == 5

test_items_count5()

def test_items_count10():
	res = request.urlopen('https://regions-test.2gis.com/1.0/regions?page_size=10')
	body = json.loads(res.read().decode('utf-8'))
	assert body['total'] == 22
	assert len(body['items']) == 10

test_items_count10()

def test_items_count15():
	res = request.urlopen('https://regions-test.2gis.com/1.0/regions?page_size=15')
	body = json.loads(res.read().decode('utf-8'))
	assert body['total'] == 22
	assert len(body['items']) == 15

test_items_count15()

#page_size default
def test_items_defaul_count():
	res = request.urlopen('https://regions-test.2gis.com/1.0/regions')
	body = json.loads(res.read().decode('utf-8'))
	assert body['total'] == 22
	assert len(body['items']) == 15

test_items_defaul_count()

#page_size BVA

def test_BVA_count4():
	res = request.urlopen('https://regions-test.2gis.com/1.0/regions?page_size=4')
	body = json.loads(res.read().decode('utf-8'))
	assert [*body.keys()] == ['error']

test_BVA_count4()

def test_BVA_count6():
	res = request.urlopen('https://regions-test.2gis.com/1.0/regions?page_size=6')
	body = json.loads(res.read().decode('utf-8'))
	assert [*body.keys()] == ['error']

test_BVA_count6()

def test_BVA_count9():
	res = request.urlopen('https://regions-test.2gis.com/1.0/regions?page_size=9')
	body = json.loads(res.read().decode('utf-8'))
	assert [*body.keys()] == ['error']

test_BVA_count9()

def test_BVA_count11():
	res = request.urlopen('https://regions-test.2gis.com/1.0/regions?page_size=11')
	body = json.loads(res.read().decode('utf-8'))
	assert [*body.keys()] == ['error']

test_BVA_count11()

def test_BVA_count14():
	res = request.urlopen('https://regions-test.2gis.com/1.0/regions?page_size=14')
	body = json.loads(res.read().decode('utf-8'))
	assert [*body.keys()] == ['error']

test_BVA_count14()

def test_BVA_count16():
	res = request.urlopen('https://regions-test.2gis.com/1.0/regions?page_size=16')
	body = json.loads(res.read().decode('utf-8'))
	assert [*body.keys()] == ['error']

test_BVA_count16()

#page_size negative

def test_count_null():
	res = request.urlopen('https://regions-test.2gis.com/1.0/regions?page_size=0')
	body = json.loads(res.read().decode('utf-8'))
	assert [*body.keys()] == ['error']

test_count_null()

def test_count_float():
	res = request.urlopen('https://regions-test.2gis.com/1.0/regions?page_size=15.5')
	body = json.loads(res.read().decode('utf-8'))
	assert [*body.keys()] == ['error']

test_count_float()

def test_count_empty():
	res = request.urlopen('https://regions-test.2gis.com/1.0/regions?page_size=')
	body = json.loads(res.read().decode('utf-8'))
	assert [*body.keys()] == ['error']

test_count_empty()

def test_char():
	res = request.urlopen('https://regions-test.2gis.com/1.0/regions?page_size=five')
	body = json.loads(res.read().decode('utf-8'))
	assert [*body.keys()] == ['error']

test_char()
#!/usr/bin/env python3

import json
from urllib import request

#page default
def test_default_count():
	res_def = request.urlopen('https://regions-test.2gis.com/1.0/regions')
	body_def = json.loads(res_def.read().decode('utf-8'))
	assert body_def['total'] == 22

	res = request.urlopen('https://regions-test.2gis.com/1.0/regions?page=1')
	body = json.loads(res.read().decode('utf-8'))
	assert body_def['total'] == body['total']
	assert body_def['items'] == body['items']

test_default_count()

#page BVA for min value

#def test_BVA_count0():
#	res = request.urlopen('https://regions-test.2gis.com/1.0/regions?page=0')
#	assert res.code == 404

#test_BVA_count0()

def test_BVA_count2():
	res = request.urlopen('https://regions-test.2gis.com/1.0/regions?page=2')
	body = json.loads(res.read().decode('utf-8'))
	assert body['total'] == 22
	assert len(body['items']) != 0

test_BVA_count2()

#page negative

def test_neg_num():
	res = request.urlopen('https://regions-test.2gis.com/1.0/regions?page=-1')
	body = json.loads(res.read().decode('utf-8'))
	assert [*body.keys()] == ['error']

test_neg_num()

def test_count_float0():
	res = request.urlopen('https://regions-test.2gis.com/1.0/regions?page=.5')
	body = json.loads(res.read().decode('utf-8'))
	assert [*body.keys()] == ['error']

test_count_float0()

def test_count_float1():
	res = request.urlopen('https://regions-test.2gis.com/1.0/regions?page=1.1')
	body = json.loads(res.read().decode('utf-8'))
	assert [*body.keys()] == ['error']

test_count_float1()

def test_count_empty():
	res = request.urlopen('https://regions-test.2gis.com/1.0/regions?page=')
	body = json.loads(res.read().decode('utf-8'))
	assert [*body.keys()] == ['error']

test_count_empty()
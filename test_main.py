from main import *

def test_simple_work():
	""" done. """
	assert simple_work_calc(10, 2, 2) == 36
	assert simple_work_calc(20, 3, 2) == 230
	assert simple_work_calc(30, 4, 2) == 650
	assert simple_work_calc(40, 5, 2) == 5390
	assert simple_work_calc(50, 6, 2) == 13592
	assert simple_work_calc(60, 7, 2) == 27416

def test_work():
	assert work_calc(10, 2, 2,lambda n: 1) == 15
	assert work_calc(20, 1, 2, lambda n: n*n) == 530
	assert work_calc(30, 3, 2, lambda n: n) == 300
	assert work_calc(30, 4, 2, lambda n: n) == 650
	assert work_calc(30, 5, 2, lambda n: n) == 1280
	assert work_calc(30, 6, 2, lambda n: n) == 2316


def test_compare_work():
	def work_fn1(n):
		return simple_work_calc(n, 2, 2)
    
	def work_fn2(n):
		return work_calc(n, 2, 2, lambda n: 1)

	res = compare_work(work_fn1, work_fn2)
	print(res)
	
def test_compare_span():
	def span_fn1(n):
		return simple_work_calc(n, 2, 2)

	def span_fn2(n):
		return work_calc(n, 2, 2, lambda n: 1)

	res = compare_span(span_fn1, span_fn2)
	print(res)


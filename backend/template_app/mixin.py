

def get_true_url_task(dic):
	if dic['type'] == 'week':
		url = 'http://localhost:8000/api/task-week/'
	elif dic['type'] == 'day':
		url = 'http://localhost:8000/api/task-day/'
	elif dic['type'] == 'month':
		url = 'http://localhost:8000/api/task-month/'
	return url
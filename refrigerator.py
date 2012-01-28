def refrigerate(current_temperature, desired_temperature, duration):
	is_off = True
	current_time = 0
	cost = 0
	while current_time != duration:
		while current_temperature > desired_temperature + 1.5:
			reduce_one_degree()
			if is_off:
				is_off = False
				cost = cost + 0.5
			cost = cost + 0.1
			current_temperature = current_temperature - 1
		wait_a_minute()
		current_time = current_time + 1
		current_temperature = current_temperature + 0.5
	return cost

def reduce_one_degree():
	# calls air conditioner hardware function reduz_um_grau()
	return

def wait_a_minute():
	# waits for one minute
	return

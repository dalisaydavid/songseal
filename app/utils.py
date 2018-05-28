def transform_value_in_tuple(tup, index, transform_function):
	temp_list = map(lambda (i,val): transform_function(val) if i == index else val, enumerate(tup))
	return tuple(temp_list)

def limit_string_length(s, l):
	return s[:l]
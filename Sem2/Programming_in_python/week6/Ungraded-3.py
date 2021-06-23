def add_record(data_table, entity_dict):
	data_table[entity_dict['uid']] = entity_dict
	return data_table

def search_record(data_table, entity_id):
	return data_table.get(entity_id, None)

def update_record(data_table, entity_id, key, value):
	try:
		data_table[entity_id][key] = value
	except KeyError:
		pass
	return data_table

def delete_record(data_table, entity_id):
	del data_table[entity_id]
	return data_table
def table_to_record(table_db):
	column_names, columns = [], []
	for dictionary in table_db:
		for k, v in dictionary.items():
			column_names.append(k)
			columns.append(v)

	out = []
	for entry in zip(*columns):
		out.append(dict(zip(column_names, entry)))

	return out

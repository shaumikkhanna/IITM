def is_file(path):
	return any(path.endswith(extention) for extention in ['.cpp', '.py', '.jpg', 'png'])

def is_folder(path):
	return not is_file(path)

def is_code(path):
	return any(path.endswith(extention) for extention in ['.cpp', '.py'])

def is_image(path):
	return any(path.endswith(extention) for extention in ['.jpg', 'png'])

def level(path):
	return path.count('/')
from jinja2 import Template


jnanpith_data = [
	{'year': 1965, 'awardee': 'G. Sankara Kurup', 'language': 'Malayalam'},
	{'year': 1966, 'awardee': 'Tarashankar Bandopadhyaya', 'language': 'Bengali'},
	{'year': 1967, 'awardee': 'Kuppali Venkatappagowda Puttappa', 'language': 'Kannada'}
]

def main():
	with open('template.html.jinja2', 'r') as f:
		TEMPLATE = f.read()

	t = Template(TEMPLATE)
	content = t.render(jnanpith_data = jnanpith_data)

	with open('new_jnanpith.html', 'w') as f:
		f.write(content)


if __name__ == '__main__':
	main()

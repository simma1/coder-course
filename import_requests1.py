import requests, bs4

for counter in range (1900,2000):

	res = requests.get('https://cineplex.com.au/movie/' + str(counter))

	res.raise_for_status()

	soup = bs4.BeautifulSoup(res.text, 'html.parser')

	body = soup.body

	try:
		h2 = body.select(".movie-header > h2")[0]
		h2str = str(h2)[4:-5]

	except Exception as e:
		print('movie locked in disney vault')

	else:
		print(h2str)
		with open ('resul2.txt', 'a+') as file:
			file.write(h2str)
			file.write('\n')
	
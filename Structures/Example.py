from imports import *

links, countrys = [], []


t1 = time()

for i in range(26):

    url = 'http://example.python-scraping.com/places/default/index/' + str(i)

    response = requests.get(url)

    if response.ok:
        # print(response)
        # print(response.headers)
        # print(response.text)

        soup = BeautifulSoup(response.text, 'lxml')

        tds = soup.find_all('td')
        for country in tds:
            links.append(url + country.find('a')['href'])
            countrys.append(country.text)
        sleep(3)  # 3s de délai

t2 = time()
print(t2 - t1)
print(countrys)


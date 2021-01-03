from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup as bs
#import dateutil.parser



app = Flask(__name__)

def chile_data():
    base_url = 'https://www.worldometers.info/coronavirus/'
    response = requests.get(base_url, headers={
        'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'
    })
    soup = bs(response.text, 'html.parser')
    table = soup.find('table', id=["main_table_countries_today"])
    table_rows = table.find_all('tr')
    data = []
    for tr in table_rows:
        td = tr.find_all('td')
        row = [i.text.strip() for i in td]
        if 'Chile' in row:
            data.append(row)
    return data
    
def chile_by_regions():
    base_url = 'https://www.minsal.cl/nuevo-coronavirus-2019-ncov/casos-confirmados-en-chile-covid-19/'
    response = requests.get(base_url, headers={
        'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'
    })
    soup = bs(response.text, 'html.parser')
    table = soup.find('table')
    table_rows = table.find_all('tr')
    data= []
    for tr in table_rows:
        td = tr.find_all('td')
        row = [i.text.strip() for i in td]
        data.append(row)
    cont = 0
    for values in data:
        if cont <= 2 :
            data.pop(0)
            cont += 1
        else:
            break

    return data

def news_scrape():
    pass



@app.route('/')
def hello_world():
    data = chile_data()
    data_regions = chile_by_regions()
    return render_template('index.html', data=data, data_regions=data_regions)

@app.route("/chile_status")
def zoek():
    return 'zoek, realmente sos un genio!'


if __name__ == '__main__':
    app.run(debug=True)
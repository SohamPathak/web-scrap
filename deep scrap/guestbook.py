from flask import Flask, render_template, request, flash,send_file
import bs4
from urllib.request import urlopen as uReq
from urllib.error import HTTPError
from bs4 import BeautifulSoup as soup
import jinja2

app = Flask(__name__)
app.secret_key = "i m the best"

def filter1(value, ch):
    try:
        if ch == 6:
        	if value is not None:
        		v = "Verified"
        		return v
        	else:
        		v = "Not Verified"
        		return v


        if ch == 5:
            year = value.find("div", {"class": "s-gold-supplier-year-icon"}).text[:2]
            return year

        if ch == 4:
            lin = value.div.a["href"]
            return lin

        if ch == 0:
            pdt_nam = value.div.a.img["alt"]
            return pdt_nam

        if ch == 1:
            low = value.findAll("span", {"itemprop": "lowPrice"})[0].text
            return low

        if ch == 2:
            high = value.findAll("span", {"itemprop": "highPrice"})[0].text
            return high

        if ch == 3:
            min_ord = value.findAll("div", {"class": "min-order"})[0].text
            return min_ord

    except IndexError as e:
        if ch == 6:
            default_value = 'Not Verified'

        else:
            default_value = 'nil'
        return default_value

    # handle the exception


def filter2(value):
    try:
        val = 'Verified'
        return val

    except IndexError:
        default_value = 'Not Verified'
        return default_value


def webscrap(my_url):
    check = 'https://www.alibaba.com/showroom/'
    count = 0

    # print("url entered")
    # my_url = 'https://www.alibaba.com/showroom/rc-car.html'
   
    print("validating URL")
    if my_url[0:33] == check:
        try:
            uReq(my_url)
        except HTTPError as e:
            print("Webpage not found")
            flash('Webpage not found')
            

    else:
        print("unable to parse :'') Try url like https://www.alibaba.com/showroom/ ")
        flash('unable to parse :'') Try url like https://www.alibaba.com/showroom/ ')
        render_template('sign.html')
        

    print("initialising connection.......")
    flash("initialising connection.......")
    # uReq(my_url)
    uClient = uReq(my_url)
    page_html = uClient.read()
    uClient.close()
    print("connection closed")
    page_soup = soup(page_html, "html.parser")
    containers = page_soup.findAll("div", {"class": "item-main"})
    num_of_items = len(containers)

    print("initialising excel file....")
    flash('initialising excel file....')

    filename = "data2.csv"
    f = open(filename, "w")
    headers = "product_name , lowest_price , highest_price , min amount , min_amount \n"
    f.write(headers)
    for cont in containers:
        pdt_name = cont.div.a.img["alt"]
        lows = cont.findAll("span", {"itemprop": "lowPrice"})
        highs = cont.findAll("span", {"itemprop": "highPrice"})
        amount = cont.findAll("div", {"class": "min-order"})
        min_ord = cont.findAll("div", {"class": "min-order"})
        try:
            # writing onto the file
            f.write(pdt_name.replace(",", "|") + "," + lows[0].text + "," + highs[0].text + "," + amount[0].text[:3] +","+ min_ord[0].text + "\n")
        # handle no attribute exception which will occur if the specific tag is not present int he tag
        except IndexError as e:
            count = count + 1
    flash('Attribute missing in')
    flash(count)
    print("Attribute missing in ")
    print(count)
    flash('finishing...')
    print("finishing...")
    f.close()
    return containers


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/sign')
def sign():
    return render_template('sign.html')


@app.route('/process', methods=['POST'])
def process():

    flash('url entered...')
    flash('Initiating >>>>>>')
    name = request.form['name']
    containers = webscrap(name)

    return render_template('index.html', name=name, containers=containers, filter1=filter1)


@app.route('/home', methods=['GET', 'POST'])
def home():
    links = ['https://www.youtube.com', 'https://www.bing.com', 'https://www.python.org', 'https://www.enkato.com']
    return render_template('example.html', links=links)

@app.route('/download_csv')
def download_csv():
	return send_file('data2.csv',
	                 mimetype='text/csv',
	                 attachment_filename='data2.csv',
	                 as_attachment=True)


if __name__ == '__main__':
    app.run(debug=True)
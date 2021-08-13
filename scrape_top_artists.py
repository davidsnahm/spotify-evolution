from bs4 import BeautifulSoup
import requests
import pandas as pd


def scrape_table(output_filename, url, output_dir="./data/"):
    print("Scraping data from " + url)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36',
        'Content-Type': 'text/html',
    }
    resp = requests.get(url, headers=headers).text
    soup = BeautifulSoup(resp, 'html.parser')
    table = soup.find('table', attrs={'class': 'resultsTab'})
    df = pd.read_html(str(table))[0]
    print("Writing table to csv file...")
    df.to_csv(output_dir + output_filename)
    print("Data preview: \n", df.head())
    print("Finished writing data to: " + output_dir + output_filename)


scrape_table(output_filename="top_1000_artists.csv", url="https://chartmasters.org/most-streamed-artists-ever-on-spotify/")

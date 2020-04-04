confirmedFile ='confirmed.csv'
deathsFile ='deaths.csv'
recoveredFile ='recovered.csv'

files = []

def saveAll():
    import requests
    import os.path

    baseUrl = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/'

    filesAndUrls = {
        confirmedFile: baseUrl + 'time_series_covid19_confirmed_global.csv',
        deathsFile: baseUrl + 'time_series_covid19_deaths_global.csv',
        recoveredFile: baseUrl + 'time_series_covid19_recovered_global.csv'
    } 

    for file, url in filesAndUrls.items():
        save(file, url)

def save(file, url):
    if not os.path.isfile('filename.txt'):
        with open(file, 'a+') as f:
            f.write(requests.get(url).text)

def load(file):
    import pandas as pd
    return pd.read_csv(file, index_col=1, header=0) \
        .drop(columns=['Province/State', 'Lat', 'Long']) \
        .groupby('Country/Region').sum() \
        

def main():
    import pandas as pd

    confirmed = load(confirmedFile)  # pd.read_csv(confirmedFile, index_col=1).drop(columns=['Province/State', 'Lat', 'Long'])
    deaths = pd.read_csv(deathsFile)
    recovered = pd.read_csv(recoveredFile)

    all = [confirmed, deaths, recovered]

    print(confirmed)

    # confirmed.astype(float, errors='ignore').plot.line(y=0, x=0)
    confirmed.loc('Algeria').transpose().astype(float, errors='ignore').plot.line()
    
    import matplotlib.pyplot as plt

# create fig1 (of type plt.figure)
# create fig2

    plt.show()  # will display fig1 and fig2 in different windows
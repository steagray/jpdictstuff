import requests
import gzip
import os

# URL to dictionaries to download 
# JMdict (w/ examples), Kanjidic2
dicts = ["http://ftp.edrdg.org/pub/Nihongo/JMdict_e_examp.gz", "http://www.edrdg.org/kanjidic/kanjidic2.xml.gz"]

# For each entry in the dicts array, downloads the gz file, and then decompresses it
# Uses the final segment of the url to determine the filename
def update_dicts():
    print("Updating dictionaries...")
    
    if not os.path.exists('dicts'):
        os.mkdir('dicts')
    for url in dicts:
        words = url.split('/')
        req = requests.get(url, allow_redirects=True)
        if req.status_code != requests.codes.ok:
            print("Unable to get ", words[-1])
            return

        open('dicts/' + words[-1], 'wb').write(req.content)
        with gzip.open('dicts/' + words[-1], 'rb') as g:
            with open('dicts/' + words[-1][:-3:1], 'wb') as f:
                f.write(g.read())
        os.remove("dicts/" + words[-1])
    
    print("Dictionaries Updated!")

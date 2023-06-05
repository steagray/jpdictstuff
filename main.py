from util.update_dict import update_dicts
from util.findword import findword
import xml.etree.ElementTree as ET

noupdate = True

if not noupdate:
    try:
        update_dicts()
    except:
        print("Unable to update dictionaries")

tree = ET.parse('dicts/JMdict_e_examp')
root = tree.getroot()

testphrase = 'まる'
print(findword(testphrase, root).find('.//reb').text)

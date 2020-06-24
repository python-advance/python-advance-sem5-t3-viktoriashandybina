from urllib.request import urlopen
from xml.etree import ElementTree as ET


def get_currencies(currencies_ids_lst=['R01239', 'R01235', 'R01035']):

    cur_res_str = urlopen("http://www.cbr.ru/scripts/XML_daily.asp")

    result = {}

    cur_res_xml = ET.parse(cur_res_str)

    root = cur_res_xml.getroot()
    valutes = root.findall('Valute')
    for el in valutes:
        valute_id = el.get('ID')

        if str(valute_id) in currencies_ids_lst:
            valute_cur_val = el.find('Value').text
            result[valute_id] = valute_cur_val

    return result

cur_vals = get_currencies()
print(cur_vals)
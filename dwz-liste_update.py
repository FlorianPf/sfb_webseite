import requests
import re
import datetime
import os

filename = 'dwz-liste.html'

def replace_umlauts(string):    # self explanatory
    umlauts = ['ä', 'ö', 'ü', 'Ä', 'Ö', 'Ü', 'ß']
    replacements = ['&auml;', '&ouml;', '&uuml;', '&Auml;', '&Ouml;', '&Uuml;', '&szlig;']
    for uml, rep in zip(umlauts, replacements):
        string = string.replace(uml, rep)
    return string

url = 'https://www.schachbund.de/verein/53002.html'
content_list = requests.get(url).text.split('\n')   # get html data from dsb website

data = []
i = content_list.index('<table id="dewisTable" class="body tablesorter">')+12   # start of relevant content
while True: # the following lines take each table row and process it to data
    if content_list[i]=='</tbody>': break
    entry = re.split('<|>', ''.join(content_list[i:i+8]))   # just the first way that came to my mind
    platz = entry[4]
    name = replace_umlauts(' '.join(entry[16].split(',')[::-1]))    # more elegant writing of name, also html umlauts
    dwz = entry[24]
    if dwz == '': dwz = '-----'
    if dwz not in ['Restp.', '-----']:  # remove number of auswertung and html artifacts
        dwz = re.sub('&nbsp;', '', dwz)
        dwz = re.sub(' ', '', dwz)
        dwz = dwz.split('-')[0]
    elo = entry[28]
    data.append([platz, name, dwz, elo])
    i += 8

# key_start and key_stop frame the content that gets replaced
# everything outside is just copied

input = open(filename).readlines()
with open(filename, 'w') as ofh:
    relevant = True
    for line in input:
        if relevant: ofh.write(line)
        if 'key_start' in line:
            ofh.write('<table class="dwz">\n')
            ofh.write('<tr>\n')
            ofh.write('<th>Platz</th>\n')
            ofh.write('<th>Name</th>\n')
            ofh.write('<th>DWZ</th>\n')
            ofh.write('<th>ELO</th>\n')
            ofh.write('</tr>\n')
            for entry in data:
                ofh.write(('<tr>'+'<td>{}</td>'*4+'</tr>\n').format(*entry))
            ofh.write('</table>\n')
            ofh.write('<p style="text-align: center;">Stand: {}. Immer aktuell auf der <a href="https://www.schachbund.de/verein/53002.html" target="_blank">Seite des DSB</a>.</p>\n'.format(datetime.datetime.today().strftime('%d.%m.%Y')))
            relevant = False    # toggle so that until key_stop everything (old) is discarded
        if 'key_stop' in line:
            relevant = True     # toggle on, the remaining lines are copied
            ofh.write('<!-- key_stop -->\n')

command_string = 'tidy -o '+filename+' -config tidy.conf '+filename+' 2>> /dev/null'
os.system(command_string)   # clean up html code

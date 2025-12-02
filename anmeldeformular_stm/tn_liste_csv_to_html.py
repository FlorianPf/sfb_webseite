import datetime

# Dieses Skript liest die Teilnehmerliste, sortiert die
# Teilnehmer nach der DWZ und schreibt eine HTML-Tabelle.

def replace_umlauts(string):
    umlauts = ['ä', 'ö', 'ü', 'Ä', 'Ö', 'Ü', 'ß']
    replacements = ['&auml;', '&ouml;', '&uuml;', '&Auml;', '&Ouml;', '&Uuml;', '&szlig;']
    for uml, rep in zip(umlauts, replacements):
        string = string.replace(uml, rep)
    return string

data = []

with open('teilnehmerliste.csv') as ifh:
    ifh.readline()  # Header ueberspringen
    while True:
        line = [x.strip() for x in ifh.readline().split(',')]
        if line == ['']: break
        data.append([replace_umlauts(line[0]), line[-1], replace_umlauts(line[-2])])

# Absteigend nach DWZ sortieren:
data = sorted(data, key=lambda x: x[1], reverse=True)

# HTML-Tabelle schreiben:
tn_anzahl = 0
with open('teilnehmerliste.html', 'w') as ofh:
    ofh.write('<p>Aktuelle Teilnehmerliste (Stand {}):</p>\n'.format(datetime.datetime.today().strftime('%d.%m.%Y')))
    ofh.write('<table class="tn-liste" style="margin-left: 10pt;">\n')
    ofh.write('  <tr>\n')
    ofh.write('    <th>Nr.</th>\n')
    ofh.write('    <th>Name</th>\n')
    ofh.write('    <th>DWZ</th>\n')
    ofh.write('    <th>Verein</th>\n')
    ofh.write('  </tr>\n')
    for row in data:
        tn_anzahl += 1
        ofh.write('  <tr>\n')
        ofh.write('    <td>{}</td>\n'.format(tn_anzahl))
        for item in row:
            if item == '0':
                ofh.write('    <td>-</td>\n')
            else:
                ofh.write('    <td>{}</td>\n'.format(item))
        ofh.write('  </tr>\n')
    ofh.write('</table>\n')
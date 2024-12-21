import datetime

def is_number(string):
    try:
        return(int(string[0]) in range(10))
    except:
        return False

def replace_umlauts(string):
    umlauts = ['ä', 'ö', 'ü', 'Ä', 'Ö', 'Ü', 'ß']
    replacements = ['&auml;', '&ouml;', '&uuml;', '&Auml;', '&Ouml;', '&Uuml;', '&szlig;']
    for uml, rep in zip(umlauts, replacements):
        string = string.replace(uml, rep)
    return string

def line_to_data(line):
    line_start = line
    line = line.split()   # remove whitespace
    # platz
    platz = line[0]
    line = line[1:]
    # name
    # extract name section:
    name = []
    for item in line:
        if item in ['Restp.', '-----']:
            break
        elif is_number(item):
            break
        else:
            name.append(item)
            line = line[1:]
    # restore pristine formatting:
    name = (' '.join(name)).split(',')
    # identify title, name and surname:
    if name[-1] == 'Dr.':
        titel = name[-1]
        name = name[:-1]
        vor = name[-1]
        nach = name[:-1]
        name = ' '.join([it for li in ([titel], [vor], nach) for it in li ])
    else:
        vor = name[-1]
        nach = name[:-1]
        name = ' '.join([it for li in ([vor], nach) for it in li ])
    name = replace_umlauts(name)
    # dwz
    if line[0] == 'Restp.':
        dwz = 'Restp.'
        auswertungen = ''
        line = line[1:]
    elif line[0] == '-----':
        dwz = '-----'
        auswertungen = ''
    else:
        dwz = line[0]
        line = line[1:]
        if line[0] == '-':
            line = line[1:]
            auswertungen = line[0]
            line = line[1:]
        else:
            auswertungen = line[0][1:]
            line = line[1:]
    # elo
    if line[0] == '-----':
        elo = '-----'
    else:
        elo = line[0]
    line = line[1:]

    if len(line) > 0:
        print(line_start)
        print('platz', platz)
        print('name', name)
        print('dwz', dwz)
        print('auswertungen', auswertungen)
        print('elo', elo)
        print('rest', line)

    return [platz, name, dwz, elo]

# Reihenfolge der Daten:
# Platz, Spielername, DWZ-Nr.Auswertung, Elo

# read data:
# with open('dwz-liste_kurz.txt') as ifh:
with open('dwz-liste.txt') as ifh:
    data = [line_to_data(line) for line in ifh.readlines()]

# output table as html:
with open('dwz-liste_inhalt.html', 'w') as ofh:
    ofh.write('<table class="dwz">\n')
    ofh.write('    <tr>\n')
    ofh.write('        <th>Platz</th>\n')
    ofh.write('        <th>Name</th>\n')
    ofh.write('        <th>DWZ</th>\n')
    ofh.write('        <th>ELO</th>\n')
    ofh.write('    </tr>\n')
    for row in data:
        ofh.write('    <tr>\n')
        for item in row:
            ofh.write('        <td>{}</td>\n'.format(item))
        ofh.write('    </tr>\n')
    ofh.write('</table>\n')
    ofh.write('<p style="text-align: center;">Stand: {}. Immer aktuell auf der <a href="https://www.schachbund.de/verein/53002.html" target="_blank">Seite des DSB</a>.</p>'.format(datetime.datetime.today().strftime('%d.%m.%Y')))
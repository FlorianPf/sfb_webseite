import urllib.request as req

link = "https://www.schachbund.de/verein/53002.html"
f = req.urlopen(link)
infile = f.read()
print(infile)
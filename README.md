# sfb_website

Kurzanleitung:
Im Hauptordner:
1. git pull (Dateien mit dem Repository synchronisieren)
2. html-Dateien aktualisieren (Inhalt der Webseite ändern)
3. python dwz-liste_update.py (DWZ-Liste automatisch aktualisieren)
4. Kalender aktualisieren (kalender_inhalt.html, dann index.html und kalender.html)
5. ./tidy_all_html.sh (vereinheitlicht den html-Code)
6. git add . ('staged' alle geänderten Dateien zum aktualisieren im Repository)
7. git commit -m '...' (fasst alle Änderungen in einem Befehl zusammen)
8. git push -u origin main (aktualisiert die Dateien im Repository)
Auf dem Server:
9. cd /war/www/html (dort liegt die Webseite)
10. sudo git pull (aktualisiert die Dateien aus dem Repository)
11. sudo chown www-data:www-data * (eingeschränkte Rechte an den Dateien, zur Sicherheit)

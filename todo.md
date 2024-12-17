# sfr_website

## To-Do-Liste:
- Anmeldeformular für die Stadtmeisterschaft realisieren!
- Weitere Seiten hinzufügen:
	Events?, DFMM-LV, SFB Jugend?, Links
- DWZ-Liste automatisieren:
	Bisher: DWZ-Liste von der Seite des DSB in eine Textdatei 
kopieren, mit dem Python-Skript in HTML übersetzen und einfügen.
	Zukünftig: Die Daten direkt von der Seit des DSB lesen und in 
eigenen HTML-Code übersetzen.
- 'nach oben'-Button verbessern: Im Moment sind es nur Links zu ebender 
Seite. Mit JS kann man bestimmt einfach zum Start der Seite scrollen, ohne 
sie neu zu laden.
- Bessere Darstellung für schmale Bildschirme und automatische Erkennung 
implementieren.
- Unterseiten und geeignete Anzeige in der Sidebar hinzufügen, vor allem für die Turniere
- Sidebar automatisch einbinden (aktuell ist es sehr aufwändig, eine neue Seite
	hinzuzufügen, weil die Sidebar auf allen anderen Seiten angepasst werden muss).
- Kernproblem: Unterseiten (Kalender, Turniere etc.) aktuell halten, wenn nur auf der
	Hauptseite gepostet wird. Am besten die Wahl der dargestellten Artikel
	automatisieren. In einer zentralen Datei werden sie hinzugefügt und automatisch
	auf allen nötigen Seiten hinzugefügt. So könnten z.B. auf der Hauptseite die
	zehn aktuellsten Meldungen dargestellt werden, alte werden automatisch entfernt.
	Im Kalender könnten die vergangenen Daten automatisch entfernt werden.
- Startseite mit Inhalt füllen



Struktur

- Turniere:
	Für jedes Turnier kurze Information zu Modus, Zeitraum und Link zur Unterseite:
	- Stadtmeisterschaft
	- Vereinsmeisterschaft
	- Schlosspokal
	Verweis auf Archiv für ältere Ergebnisse
- Archiv:
	Kurze Information. Welche Unterseiten?
	- Turniere
	- Mannschaften

# GitHub
## allgemein
Onlinedienst, der Software-Entwicklungsprojekte auf seinen 
Servern bereitstellt.
- repositories: verzeichnisse
- branch: erstellen
- merge: zusammenführen
- fork: respositories abspalten
- pull request: anfragen, änderungen zu übernehmen
## Git
### in terminal git repository erstellen
1. einen leeres git verzeichniss erstellen: git init
2. git status: zeigt den status des projektes
3. neues file erstellen: touch "datei" 
4. git status
5. änderungen vorschlagen, index hinzufügen: git add "datei"
6. änderungen bestätigen: git commit -m "add datei"
### local repository mit GitHub repository verknüpfen
1. auf GitHub seite repository seite erstellen
2. im terminal: git remote add origin "link zu repository"
3. gucken ob es richtig ist: git remote -v
4. inhalt der repositories synchronisieren: git push -u origin master
5. git status
6. änderungen sehen: git diff
7. änderungen "bestätigen": git add "datei", git commit -m "add message"
8. was haben wir im repository gemacht: git log
9. änderungen im lokalen zu remote repository senden: git push
10. änderungen von remote in lokal senden: git pull
### repository aus GitHub auf pc speichern
1. clone repository: repository auf pc speichern
- git clone "link des repository"
### github collab
1. name des partners suche
2. repositories 
3. auf eins drauf 
4. fork
5. auf eigene fork gehen
6. new pull request
7. create new pull request

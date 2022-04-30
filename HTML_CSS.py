import os

class HTML_CSS:
    def fCSS():
        return('''



body
{
    background-color: #2b2b2b;
    color: #ffffff;
    font-family: "Courier New", Courier, monospace;
    font-size: 12px;
    text-align: center;
}

p
{
    font-size: 12px;
}

header
{
    position: absolute;
    font-size: 11px;
    font-family:'Arial Narrow Bold', sans-serif;
    width: 40%;
    left: 30%;
    top: 0px;
    height: 90px;
    background-color: #0051ad;
}
nav
{
    position: absolute;
    color: #fff;
    width: 30%;
    top: 0px;
    left: 0%;
    height: 100%;
    background-color: rgb(34, 46, 46);
    z-index: 100;
}
nav h2
{
    padding-left: 10px;
}
  
nav a
{
    font-size: 14px;
    color: #fff;
    display: block;
    padding: 12px;
    padding-left: 5%;
    text-decoration: none;
    outline: none;
}
nav a:hover
{
    color: #386aff;
    background: #fff;
    position: relative;
    background-color: #fff;
    border-top-right-radius: 22px;
    border-bottom-right-radius: 22px;
}

nav .current
{
    background-color: #386aff;
    color: white;
    border-top-right-radius: 22px;
    border-bottom-right-radius: 22px;
}

.display
{
    position: absolute;
    top: 0px;
    right: 0px;
    width: 30%;
    height: 90px;
    background-color: #2b2b2b;
    z-index: 100;
}

.display h2
{
    padding-top: 0px;
    font-size: 17px;
}

.bilan
{
    position: absolute;
    width: 70%;
    left: 30%;
    height: 150px;
    top: 90px;
    background-color: #5a86ff;
}
.bilan:hover {
    color: #83fbff;
}
.container
{
    position: absolute;
    width: 70%;
    left: 30%;
    top: 240px;
    background-color: #366cff;
}
.coupure:hover {
    color: #c27efa;
}''')

    def fHTML(heuredebuttest, heurefintest, dureetest, nombrecoupures, dureecoupures, moyennecoupures, totalcoupures, heurefintestchange):
        Fichtexte = f'''<nav><h2>Navigation:</h2>'''
        i = 0
        isclass = ""
        for fichiers in os.listdir(os.path.dirname(__file__)):
            if fichiers.endswith(".html") and fichiers.startswith("docping---"):
                if "en_cours" in fichiers:
                    heurefintestchange2 = f'{heurefintestchange}'.replace("_", "<br>")
                    Fichtexte = Fichtexte + f'''<a class="current", href="docping---{heurefintestchange}.html">{heurefintestchange2}</a>'''
                else:
                    fichiersnohtml = fichiers.replace(".html", "")
                    fichiersnohtml = fichiersnohtml.replace("docping---", "")
                    fichiersnohtml = fichiersnohtml.replace("_", "<br>")
                    Fichtexte = Fichtexte + f'''<a href="{fichiers}">{fichiersnohtml}</a>'''
        Fichtexte = Fichtexte + f'''</nav>
'''

        for fichiers in os.listdir(os.path.dirname(__file__)):
            stop=False
            if fichiers.endswith(".html") and fichiers.startswith("docping---"):
                if "en cours" in fichiers:
                    pass
                else:
                    with open(f"{os.path.dirname(__file__)}\\{fichiers}", "r", encoding="utf-8") as fichier:
                        contenu = fichier.readlines()
                    
                    for ligne in contenu:
                        i = i + 1
                        if "<nav>" in ligne and stop==False:
                            try:
                                contenu[i-1] = Fichtexte
                                stop=True
                            except:
                                print(len(contenu))
                    i = 0
                    
                    with open(f"{os.path.dirname(__file__)}\\{fichiers}", "w", encoding="utf-8") as fichier:
                        fichier.writelines(contenu)


        fichiers2 = f"docping---{heurefintestchange}.html"
        fichiersbr = f"{fichiers2}".replace("_", "_<br>")
        return(f'''
<html>
    <head>
        <meta charset="utf-8">
        <link rel="stylesheet"href="docping.css">
        <title>Ping</title>
    </head>
    <body>
{Fichtexte}
        <header>
            <h1>Résultats du test de coupures<br>de connection</h1>
        </header>
        <div class="display">
            <h2>{fichiersbr}</h2>
        </div>
        <div class="bilan">
            <p>---------------------------------------------------------------<br>
            <strong>Début du test:</strong> {heuredebuttest}<br>
            <strong>Fin du test:</strong> {heurefintest}<br>
            <strong>Durée du test:</strong> {dureetest}<br><br>
            <strong>Nombre de coupures:</strong> {nombrecoupures}<br>
            <strong>Durée totale des coupures:</strong> {dureecoupures}<br>
            <strong>Durée moyenne des coupures:</strong> {moyennecoupures}<br>
            ---------------------------------------------------------------
            </p>
        </div>
        <div class="container">
            {totalcoupures}
        </div>
    </body>
</html>
''')


    def currentHTML(fichierpath):
        for fichiers in os.listdir(os.path.dirname(__file__)):
            i=0
            contenu = ""
            lignesplit = ""
            lignejoin = ""
            if fichiers.endswith(".html") and fichiers.startswith("docping---"):
                if "en cours" in fichiers:
                    pass
                else:
                    with open(f"{os.path.dirname(__file__)}\\{fichiers}", "r", encoding="utf-8") as fichier:
                        contenu = fichier.readlines()
                        j=0
                        for ligne in contenu:
                            i = i + 1
                            if "<nav>" in ligne:
                                ligne = ligne.replace('class="current",', "")
                                lignesplit = ligne.split()
                                stop = False
                                j = 0
                                for item in lignesplit:
                                    j = j + 1

                                    fichierpath2 = f'{fichierpath}'.replace('\\', '\\\\')
                                    changefichier = f"{fichier}"
                                    changefichier = f"{changefichier}".replace(f"<_io.TextIOWrapper name='","")
                                    changefichier = f"{changefichier}".replace(f"{fichierpath2}\\\\", "")
                                    changefichier = f"{changefichier}".replace("' mode='r' encoding='utf-8'>","")

                                    if f"{changefichier}" in item and stop == False:

                                        stop = True
                                        l = i
                                        print(j)
                                        lignesplit.insert(j-1, 'class="current",')

                        if lignesplit != None:
                            lignejoin = " ".join(lignesplit)
                            print(lignejoin)
                            print(i)
                            contenu[l-1] = lignejoin + "\n"
                            i = 0
                            l = 0
                        with open(f"{os.path.dirname(__file__)}\\{fichiers}", "w", encoding="utf-8") as fichier:
                            if contenu != []:
                                fichier.writelines(contenu)


    def bat(heurefintestchange):
        stop = False
        i=0
        with open(f"{os.path.dirname(__file__)}\\launch.bat", "r", encoding="utf-8") as fichier:
            contenu = fichier.readlines()
        with open(f"{os.path.dirname(__file__)}\\launch.bat", "w", encoding="utf-8") as fichier:
        
            for ligne in contenu:
                i = i + 1
                if "start" in ligne and stop==False:
                    try:
                        contenu[i-1] = f'start "" "docping---{heurefintestchange}.html"\n'
                        stop=True
                    except:
                        print(len(contenu))
            i = 0
            fichier.writelines(contenu)
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
    font-family:'Arial Narrow Bold', sans-serif;
    width: 100%;
    left: 0px;
    top: 0px;
    height: 60px;
    background-color: #4389da;
}

nav
{
    position: absolute;
    color: #fff;
    width: 250px;
    top: 0px;
    left: 0px;
    height: 1000px;
    background-color: rgb(34, 46, 46);
    z-index: 100;
}

nav h2
{
    cursor: pointer;
    padding-left: 20px;
}
  
nav a
{
    font-size: 14px;
    color: #fff;
    display: block;
    padding: 12px;
    padding-left: 30px;
    text-decoration: none;
    outline: none;
}

nav a:hover
{
    color: #38f2ff;
    background: #fff;
    position: relative;
    background-color: #fff;
    border-top-right-radius: 22px;
    border-bottom-right-radius: 22px;
}

.bilan
{
    position: absolute;
    width: 100%;
    right: 0px;
    height: 150px;
    top: 60px;
    background-color: #5a86ff;
}

.bilan:hover {
    color: #83fbff;
}

.container
{
    position: absolute;
    width: 100%;
    right: 0px;
    top: 210px;
    background-color: #366cff;
}

.coupure:hover {
    color: #c27efa;
}''')

    def fHTML(heuredebuttest, heurefintest, dureetest, nombrecoupures, dureecoupures, moyennecoupures, totalcoupures, heurefintestchange):
        Fichtexte = f'''<nav><h2>Navigation:</h2>'''
        i = 0
        for fichiers in os.listdir(os.path.dirname(__file__)):
            if fichiers.endswith(".html") and fichiers.startswith("docping -"):
                if "en cours" in fichiers:
                    Fichtexte = Fichtexte + f'''<a href="docping - {heurefintestchange}.html">docping - {heurefintestchange}.html</a>'''
                else:
                    Fichtexte = Fichtexte + f'''<a href="{fichiers}">{fichiers}</a>'''
        Fichtexte = Fichtexte + f'''</nav>
'''

        for fichiers in os.listdir(os.path.dirname(__file__)):
            stop=False
            if fichiers.endswith(".html") and fichiers.startswith("docping -"):
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
            <h1>Résultats du test de coupures de connection</h1>
        </header>
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

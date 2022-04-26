import os, tkinter
from time import strftime, sleep
from datetime import datetime
from threading import Thread

exit=False
numberFichier = 1
totalcoupures = ""

def ftkinter():
    global gui
    gui = tkinter.Tk()
    btn = tkinter.Button(gui, text ="Exit", command = fexit)
    btn.pack()
    Thread(target=prg).start()
    gui.mainloop()

def fexit():
    global exit
    exit=True
    gui.destroy()
    return exit

def prg():
    global numberFichier, totalcoupures
    var=True
    while True:
        if os.path.isfile(f"{os.path.dirname(__file__)}\\docping-{numberFichier}.html") == False:
            fichier = open(f"{os.path.dirname(__file__)}\\docping{numberFichier}.html", "w", encoding="utf-8")
            break
        else:
            numberFichier += 1
    
    fichierpath = os.path.dirname(__file__)
    fichier.truncate(0)
    fichier.write('''
<html>
    <head>
        <meta charset="utf-8">
        <link rel="stylesheet"href="docping.css">
        <title>Ping</title>
    </head>
    <body>
        <header>
            <h1>Résultats du test de coupures de connection</h1>
        </header>
''')
    heuredebuttest = datetime.now()
    dureecoupures = 0
    nombrecoupures = 0
    while exit == False:
        sleep(0.1)
        response = os.system("ping -n 1 google.com")
        a = datetime.now()
        heure = strftime(a.strftime("%Y-%m-%d %H:%M:%S"))

        if response == 1 and var == True:
            heuredebut=a
            totalcoupures = totalcoupures + f"<p><strong>Début de coupure:</strong> {heure}</p>"
            var=False

        if response == 0 and var == False:
            heurefin=datetime.now()

            if dureecoupures == 0:
                dureecoupures = heurefin - heuredebut
            else:
                dureecoupures = dureecoupures + (heurefin - heuredebut)
            totalcoupures = totalcoupures + f"<p><strong>Fin de coupure:</strong> {heure}\tDurée de coupure: {str(heurefin - heuredebut)}</p>"
            nombrecoupures += 1
            fichier.close()
            fichier = open(f"{os.path.dirname(__file__)}\\docping{numberFichier}.html", "a", encoding="utf-8")
            var=True
    dureetest = datetime.now() - heuredebuttest
    if nombrecoupures != 0:
        moyennecoupures = dureecoupures/nombrecoupures
    else:
        moyennecoupures = "0"
    heurefintest = datetime.now()
    fichier.write(f"""
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
""")
    print(totalcoupures)
    fichier.close()
    heurefintestchange = heurefintest.strftime("%Y-%m-%d %H-%M-%S")
    os.rename(f"{fichierpath}\\docping{numberFichier}.html", f"{fichierpath}\\docping - {heurefintestchange}.html")
    
ftkinter()

def css():
    fcss = open(f"{os.path.dirname(__file__)}\\docping.css", "w", encoding="utf-8")
    fcss.truncate(0)
    fcss.write('''
body {
    background-color: #2b2b2b;
    color: #ffffff;
    font-family: "Courier New", Courier, monospace;
    font-size: 12px;
    text-align: center;
}
p {
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

.container:hover {
    color: #c27efa;

}''')
    fcss.close()

css()

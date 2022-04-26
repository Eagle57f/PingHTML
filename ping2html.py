import os, tkinter
from time import strftime, sleep
from datetime import datetime
from threading import Thread

exit=False
numberFichier = 1


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
    global numberFichier
    var=True
    while True:
        if os.path.isfile(f"{os.path.dirname(__file__)}\\docping{numberFichier}.html") == False:
            fichier = open(f"{os.path.dirname(__file__)}\\docping{numberFichier}.html", "w", encoding="utf-8")
            break
        else:
            numberFichier += 1
    
    fichier.truncate(0)
    fichier.write('''
<html>
    <head>
        <meta charset="utf-8">
        <link rel="stylesheet"href="docping.css">
        <title>Ping</title>
    </head>
    <body>
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
            fichier.write(f"<p><strong>Début de coupure:</strong> {heure}</p>")
            var=False

        if response == 0 and var == False:
            heurefin=datetime.now()

            if dureecoupures == 0:
                dureecoupures = heurefin - heuredebut
            else:
                dureecoupures = dureecoupures + (heurefin - heuredebut)
            fichier.write(f"<p><strong>Fin de coupure:</strong> {heure}\tDurée de coupure: {str(heurefin - heuredebut)}</p>")
            nombrecoupures += 1
            fichier.close()
            fichier = open(f"{os.path.dirname(__file__)}\\docping{numberFichier}.html", "a", encoding="utf-8")
            var=True
    dureetest = datetime.now() - heuredebuttest
    if nombrecoupures != 0:
        moyennecoupures = dureecoupures/nombrecoupures
    else:
        moyennecoupures = "0"
    fichier.write(f"""
        <p>---------------------------------------------------------------<br>
        <strong>Début du test:</strong> {heuredebuttest}<br>
        <strong>Fin du test:</strong> {datetime.now()}<br>
        <strong>Durée du test:</strong> {dureetest}<br><br>

        <strong>Nombre de coupures:</strong> {nombrecoupures}<br>
        <strong>Durée totale des coupures:</strong> {dureecoupures}<br>
        <strong>Durée moyenne des coupures:</strong> {moyennecoupures}<br>
        ---------------------------------------------------------------
        </p>
    </body>
</html>
""")


ftkinter()


def css():
    fcss = open("D:\\Python\\docping.css", "w", encoding="utf-8")
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
text-align: center;
}
p:hover {
color: #acd8ff;
}''')
    fcss.close()


css()

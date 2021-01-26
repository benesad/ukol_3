import json

class File:
    def __init__(self, name):
        self.name=name

    def read():
        try:
            with open(name, "r", encoding="UTF-8") as soubor:
                return json.load(soubor)["features"]
        except FileNotFoundError: # zjistuje, zda existuje
            print(f"CHYBA: Pozadovany soubor {name} neexistuje. Program skonci.")
            exit()
        except PermissionError: # zjistuje pristup k souboru
            print(f"CHYBA: Nemam pristup k {name}.Program skonci.")
            exit()
        except ValueError as e: # validuje i pokud se jedna o validni JSON
            print(f"CHYBA: Soubor {name} neni validni. Program skonci.\n", e)
            exit()
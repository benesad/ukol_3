import json

class File:
    def __init__(self, name):
        self.name=name

    def read(self):
        try:
            with open(self.name, "r", encoding="UTF-8") as physicFile:
                return json.load(physicFile)["features"]
        except FileNotFoundError: # zjistuje, zda existuje
            print(f"CHYBA: Pozadovany soubor {self.name} neexistuje. Program skonci.")
            exit()
        except PermissionError: # zjistuje pristup k souboru
            print(f"CHYBA: Nemam pristup k {self.name}.Program skonci.")
            exit()
        except ValueError as e: # validuje i pokud se jedna o validni JSON
            print(f"CHYBA: Soubor {self.name} neni validni. Program skonci.\n", e)
            exit()
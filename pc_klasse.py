import json
import os
import difflib

class pc():
    def __init__(self,name):
        self.name = name
        self.cpu = "empty"
        self.grafik_karte   = "empty"
        self.mainboard  = "empty"
        self.ram  = "empty"
        self.netzteil  = "empty"
        self.speicher  = "empty"
        self.gehäuse  = "empty"
        self.teile = [self.cpu,self.grafik_karte,self.mainboard,self.ram,self.netzteil,self.speicher,self.gehäuse]

    def mainboard_wechseln(self, neues_mainboard_name):
        neues_mainboard = self.teil_finden('mainboard', neues_mainboard_name)
        if self.cpu and neues_mainboard["sockel"] != self.cpu["sockel"]:
            raise "Das neue Mainboard ist nicht kompatibel mit dem Sockel des CPUs."
        if self.ram and (neues_mainboard["ram_slots"] < self.ram["anzahl_der_module"] or
                         neues_mainboard["ram_slot_typ"] != self.ram["speichertyp"]):
            raise "Das neue Mainboard ist nicht kompatibel mit dem RAM."
        self.mainboard = {
            "modell": neues_mainboard["modell"],
            "sockel": neues_mainboard["sockel"],
            "form_faktor": neues_mainboard["form_faktor"],
            "ram_slots": neues_mainboard["ram_slots"],
            "ram_slot_typ": neues_mainboard["ram_slot_typ"],
            "stromverbrauch": neues_mainboard["stromverbrauch"]
        }

    def cpu_wechseln(self, neuer_cpu_name):
        neuer_cpu = self.teil_finden('cpu', neuer_cpu_name)
        if isinstance(self.mainboard, dict) and self.mainboard.get("sockel") != neuer_cpu["sockel"]:
            raise "Der neue CPU ist nicht kompatibel mit dem Sockel des Mainboards."
        self.cpu = {
            "modell": neuer_cpu["modell"],
            "taktfrequenz": neuer_cpu["taktfrequenz"],
            "kerne": neuer_cpu["kerne"],
            "sockel": neuer_cpu["sockel"],
            "stromverbrauch": neuer_cpu["stromverbrauch"]
        }

    def ram_wechseln(self, neuer_ram_name):
        neuer_ram = self.teil_finden('ram', neuer_ram_name)
        if self.mainboard and (neuer_ram["anzahl_der_module"] > self.mainboard["ram_slots"] or
                           neuer_ram["speichertyp"] != self.mainboard["ram_slot_typ"]):
            raise "Der neue RAM ist nicht kompatibel mit dem Mainboard."
        self.ram = {
            "modell": neuer_ram["modell"],
            "speichergröße": neuer_ram["speichergröße"],
            "speichertyp": neuer_ram["speichertyp"],
            "taktfrequenz": neuer_ram["taktfrequenz"],
            "anzahl_der_module": neuer_ram["anzahl_der_module"],
            "stromverbrauch": neuer_ram["stromverbrauch"]
        }

    def set_netzteil(self, neues_netzteil_name):
        neues_netzteil = self.teil_finden('netzteil', neues_netzteil_name)
        self.netzteil = {
            "modell": neues_netzteil["modell"],
            "watt": neues_netzteil["watt"],
            "zertifizierung": neues_netzteil["zertifizierung"],
            "modular": neues_netzteil["modular"],
             "form_faktor": neues_netzteil["form_faktor"]
        }

    def grafik_karte_wechseln(self, neue_grafik_karte_name):
        neue_grafik_karte = self.teil_finden('grafikkarte', neue_grafik_karte_name)
        self.grafik_karte = {
            "modell": neue_grafik_karte["modell"],
            "chipset": neue_grafik_karte["chipset"],
            "speicher": neue_grafik_karte["speicher"],
            "taktung": neue_grafik_karte["taktung"],
            "stromverbrauch": neue_grafik_karte["stromverbrauch"]
        }

    def speicher_wechseln(self, neuer_speicher_name):
        neuer_speicher = self.teil_finden('speicher', neuer_speicher_name)
        self.speicher = {
            "typ": neuer_speicher["typ"],
            "größe": neuer_speicher["größe"],
            "stromverbrauch": neuer_speicher["stromverbrauch"]
        }

    def gehäuse_wechseln(self, neues_gehäuse_name):
        neues_gehäuse = self.teil_finden('gehäuse', neues_gehäuse_name)
        self.gehäuse = {
             "modell": neues_gehäuse["modell"],
            "typ": neues_gehäuse["typ"],
            "farbe": neues_gehäuse["farbe"],
        }

    def strom_verbrauch_berechnen(self):
        gesamt_stromverbrauch = None
        for pc_teil in self.teile:
            gesamt_stromverbrauch += pc_teil["stromverbrauch"]
        return gesamt_stromverbrauch

    def teil_finden(self, teil_typ, teil_name):
        # Definieren Sie den Pfad zur JSON-Datei
        datei_pfad = os.path.join(os.getcwd(), "data", "json", f"{teil_typ}.json")

        with open(datei_pfad, 'r') as json_datei:
            teil_data = json.load(json_datei)

            # Erzeugen Sie eine Liste von Teilen Namen
            teil_namen = [teil['name'] for teil in teil_data]

            # Finden Sie nahe Übereinstimmungen im Fall eines Tippfehlers
            übereinstimmungen = difflib.get_close_matches(teil_name, teil_namen, n=1, cutoff=0.6)

            if übereinstimmungen:
                teil_name = übereinstimmungen[0]

                # Finden Sie das richtige Teil basierend auf seinem Namen
            for teil in teil_data:
                if teil['name'] == teil_name:
                    return self.dict_formatieren(teil, teil_typ)

            # Wenn das Teil nach der Schleife nicht gefunden wurde, werfen Sie eine Ausnahme
            raise Exception(f'Teil {teil_name} von Typ {teil_typ} nicht gefunden.')

    def dict_formatieren(self,teil_dict,teil_typ):
        teil = {}
        if teil_typ == "grafikkarte":
            teil ={
            "modell": teil_dict["name"],
            "speicher":teil_dict["memory"],
            "chipset":teil_dict["chipset"],
            "taktung": teil_dict["core_clock"],
            "stromverbrauch": 200
            }
            # code to execute if teil_typ is 'grafikkarte'

        elif teil_typ == "cpu":
            teil = {
            "modell": teil_dict["name"],
            "taktfrequenz": teil_dict["core_clock"],
            "kerne": teil_dict["core_count"],
            "sockel": self.get_sockel(teil_dict["name"]),
            "stromverbrauch": teil_dict["tdp"]
            }

        elif teil_typ == "mainboard":
            teil = {
             "modell": teil_dict["name"],
            "sockel": teil_dict["socket"],
            "form_faktor": teil_dict["form_factor"],
            "ram_slots": teil_dict["memory_slots"],
            "ram_slot_typ": self.get_speichertyp(teil_dict["max_memory"]),
            "stromverbrauch": 20
            }

        elif teil_typ == "ram":
            teil = {
        "modell": teil_dict["name"],
            "speichergröße":teil_dict["modules"][1],
            "speichertyp": self.get_ram_speichertyp(teil_dict[teil_dict["speed"]]),
            "taktfrequenz": teil_dict["speed"][1],
            "anzahl_der_module": teil_dict["modules"][0],
            "stromverbrauch": 10
            }

        elif teil_typ == "netzteil":
            teil = {
            "modell": teil_dict["name"],
            "watt": teil_dict["wattage"],
            "zertifizierung": teil_dict["efficiency"],
            "modular": teil_dict["modular"],
            "form_faktor": teil_dict["type"],
            }
        elif teil_typ == "speicher":
            teil = {
                "typ": teil_dict["type"],
                "größe": teil_dict["capacity"],
                "stromverbrauch": 10
            }
            # code to execute if teil_typ is 'speicher'

        elif teil_typ == "gehäuse":
            teil = {
                "modell":teil_dict["name"],
                "typ": teil_dict["type"],
                "farbe": teil_dict["color"],
            }
            # code to execute if teil_typ is 'gehäuse'

        else:
            print("Unbekannter Teil-Typ")
        return teil

    def get_sockel(self, prozessor_modell):
        # Socket determination based on AMD Ryzen and Intel Core model names
        prozessor_modell = prozessor_modell.lower()
        if 'intel core' in prozessor_modell:
            generation = int(prozessor_modell.split('-')[1][:2])
            if generation < 7:
                return 'LGA 1155'
            elif 7 <= generation < 10:
                return 'LGA 1151'
            elif generation >= 10:
                return 'LGA 1200'
        elif 'amd ryzen' in prozessor_modell:
            generation = int(prozessor_modell.split()[2].split('X')[0][0])
            if generation <= 5:
                return 'AM4'
            elif generation >= 6:
                return 'AM5'

        return 'Unbekannter Sockel'

    def get_speichertyp(self, sockel):
        # A basic implementation to determine memory type based on socket
        if 'LGA' in sockel:
            return 'DDR4'
        elif 'AM4' in sockel:
            return 'DDR4'
        elif 'AM5' in sockel:
            return 'DDR5'
        return 'Unbekannter Typ'

    def get_ram_speichertyp(self, speed):
        # Determine memory type based on speed
        if 200 <= speed <= 400:
            return 'DDR'
        elif 400 < speed <= 800:
            return 'DDR2'
        elif 800 < speed <= 1600:
            return 'DDR3'
        elif 1600 < speed <= 3200:
            return 'DDR4'
        elif 3200 < speed <= 6400:
            return 'DDR5'
        else:
            return 'Unknown type'
from prettytable import PrettyTable

class pc:
    def __init__(self,name):
        self.name = name
        self.cpu = "empty"
        self.grafik_karte = "empty"
        self.mainboard = "empty"
        self.ram = "empty"
        self.netzteil  = "empty"
        self.speicher = "empty"
        self.gehäuse = "empty"
        self.teile = [self.cpu,self.grafik_karte,self.mainboard,self.ram,self.netzteil,self.speicher,self.gehäuse]

    def __str__(self):
        # Define a table
        table = PrettyTable()

        # Add columns
        table.field_names = ["Component", "Details"]

        # Iterate over the PC components
        for key, value in self.__dict__.items():
            # If a component has more details in form of a dictionary
            if isinstance(value, dict):
                table.add_row([key.capitalize(), ""])  # add a row for the component with no details
                for subkey, subvalue in value.items():
                    # add a row for each detail of the component
                    table.add_row(["", f'{subkey.capitalize()}: {subvalue}'])
            else:
                table.add_row([key.capitalize(), value])  # just add a row with the component and its value

        return "\n" + str(table)
    # Mainboard wechseln Funktion
    def mainboard_wechseln(self, modell, marke, sockel, form_faktor, ram_slots, ram_slot_typ, stromverbrauch):
        if isinstance(self.cpu, dict) and sockel != self.cpu["sockel"]:
            raise "Das neue Mainboard ist nicht kompatibel mit dem Sockel des CPUs."
        if isinstance(self.ram, dict) and (
                ram_slots < self.ram["anzahl_der_module"] or ram_slot_typ != self.ram["speichertyp"]):
            raise "Das neue Mainboard ist nicht kompatibel mit dem RAM."
        self.mainboard = {
            "modell": modell,
            "marke": marke,
            "sockel": sockel,
            "form_faktor": form_faktor,
            "ram_slots": ram_slots,
            "ram_slot_typ": ram_slot_typ,
            "stromverbrauch": stromverbrauch
        }

    # Netzteil wechseln Funktion
    def set_netzteil(self, modell, marke, watt, zertifizierung, modular, form_faktor, stromverbrauch):
        self.netzteil = {
            "modell": modell,
            "marke": marke,
            "watt": watt,
            "zertifizierung": zertifizierung,
            "modular": modular,
            "form_faktor": form_faktor,
            "stromverbrauch": stromverbrauch }

    # CPU wechseln Funktion
    def cpu_wechseln(self, modell, marke, taktfrequenz, kerne, socket, stromverbrauch):
        if isinstance(self.mainboard, dict) and socket != self.mainboard.get("sockel"):
            raise "Der neue CPU ist nicht kompatibel mit dem Socket des Mainboards."
        self.cpu = {
            "modell": modell,
            "marke": marke,
            "taktfrequenz": taktfrequenz,
            "kerne": kerne,
            "sockel": socket,
            "stromverbrauch": stromverbrauch
        }

    # RAM wechseln Funktion
    def ram_wechseln(self, modell, marke, speichergröße, speichertyp, taktfrequenz, anzahl_der_module, stromverbrauch):
        if self.mainboard and (anzahl_der_module > self.mainboard["ram_slots"] or speichertyp != self.mainboard["ram_slot_typ"]):
            raise "Der neue RAM ist nicht kompatibel mit dem Mainboard."
        self.ram = {
            "modell": modell,
            "marke": marke,
            "speichergröße": speichergröße,
            "speichertyp": speichertyp,
            "taktfrequenz": taktfrequenz,
            "anzahl_der_module": anzahl_der_module,
            "stromverbrauch": stromverbrauch }

    # Grafikkarte wechseln Funktion
    def grafik_karte_wechseln(self, modell, marke, chipset, speicher, taktung, stromverbrauch):
        self.grafik_karte = {
            "modell": modell,
            "marke": marke,
            "chipset": chipset,
            "speicher": speicher,
            "taktung": taktung,
            "stromverbrauch": stromverbrauch }

    # Speicher wechseln Funktion
    def speicher_wechseln(self, typ, marke, größe, stromverbrauch):
        self.speicher = {
            "typ": typ,
            "marke": marke,
            "größe": größe,
            "stromverbrauch": stromverbrauch }

    # Gehäuse wechseln Funktion
    def gehäuse_wechseln(self, modell, marke, typ, farbe):
        self.gehäuse = {
            "modell": modell,
            "marke": marke,
            "typ": typ,
            "farbe": farbe }

    # Funktion zur Berechnung des Stromverbrauchs
    def strom_verbrauch_berechnen(self):
        gesamt_stromverbrauch = 0
        for pc_teil in self.__dict__.values():
            if isinstance(pc_teil, dict) and "stromverbrauch" in pc_teil:
                gesamt_stromverbrauch += pc_teil["stromverbrauch"]
        return gesamt_stromverbrauch


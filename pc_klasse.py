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

    # Mainboard wechseln Funktion
    def mainboard_wechseln(self, modell, sockel, form_faktor, ram_slots, ram_slot_typ, stromverbrauch):
        if self.cpu and sockel != self.cpu["sockel"]:
            raise "Das neue Mainboard ist nicht kompatibel mit dem Sockel des CPUs."
        if self.ram and (ram_slots < self.ram["anzahl_der_module"] or ram_slot_typ != self.ram["speichertyp"]):
            raise "Das neue Mainboard ist nicht kompatibel mit dem RAM."
        self.mainboard = {
            "modell": modell,
            "sockel": sockel,
            "form_faktor": form_faktor,
            "ram_slots": ram_slots,
            "ram_slot_typ": ram_slot_typ,
            "stromverbrauch": stromverbrauch }

    # Netztteil wechseln Funktion
    def set_netzteil(self, modell, watt, zertifizierung, modular, form_faktor):
        self.netzteil = {
            "modell": modell,
            "watt": watt,
            "zertifizierung": zertifizierung,
            "modular": modular,
            "form_faktor": form_faktor }

    # CPU wechseln Funktion
    def cpu_wechseln(self, modell, taktfrequenz, kerne, sockel, stromverbrauch):
        if self.mainboard and self.mainboard.get("sockel") != sockel:
            raise "Der neue CPU ist nicht kompatibel mit dem Sockel des Mainboards."
        self.cpu = {
            "modell": modell,
            "taktfrequenz": taktfrequenz,
            "kerne": kerne,
            "sockel": sockel,
            "stromverbrauch": stromverbrauch }

    # RAM wechseln Funktion
    def ram_wechseln(self, modell, speichergröße, speichertyp, taktfrequenz, anzahl_der_module, stromverbrauch):
        if self.mainboard and (anzahl_der_module > self.mainboard["ram_slots"] or speichertyp != self.mainboard["ram_slot_typ"]):
            raise "Der neue RAM ist nicht kompatibel mit dem Mainboard."
        self.ram = {
            "modell": modell,
            "speichergröße": speichergröße,
            "speichertyp": speichertyp,
            "taktfrequenz": taktfrequenz,
            "anzahl_der_module": anzahl_der_module,
            "stromverbrauch": stromverbrauch }

    # Grafikkarte wechseln Funktion
    def grafik_karte_wechseln(self, modell, chipset, speicher, taktung, stromverbrauch):
        self.grafik_karte = {
            "modell": modell,
            "chipset": chipset,
            "speicher": speicher,
            "taktung": taktung,
            "stromverbrauch": stromverbrauch }

    # Speicher wechseln Funktion
    def speicher_wechseln(self, typ, größe, stromverbrauch):
        self.speicher = {
            "typ": typ,
            "größe": größe,
            "stromverbrauch": stromverbrauch }

    # Gehäuse wechseln Funktion
    def gehäuse_wechseln(self, modell, typ, farbe):
        self.gehäuse = {
             "modell": modell,
            "typ": typ,
            "farbe": farbe }

    # Funktion zur Berechnung des Stromverbrauchs
    def strom_verbrauch_berechnen(self):
        gesamt_stromverbrauch = None
        for pc_teil in self.teile:
            gesamt_stromverbrauch += pc_teil["stromverbrauch"]
        return gesamt_stromverbrauch
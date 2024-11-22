from pc_klasse import pc


def main():
    mein_neuer_pc = pc("my-new-pc")

    # Wechseln Sie den CPU zu Ryzen 5 5500U
    mein_neuer_pc.cpu_wechseln("ryzen 5 5500U", "AMD", "4.0 GHz", "6", "AM4", 65)

    # Weitere Bauteile hinzufügen - ACHTUNG, diese Werte sind nur Beispiele und können nicht korrekt sein

    mein_neuer_pc.mainboard_wechseln("B450 TOMAHAWK MAX", "MSI", "AM4", "ATX", 4, "DDR4", 55)

    mein_neuer_pc.set_netzteil("EVGA 600 W1", "EVGA", "600 W", "80 PLUS", "Ja", "ATX", 0)

    mein_neuer_pc.ram_wechseln("Vengeance LPX", "Corsair", "16 GB", "DDR4", "3200 MHz", 2, 3.2)

    mein_neuer_pc.grafik_karte_wechseln("RTX 2070 SUPER",
                                        "GeForce", "NVIDIA Turing",
                                        "8 GB", "1770 MHz", 215)

    mein_neuer_pc.speicher_wechseln("SATA SSD", "Samsung", "1 TB", 2)

    mein_neuer_pc.gehäuse_wechseln("H510", "NZXT", "ATX Mid Tower", "schwarz")

    gesamt_stromverbrauch = mein_neuer_pc.strom_verbrauch_berechnen()

    print(mein_neuer_pc,gesamt_stromverbrauch)













if __name__ == '__main__':
    main()
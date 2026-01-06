import sys

def print_menu():
    """
    Zeigt das Hauptmenü an. / Displays the main menu.
    """
    print("\n--- Zahlensystem-Konverter / Number System Converter ---")
    print("1. Dezimal -> Binär, Hexadezimal")
    print("2. Binär -> Dezimal, Hexadezimal")
    print("3. Hexadezimal -> Dezimal, Binär")
    print("4. Beenden / Exit")

def dec_to_others(value):
    """
    Konvertiert Dezimal in andere Systeme. / Converts Decimal to other systems.
    """
    try:
        dec_num = int(value)
        print(f"Dezimal (DEC): {dec_num}")
        print(f"Binär (BIN):   {bin(dec_num)[2:]}") # '0b' entfernen
        print(f"Hex (HEX):     {hex(dec_num)[2:].upper()}") # '0x' entfernen
    except ValueError:
        print("❌ Fehler: Bitte geben Sie eine gültige Ganzzahl ein! / Error: Please enter a valid integer!")

def bin_to_others(value):
    """
    Konvertiert Binär in andere Systeme. / Converts Binary to other systems.
    """
    try:
        dec_num = int(value, 2)
        print(f"Binär (BIN):   {value}")
        print(f"Dezimal (DEC): {dec_num}")
        print(f"Hex (HEX):     {hex(dec_num)[2:].upper()}")
    except ValueError:
        print("❌ Fehler: Ungültige Binärzahl! (Nur 0 und 1 erlaubt) / Error: Invalid binary number!")

def hex_to_others(value):
    """
    Konvertiert Hexadezimal in andere Systeme. / Converts Hexadecimal to other systems.
    """
    try:
        dec_num = int(value, 16)
        print(f"Hex (HEX):     {value.upper()}")
        print(f"Dezimal (DEC): {dec_num}")
        print(f"Binär (BIN):   {bin(dec_num)[2:]}")
    except ValueError:
        print("❌ Fehler: Ungültiger Hex-Code! (0-9, A-F) / Error: Invalid Hex code!")

def main():
    while True:
        print_menu()
        choice = input("\nBitte wählen Sie eine Option (1-4): ")

        if choice == '1':
            val = input("Dezimalzahl eingeben: ")
            dec_to_others(val)
        elif choice == '2':
            val = input("Binärzahl eingeben: ")
            bin_to_others(val)
        elif choice == '3':
            val = input("Hexadezimalzahl eingeben: ")
            hex_to_others(val)
        elif choice == '4':
            print("Programm beendet. Auf Wiedersehen! / Goodbye!")
            break
        else:
            print("⚠️ Ungültige Auswahl! / Invalid selection!")

if __name__ == "__main__":
    main()


import tkinter as tk
from tkinter import messagebox

# Import der Service-Schicht 
from src.buergerregister.models import Person
from src.buergerregister.register import Buergerregister

"""
GUI für das Bürgerregister Light.
Zweck: Grafische Oberfläche zur Erfassung und Anzeige von Personen.
Abhängigkeiten: Benötigt das Paket 'buergerregister' (Service-Schicht).
"""

def main():
    # --- Schritt 7: Verbindung zur Serviceschicht ---
    # Wir erstellen EINE Instanz des Registers, die solange lebt wie das Fenster.
    register = Buergerregister()

    # --- Schritt 2: Hauptfenster erstellen ---
    root = tk.Tk()
    root.title("Bürgerregister Light")
    root.geometry("600x500")

    # --- Schritt 3: Eingabebereich (Label + Entry) ---
    input_frame = tk.Frame(root)
    input_frame.pack(padx=10, pady=10, fill="x")

    # Konfiguration des Grids für schöne Ausrichtung
    input_frame.columnconfigure(1, weight=1)

    # Hilfsvariablen (StringVars) für die Eingabefelder
    var_vorname = tk.StringVar()
    var_nachname = tk.StringVar()
    var_ort = tk.StringVar()
    var_jahr = tk.StringVar()

    # -- Zeile 0: Vorname --
    tk.Label(input_frame, text="Vorname:").grid(row=0, column=0, sticky="w")
    tk.Entry(input_frame, textvariable=var_vorname).grid(row=0, column=1, sticky="ew", padx=5, pady=2)

    # -- Zeile 1: Nachname --
    tk.Label(input_frame, text="Nachname:").grid(row=1, column=0, sticky="w")
    tk.Entry(input_frame, textvariable=var_nachname).grid(row=1, column=1, sticky="ew", padx=5, pady=2)

    # -- Zeile 2: Wohnort --
    tk.Label(input_frame, text="Wohnort:").grid(row=2, column=0, sticky="w")
    tk.Entry(input_frame, textvariable=var_ort).grid(row=2, column=1, sticky="ew", padx=5, pady=2)

    # -- Zeile 3: Geburtsjahr --
    tk.Label(input_frame, text="Geburtsjahr:").grid(row=3, column=0, sticky="w")
    tk.Entry(input_frame, textvariable=var_jahr).grid(row=3, column=1, sticky="ew", padx=5, pady=2)


    # --- Schritt 6: Label für Status und Fehlermeldungen ---
    # (Wir definieren das Label hier, damit wir es in den Funktionen nutzen können)
    status_var = tk.StringVar(value="Bereit.")
    status_label = tk.Label(root, textvariable=status_var, fg="blue", anchor="w")
    # Packen wir es ganz nach unten
    status_label.pack(side="bottom", fill="x", padx=10, pady=5)


    # --- Schritt 5: Anzeige aller Personen (Listbox) ---
    list_frame = tk.Frame(root)
    list_frame.pack(padx=10, pady=5, fill="both", expand=True)
    
    tk.Label(list_frame, text="Registrierte Personen:").pack(anchor="w")

    person_listbox = tk.Listbox(list_frame)
    person_listbox.pack(side="left", fill="both", expand=True)

    scrollbar = tk.Scrollbar(list_frame, orient="vertical", command=person_listbox.yview)
    scrollbar.pack(side="right", fill="y")
    person_listbox.config(yscrollcommand=scrollbar.set)


    # --- Hilfsfunktion: Liste aktualisieren (Schritt 5 Punkt 4) ---
    def refresh_person_list():
        """Leert die Listbox und füllt sie neu aus dem Register."""
        person_listbox.delete(0, tk.END)
        all_persons = register.list()
        
        for p in all_persons:
            # Formatierung für die Anzeige
            display_text = f"{p.nachname}, {p.vorname} ({p.geburtsjahr}) aus {p.wohnort}"
            person_listbox.insert(tk.END, display_text)


    # --- Schritt 4 & 8: Button-Logik (Hinzufügen) ---
    def on_add_person():
        """Liest Eingaben, validiert sie und ruft die Service-Schicht auf."""
        
        # 1. Eingaben lesen
        vname = var_vorname.get().strip()
        nname = var_nachname.get().strip()
        ort = var_ort.get().strip()
        jahr_str = var_jahr.get().strip()

        # 2. GUI-seitige Validierung (Plausibilität Typen)
        # Hinweis: Inhaltliche Validierung (z.B. Jahr logisch?) macht eigentlich der Service (Validator),
        # aber wir müssen sicherstellen, dass wir überhaupt ein int übergeben können.
        
        if not vname or not nname or not ort:
            status_var.set("Fehler: Bitte alle Textfelder ausfüllen.")
            status_label.config(fg="red")
            return

        try:
            jahr = int(jahr_str)
        except ValueError:
            status_var.set("Fehler: Geburtsjahr muss eine Zahl sein.")
            status_label.config(fg="red")
            return

        # Objekt erstellen
        neue_person = Person(vname, nname, jahr, ort)

        # 3. Aufruf der Service-Schicht
        success, message = register.add(neue_person)

        # 4. Feedback geben
        if success:
            status_var.set(message)
            status_label.config(fg="blue")
            
            # Felder leeren
            var_vorname.set("")
            var_nachname.set("")
            var_ort.set("")
            var_jahr.set("")
            
            # Liste aktualisieren
            refresh_person_list()
        else:
            # Fehler vom Service (z.B. Duplikat oder Validierungsfehler)
            status_var.set(f"Fehler: {message}")
            status_label.config(fg="red")


    # Button erstellen und mit Funktion verknüpfen
    add_button = tk.Button(input_frame, text="Person hinzufügen", command=on_add_person)
    add_button.grid(row=4, column=0, columnspan=2, pady=10, sticky="ew")

    # Start-Zustand herstellen
    refresh_person_list()

    # --- Startpunkt ---
    root.mainloop()

if __name__ == "__main__":
    main()
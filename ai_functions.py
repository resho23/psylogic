def erstelle_gutachten(roht_text):
    diagnose = "Keine eindeutige Diagnose ableitbar"

    if "depress" in roht_text.lower():
        diagnose = "Verdacht auf depressive Episode"

    if "angst" in roht_text.lower():
        diagnose = "Hinweise auf Angststörung"

    return f'''
1. Anamnese
{roht_text}

2. Psychopathologischer Befund
Automatisch aus Eingabe erkannt

3. Diagnose
{diagnose}

4. Beurteilung
Weitere klinische Prüfung erforderlich

5. Prognose
Abhängig vom Verlauf
'''


def analysiere_gutachten(gutachten_text):
    schwächen = []

    if "Keine eindeutige" in gutachten_text:
        schwächen.append("Diagnose unscharf")

    return {
        "schwaechen": schwächen or ["Keine gravierenden Schwächen erkannt"],
        "verbesserungsvorschlaege": [
            "Mehr Symptomdetails ergänzen",
            "Zeitlichen Verlauf genauer beschreiben"
        ]
    }

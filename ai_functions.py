def erstelle_gutachten(roht_text):
    gutachten_template = f"""
1. Anamnese
--------------------
{roht_text}

2. Psychopathologischer Befund
--------------------
[Zu ergänzen]

3. Diagnose (mit Begründung)
--------------------
[Zu ergänzen]

4. Beurteilung
--------------------
[Zu ergänzen]

5. Prognose
--------------------
[Zu ergänzen]
"""
    return gutachten_template


def analysiere_gutachten(gutachten_text):
    return {
        "schwaechen": [
            "Diagnose könnte präziser begründet sein",
            "Befund sollte detaillierter ausgeführt werden"
        ],
        "verbesserungsvorschlaege": [
            "Anamnese stärker strukturieren",
            "Diagnostische Ableitung expliziter darstellen"
        ]
    }

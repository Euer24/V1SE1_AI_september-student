#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Oriëntatie op AI

Opdracht: simulatie

(c) 2025 Hogeschool Utrecht,
Peter van den Berg (peter.vandenberg@hu.nl)

Opdracht:
Werk onderstaande functies uit, om de tegenstanders 'Always defect',
'Tit for tat' en 'Alternate te verslaan'.

Je kunt je functies testen met het gegeven raamwerk door het bestand
uit te voeren (of met behulp van `pytest`, als je weet hoe dat werkt).
Lever je werk in op Canvas als alle tests slagen.

Let op! Het is niet toegestaan om bestaande modules te importeren en te
        gebruiken, zoals `math` en `statistics`.
"""

# TODO: Vul hier je naam, klas en studentnummer in.
naam = "Euer"
klas = "V1H"
studentnummer = -1893754

debuginfo = True

"""
1. Implementatie is_always_defect
    Implementeer onderstaande functie om te achterhalen of de tegenstander 'Always defect' is.

"""
def is_always_defect(my_history, opponent_history):
    """
    Checkt of je tegenstander 'Always defect' is.

    Deze blijft de heletijd False spammen dus hier kan je niet tegen winnen alleen gelijk spelen
    """
 
    if len(opponent_history) == 0:
        return False

    #    ik kijk hier of de tegenstander true speelt als het antwoord ja is weet ik dat dit niet always defect is
    for actie in opponent_history:
        if actie == True:
            return False

   
    return True

"""
2. Implementatie play_against_always_defect
    Implementeer onderstaande functie om de beste actie te spelen tegen 'Always defect'.

"""
def play_against_always_defect(my_history, opponent_history):
    """
    Ik gebruik hier tegen de heletijd false Anders verlies ik en nu speel ik gelijk
    """
    return False

"""
3. Implementatie is_alternate
    Implementeer onderstaande functie om te achterhalen of de tegenstander 'Alternate' is.

"""
def is_alternate(my_history, opponent_history):
    """
    Checkt of je tegenstander 'Alternate' is.

    Args:
        my_history (list[bool]): Een lijst met jouw gespeelde acties in het verleden.
        opponent_history (list[bool]): Een lijst de door jouw tegenstander gespeelde acties in het verleden.

    Returns:
        bool: True als je tegenstander 'Alternate' is, anders False.
    """
    # We hebben minimaal 2 rondes nodig om het afwisselende patroon te herkennen
    if len(opponent_history) < 2:
        return False

    # Loop door alle acties van de tegenstander met hun index
    for i in range(len(opponent_history)):
        # Alternate speelt True op even indices (0, 2, 4, ...) en False op oneven indices (1, 3, 5, ...)
        # Dus: als i % 2 == 0 (even), verwachten we True
        verwachte_actie = (i % 2 == 0)
        werkelijke_actie = opponent_history[i]

        # Als de werkelijke actie niet overeenkomt met wat we verwachten,
        # dan is het NIET Alternate
        if werkelijke_actie != verwachte_actie:
            return False

    # Als alle acties overeenkomen met het patroon, is het Alternate!
    return True


"""
4. Implementatie play_against_alternate
    Implementeer onderstaande functie om de beste actie te spelen tegen 'Alternate'.

"""
def play_against_alternate(my_history, opponent_history):
    """
    Geeft de actie terug die gespeeld zal worden tegen 'Alternate' door jouw agent,
    gegeven jouw en jouw tegenstanders' acties in het verleden.

    Args:
        my_history (list[bool]): Een lijst met jouw gespeelde acties in het verleden.
        opponent_history (list[bool]): Een lijst de door jouw tegenstander gespeelde acties in het verleden.

    Returns:
        bool: Jouw actie; samenwerken (True) of zelfzuchtig zijn (False).
    """
    # Tegen Alternate is altijd False spelen de beste strategie
    # Even rondes: zij True, jij False → 3 punten (exploiteren!)
    # Oneven rondes: zij False, jij False → 1 punt
    # Totaal: 10×3 + 10×1 = 40 punten
    return False

"""
5. Implementatie is_tit_for_tat
    Implementeer onderstaande functie om te achterhalen of de tegenstander 'Tit for tat' is.

"""
def is_tit_for_tat(my_history, opponent_history):
    """
    Checkt of je tegenstander 'Tit for tat' is.

    Args:
        my_history (list[bool]): Een lijst met jouw gespeelde acties in het verleden.
        opponent_history (list[bool]): Een lijst de door jouw tegenstander gespeelde acties in het verleden.

    Returns:
        bool: True als je tegenstander 'Tit for tat' is, anders False.
    """
    # We hebben minimaal 1 ronde nodig om te detecteren
    # (Tit for Tat begint altijd met True in ronde 1, daarna kopieert het jou)
    if len(opponent_history) == 0:
        return False

    # Check eerste actie: Tit for Tat begint ALTIJD met True (samenwerken)
    if opponent_history[0] != True:
        return False

    # Als er maar 1 ronde is gespeeld, kunnen we nog niet zeker weten
    # (meerdere strategieën kunnen met True beginnen)
    if len(opponent_history) == 1:
        return False

    # Vanaf ronde 2 moet Tit for Tat kopiëren wat JIJ de vorige ronde deed
    # opponent_history[i] moet gelijk zijn aan my_history[i-1]
    for i in range(1, len(opponent_history)):
        # Wat deed ik de vorige ronde?
        mijn_vorige_actie = my_history[i - 1]
        # Wat deed de tegenstander deze ronde?
        hun_huidige_actie = opponent_history[i]

        # Als ze niet hetzelfde zijn, is het NIET Tit for Tat
        if hun_huidige_actie != mijn_vorige_actie:
            return False

    # Als alle checks kloppen, is het Tit for Tat!
    return True

"""
6. Implementatie play_against_tit_for_tat
    Implementeer onderstaande functie om de beste actie te spelen tegen 'Tit for tat'.

"""
def play_against_tit_for_tat(my_history, opponent_history):
    """
    Geeft de actie terug die gespeeld zal worden tegen 'Tit for tat' door jouw agent,
    gegeven jouw en jouw tegenstanders' acties in het verleden.

    Args:
        my_history (list[bool]): Een lijst met jouw gespeelde acties in het verleden.
        opponent_history (list[bool]): Een lijst de door jouw tegenstander gespeelde acties in het verleden.

    Returns:
        bool: Jouw actie; samenwerken (True) of zelfzuchtig zijn (False).
    """
    # Tegen Tit for Tat is altijd samenwerken (True) de beste strategie
    # Als jij True speelt, spelen zij ook True → beide 2 punten per ronde
    # 20 rondes × 2 punten = 40 punten totaal
    #
    # Als je False zou spelen:
    # Ronde 1: jij False, zij True → jij 3 punten
    # Ronde 2-20: beide False → beide 1 punt per ronde
    # Totaal: 3 + 19 = 22 punten (veel minder!)
    return True

"""
7. Implementatie play_against_unknown
    Implementeer onderstaande functie om de beste actie te spelen tegen een (nog) onbekende tegenstander.

"""
def play_against_unknown(my_history, opponent_history):
    """
    Geeft de actie terug die gespeeld zal worden tegen een onbekende tegenstander door jouw agent,
    gegeven jouw en jouw tegenstanders' acties in het verleden.

    Args:
        my_history (list[bool]): Een lijst met jouw gespeelde acties in het verleden.
        opponent_history (list[bool]): Een lijst de door jouw tegenstander gespeelde acties in het verleden.

    Returns:
        bool: Jouw actie; samenwerken (True) of zelfzuchtig zijn (False).
    """
    # Als we de tegenstander nog niet herkennen, spelen we voorzichtig
    # We beginnen met True (samenwerken) om te testen hoe ze reageren
    # Dit helpt ons om ze in latere rondes te herkennen
    #
    # True is een goede keuze omdat:
    # - Het helpt Tit for Tat herkennen (ze kopiëren ons)
    # - Het helpt Alternate herkennen (ze hebben een vast patroon)
    # - Tegen Always Defect verliezen we wel punten, maar dat herkennen we snel
    return True

"""
8. Optioneel: Implementatie is_final_round
    Implementeer onderstaande functie om te achterhalen of je in de laatste ronde zit.

"""
def is_final_round(my_history, opponent_history):
    """
    Checkt of je in de laatste ronde zit.

    Args:
        my_history (list[bool]): Een lijst met jouw gespeelde acties in het verleden.
        opponent_history (list[bool]): Een lijst de door jouw tegenstander gespeelde acties in het verleden.

    Returns:
        bool: True als je in de laatste ronde zit, anders False.
    """
    return

"""
9. Optioneel: Implementatie play_final_round
    Implementeer onderstaande functie om de beste actie te spelen in de laatste ronde.

"""
def play_final_round(my_history, opponent_history):
    """
    Geeft de actie terug die gespeeld zal worden in de laatste ronde.

    Args:
        my_history (list[bool]): Een lijst met jouw gespeelde acties in het verleden.
        opponent_history (list[bool]): Een lijst de door jouw tegenstander gespeelde acties in het verleden.

    Returns:
        bool: Jouw actie; samenwerken (True) of zelfzuchtig zijn (False).
    """
    return


def strategy(my_history, opponent_history):
    """
    Geeft de actie terug die gespeeld zal worden door jouw agent, 
    gegeven jouw en jouw tegenstanders' acties in het verleden.

    Args:
        my_history (list[bool]): Een lijst met jouw gespeelde acties in het verleden.
        opponent_history (list[bool]): Een lijst de door jouw tegenstander gespeelde acties in het verleden.

    Returns:
        bool: Jouw actie; samenwerken (True) of zelfzuchtig zijn (False).
    """
    # 10. Optioneel: uncomment deze code en implementeer is_final_round en play_final_round
    # if is_final_round(my_history, opponent_history):
    #     return play_final_round(my_history, opponent_history)
    
    if is_always_defect(my_history, opponent_history):
        return play_against_always_defect(my_history, opponent_history)
    elif is_alternate(my_history, opponent_history):
        return play_against_alternate(my_history, opponent_history)
    elif is_tit_for_tat(my_history, opponent_history):
        return play_against_tit_for_tat(my_history, opponent_history)
    else:
        return play_against_unknown(my_history, opponent_history)

def always_defect(my_history, opponent_history):
    """
    Geeft de actie terug die 'Always defect' speelt.

    Args:
        my_history (list[bool]): Een lijst met de gespeelde acties van 'Always defect' in het verleden.
        opponent_history (list[bool]): Een lijst de door de tegenstander gespeelde acties in het verleden.

    Returns:
        bool: De gespeelde actie; samenwerken (True) of zelfzuchtig zijn (False).
    """
    return False

def alternate(my_history, opponent_history):
    """
    Geeft de actie terug die 'Alternate' speelt.

    Args:
        my_history (list[bool]): Een lijst met de gespeelde acties van 'Alternate' in het verleden.
        opponent_history (list[bool]): Een lijst de door de tegenstander gespeelde acties in het verleden.

    Returns:
        bool: De gespeelde actie; samenwerken (True) of zelfzuchtig zijn (False).
    """
    return len(opponent_history) % 2 == 0

def tit_for_tat(my_history, opponent_history):
    """
    Geeft de actie terug die 'Tit for tat' speelt.

    Args:
        my_history (list[bool]): Een lijst met de gespeelde acties van 'Tit for tat' in het verleden.
        opponent_history (list[bool]): Een lijst de door de tegenstander gespeelde acties in het verleden.

    Returns:
        bool: De gespeelde actie; samenwerken (True) of zelfzuchtig zijn (False).
    """
    if not opponent_history:
        return True
    return opponent_history[-1]

strategies = {
    "Always defect": always_defect,
    "Alternate": alternate,
    "Tit for Tat": tit_for_tat,
    "Jouw strategie": strategy
}

def play_game(strategy1, strategy2, rounds):
    """
    Speelt een aantal ronden van het repeated prisoner's dilemma tussen twee agents.

    Args:
        strategy1 (function): De strategie van agent 1.
        strategy2 (function): De strategie van agent 2.
        rounds (int): Het aantal te spelen ronden

    Returns:
        pair[pair[int, int], list[string]]: de eindscores en eventuele errors.
    """
    history = []
    errors = []
    for _ in range(rounds):
        try:
            history1 = [h[0] for h in history]
            history2 = [h[1] for h in history]
            action1 = strategy1(history1, history2)
            action2 = strategy2(history2, history1)
            if not isinstance(action1, bool) or not isinstance(action2, bool):
                raise ValueError("Jouw strategie moet een boolean teruggeven.")
            history.append((action1, action2))
        except Exception as e:
            errors.append(str(e))
    return calculate_scores(history), errors

def calculate_scores(history):
    """
    Berekent de eindscores.

    Args:
        history (list[pair[bool, bool]]): De geschiedenis van gespeelde potjes tussen twee strategieën.

    Returns:
        pair[int, int]: de eindscores van de twee strategieën.
    """
    payoff_matrix = (
        ((1, 1), (3, 0)),
        ((0, 3), (2, 2))
    )
    score1, score2 = 0, 0
    for action1, action2 in history:
        s1, s2 = payoff_matrix[int(action1)][int(action2)]
        score1 += s1
        score2 += s2
        if debuginfo:
            print(f"({action1}, {action2}) -> ({s1}, {s2})")
    return score1, score2

def run_tournament(strategies, rounds):
    """
    Speelt het repeated prisoner's dilemma in tournooi vorm met de gegeven strategieën voor het gegeven aantal ronden.

    Args:
        strategies (dict[string, function]): Een dictionary van strategieën die meespelen.
        rounds (int): het aantal ronden dat wordt gespeeld.

    Returns:
        pair[dict, dict]: de resultaten van het tournooi en de eindscores.
    """
    results = {}
    total_scores = {name: 0 for name in strategies}

    for name1, strat1 in strategies.items():
        for name2, strat2 in strategies.items():
            if name1 < name2:
                if debuginfo:
                    print(f"{name1} vs {name2}")
                (score1, score2), errors = play_game(strat1, strat2, rounds)
                results[(name1, name2)] = (score1, score2)
                total_scores[name1] += score1
                total_scores[name2] += score2
                
                if debuginfo:
                    print(f"Eindscore {name1} vs {name2}: {score1} - {score2}")
                if errors:
                    print(f"Errors in spel: {name1} vs {name2}: {errors[0]}")

    return results, total_scores

if __name__ == "__main__":
    rounds = 20
    results, total_scores = run_tournament(strategies, rounds)

    positions = sorted(total_scores.items(), key=lambda x: x[1], reverse=True)
    print("\nEindscores:")
    for strategy, score in positions:
        print("{}: {}".format(strategy, score))
        
    if positions[0][0] == "Jouw strategie" == "Jouw strategie":
        print("\x1b[32m")
        print("Jouw strategie heeft gewonnen!")

        print("\nGefeliciteerd, alles lijkt te werken!")
        print("Lever je werk nu in op Canvas...")
    else:
        print("\x1b[31m")   # Rode tekstkleur
        print(f"Jouw strategie heeft niet gewonnen")
    
    print("\x1b[0m")

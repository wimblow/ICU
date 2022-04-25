from icu.services.alerts import AlertDiscord

alert = AlertDiscord()

def test_alert():
    assert alert.test_alert() == "Système d'alerte actif"

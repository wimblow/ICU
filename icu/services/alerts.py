from discord_webhook import DiscordWebhook

class AlertDiscord:

    @classmethod
    def __init__(cls):
        cls.webhook_url_mask = "https://discord.com/api/webhooks/967029818036207637/4JQ-Zc4BwK28XGaaYgKcs7Qo4f8Hr_gkEyFyvdYb-cogRkyIHLwHz8mt46EH_AxqEPI_"
        cls.webhook_url_connect = "https://gitlark.s.arkea.com/data_labs/x250/ml-projects-team/-/issues/41"

    @classmethod
    def alert(cls, date, heure):
        webhook = DiscordWebhook(url=cls.webhook_url_mask, content=f"Personne sans masque détectée le {date} à {heure}")
        webhook.execute()
    
    @classmethod
    def test_alert(cls):
        webhook = DiscordWebhook(url=cls.webhook_url_connect, content="Teste de connexion à l'application")
        webhook.execute()
        return "Système d'alerte actif"



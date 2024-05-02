from discord import File, SyncWebhook, utils
from os import environ
from sys import exit
import requests

class DiscordService:
    def __init__(self):
        webhook_url = environ.get('WEBHOOK_URL')

        if webhook_url is None:
            print('Webhook URL was not set!')
            exit()

        try:
            self.webhook = SyncWebhook.from_url(webhook_url)
        except ValueError:
            print('Webhook URL is invalid!')
            exit()

    def send(self, message, file = utils.MISSING):
        if (type(file).__name__ != '_MissingSentinel'):
            file = File(file)

        self.webhook.send(message, file=file)
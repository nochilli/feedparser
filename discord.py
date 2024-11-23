import requests
import settings


settings_url = ""

class discord:
    def __init__(self, webhook, username, avatar_url, feed):
        self.webhook = webhook
        self.username = username
        self.avatar_url = avatar_url
        self.feed = feed
    
    def init_settings(source):
        global webhook, whitelist, username, avatar_url, feed_url
        if (source == "online"):
            r = requests.get(settings_url).text
            webhook = r.webhook;
            whitelist = r.whitelist;
            username = r.username;
            avatar_url = r.avatar_url;
            feed_url = r.feed_url;
            
        else:
            webhook = settings.webhook
            whitelist = settings.whitelist
            username = settings.username
            avatar_url = settings.avatar_url
            feed_url = settings.feed_url
            
            return webhook, whitelist, username, avatar_url, feed_url

    def prepare_and_notify(self):
        for entry in self.feed.entries:
            for x in whitelist:
                if(x.lower() in entry.title.lower()):
            # if "orb:" in entry.title.lower():
                    self.__notify_to_discord_channel(entry)

    def __notify_to_discord_channel(self, data):
        headers = {"Content-Type": "application/json"}
        content = f"""
        # [{data.title}]({data.link})
        """
        payload = {
            "username": self.username,
            "content": content,
            "avatar_url": self.avatar_url,
        }
        return requests.post(url=self.webhook, headers=headers, json=payload)
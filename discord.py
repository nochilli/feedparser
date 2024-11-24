import requests

settings_url = "https://raw.githubusercontent.com/nochilli/feedparser/refs/heads/main/settings.py"

class discord:
    def __init__(self, webhook, username, avatar_url, feed):
        self.webhook = webhook
        self.username = username
        self.avatar_url = avatar_url
        self.feed = feed
    
    def init_settings(source):
        global webhook, whitelist, username, avatar_url, feed_url
        if (source == "online"):
            r = requests.get(settings_url).text.split(";")
            whitelist = eval(r[0])
            username = r[1]
            webhook = r[2]
            avatar_url = r[3]
            feed_url = r[4]
            
        else:
            import settings
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
# -*- coding: utf-8 -*-
from telethon import events

# Module-wide variables, because all the incoming and outgoing messages have to be able to read and modify this.
afk = False
afk_reason = ""

def register(client):    
    # Handles any private messages
    @client.on(events.NewMessage(incoming=True))
    async def incoming_handler(event):
        if afk and event.message.to_id.isinstanceof(PeerUser):
            await event.reply("Beep boop, I'm a bot. @AgEzRo is now AFK because: " + afk_reason)

    # Handles any messages except those starting with "Beep boop",
    # so that the bot doesn't trigger itself into turning off AFK mode
    @client.on(events.NewMessage(outgoing=True, pattern="(?!^Beep boop).*"))
    async def outgoing_handler(event):
        global afk, afk_reason
        if afk:
            afk = False

   @client.on(events.NewMessage(outgoing=True, pattern="^!afk (.*)"))
    async def afk_handler(event):
        global afk, afk_reason
        afk = True
        afk_reason = event.pattern_match.group(1)
        await event.message.edit("Beep boop, I'm a bot. @AgEzRo is now AFK because: " + afk_reason)

   @client.on(events.NewMessage(outgoing=True, pattern="^!github$"))
    async def github_handler(event):
        await event.edit("GitHub: https://github.com/Agusyc/")

    @client.on(events.NewMessage(outgoing=True, pattern='^!source'))
    async def source_handler(event):
        await event.edit("Source: https://github.com/Agusyc/TUB/")

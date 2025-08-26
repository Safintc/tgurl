#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Shrimadhav U K

# the logging things
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import os

# the secret configuration specific things
if bool(os.environ.get("WEBHOOK", False)):
    from sample_config import Config
else:
    from config import Config

import pyrogram
logging.getLogger("pyrogram").setLevel(logging.WARNING)


if __name__ == "__main__" :
    # create download directory, if not exist
    if not os.path.isdir(Config.DOWNLOAD_LOCATION):
        os.makedirs(Config.DOWNLOAD_LOCATION)
    plugins = dict(
        root="plugins"
    )
    app = pyrogram.Client(
        "AnyDLBot"
        bot_token=Config.TG_BOT_TOKEN,'8403069481:AAFFIdos6QteJ9EZclx7rxpGjovMThlOWaA'
        api_id=Config.APP_ID,'21116415'
        api_hash=Config.API_HASH,'8e23c9d97d71d525741e33f6b3584f45'
        plugins=plugins
    )
    Config.AUTH_USERS.add(-1003073675420)
    app.run()

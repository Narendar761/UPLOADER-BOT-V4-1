import os

import logging

logging.basicConfig(
    format='%(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler('log.txt'),
              logging.StreamHandler()],
    level=logging.INFO
)

class Config(object):
    
    API_ID = "22808125"
    API_HASH = "406c09543fec722fe3c48ca2f06d78de"
    BOT_TOKEN = "6421258723:AAH97XzwDvFr3jf_qyI4CaYwM3BxAIwo-Vo"
    DATABASE_URL = "mongodb+srv://Nkbot001:nkbot123@helpy.wfrytzq.mongodb.net/?retryWrites=true&w=majority&appName=Helpy"
    OWNER_ID = "819861991"
    LOG_CHANNEL = "-1001916142483"
    UPDATES_CHANNEL = "-1001988879902"
    
    DOWNLOAD_LOCATION = "./DOWNLOADS"
    
    MAX_FILE_SIZE = 2097152000
    
    TG_MAX_FILE_SIZE = 2097152000
    
    FREE_USER_MAX_FILE_SIZE = 2097152000
    
    CHUNK_SIZE = int(os.environ.get("CHUNK_SIZE", 128))
    
    DEF_THUMB_NAIL_VID_S = os.environ.get("DEF_THUMB_NAIL_VID_S", "")
    
    HTTP_PROXY = os.environ.get("HTTP_PROXY", "")
    
    OUO_IO_API_KEY = ""
    
    MAX_MESSAGE_LENGTH = 4096
    
    PROCESS_MAX_TIMEOUT = 0
    
    DEF_WATER_MARK_FILE = "UploadLinkToFileBot"
    
    
    SESSION_NAME = os.environ.get("SESSION_NAME", "UploadLinkToFileBot")
    
    
    
    LOGGER = logging

    
    TG_MIN_FILE_SIZE = 2097152000
    
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "Hx_URLuploadBot")
                                  

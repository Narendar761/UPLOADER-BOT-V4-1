import os

import logging

logging.basicConfig(
    format='%(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler('log.txt'),
              logging.StreamHandler()],
    level=logging.INFO
)

class Config(object):
    
    API_ID = "2532603"
    API_HASH = "f565b00bbe3ad9c6748e39a3a71d16e7"
    BOT_TOKEN = "1732757652:AAG8mCfPT2Ils5sDu5RgbrZ_MnjI1j2dQkY"
    DATABASE_URL = "mongodb+srv://user:user@cluster0.0vi8sg6.mongodb.net"
    OWNER_ID = "754495556"
    LOG_CHANNEL = "-1001879335914"
    UPDATES_CHANNEL = "-1001428601312"
    
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
                                  

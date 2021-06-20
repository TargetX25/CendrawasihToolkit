import os
try:
    from .ExecVarsSample import ExecVars
except:
    class ExecVars:
        # TODO optimize for vps use fully - currently only heroku is focused
        # Set true if its VPS [currently not fully working]
        IS_VPS = False
        API_HASH = os.environ.get("API_HASH")
        API_ID = int(os.environ.get("API_ID"))
        BOT_TOKEN = os.environ.get("BOT_TOKEN")
        BASE_URL_OF_BOT = os.environ.get("BASE_URL")
        # ALLOWED USERS [ids of user or supergroup] seperate by commas
        ALD_USR = [-534865962,847231339]
        #ALD_USR = os.environ.get('AUTHORIZED_CHATS')
        #ALD_USR = list(map(int, ALD_USR.split(' '))) if ALD_USR else []

        # Time to wait before edit message
        EDIT_SLEEP_SECS = 5

        # Telegram Upload Limit (in bytes)
        TG_UP_LIMIT = 2093796556

        # Should force evething uploaded into Document
        FORCE_DOCUMENTS = False

        # Chracter to use as a completed progress
        COMPLETED_STR = "⬤"

        # Chracter to use as a incomplete progress
        REMAINING_STR = "○"

        # Time to wait before edit message
        EDIT_SLEEP_SECS = 10

        # MEGA CONFIG
        MEGA_ENABLE = os.environ.get("MEGA_ENABLE", False)
        MEGA_API = os.environ.get("MEGA_API")
        MEGA_UNAME = os.environ.get("MEGA_UNAME")
        MEGA_PASS = os.environ.get("MEGA_PASS")

        # DB URI for access
        DB_URI = os.environ.get("DATABASE_URL")

        # The base direcory to which the files will be upload if using RCLONE
        RCLONE_BASE_DIR = "/"

        # This value will be considered only if Rclone is True - this may be defied now ;)
        # Cuz at least one needs to be Ture at a time either RCLONE or Leech.
        LEECH_ENABLED = True

        # Will be enabled once its set
        # For vps change it to True if config loaded
        RCLONE_ENABLED = False

        # If the user fails to select whether to use rclone or telegram to upload this will be the deafult.
        DEFAULT_TIMEOUT = "leech"

        # For vps set path here or you can use runtime too
        RCLONE_CONFIG = False

        # Name of the RCLONE drive from the config
        DEF_RCLONE_DRIVE = os.environ.get("RCLONE_DRIVE")

        # Max size of the torrent allowed
        MAX_YTPLAYLIST_SIZE = 20

        # Max size of the torrent allowed
        MAX_TORRENT_SIZE = 100000

        # Set this to your bot username if you want to add the username of your bot at the end of the commands like
        # /leech@TorToolkitBot so the value will be @TorToolkitBot
        BOT_CMD_POSTFIX = os.environ.get("CMD_POSTFIX", True)

        # Time out for the status Delete.
        STATUS_DEL_TOUT = os.environ.get("STATUS_DEL", 5)

        # Allow the user settings to be accessed in private
        USETTINGS_IN_PRIVATE = False

        # Torrent max time to collect metadata in seconds
        TOR_MAX_TOUT = 300

        # This is to stop someone from abusing the system by imposing the limit
        # [<GBs of total torrent sapce>, <Number of youtube videos allowed to download>, <Number of youtube playlists allowed to download>]
        USER_CAP_ENABLE = False
        USER_CAP_LIMIT = [50, 10, 2]

        # No need to worry about these
        # CHANGE THESE AT YOUR RISK
        LOCKED_USERS = False
        RSTUFF = False
        FORCE_DOCS_USER = False
        FAST_UPLOAD = True
        METAINFO_BOT = False
        EXPRESS_UPLOAD = True

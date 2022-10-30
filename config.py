import os
import ProxyCloud

#Bot Config
BOT_TOKEN = os.environ.get('bot_token','')
#Storage Config
BASE_ROOT_PATH = 'root/'
#Account Config
OWN_USER = os.environ.get('account_user','strujillo')
OWN_PASSWORD = os.environ.get('account_password','Str..96102512490')
# Proxy Config
PROXY_OBJ = ProxyCloud.parse(os.environ.get('proxy_enc','http://KEGEJEYEJELEFEYEKEKECEYEJEGEHEREDELEDELE'))
# Sync Options
SPLIT_SYNC = 1024 * 1024 * int(os.environ.get('split_sync',10))
UPLOAD_SYNC = 3
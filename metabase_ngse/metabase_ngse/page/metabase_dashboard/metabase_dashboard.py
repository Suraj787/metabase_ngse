# You'll need to install PyJWT via pip 'pip install PyJWT' or your project packages file

import jwt

METABASE_SITE_URL = "http://nandanerp.com:3000"
METABASE_SECRET_KEY = "fbcc85961d263de8db6c74aeb24be33c6c167dca96164911e613e127a48c57bf"

payload = {
  "resource": {"dashboard": 1},
  "params": {
    
  }
}
token = jwt.encode(payload, METABASE_SECRET_KEY, algorithm="HS256")

iframeUrl = METABASE_SITE_URL + "/embed/dashboard/" + token.decode("utf8") + "#bordered=false&titled=false"
# print(iframeUrl)
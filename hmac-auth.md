# HMAC Authentication

HMAC Authentication can be used for authentication through the coins.ph API as yourself. While you can use this type of authentication for executing requests from users of your app (aside from yourself), we do not recommend it and would suggest to look into [OAuth2 Authentication](https://github.com/coinsph/api/wiki/03-Authentication-with-client-a-token-OAuth2) instead, especially for client-side applications. This is because HMAC requires you to use your API secret to sign requests.

You can get your API Key and secret by clicking "show" in your desired application in [API Access Dashboard](https://coins.ph/user/api).

## Signing a request

Each request made with HMAC Authentication needs to be signed. Please refer to the following code examples for signing a request.

### Python

```python
import time, os, hmac, requests, hashlib
url = "http://coins.local/api/v2/buyorder"
body = ''
nonce = int(time.time() * 1e6)
API_SECRET = "your_api_secret"
ACCESS_KEY = "your_api_key"
message = str(nonce) + url + ('' if body is None else body)
signature = hmac.new(API_SECRET, message, hashlib.sha256).hexdigest()

# Include the signature in the headers
headers = {
    'ACCESS_KEY' : ACCESS_KEY,
    'ACCESS_SIGNATURE': signature,
    'ACCESS_NONCE': nonce,
    'Accept': 'application/json',
    'Content-Type': 'application/json' # Only for POST requests
}

# Now that your request is signed, you can initiate an API call
print requests.get(url, headers=headers)
```

### Java

```java
String nonce = String.valueOf(System.currentTimeMillis());
String message = nonce + url + (body != null ? body : "");

Mac mac = Mac.getInstance("HmacSHA256");
mac.init(new SecretKeySpec(API_SECRET.getBytes(), "HmacSHA256"));
String signature = new String(Hex.encodeHex(mac.doFinal(message.getBytes())));
request.setHeader("ACCESS_KEY", API_KEY);
request.setHeader("ACCESS_SIGNATURE", signature);
request.setHeader("ACCESS_NONCE", nonce);
```

## Making Requests

Each HMAC requests expect the following HTTP Headers:

* **ACCESS_KEY** - Select `show` on your chosen application's [API Access](https://coins.ph/user/api) dashboard. This is the API Key as displayed on the dialog.
* **ACCESS_SIGNATURE** - An HMAC-SHA256 hash of the nonce concatenated with the full URL and body of the HTTP request, signed using your API secret.
* **ACCESS_NONCE** - A number that can only be used once per user. See [Authentication](https://github.com/coinsph/api/wiki/02-API-Access#use-a-nonce)

Additional headers may be required depending on the API call you are making. For instance, POST requests require the header `Content-Type: application/json`, while GET requests do not expect this header.

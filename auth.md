# Authentication

There are two ways to authenticate with the Coins API:

* [OAuth2](oauth-auth.html) - Popular social networks as well as other Web heavyweights use OAuth 2. This requires a user to allow the developer to associate the user's account with the third party service.
* [HMAC](hmac-auth.html) - HMAC requests do not require user permissions, because the developer executes the request in behalf of the user.

Authorization methods should not be combined. In the event where both OAuth and HMAC authorization are used in a single request, HMAC authorization will take precedence.

## Validating SSL Certificates

SSL Certificates help prevent man-in-the-middle attacks. Your application should validate our SSL certificate whenever it establishes an https connection. If you are using a client library, make sure SSL Verification is turned on.

## Use a Nonce

A [nonce](http://en.wikipedia.org/wiki/Cryptographic_nonce) is used to prevent replay-attacks. Every API call requires a nonce. We expect the nonce to always increase for every request from the same user. The simplest form of nonce you can use is a Unix Epoch timestamp, but feel free to use other forms.

## Storing Credentials Securely

Always make sure your API Credentials are stored securely, Your `api_key`, `api_secret`, and access tokens may be used to access and perform actions in your coins account. In particular, you should avoid storing credentials in your code base and code repositories (like github).

Coins will never ask for your API secret. There is no need to include the API secret on a request.

If there's a need for you to store your secret in a device you don't control (say, a mobile device), it is completely your responsibility to protect the secret. We recommend using encryption and using obfuscators to protect your application from disassemblers and reverse-engineering. Please refer to your chosen platform's documentation for more information.

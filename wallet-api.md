# Wallets API

The Wallets API allows developers to integrate with Coins Crypto Accounts and
build apps that can send and receive Bitcoins.

##Crypto Accounts

This endpoint enables users to see details about their crypto accounts. Crypto
accounts are accounts that hold the user's balance, such as BTC.

### Authentication

This endpoint requires authentication. Please see
[API Authentication](auth.html) for further details.


Resource URL: https://coins.ph/d/api/crypto-accounts/

### HTTP Method

**GET**

### OAuth HTTP Headers

* **Authorization**: `Bearer token`

### HMAC HTTP Headers

* **ACCESS_KEY**: `applicationclientid`. Please see the [HMAC guide](hmac-auth.html) for more information.
* **ACCESS_SIGNATURE**: Computed HMAC hash of the request. Please see the [HMAC guide](hmac-auth.html) for more information.
* **ACCESS_NONCE**: A one time use number. Please see [nonce](auth.html) for more information.

### Parameters

* **currency** - The account currency to be retrieved. Currently, only "BTC" is supported.

### Endpoint

`https://coins.ph/d/api/crypto-accounts/`

### Example Request

https://coins.ph/d/api/crypto-accounts?currency=BTC

### Example Response

```json
{
   "crypto-accounts":[
      {
         "id":"theid",
         "name":"Default Account",
         "currency":"BTC",
         "balance":"0.00030000",
         "pending_balance":"0.00000000",
         "default_address":"theaddress"
      }
   ]
}
```

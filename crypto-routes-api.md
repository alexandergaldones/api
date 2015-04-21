# Crypto Routes

A crypto route automatically redirects funds from one address to another.
If the two addresses are using different currencies, the route would
handle the necessary currency conversion. For instance, a crypto route
can be setup from a BTC address to a PHP address. When the user receives
funds in the BTC address (monitored address), the funds will
automatically be transferred to the PHP address (stock address) and
converted to pesos using the exchange rate at the time of receipt.

## Authentication

This endpoint requires authentication. Please see
[API Authentication](auth.html) for further details.

## Common HTTP Headers

* **Content-Type**: `application/json`

## OAuth HTTP Headers

* **Authorization**: `Bearer token`

## HMAC HTTP Headers

* **ACCESS_KEY**: `applicationclientid`. Please see the [HMAC guide](hmac-auth.html) for more information.
* **ACCESS_SIGNATURE**: Computed HMAC hash of the request. Please see the [HMAC guide](hmac-auth.html) for more information.
* **ACCESS_NONCE**: A one time use number. Please see [nonce](auth.html) for more information.

## Endpoint

`https://coins.ph/api/v3/crypto-routes/`

## Creating Crypto Routes

### HTTP Method

**POST**

### Body

* **monitored_address** - The address to monitor for incoming funds
* **stock_address** - The address where the funds should be transferred

### Example Request

URL: `https://coins.ph/api/v3/crypto-routes/`

```sh
curl -X POST \
    -H 'Content-Type: application/json' \
    -d '{"monitored_address": "1a2b3c", "stock_address": "2a1b4c"}' \
    https://coins.ph/api/v3/crypto-routes
```

### Example Response

```json
{
    "id": "1af3b1",
    "monitored_address": "1a2b3c",
    "stock_address": "2a1b4c",
    "created_at": "2014-08-28T12:11:36.938Z"
}
```

## Retrieving Existing Crypto Routes

### HTTP Method

**GET**

### Example Request

URL: `https://coins.ph/api/v3/crypto-routes/`

```sh
curl -X GET https://coins.ph/api/v3/crypto-routes
```

### Example Response

```json
{
    "id": "1af3b1",
    "monitored_address": "1a2b3c",
    "stock_address": "2a1b4c",
    "created_at": "2014-08-28T12:11:36.938Z"
}
```

## Removing a Crypto Route

### HTTP Method

**DELETE**

### Example Request

URL: `https://coins.ph/api/v3/crypto-routes/1af3b1`

```sh
curl -X DELETE https://coins.ph/api/v3/crypto-routes/1af3b1
```

### Example Response

```json
{
    "id": "1af3b1",
    "monitored_address": "1a2b3c",
    "stock_address": "2a1b4c",
    "created_at": "2014-08-28T12:11:36.938Z"
}
```

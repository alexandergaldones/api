# Transfers

The wallet payments API only work for sending funds that have the same,
currency (ie. BTC -> BTC). The transfers API supports sending funds
across currencies, (ie. PHP -> BTC)

## Authentication

This endpoint requires authentication. Please see
[API Authentication](auth.html) for further details.

## HTTP Method

**POST**

## Common HTTP Headers

* **Content-Type**: `application/json`

## OAuth HTTP Headers

* **Authorization**: `Bearer token`

## HMAC HTTP Headers

* **ACCESS_KEY**: `applicationclientid`. Please see the [HMAC guide](hmac-auth.html) for more information.
* **ACCESS_SIGNATURE**: Computed HMAC hash of the request. Please see the [HMAC guide](hmac-auth.html) for more information.
* **ACCESS_NONCE**: A one time use number. Please see [nonce](auth.html) for more information.

## Endpoint

`https://coins.ph/d/api/transfers/`

## Body

* **account** - The account id of the user (from cypto-accounts request)
* **target_address** - The wallet address of the recipient of funds
* **amount** - The amount to transfer. Currency is determined by the provided account, and conversion will be handled by this endpoint. For example, if the provided `account` is a BTC account and the `target_address` is a PHP account, this endpoint will handle the necessary currency conversion.

## Example Request

URL: `https://coins.ph/d/api/transfers/`

```sh
curl -X POST \
    -H 'Content-Type: application/json' \
    -d '{"target_address": "address", "amount": 0.0001, "account": "2a"}' \
    https://coins.ph/d/api/transfers
```

## Example Response

```json
{
    "transfer": {
        "id":"1b",
        "account":"2a",
        "amount":"0.00010000",
        "target_address":"address",
        "payment": "134abc",
        "exchange": "BTC-PHP",
        "status":"pending",
        "created_at":"2014-08-28T12:11:36.938Z"
    }
}
```
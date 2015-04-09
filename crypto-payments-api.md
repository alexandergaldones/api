# Payments

This endpoint allows sending of Bitcoins and retrieval of the user's transaction
history

## Authentication

This endpoint requires authentication. Please see
[API Authentication](auth.html) for further details.

## Sending Bitcoins

Sending Bitcoins from one account to another can be done by doing a
`POST` through this endpoint.

### HTTP Method

**POST**

### Common HTTP Headers

* **Content-Type**: `application/json`

### OAuth HTTP Headers

* **Authorization**: `Bearer token`

### HMAC HTTP Headers

* **ACCESS_KEY**: `applicationclientid`. Please see the [HMAC guide](hmac-auth.html) for more information.
* **ACCESS_SIGNATURE**: Computed HMAC hash of the request. Please see the [HMAC guide](hmac-auth.html) for more information.
* **ACCESS_NONCE**: A one time use number. Please see [nonce](auth.html) for more information.

### Endpoint

`https://coins.ph/d/api/crypto-payments/`


### Body

* **account** - The account id of the user (from cypto-accounts request)
* **target_address** - The wallet address of the recipient of the bitcoins
* **amount** - The amount in BTC
* **user_comment** - A text or message attached with the transaction (optional)
* **code** - Two-Factor code (only needed when user has two-factor enabled in his/her account)

### Example Request

URL: `https://coins.ph/d/api/crypto-payments/`

```sh
curl -X POST \
    -H 'Content-Type: application/json' \
    -d '{"target_address": "address", "amount": 0.0001, "account": "2a"}' \
    https://coins.ph/d/api/crypto-payments
```

### Example Response

```json
{
    "crypto-payment": {
        "id":"1b",
        "account":"2a",
        "tx_id":"",
        "target_address":"address",
        "entry_type":"outgoing",
        "status":"pending",
        "amount":"0.00010000",
        "fee_amount":"0.00000000",
        "created_at":"2014-08-28T12:11:36.938Z"
    }
}
```

## Transaction History

Users can retrieve their transaction history by calling this endpoint with a `GET` method.

### Endpoint

`https://coins.ph/d/api/crypto-payments`

### OAuth HTTP Headers

* **Authorization**: `Bearer token`

### HMAC HTTP Headers

* **ACCESS_KEY**: `applicationclientid`. Please see the [HMAC guide](hmac-auth.html) for more information.
* **ACCESS_SIGNATURE**: Computed HMAC hash of the request. Please see the [HMAC guide](hmac-auth.html) for more information.
* **ACCESS_NONCE**: A one time use number. Please see [nonce](auth.html) for more information.

### Example Request

URL: `https://coins.ph/d/api/crypto-payments`

```sh
curl -X GET https://coins.ph/d/api/crypto-payments
```

### Example Response

```json
{
   crypto-payments:[
      {
         id:"1b",
         account:"1a",
         tx_id:"",
         target_address:"address",
         entry_type:"incoming",
         status:"success",
         amount:"0.00010000",
         fee_amount:"0.00000000",
         created_at:"2014-08-28T12:11:36.938Z"
      },
      {
         id:"2a",
         account:"1a",
         tx_id:"",
         target_address:"address1",
         entry_type:"outgoing",
         status:"success",
         amount:"0.00010000",
         fee_amount:"0.00000000",
         created_at:"2014-08-29T07:36:56.441Z"
      }
   ]
}
```

## Error Responses

### Invalid target address

HTTP/1.1 400 BAD REQUEST

```json
{
   "errors":{
      "target_address":[
         "Invalid address format."
      ]
   }
}
```

### Insufficient balance

HTTP/1.1 400 BAD REQUEST

```json
{
   "errors":{
      "non_field_errors":[
         "Insufficient balance."
      ]
   }
}
```
### Invalid two-factor code

HTTP/1.1 422 UNPROCESSABLE ENTITY

```json
{
   "errors":{
      "code":"Two-factor code invalid!"
   },
   "success":false
}
```

### Missing Parameters

HTTP/1.1 400 BAD REQUEST

```json
{
   "errors":{
      "target_address":[
         "This field is required."
      ],
      "account":[
         "This field is required."
      ],
      "amount":[
         "This field is required."
      ]
   }
}
```
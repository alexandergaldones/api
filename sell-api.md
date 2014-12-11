# Send Money API

Developers can use the send money API to send money across different countries, or to sell bitcoins to coins.ph. Each sell order generates a new wallet address where the user should send the Bitcoins. Once the Bitcoin payment is received, coins.ph will deposit the current market value of the Bitcoin into the specified "Payment Outlet". While coins.ph does not impose a fee on sending money itself, some payment outlets do impose fees based on a specified range. The payment outlet fee is added on the total price to be paid by the user.


## Getting Quotes

The Sell Quote API provides methods for a user to determine the current market value of Bitcoin when converted to a currency. Price is listed per payment outlet supported by coins.ph.


### HTTP Method

**GET**

### Endpoint

https://coins.ph/api/v2/sellquote

### Parameters

* **btc_amount** (optional)- Mutually exclusive with `amount`. Either this, or `amount` should be present in the request. The total amount in Bitcoins, as provided by the user. _NOTE: The amount is in BTC format (900mbtc = .9 BTC)._
* **amount** (optional) - Mutually exclusive with `btc_amount`. Either this, or `btc_amount` should be present in the request. The total amount in Fiat currency. Use this if you prefer specifying amounts in fiat instead of BTC.
* **currency** - An ISO 4217 fiat currency symbol (ie, "PHP", "USD", "SGD"). If `btc_amount` is provided instead of `amount`, this is the currency to which the BTC price will be converted into. Otherwise, if `amount` is specified instead of `btc_amount`, this is the currency of the specified amount.
* **full** (optional, defaults to `False`) - Show the `required_fields` for each payment outlet as an array of {`id`, `name`} objects. This accepts either `True` or `False`. When not provided or if the value is `False`, the `required_fields` for each Payment Outlet are returned as an array of `id` strings. For more information about `required_fields`, please refer to the [Payment Outlet Documentation](payment-outlets.html).

### Example Request

URL: https://coins.ph/api/v2/sellquote?btc_amount=1&currency=PHP

```sh
curl -X GET "https://coins.ph/api/v2/sellquote?btc_amount=1&currency=PHP"
```

### Example Response

```json
{
  "quote": {
    "btc_amount": 1,
    "currency": "PHP",
    "outlets": {
      "bdo": {
        "fee": 0.00,
        "outlet_id": "bdo",
        "outlet_type_id": "bank",
        "required_fields": [
          "bank_account_name",
          "bank_account_number"
        ],
        "subtotal": 26622,
        "total": 26622.00
      },
      "bdo_deposit": {
        "fee": 0.00,
        "outlet_id": "bdo_deposit",
        "outlet_type_id": "bank_deposit",
        "required_fields": [],
        "subtotal": 26622,
        "total": 26622.00
      },
      "bpi": {
        "fee": 0.00,
        "outlet_id": "bpi",
        "outlet_type_id": "bank",
        "required_fields": [
          "bank_account_name",
          "bank_account_number"
        ],
        "subtotal": 26622,
        "total": 26622.00
      },
      "bpi_deposit": {
        "fee": 0.00,
        "outlet_id": "bpi_deposit",
        "outlet_type_id": "bank_deposit",
        "required_fields": [],
        "subtotal": 26622,
        "total": 26622.00
      },
      "bpi_family": {
        "fee": 0.00,
        "outlet_id": "bpi_family",
        "outlet_type_id": "bank",
        "required_fields": [
          "bank_account_name",
          "bank_account_number"
        ],
        "subtotal": 26622,
        "total": 26622.00
      },
      "bpie_deposit": {
        "fee": 0.00,
        "outlet_id": "bpie_deposit",
        "outlet_type_id": "bank_deposit",
        "required_fields": [],
        "subtotal": 26622,
        "total": 26622.00
      },
      "cebuana_lhuillier_perapadala": {
        "fee": 400.00,
        "outlet_id": "cebuana_lhuillier_perapadala",
        "outlet_type_id": "moneygram_pickup",
        "required_fields": [
          "full_name",
          "full_address"
        ],
        "subtotal": 26622,
        "total": 26222.00
      },
      "china_bank": {
        "fee": 0.00,
        "outlet_id": "china_bank",
        "outlet_type_id": "bank",
        "required_fields": [
          "bank_account_name",
          "bank_account_number"
        ],
        "subtotal": 26622,
        "total": 26622.00
      },
      "citi": {
        "fee": 0.00,
        "outlet_id": "citi",
        "outlet_type_id": "bank",
        "required_fields": [
          "bank_account_name",
          "bank_account_number"
        ],
        "subtotal": 26622,
        "total": 26622.00
      },
      "eastwest": {
        "fee": 0.00,
        "outlet_id": "eastwest",
        "outlet_type_id": "bank",
        "required_fields": [
          "bank_account_name",
          "bank_account_number"
        ],
        "subtotal": 26622,
        "total": 26622.00
      },
      "gcash": {
        "fee": 270.00,
        "outlet_id": "gcash",
        "outlet_type_id": "phone_account",
        "required_fields": [
          "phone_number"
        ],
        "subtotal": 26622,
        "total": 26352.00
      },
      "lbc_pesopadala": {
        "fee": 1350.00,
        "outlet_id": "lbc_pesopadala",
        "outlet_type_id": "moneygram_pickup",
        "required_fields": [
          "full_name",
          "full_address"
        ],
        "subtotal": 26622,
        "total": 25272.00
      },
      "union_bank": {
        "fee": 0.00,
        "outlet_id": "union_bank",
        "outlet_type_id": "bank",
        "required_fields": [
          "bank_account_name",
          "bank_account_number"
        ],
        "subtotal": 26622,
        "total": 26622.00
      }
    },
    "rate": 26622
  },
  "success": true
}
```

***

## Sell Order

Sending money and selling Bitcoins use the same API endpoint. This endpoint supports creating new sell orders, and retrieving existing ones.

### Authentication

This endpoint requires authentication. Please see [API Authentication](auth.html) for further details.

### Creating Sell Orders

#### HTTP Method
**POST**

#### Common HTTP Headers

* **Content-Type**: `application/json`

#### OAuth HTTP Headers

* **Authorization**: `Bearer token`

#### HMAC HTTP Headers

* **ACCESS_KEY**: `applicationclientid`. Please see the [HMAC guide](hmac-auth.html) for more information.
* **ACCESS_SIGNATURE**: Computed HMAC hash of the request. Please see the [HMAC guide](hmac-auth.html) for more information.
* **ACCESS_NONCE**: A one time use number. Please see [nonce](auth.html) for more information.

#### Endpoint

`https://coins.ph/api/v2/sellorder/<order_id>`

#### Body

* **btc_amount** - Transaction total amount in bitcoins.   _NOTE: The amount is in BTC format (900mbtc = .9 BTC)._
* **currency** - ISO 4217 fiat currency symbol (ie, "PHP", "USD", "SGD").
* **payment_outlet** - The **outlet_id** as provided by sell qoute api.
* **other field** - Payment outlets have different required fields such as, and are not limited to, `first_name`, `bank_account_name`, `bank_account_number`, etc. These are listed as **required_fields** when retrieving a sell quote. Please refer to the [Payment Outlet Documentation](payment-outlets.html) and the [Sell Quote Documentation](sell-api.html) for more information.

#### Example Request

URL: `https://coins.ph/api/v2/sellorder`

```sh
# OAuth Request
curl -X POST -H 'Content-Type: application/json' -H 'Authorization: Bearer yourtoken' -d '{"currency": "PHP", "btc_amount": 0.5, "payment_outlet": "bdo", "bank_account_name": "John Smith", "bank_account_number": 0123456789}' https://coins.ph/api/v2/sellorder

# HMAC Request
curl -X POST -H 'Content-Type: application/json' -H 'ACCESS_KEY: yourtoken' -H 'ACCESS_SIGNATURE requestsignature' -H 'ACCESS_NONCE 1234' -d '{"currency": "PHP", "btc_amount": 0.5, "payment_outlet": "bdo", "bank_account_name": "John Smith", "bank_account_number": 0123456789}' https://coins.ph/api/v2/sellorder
```

#### Example Response

```json
{
  "order": {
    "btc_amount": 0.5000000000,
    "confirmation_code": "9d6eb",
    "expires_epoch": "1402483355",
    "fields": {
      "bank_account_name": "John Smith",
      "bank_account_number": "0123456789"
    },
    "id": "9d6eb8f98b754cd7aa9d8d930054cda1",
    "payment_outlet_id": "bdo",
    "qr_img_uri": "https://chart.googleapis.com/chart?chl=bitcoin%3A1MRPzpzANvVaBneVsn5rEVqApHRmZq1SBV%3Famount%3D0.50000000&chs=400x400&cht=qr&choe=UTF-8&chld=L%7C0",
    "user_uri": "https://localhost.dev:5000/sellorder/9d6eb8f98b754cd7aa9d8d930054cda1",
    "wallet_address": "1MRPzpzANvVaBneVsn5rEVqApHRmZq1SBV"
  },
  "success": true
}
```

### Retrieving existing Sell Orders

#### Authentication

This endpoint requires authentication. Please see [API Authentication](auth.html) for further details.

#### HTTP Method

**GET**

#### Endpoint

`https://coins.ph/api/v2/sellorder/<order_id>`

#### OAuth HTTP Headers

* **Authorization**: `Bearer token`

#### HMAC HTTP Headers

* **ACCESS_KEY**: `applicationclientid`. Please see the [HMAC guide](hmac-auth.html) for more information.
* **ACCESS_SIGNATURE**: Computed HMAC hash of the request. Please see the [HMAC guide](hmac-auth.html) for more information.
* **ACCESS_NONCE**: A one time use number. Please see [nonce](auth.html) for more information.

#### Example Request

URL: `https://coins.ph/api/v2/sellorder/1o2r3d4e5r`

```sh
curl https://coins.ph/api/v2/sellorder/1o2r3d4e5r
```

#### Example Response
```json
{
    "order": {
        "btc_amount": "0.025",
        "btc_pending": "0",
        "btc_received": "0",
        "confirmation_code": "94d21",
        "created_at": "1409206264",
        "currency": "PHP",
        "currency_amount": "0",
        "currency_fees": "0",
        "currency_settled": "0",
        "expires_epoch": "1409209864",
        "fields": {
            "bank_account_name": "User Name",
            "bank_account_number": "1234"
        },
        "id": "1o2r3d4e5r",
        "payment_outlet_id": "bdo",
        "qr_img_uri": "https://chart.googleapis.com/chart?chl=bitcoin%3A1FopCYYRs3Tg4YTjsT7XaBYKPg4pEAtv5a%3Famount%3D0.02500000&chs=400x400&cht=qr&choe=UTF-8&chld=L%7C0",
        "status": "pending",
        "user_uri": "https://coins.ph/sellorder/1o2r3d4e5r",
        "wallet_address": "1FopCYYRs3Tg4YTjsT7XaBYKPg4pEAtv5a"
    },
    "success": true
}
```

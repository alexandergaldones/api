# Sending Phone Load

Using the coins API, you can send load to any supported phone number.
It could be your phone number, or anyone else's. The [Sell API](sell-api.html)
makes this possible by converting Bitcoins into phone load.

## Prerequisites

* A properly set up [API key](https://coins.ph/user/api)
* [Authentication](auth.html)
* Sender must have either BTC or PHP balance

## Accepted Currencies

Load can be paid using the user's BTC balance, or PHP balance. To pay using
BTC, the `pay_with_wallet` parameter should indicate `BTC`. Conversely, `PBTC`
should be indicated when `PHP` would be used to pay for the load. However,
please do take note that regardless of the currency to be used for payment,
the current `BTC` conversion rate should be indicated in the `btc_amount`
parameter.

## Using the Sell API to Send Load

Sending load is a `POST` request to the `sellorder` endpoint. The body must have:

* **payment_outlet** - This can either be `load-globe`, `load-smart`, or `load-suncell`.
* **currency_amount_locked** - The amount of load to send.
* **currency** - The medium of exchange to use for buying load. Can either be `BTC` or `PHP`.
* **pay_with_wallet** - The user's wallet to use to pay for the load. Can either be `BTC` or `PBTC`.
* **phone_number_load** - The phone number to send load to.
* **btc_amount** - Converted BTC amount of `currency_amount_locked`. Please see the [Sell Quote API](sell-api.html) on how to convert from fiat to BTC.

```
https://coins.ph/api/v2/sellorder

{
    "payment_outlet": "load-globe",
    "btc_amount": 0.0020504,
    "code": 189772,
    "currency": "PHP",
    "currency_amount_locked": 25,
    "pay_with_wallet": "BTC",
    "phone_number_load": "+639171234567"
}
```

A successful response:

```
{
  "order": {
    "amount": "25",
    "btc_amount": "0.00205",
    "btc_pending": "0",
    "btc_received": "0",
    "confirmation_code": "12323",
    "confirmations": [],
    "created_time": "1425466700",
    "currency": "PHP",
    "currency_amount": "25",
    "currency_fees": "0",
    "currency_net": "25",
    "currency_settled": "0",
    "due_btc_amount": "0.00205",
    "expires_epoch": "1425470360",
    "fields": {
      "phone_number_load": "+639171234567"
    },
    "id": "123",
    "payment_account": {
      "id": "123",
      "payment_outlet": {
        "id": "load-globe",
        "name": "Globe / TM Prepaid"
      },
      "required_fields": [
        {
          "name": "phone_number_load",
          "value": "+639171234567"
        }
      ]
    },
    "payment_outlet_id": "load-globe",
    "payment_outlet_name": "Globe / TM Prepaid",
    "payment_outlet_type_id": "mobile-load",
    "phone_number_load": "+639171234567",
    "qr_img_url": "https://the.chart.uri",
    "rate": "12188",
    "region": "PH",
    "settlements": [],
    "status": "pending",
    "user_id": "123",
    "user_uri": "https://coins.ph/sellorder/456",
    "wallet_address": "1f73WCSwMGwvA8p3E6DkwseDE5qN3FxMRn"
  },
  "success": true
}
```

The usual [authentication](auth.html) headers apply, which may either be HMAC or OAuth.

## Load Denominations

Not all network providers support the same load denomination, let alone an arbitrary
amount. The following are the valid load denominations.

### Globe/Touch Mobile

Values of 25, 50, 150, 300, and 500 are supported.

### Smart/Talk N Text

Values of 30, 50, 60, 100, 115, 200, 300, and 500 are supported.

### Sun Cellular

Values of 25, 30, 50, 100, 150, 300, and 500 are supported.
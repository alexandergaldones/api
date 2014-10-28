# Buy Order API

Developers can use the Buy Order API to buy bitcoins from coins.ph. Each buy order should specify a payment method to which the fiat currency will be sent. Once coins.ph receives the currency, coins.ph will release the Bitcoins either to the user's coins.ph wallet, or to a provided wallet address.

## Getting Quotes

The Buy Quote API provides methods for a user to determine the current market value of Bitcoin when converted to a currency. Price is listed per mayment method supported by coins.ph.

### HTTP Method

**GET**

### Endpoint

https://coins.ph/api/v2/buyquote

### Parameters

* **btc_amount** - The total amount in Bitcoins, as provided by the user. _NOTE: The amount is in BTC format (900mbtc = .9 BTC)._
* **currency** - An ISO 4217 fiat currency symbol (ie, "PHP", "USD", "SGD") to which the BTC price will be converted into.

### Example Request

URL: https://coins.ph/api/v2/buyquote?btc_amount=1&currency=PHP

```sh
curl -X GET "https://coins.ph/api/v2/buyquote?btc_amount=1&currency=PHP"
```

### Example Response

```json
{
   "quote":{
      "btc_amount":1,
      "currency":"PHP",
      "outlets":{
         "bdo-online_deposit":{
            "available":true,
            "coins_fee":"203",
            "collections_outlet":true,
            "fee":"0",
            "help_link":"https://coinsph.zendesk.com/hc/en-us/articles/202270604-How-do-I-pay-for-Bitcoin-using-BDO-Online-Banking-",
            "help_text":"Transfer funds online to our BDO account using BDO Online Banking. NOTE: Please enable your account for online fund transfers and enroll our account as a Third Party Account before placing an order.",
            "name":"BDO Online Banking",
            "outlet_id":"bdo-online_deposit",
            "outlet_type_id":"bank_deposit",
            "outlet_type_name":"Bank Deposit",
            "required_fields":[

            ],
            "subtotal":"20337",
            "total":"20540"
         },
         "bdo_deposit":{
            "available":true,
            "coins_fee":"203",
            "collections_outlet":true,
            "fee":"0",
            "help_link":"https://coinsph.zendesk.com/hc/en-us/articles/201511440-How-do-I-pay-for-bitcoin-through-a-BDO-deposit-",
            "help_text":"Make a cash deposit to our BDO account at any BDO branch.",
            "name":"BDO",
            "outlet_id":"bdo_deposit",
            "outlet_type_id":"bank_deposit",
            "outlet_type_name":"Bank Deposit",
            "required_fields":[

            ],
            "subtotal":"20337",
            "total":"20540"
         },
         "bdoatm_deposit":{
            "available":true,
            "coins_fee":"203",
            "collections_outlet":true,
            "fee":"0",
            "help_link":"https://coinsph.zendesk.com/hc/en-us/articles/202379090-How-do-I-pay-for-bitcoin-through-a-24-hour-BDO-ATM-",
            "help_text":"Make a cash deposit via a BDO ATM. Please note that the machines do not dispense change and only accept bills in the following denominations: PHP100, PHP200, PHP500 and PHP1,000",
            "name":"BDO 24-hour ATM Deposit",
            "outlet_id":"bdoatm_deposit",
            "outlet_type_id":"atm_deposit",
            "outlet_type_name":"ATM Deposit",
            "required_fields":[

            ],
            "subtotal":"20337",
            "total":"20540"
         },
         "bpi_deposit":{
            "available":true,
            "coins_fee":"203",
            "collections_outlet":true,
            "fee":"0",
            "help_link":"https://coinsph.zendesk.com/hc/en-us/articles/201511430-How-do-I-pay-for-bitcoin-through-a-BPI-deposit-",
            "help_text":"Make a cash deposit to our BPI account at any BPI branch.",
            "name":"BPI",
            "outlet_id":"bpi_deposit",
            "outlet_type_id":"bank_deposit",
            "outlet_type_name":"Bank Deposit",
            "required_fields":[

            ],
            "subtotal":"20337",
            "total":"20540"
         },
         "bpiatm_deposit":{
            "available":true,
            "coins_fee":"203",
            "collections_outlet":true,
            "fee":"0",
            "help_link":"https://coinsph.zendesk.com/hc/en-us/articles/202637070",
            "help_text":"Make a cash deposit via a BPI ATM. Please note that the machines do not dispense change and only accept bills in the following denominations: PHP100, PHP500 and PHP1,000",
            "name":"BPI 24-hour ATM Deposit",
            "outlet_id":"bpiatm_deposit",
            "outlet_type_id":"atm_deposit",
            "outlet_type_name":"ATM Deposit",
            "required_fields":[

            ],
            "subtotal":"20337",
            "total":"20540"
         },
         "bpie_deposit":{
            "available":true,
            "coins_fee":"203",
            "collections_outlet":true,
            "fee":"0",
            "help_link":"https://coinsph.zendesk.com/hc/en-us/articles/201432304-How-do-I-pay-for-Bitcoin-using-BPI-Express-Online-",
            "help_text":"Transfer funds online to our BPI account using BPI Express Online. NOTE: Please enable your account for online fund transfers and enroll our account as a Third Party Account before placing an order.",
            "name":"BPI Express Online",
            "outlet_id":"bpie_deposit",
            "outlet_type_id":"bank_deposit",
            "outlet_type_name":"Bank Deposit",
            "required_fields":[

            ],
            "subtotal":"20337",
            "total":"20540"
         },
         "gcash_deposit":{
            "available":false,
            "collections_outlet":true,
            "help_link":"https://coinsph.zendesk.com/hc/en-us/articles/201767920-How-do-I-pay-for-bitcoin-through-a-GCash-transfer-",
            "help_text":"Transfer GCash using your mobile phone to our GCash account. Only available for orders PHP10,000 and below.",
            "name":"GCash",
            "outlet_id":"gcash_deposit",
            "outlet_type_id":"phone_deposit",
            "outlet_type_name":"Mobile Money"
         },
         "mlhuillier_deposit":{
            "available":false,
            "collections_outlet":true,
            "help_link":"https://coinsph.zendesk.com/hc/en-us/articles/202694180",
            "help_text":"Pay with cash at any M Lhuillier outlet by presenting your transaction code (to be given once you confirm your order). Only available for orders PHP50,000 and below. NOTE: You must have a validated account in order to use this option. ",
            "name":"M Lhuillier ePay",
            "outlet_id":"mlhuillier_deposit",
            "outlet_type_id":"validated_deposit",
            "outlet_type_name":"Validated Bank Deposit"
         },
         "union_deposit":{
            "available":true,
            "coins_fee":"203",
            "collections_outlet":true,
            "fee":"0",
            "help_link":"https://coinsph.zendesk.com/hc/en-us/articles/202641930",
            "help_text":"Make a cash deposit to our UnionBank account at any UnionBank branch.",
            "name":"UnionBank",
            "outlet_id":"union_deposit",
            "outlet_type_id":"bank_deposit",
            "outlet_type_name":"Bank Deposit",
            "required_fields":[

            ],
            "subtotal":"20337",
            "total":"20540"
         }
      },
      "rate":20337
   },
   "success":true
}
```

***

## Buy Order

This endpoint supports creating new buy orders, retrieving existing ones, and marking the status of the buy order as paid.

### Authentication

This endpoint requires authentication. Please see [API Authentication](https://github.com/coinsph/coins-examples/wiki/02-API-Access) for further details.

### Creating Buy Orders

#### HTTP Method

**POST**

#### Common HTTP Headers

* **Content-Type**: `application/json`

#### OAuth HTTP Headers

* **Authorization**: `Bearer token`

#### HMAC HTTP Headers

* **ACCESS_KEY**: `applicationclientid`. Please see the [HMAC guide](https://github.com/coinsph/api/wiki/04-Authentication-with-API-Key---Secret#making-requests) for more information.
* **ACCESS_SIGNATURE**: Computed HMAC hash of the request. Please see the [HMAC guide](https://github.com/coinsph/api/wiki/04-Authentication-with-API-Key---Secret#making-requests) for more information.
* **ACCESS_NONCE**: A one time use number. Please see [nonce](https://github.com/coinsph/api/wiki/02-API-Access#use-a-nonce) for more information.

#### Endpoint

`https://coins.ph/api/v2/buyorder`

#### Body

* **btc_amount** - Transaction total amount in bitcoins.   _NOTE: The amount is in BTC format (900mbtc = .9 BTC)._
* **currency** - ISO 4217 fiat currency symbol (ie, "PHP", "USD", "SGD").
* **payment_method** - The **outlet_id** as provided by buy qoute api.
* **target_wallet** - The Bitcoin address where the Bitcoins will be sent.
* **rate** - The current **rate** as provided by buy qoute api.

#### Example Request

URL: `https://coins.ph/api/v2/buyorder`

```sh
curl -X POST\
    -H 'Content-Type: application/json'\
    -d '{"currency": "PHP", "btc_amount": 0.5, "payment_method": "bpi_deposit", "target_wallet": "YOURTARGETWALLETGOESHERE", "rate": 21230}' https://coins.ph/api/v2/buyorder
```

#### Example Response

```json
{
    "order": {
        "btc_amount": "0.001",
        "btc_released": "0",
        "canceled_time": null,
        "created_at": "1408420128",
        "currency_amount": "20",
        "id": "48e34b7161c34d5eb45e8c42d6b04924",
        "marked_paid_time": null,
        "payment_method": "bpi_deposit",
        "rate": "20328",
        "status": "pending_payment",
        "wallet_address": "13i4jDpG7vuX17Rvwe1TnbsGrkBo54Jga7"
    },
    "success": true
}
```

### Retrieving existing Buy Orders

#### Authentication

This endpoint requires authentication. Please see [API Authentication](https://github.com/coinsph/coins-examples/wiki/02-API-Access) for further details.

#### HTTP Method

**GET**

#### Endpoint

`https://coins.ph/api/v2/buyorder/<order_id>`

#### OAuth HTTP Headers

* **Authorization**: `Bearer token`

#### HMAC HTTP Headers

* **ACCESS_KEY**: `applicationclientid`. Please see the [HMAC guide](https://github.com/coinsph/api/wiki/04-Authentication-with-API-Key---Secret#making-requests) for more information.
* **ACCESS_SIGNATURE**: Computed HMAC hash of the request. Please see the [HMAC guide](https://github.com/coinsph/api/wiki/04-Authentication-with-API-Key---Secret#making-requests) for more information.
* **ACCESS_NONCE**: A one time use number. Please see [nonce](https://github.com/coinsph/api/wiki/02-API-Access#use-a-nonce) for more information.

#### Example Request

URL: `https://coins.ph/api/v2/buyorder/1o2r3d4e5r`

```sh
curl -X GET https://coins.ph/api/v2/buyorder/1o2r3d4e5r
```

#### Example Response

```json
{
    "order": {
        "btc_amount": "0.025",
        "btc_released": "0",
        "canceled_time": null,
        "created_at": "1409207466",
        "currency_amount": "624",
        "expiration_time": "1409211066",
        "id": "1o2r3d4e5r",
        "instructions": "Deposit to BDO",
        "marked_paid_time": null,
        "payment_method": "bdo_deposit",
        "rate": "24489",
        "status": "pending_payment",
        "wallet_address": "1GEw9EPAVpZAbZQqCe1nc19Uiq38J4QxXE"
    },
    "success": true
}
```

### Cancelling a Buy Order

#### Authentication

This endpoint requires authentication. Please see [API Authentication](https://github.com/coinsph/coins-examples/wiki/02-API-Access) for further details.

#### HTTP Method

**DELETE**

#### OAuth HTTP Headers

* **Authorization**: `Bearer token`

#### HMAC HTTP Headers

* **ACCESS_KEY**: `applicationclientid`. Please see the [HMAC guide](https://github.com/coinsph/api/wiki/04-Authentication-with-API-Key---Secret#making-requests) for more information.
* **ACCESS_SIGNATURE**: Computed HMAC hash of the request. Please see the [HMAC guide](https://github.com/coinsph/api/wiki/04-Authentication-with-API-Key---Secret#making-requests) for more information.
* **ACCESS_NONCE**: A one time use number. Please see [nonce](https://github.com/coinsph/api/wiki/02-API-Access#use-a-nonce) for more information.

#### Endpoint

`https://coins.ph/api/v2/buyorder/<order_id>`

#### Example Request

URL: `https://coins.ph/api/v2/buyorder/1o2r3d4e5r`

```sh
curl -X DELETE https://coins.ph/api/v2/buyorder/1o2r3d4e5r
```

#### Example Response

```json
{
    "order": {
        "btc_amount": "0.025",
        "btc_released": "0",
        "canceled_time": "1409207466",
        "created_at": "1409207466",
        "currency_amount": "624",
        "expiration_time": "1409211066",
        "id": "1o2r3d4e5r",
        "instructions": "Deposit to BDO",
        "marked_paid_time": null,
        "payment_method": "bdo_deposit",
        "rate": "24489",
        "status": "pending_payment",
        "wallet_address": "1GEw9EPAVpZAbZQqCe1nc19Uiq38J4QxXE"
    },
    "success": true
}
```

### Marking a Buy Order as Paid

#### Authentication

This endpoint requires authentication. Please see [API Authentication](https://github.com/coinsph/coins-examples/wiki/02-API-Access) for further details.

#### HTTP Method

**PUT**

#### OAuth HTTP Headers

* **Authorization**: `Bearer token`

#### HMAC HTTP Headers

* **ACCESS_KEY**: `applicationclientid`. Please see the [HMAC guide](https://github.com/coinsph/api/wiki/04-Authentication-with-API-Key---Secret#making-requests) for more information.
* **ACCESS_SIGNATURE**: Computed HMAC hash of the request. Please see the [HMAC guide](https://github.com/coinsph/api/wiki/04-Authentication-with-API-Key---Secret#making-requests) for more information.
* **ACCESS_NONCE**: A one time use number. Please see [nonce](https://github.com/coinsph/api/wiki/02-API-Access#use-a-nonce) for more information.

#### Endpoint

`https://coins.ph/api/v2/buyorder/<order_id>`

#### Example Request

URL: `https://coins.ph/api/v2/buyorder/1o2r3d4e5r`

```sh
curl -X PUT https://coins.ph/api/v2/buyorder/1o2r3d4e5r
```

#### Example Response

```json
{
    "order": {
        "btc_amount": "0.025",
        "btc_released": "0",
        "canceled_time": "1409207466",
        "created_at": "1409207466",
        "currency_amount": "624",
        "expiration_time": "1409211066",
        "id": "1o2r3d4e5r",
        "instructions": "Deposit to BDO",
        "marked_paid_time": "140920000",
        "payment_method": "bdo_deposit",
        "rate": "24489",
        "status": "pending_payment",
        "wallet_address": "1GEw9EPAVpZAbZQqCe1nc19Uiq38J4QxXE"
    },
    "success": true
}
```

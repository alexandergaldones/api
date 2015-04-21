# Coins API Reference.

Coins.ph provides a simple and powerful REST API to perform Bitcoin backed
transactions in Asia.

We currently serve the following markets:

* [Philippines](https://coins.ph)
* [Thailand](https://coins.co.th)

Some of the things you can do with the coins.ph API:

* **Accept Bitcoin** payments as a merchant
* **Bitcoin in, Cash out**: send money to anyone via our local [pay-out network](https://coinsph.zendesk.com/hc/en-us/articles/202398194-Which-payout-methods-are-available-) (local banks deposits, pick-up at 5000+ retail locations, door-to-door, and mobile money).
* **Buy and Sell** Bitcoin using our [pay-in](https://coinsph.zendesk.com/hc/en-us/articles/201322620-Which-payment-methods-do-you-accept-) and [pay-out](https://coinsph.zendesk.com/hc/en-us/articles/202398194-Which-payout-methods-are-available-) options.
* Get current **exchange rates** in local currency

All requests go over https. The base URL is `https://coins.ph/api/v2/` and
endpoints are in the format `https://coins.ph/api/v2/<endpoint>`. For instance,
the Buy Quote API can be accessed through `https://coins.ph/api/v2/buyquote`.
Please refer to a particular endpoint's documentation for more usage examples.

For API support you can post a question in our
[issue tracker](https://github.com/coinsph/api/issues).

Please take note that all data from the examples provided may vary from actual
production data.

## Creating a new application

It is required to create a new application to get started with the Coins API.
Please login to your account and visit [API Access](https://coins.ph/user/api).

API access is turned off by default on all accounts. If you decide to use our
API, you will need to enable it first via your account settings. You can
always disable your API Access, or regenerate your API keys, if you think your
keys have been compromised.

## Getting started

* [Authentication](auth.html)
* [Endpoints](endpoints.html)
* [Register an application](https://coins.ph/user/api)

## Quotes API

* [Getting Market Rates](quote-api.html)

## Payment Outlets API

* [Payin Outlets](payin-outlets-api.html)
* [Payout Outlets](payout-outlets-api.html)

## Send Money API

* [Sell Quotes](sell-api.html#getting-quotes)
* [Create Sell Order](sell-api.html#creating-sell-orders)
* [View Sell Order](sell-api.html#retrieving-existing-sell-orders)
* [Supported Payout Outlets](payment-outlets.html)

## Buy Order API

* [Buy Quotes](buy-api.html#getting-quotes)
* [Create Buy Order](buy-api.html#creating-buy-orders)
* [View Buy Order](buy-api.html#retrieving-existing-buy-orders)
* [Cancel Buy Order](buy-api.html#cancelling-a-buy-order)
* [Mark Buy Order as Paid](buy-api.html#marking-a-buy-order-as-paid)

## Wallet API
* [Accounts](crypto-accounts-api.html)
* [Transfers](crypto-transfers-api.html)
* [Routes](crypto-routes-api.html)

## Merchant API

If are using coins.ph to accept Bitcoin payments, please sign up here:

* [Merchant tools overview](https://coins.ph/merchants)
* [Merchant API reference](merchant-api.html)
* [Magento plugin](https://github.com/coinsph/coins-magento)
* [Merchant registration](https://coins.ph/merchants/signup)

## Usage Examples

* [Sending Phone Load](send-load.html)
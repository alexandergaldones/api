# Send Money to Anyone

Using the coins API, you can send money to anyone through the
[Sell API](sell-api.html). This converts your Bitcoin into cash, which would
then be sent to a payout outlet of your choice.

## Prerequisites

* A properly set up [API key](https://coins.ph/user/api)
* [Authentication](auth.html)
* Sender must have either BTC or PHP balance

## Supported Payout Outlets

To view the list of supported payout outlets, you can use the
[Payout Outlet API](payout-outlets.html).

## Working Example

An HMAC [example](https://github.com/coinsph/api/blob/master/python/hmac_sendmoney.py)
for this flow can be found on the master branch of the coinsph API repo. There's
also an [example](https://github.com/coinsph/api/blob/master/python/oauth_sendmoney.py)
on how to do the same flow using OAuth.
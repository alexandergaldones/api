# Coins PHP examples

This currently contains a `Coins` PHP class, which serves as a wrapper for the coins
sendmoney and sendbitcoin APIs.

## Installation

The wrapper class depends on the PHP library
[Requests](http://requests.ryanmccue.info/). Please refer to the Requests
[documentation](https://github.com/rmccue/Requests#installation) for instructions on
how to obtain this dependency.

To install the Coins wrapper, copy it to your project directory.

## Usage

Instantiate the `Coins` class with either HMAC or OAuth authentication:

```
$coins = Coins::withHMAC('ID', 'KEY') /* If you're planning to use hmac */
$coins = Coins::withOAuthToken('TOKEN') /* If you're planning to use oauth */
```

### Sendbitcoin

#### Parameters

Sending Bitcoin requires two parameters:

* `$target_address` - The address to send to. It can be a Bitcoin address, email address, or phone number.
* `$amount` - The amount to send.
* `$account` - (Optional) the sender account. If not provided, the account would be retrieved through the API based on current credentials.

#### Signature

```
$coins->sendBitcoin($target_address, $amount, $account)
```

### Sendmoney

#### Parameters

* `$params` - An associative array that would contain the request body. This array should contain the following keys:
    * btc_amount - Transaction total amount in bitcoins. NOTE: The amount is in BTC format (900mbtc = .9 BTC).
    * amount - Transaction total amount in the passed currency.
    * currency - ISO 4217 fiat currency symbol (ie, “PHP”, “USD”, “SGD”).
    * rate - Equivalent amount in settlement currency of 1BTC. (This can be retrieved from the sell_quote API endpoint.) The system will respond with an error if this value is outdated.
    * payment_outlet - The outlet_id as provided by sell qoute api.
    * pay_with_wallet - Indicate whether this order should be paid using the user’s wallet. Currently, the only valid value is “BTC”.
    * other field - Payment outlets have different required fields such as, and are not limited to, first_name, bank_account_name, bank_account_number, etc. These are listed as required_fields when retrieving a sell quote. Please refer to the Payment Outlet Documentation and the Sell Quote Documentation for more information.

For more information about the sendmoney request body, please see the sendmoney
[documentation](http://coinsph.github.io/api/sell-api.html#creating-sell-orders).

#### Signature

```
$coins->sendMoney($params)
```

# Merchant API
Coins Merchant API is used by developers to generate a payment page. Our API
helps to make calls to our platform easier to make.

## Authentication
Merchant API uses a shared-secret digest for authentication to verify a checkout
payment request comes from a certain merchant and a "**digest**" parameter that
is **SHA1 hash** including the shared secret key.

**Digest Format:**  merchant_id:txnid:amount:currency:description:email_addr:secret_key
**merchant_id** & **secret_key** will be given after you **[register](https://coins.ph/merchants/signup)** for a merchant account.

To know more on becoming a merchant. You can visit our **[merchant](https://coins.ph/merchants)** page.

## Methods
### Payment Session
Generate coins checkout payment session.

Resource URL: **http://coins.ph/pay**

Resource verb: **GET**

GET Parameters

* **merchantid** - This is your merchant id when you **[register](https://coins.ph/merchants/signup)** for a merchant account.
* **txnid** - A unique identifier you generated to track your orders. This can be your own transaction ids.
* **amount** - transaction total amount. _NOTE: The amount is rounded to two decimals places._
* **ccy** - currency (ie, "PHP", "USD", "SGD")
* **description** - description shown to user on the checkout payment screen
* **email** - email address to send confirmation and use to identify user support issues.
* **digest** - hash to validate origin merchant. (see **[Authentication](merchant-api.html#authentication)**)
* **custom** - a pass-through parameter that is not secure

### Example
URL:
https://coins.ph/pay?merchantid=8888&txnid=1234&amount=20.00&ccy=PHP&description=CoinsPH&email=iggy@coins.ph&digest=a8761&custom=desktop

### Callbacks
Merchant are required to setup urls for redirect and callback.

1. Redirect URL - The url where users will be redirected once the payment made was confirmed. Usually a 'Thank You' page.
2. Callback URL - The url referred by coins on notifying about the status of the payment.

* **txnid** - A unique identifier you generated to track your orders. This can be your own transaction ids.
* **refno**- our transaction reference number
* **status** - Payment Status code
* **message** - an encrypted confirmation token.  This is the proof of payment token.
* **digest** - our encrypted digest (**Important:** You should verify this)

Callback Status:  **F** - Expired, **P** - Pending Payment, **S** - Success

For a callback, the digest we calculate is based on
**txnid:refno:amount:status:message:secret_key**

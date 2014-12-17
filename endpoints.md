# Endpoint Index

## [Send Money API](sell-api.html)

Coins Send Money API is used to generate Sell orders.

A unique Bitcoin Wallet address is generated for each order, and once payment is made the funds will be deposited into the specified bank account or other payment outlet.

<table>
    <th>Resource</th>
    <th>Method</th>
    <th>Description</th>

    <tr>
        <td><a href="https://github.com/coinsph/api/wiki/05-Send-Money-API#getting-quotes">/api/v2/sellquote</a></td>
        <td>GET</td>
        <td>Provides coins supported payment options including the processing fee depending on the amount of bitcoin to be sold.</td>
    </tr>

    <tr>
        <td><a href="https://github.com/coinsph/api/wiki/05-Send-Money-API#creating-sell-orders">/api/v2/sellorder</a></td>
        <td>POST</td>
        <td>Provides developers to create a sell order. The created sell order will be added on the user's transaction history.</td>
    </tr>

    <tr>
        <td><a href="https://github.com/coinsph/api/wiki/05-Send-Money-API#retrieving-existing-sell-orders">/api/v2/sellorder</a></td>
        <td>GET</td>
        <td>Provides developers a way to retrieve existing sell orders.</td>
    </tr>
</table>

## [Buy Order API](buy-api.html)

Coins Buy Order API is used to generate, view, and edit Buy Orders.

<table>
    <th>Resource</th>
    <th>Method</th>
    <th>Description</th>

    <tr>
        <td><a href="https://github.com/coinsph/api/wiki/06-Buy-API#getting-quotes">/api/v2/buyquote</a></td>
        <td>GET</td>
        <td>Provides coins supported payment methods including the processing fee depending on the amount of bitcoin to be bought.</td>
    </tr>

    <tr>
        <td><a href="https://github.com/coinsph/api/wiki/06-Buy-API#creating-buy-orders">/api/v2/buyorder</a></td>
        <td>POST</td>
        <td>Provides developers to create a buy order. The created buy order will be added on the user's transaction history.</td>
    </tr>

    <tr>
        <td><a href="https://github.com/coinsph/api/wiki/06-Buy-API#retrieving-existing-buy-orders">/api/v2/buyorder</a></td>
        <td>GET</td>
        <td>Provides developers a way to retrieve existing buy orders.</td>
    </tr>

    <tr>
        <td><a href="https://github.com/coinsph/api/wiki/06-Buy-API#cancelling-a-buy-order">/api/v2/buyorder</a></td>
        <td>DELETE</td>
        <td>Provides developers a way to cancel existing buy orders</td>
    </tr>

    <tr>
        <td><a href="https://github.com/coinsph/api/wiki/06-Buy-API#marking-a-buy-order-as-paid">/api/v2/buyorder</a></td>
        <td>PUT</td>
        <td>Provides developers a way to mark existing buy orders as paid.</td>
    </tr>
</table>

## [Wallet API](wallet-api.html)

Coins Wallet API is used to let third parties use Coins to store and send Bitcoins.

<table>
    <th>Resource</th>
    <th>Method</th>
    <th>Description</th>

    <tr>
        <td><a href="https://coins.ph/d/api/crypto-accounts/">/d/api/crypto-payments/</a></td>
        <td>GET</td>
        <td>Provides developers and users a way to retrieve their wallet details.</td>
    </tr>

    <tr>
        <td><a href="https://coins.ph/d/api/crypto-payments/">/d/api/crypto-payments</a></td>
        <td>POST</td>
        <td>Provides developers and users a way to transfer funds from their wallet</td>
    </tr>
</table>

## [Merchant API](merchant-api.html)

Coins Merchant API is used by developers to generate a payment page.

<table>
<th>Resource</th><th>Method</th><th>Description</th>
<tr>
<td><a href="https://github.com/coinsph/coins-api/wiki/Merchant-API#payment-session">/pay</a></td>
<td>GET</td>
<td>Generate coins checkout payment session.</td>
</tr>
</table>

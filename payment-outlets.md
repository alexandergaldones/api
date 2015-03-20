# Payment Outlets

Users can receive their fiat currency payouts via selected Payment Outlets.
Coins.ph supports multiple Payment Outlets, and we are regularly adding
additional payment outlets.

## Payment Outlet Types

Payment Outlets are grouped into several categories. These categories are
described in their respective sections.

### Bank

Users can opt to receive their payout through a bank account. These
establishments require the following details for a payout to be successful:

* Account Holder Name - Bank account name where the user wants the payout to be sent. This is not necessarily the user's own bank account name. The user is free to send the payout to someone else.
* Bank Account Number - The bank account number assigned to the provided bank account name.

#### API Required Fields

For API calls, the required fields are translated into the following
identifiers:

* `bank_account_name` - Same as Account Holder Name as described above. This accepts unicode characters of an arbitrary length.
* `bank_account_number` - Same as Bank Account Number as described above. This accepts unicode characters of an arbitrary length.

Sell Orders that have a selected Payment Outlet option of this category should
include these fields in the request payload, like so:

```json
{
    "currency": "PHP",
    "btc_amount": 0.5,
    "payment_outlet": "bpi",
    "bank_account_name": "John Smith",
    "bank_account_number": 0123456789
}
```

#### Amount Limits

Technically, Payment Outlets of this category do not have a minimum and a
maximum amount limit per transaction. However, usual bank policies still apply
for higher amounts, and the recipient might need to ask the bank for reservation
beforehand. It is the responsibility of the user/recipient to ask the bank for
reservation.

#### Fees

Currently, establishments of this category do not have processing fees.

### Cash Pickup

Users can opt to receive their payout by picking it up on an establishment that
allows cash pickup. These establishments require the following details for a
payout to be successful:

* Full Name - The recipient's full name. This is not necessarily the same user who initiated the payout. The user is free to send the payout to a different recipient.
* Full Address - The recipient's full address.
* Phone Number - The recipient's phone number.

Additionally, these establishments usually require the recipient to present at
least one valid ID (preferrably government issued). The information provided by
the user should exactly match the details in the recipient's ID.

#### API Required Fields

For API calls, the required fields are translated into the following identifiers:

* `full_name` - Same as Full Name described above. This accepts unicode characters of an arbitrary length.
* `full_address` - Same as Full Address described above. This accepts unicode characters of an arbitrary length.
* `phone_number_recipient` - Same as Phone Number described above. This accepts unicode characters of an arbitrary length.

Sell Orders that have a selected Payment Outlet option of this category should
include these fields in the request payload, like so:

```json
{
    "currency": "PHP",
    "btc_amount": 0.5,
    "payment_outlet": "mlhuillier_kwartapadala",
    "full_name": "John Smith",
    "full_address": "123, The Long Walk Street, Fast Lane City, Philippines, 12345",
    "phone_number_recipient": 0123456789
}
```

#### Amount Limits

Certain establishments of this category only accepts payouts within a certain
range. These values are as of Oct. 21, 2014:

<table>
    <thead>
        <th>Payment Outlet</th>
        <th>Minimum</th>
        <th>Maximum</th>
    </thead>
    <tbody>
        <tr>
            <td>Cebuana Lhuillier Pera Padala</td>
            <td>PHP 0</td>
            <td>PHP 500,000</td>
        </tr>

        <tr>
            <td>M Lhuillier Kwarta Padala</td>
            <td>PHP 0</td>
            <td>PHP 500,000</td>
        </tr>

        <tr>
            <td>LBC Peso Padala</td>
            <td>PHP 1</td>
            <td>PHP 100,000</td>
        </tr>

        <tr>
            <td>Palawan Express Pera Padala</td>
            <td>PHP 0</td>
            <td>PHP 50,000</td>
        </tr>
    </tbody>
</table>

#### Fees

Establishments of this category usually have processing fees based on specific
ranges (ie. PHP 0 - PHP 1000 and so on). These fees vary per establishment and
are usually already provided in the
[Sell Quote API](sell-api.html#getting-quotes). For more information about
particular establishment fees, please refer to their websites.

### Mobile money

Users can opt to receive their payout through a mobile number that supports
mobile money (such as GCash and Smart Money). These payout options only require
the recipient's phone number. The user can opt to send the payout to a different user.

* GCash/Smart Money card number - The recipient's phone number or cash card number. This is not necessarily the same user who initiated the payout. The user is free to send the payout to a different recipient.
* Account Holder Name - The recipient's account holder name. This is not necessarily the name of the user who initiated the payout.

Please take note that Smart Money Card might be separated into its own category in the near future.

#### API Required Fields

For API calls, the required fields are translated into the following identifiers:

* `phone_number` - Same as GCash/Smart Money Card Number described above. This accepts unicode characters of an arbitrary length.
* `account_holder_name` - Same as Account Holder Name described above. This accepts unicode characters of an arbitrary length.

Sell Orders that have a selected Payment Outlet option of this category should include these fields in the request payload, like so:

```json
{
    "currency": "PHP",
    "btc_amount": 0.5,
    "payment_outlet": "gcash",
    "phone_number": 0123456789,
    "account_holder_name": "John Smith"
}
```

#### Amount Limits

Certain services of this category only accepts payouts within a certain range.
These values are as of Oct. 21, 2014:

<table>
    <thead>
        <th>Payment Outlet</th>
        <th>Minimum</th>
        <th>Maximum</th>
    </thead>
    <tbody>
        <tr>
            <td>Globe GCash</td>
            <td>PHP 10</td>
            <td>PHP 40,000</td>
        </tr>

        <tr>
            <td>Smart Money Card</td>
            <td>PHP 0</td>
            <td>No maximum amount</td>
        </tr>
    </tbody>
</table>

#### Fees

Smart Money Card doesn't have any transaction fees. Globe GCash, on the other
hand, have range specific transaction fees. These fees are already provided for
you by the [Sell Quote API](sell-api.html#getting-quotes). Please refer to the
Globe GCash website for more information about their transaction fees.

### Door to Door Delivery

Users can opt to receive their payout through delivery. These services require
the user to provide the following details:

* Full Name - The recipient's full name. This is not necessarily the same user who initiated the payout. The user is free to send the payout to a different recipient.
* Full Address -  The recipient's full address. This is not necessarily the address of the same user who initiated the payout. The user is free to send the payout to a different recipient.
* Phone Number - The recipient's phone number.

Additionally, the recipient might be required to present at least one valid ID
(preferrably government issued) upon delivery. The details provided in the sell
order should match the exact details in the recipient's ID.

#### API Required Fields

For API calls, the required fields are translated into the following identifiers:

* `full_name` - Same as Full Name described above. This accepts unicode characters of an arbitrary length.
* `full_address` - Same as Full Address described above. This accepts unicode characters of an arbitrary length.
* `phone_number_recipient` - Same as Phone Number described above. This accepts unicode characters of an arbitrary length.

Sell Orders that have a selected Payment Outlet option of this category should
include these fields in the request payload, like so:

```json
{
    "currency": "PHP",
    "btc_amount": 0.5,
    "payment_outlet": "2go_quikcash",
    "full_name": "John Smith",
    "full_address": "123, The Long Walk Street, Fast Lane City, Philippines, 12345"
}
```

#### Amount Limits

Services of this category only accepts payouts within a certain range. These
values are as of Oct. 21, 2014:

<table>
    <thead>
        <th>Payment Outlet</th>
        <th>Minimum</th>
        <th>Maximum</th>
    </thead>
    <tbody>
        <tr>
            <td>2GO Quikcash</td>
            <td>PHP 500</td>
            <td>PHP 5,000</td>
        </tr>

        <tr>
            <td>LBC Pesopak</td>
            <td>PHP 100</td>
            <td>PHP 50,000</td>
        </tr>
    </tbody>
</table>

#### Fees

2Go Quikcash has a fixed transaction fee of PHP 120. LBC Pesopak, on the other
hand, have range specific transaction fees. These fees are already provided for
you by the [Sell Quote API](sell-api.html#getting-quotes). Please refer to the
LBC Pesopak website for more information about their transaction fees.

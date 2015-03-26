# Payout Outlets

Payout outlets are establishments where users can cash out their Bitcoins
through either coins.ph, or coins.co.th. This API allows users to get
payout outlet data, which includes their categories, and a table of fees.

## Getting Payout Outlets

This endpoint returns payout outlets, with their types. A payout outlet has the
following properties:

* **id** - A unique identifier for the payout outlet
* **payment_outlet_type** - The outlet's category. These are usually establishments where the user can cash out their Bitcoins.
* **name** - The outlet's name in human readable form.
* **region** - An [ISO 3166-1 Alpha 2](http://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country code of the region where the outlet is located.
* **help_text** - Optional text that further describes the outlet. May be null.
* **help_link** - Optional help article that further describes the outlet. May be null.
* **instructions** - Instructions on how the user should process payment through the outlet.

### HTTP Method

**GET**

### Endpoint

https://coins.ph/d/api/payout-outlets/

### Example Response

```json
{
    "meta": {
        "total_count": 74,
        "next_page": 2,
        "previous_page": null
    },
    "payout-outlets": [
        {
            "id": "egivecash",
            "payment_outlet_type": {
                "id": "atm_pickup",
                "name": "ATM Pickup",
                "fields": [
                    {
                        "payment_outlet_type_field_id": "recipient_full_name",
                        "name": "Recipient Full Name",
                        "help_text": "Recipient Full Name",
                        "help_link": ""
                    },
                    {
                        "payment_outlet_type_field_id": "recipient_mobile",
                        "name": "Recipient Mobile Phone",
                        "help_text": "Recipient Mobile Phone Number (e.g. 09178147839)",
                        "help_link": ""
                    }
                ],
                "fee_structure_description": null,
                "payout_duration_description": null
            },
            "name": "Security Bank eGiveCash",
            "region": "PH",
            "help_text": "",
            "help_link": "",
            "instructions": "Withdraw from any ATM"
        },
        {
            "id": "gcash",
            "payment_outlet_type": {
                "id": "phone_deposit",
                "name": "Mobile Money",
                "fields": [
                    {
                        "payment_outlet_type_field_id": "phone_number",
                        "name": "Phone Number",
                        "help_text": "Phone Number",
                        "help_link": ""
                    }
                ],
                "fee_structure_description": null,
                "payout_duration_description": null
            },
            "name": "Globe Cash",
            "region": "PH",
            "help_text": "",
            "help_link": "",
            "instructions": "Transfer from your Phone"
        }
    ]
}
```

## Payout Outlet Categories

Payout outlets are grouped into categories. Categories determine the required
fields that payout outlets accept. The data gathered from these fields are
used to process the payout. Payout outlet categories have the following
properties:

* **id** - Unique identifier for the payout outlet category.
* **name** - The category's name in human readable form.
* **fields** - A collection of fields that payment outlets of this category requires.
* **fee_structure_description** - Describes how fees in this category are structured in general.
* **payout_duration_description** - Describes how long it usually takes to process payouts to outlets of this category.

A field is usually just an input field that accepts data. To see an example
of how they are used, see the `POST` example on the (Sell Order API)[sell-api.html].

### HTTP Method

**GET**

### Endpoint

https://coins.ph/d/api/payout-outlet-categories/

### Example Response

```json
{
    "payout-outlet-categories": [
        {
            "id": "mobile_load",
            "name": "Mobile Load",
            "fields": [
                {
                    "payment_outlet_type_field_id": "phone_number",
                    "name": "Phone Number",
                    "help_text": "Phone Number",
                    "help_link": ""
                }
            ],
            "fee_structure_description": null,
            "payout_duration_description": null
        },
        {
            "id": "atm_pickup",
            "name": "ATM Pickup",
            "fields": [
                {
                    "payment_outlet_type_field_id": "recipient_full_name",
                    "name": "Recipient Full Name",
                    "help_text": "Recipient Full Name",
                    "help_link": ""
                },
                {
                    "payment_outlet_type_field_id": "recipient_mobile",
                    "name": "Recipient Mobile Phone",
                    "help_text": "Recipient Mobile Phone Number (e.g. 09171234567)",
                    "help_link": ""
                }
            ],
            "fee_structure_description": null,
            "payout_duration_description": null
        }
    ],
    "meta": {
        "total_count": 13,
        "next_page": 2,
        "previous_page": null
    }
}
```

## Payout Outlet Fees

Fees may apply on different payout outlets. If a payout outlet does have fees,
it's either a fixed fee, or it may vary depending on the amount of transaction.
Fees have the following properties:

* **payment_outlet** - The payment outlet that owns the fee.
* **currency** - Currency symbol of the fee.
* **from_amount** - Starting amount where the fee applies.
* **until_amount** - Highest amount where the fee applies.
* **fee_amount** - A fixed fee amount for the range given by `from_amount` and `until_amount`.
* **fee_percent** - A percentage of the transaction amount as a fee.

The total fees is calculated as `transaction_amount * fee_percent + fee_amount`
for a certain range given by `from_amount` and `until_amount`.

### HTTP Method

**GET**

### Endpoint

https://coins.ph/d/api/payout-outlet-fees/

### Example Response

```json
{
    "meta": {
        "total_count": 76,
        "next_page": 2,
        "previous_page": null
    },
    "payout-outlet-fees": [
        {
            "payment_outlet": "bdo",
            "currency": "PHP",
            "from_amount": "0",
            "until_amount": "100000000",
            "fee_amount": "0",
            "fee_percent": "0.01"
        },
        {
            "payment_outlet": "bdo",
            "currency": "PHP",
            "from_amount": "1001",
            "until_amount": "100000000000.00",
            "fee_amount": "10.00",
            "fee_percent": "0.00"
        }
    ]
}
```
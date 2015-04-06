# Payout Outlets

**Unstable**
**We are currently making improvements on this new endpoint. Use at your own risk.**

Payout outlets are establishments where users can cash out their Bitcoins
through either coins.ph, or coins.co.th. This API allows users to get
payout outlet data, which includes their categories, and a table of fees.

## Getting Payout Outlets

This endpoint returns payout outlets, with their types. A payout outlet has the
following properties:

* **id** - A unique identifier for the payout outlet
* **outlet_category** - The outlet's category id. These are usually establishments where the user can cash out their Bitcoins.
* **name** - The outlet's name in human readable form.
* **region** - An [ISO 3166-1 Alpha 2](http://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country code of the region where the outlet is located.
* **help_text** - Optional text that further describes the outlet. May be null.
* **help_link** - Optional help article that further describes the outlet. May be null.
* **instructions** - Instructions on how the user should process payment through the outlet.

### HTTP Method

**GET**

### Endpoint

https://coins.ph/d/api/payout-outlets/

### Parameters

* **payment_outlet_type** - A payment outlet type ID used to filter results.
* **name** - Filter results by the given name.
* **region** - Filter results based on the given region.
* **is_enabled** - If `True`, results will not include disabled outlets.
* **ui_view** - Filter results based on the view the outlet usually appears.

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
            "outlet_category": "atm_pickup",
            "name": "Security Bank eGiveCash",
            "region": "PH",
            "help_text": "",
            "help_link": "",
            "instructions": "Withdraw from any ATM"
        },
        {
            "id": "gcash",
            "outlet_category": "phone_deposit",
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
* **outlets** - An array of outlet IDs that belong to the category.

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
                    "id": "phone_number",
                    "name": "Phone Number",
                    "help_text": "Phone Number",
                    "help_link": ""
                }
            ],
            "outlets": [
                "load_globe",
                "load_smart"
            ],
            "fee_structure_description": "PHP 10 for every PHP 1000",
            "payout_duration_description": "Same day payout"
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
            "outlets": [
                "egivecash"
            ],
            "fee_structure_description": "PHP 10 for every PHP 1000",
            "payout_duration_description": "Same day payout"
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
            "outlet": "bdo",
            "currency": "PHP",
            "from_amount": "0",
            "until_amount": "1000",
            "fee_amount": "10",
            "fee_percent": "0.01"
        },
        {
            "outlet": "bdo",
            "currency": "PHP",
            "from_amount": "1001",
            "until_amount": "2000",
            "fee_amount": "20",
            "fee_percent": "0.00"
        }
    ]
}
```
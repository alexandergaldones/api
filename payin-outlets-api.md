# Payin Outlets

**Unstable**
**We are currently making improvements on this new endpoint. Use at your own risk.**

Payin outlets are establishments where users can send cash to convert to
Bitcoins. Payment received from these outlets will be processed by coins.ph,
or coins.co.th, depending on the outlet's region. This API allows users to get
payin outlet data, which includes their categories, and a table of fees.

## Getting Payin Outlets

This endpoint returns payin outlets, with their types. A payin outlet has the
following properties:

* **id** - A unique identifier for the payin outlet
* **outlet_category** - The outlet's category id. These are usually establishments where coins accepts fiat.
* **name** - The outlet's name in human readable form.
* **region** - An [ISO 3166-1 Alpha 2](http://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country code of the region where the outlet is located.
* **help_text** - Optional text that further describes the outlet. May be null.
* **help_link** - Optional help article that further describes the outlet. May be null.
* **instructions** - Instructions on how the user should process payment through the outlet.

### HTTP Method

**GET**

### Endpoint

https://coins.ph/d/api/payin-outlets/

### Parameters

* **payment_outlet_type** - A payment outlet type ID used to filter results.
* **name** - Filter results by the given name.
* **region** - Filter results based on the given region.
* **is_enabled** - If `True`, results will not include disabled outlets.
* **ui_view** - Filter results based on the view the outlet usually appears.

### Example Response

```json
{
    "payin-outlets": [
        {
            "id": "citibank_deposit",
            "outlet_category": "bank_deposit",
            "name": "Citibank",
            "region": "PH",
            "help_text": "",
            "help_link": "",
            "instructions": "Deposit to account 1234"
        },
        {
            "id": "bdo_deposit",
            "payment_outlet_type": {
                "id": "bank_deposit",
                "name": "Bank Deposit",
                "fields": [],
                "fee_structure_description": null,
                "payout_duration_description": null
            },
            "name": "BDO Bank",
            "region": "PH",
            "help_text": "",
            "help_link": "",
            "instructions": "Deposit to account 5169"
        }
    ],
    "meta": {
        "total_count": 6,
        "next_page": null,
        "previous_page": null
    }
}
```

## Payin Outlet Categories

Payin outlets are grouped into categories. Unlike
[Payout Outlet Categories](payout-outlets-api.md), payin outlet categories
usually don't have required fields. Payin outlet categories have the following
properties:

* **id** - Unique identifier for the payout outlet category.
* **name** - The category's name in human readable form.
* **fields** - A collection of fields that payment outlets of this category requires.
* **fee_info** - Describes how fees in this category are structured in general.
* **payout_duration** - Describes how long it usually takes to process payouts to outlets of this category.
* **outlets** - An array of outlet IDs that belong to the category.
* **outlet_names_subset** - A subset of outlet names that can be used as examples for the category.

### HTTP Method

**GET**

### Endpoint

https://coins.ph/d/api/payin-outlet-categories/

### Parameters

* **region** - Filter to only the categories with outlets based on the given region.
* **ui_view** - Filter to only the categories with outlets that belong to the given `ui_view`.

### Example Response

```json
{
    "payin-outlet-categories": [
        {
            "id": "bank_deposit",
            "name": "Bank Deposit",
            "fields": [],
            "outlets": [
                "bpi",
                "bdo"
            ],
            "fee_structure_description": "PHP 10 for every PHP 1000",
            "payout_duration_description": "Same day payout",
            "outlet_names_subset": [
                "BPI",
                "BDO"
            ]
        },
        {
            "id": "validated_deposit",
            "name": "Validated Bank Deposit",
            "fields": [],
            "outlets": [
                "bpi_family",
                "citibank"
            ],
            "fee_structure_description": "PHP 10 for every PHP 1000",
            "payout_duration_description": "Same day payout",
            "outlet_names_subset": [
                "BPI Family",
                "CitiBank"
            ]
        }
    ],
    "meta": {
        "total_count": 3,
        "next_page": null,
        "previous_page": null
    }
}
```

## Payin Outlet Fees

Fees may apply on different payin outlets. If a payin outlet does have fees,
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

https://coins.ph/d/api/payin-outlet-fees/

### Example Response

```json
{
    "payin-outlet-fees": [
        {
            "payment_outlet": "bdo_deposit",
            "currency": "PHP",
            "from_amount": "0",
            "until_amount": "1000",
            "fee_amount": "10",
            "fee_percent": "0.01"
        },
        {
            "payment_outlet": "bpi_deposit",
            "currency": "PHP",
            "from_amount": "1001",
            "until_amount": "2000",
            "fee_amount": "20",
            "fee_percent": "0"
        }
    ],
    "meta": {
        "total_count": 6,
        "next_page": null,
        "previous_page": null
    }
}
```

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
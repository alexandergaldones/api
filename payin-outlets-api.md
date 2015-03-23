# Payin Outlets

Payin outlets are establishments where users can send cash to convert to
Bitcoins. Payment received from these outlets will be processed by coins.ph,
or coins.co.th, depending on the outlet's region. This API allows users to get
payin outlet data, which includes their categories, and a table of fees.

## Getting Payin Outlets

### HTTP Method

**GET**

### Endpoint

https://coins.ph/d/api/payin-outlets/

### Example Response

```json
{
    "payin-outlets": [
        {
            "id": "citibank_deposit",
            "payment_outlet_type": {
                "id": "bank_deposit",
                "name": "Bank Deposit",
                "fields": [],
                "fee_structure_description": null,
                "payout_duration_description": null
            },
            "name": "Citibank",
            "region": "PH",
            "help_text": "",
            "help_link": "",
            "instructions": "Pay the money!"
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
            "instructions": "Pay the money!"
        }
    ],
    "meta": {
        "total_count": 6,
        "next_page": null,
        "previous_page": null
    }
}
```

## Payout Outlet Categories

### HTTP Method

**GET**

### Endpoint

https://coins.ph/d/api/payin-outlet-categories/

### Example Response

```json
{
    "payin-outlet-categories": [
        {
            "id": "bank_deposit",
            "name": "Bank Deposit",
            "fields": [],
            "fee_structure_description": null,
            "payout_duration_description": null
        },
        {
            "id": "validated_deposit",
            "name": "Validated Bank Deposit",
            "fields": [],
            "fee_structure_description": null,
            "payout_duration_description": null
        }
    ],
    "meta": {
        "total_count": 3,
        "next_page": null,
        "previous_page": null
    }
}
```

## Payout Outlet Fees

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
            "until_amount": "100000000",
            "fee_amount": "0",
            "fee_percent": "0.01"
        },
        {
            "payment_outlet": "bpi_deposit",
            "currency": "PHP",
            "from_amount": "0",
            "until_amount": "100000",
            "fee_amount": "100",
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

# Quote API

Quotes can be directly accessed from this API, in addition to the `buyquote`
and `sellorder` endpoints. This API is the preferred way to access
multi-currency quotes, such as PHP-BTC or THB-BTC.

https://quote.coins.ph/v1/

The quotes API is public. It requires no authentication.

## Formats

Dates are in ISO 8601 format.

## Pagination

By default API returns `10` objects per page. It can be changed by
`?per_page=20` query parameter. Its maximum value is `100`.

## Resources

### Markets

Represents a quote ticker for several supported markets. Currently supports
quoting for PHP, THB, HKD, and TWD to BTC.

#### Endpoint

https://quote.coins.ph/v1/markets/

#### HTTP Method

**GET**

#### Parameters:

* **symbol** - Market symbol, such as BTC-PHP and BTC-THB.
* **currency** - Fiat currency symbol.
* **product** - Product of converting fiat.
* **bid** - Rate when converting from fiat to product.
* **ask** - Rate when converting from product to fiat.

#### Example Requests

URL: https://quote.coins.ph/v1/markets/
URL: https://quote.coins.ph/v1/markets/BTC-PHP/

#### Example Responses

```json
{
  "meta": {"total_count":5,"next_page":null,"previous_page":null},
  "markets":[
    {
      "symbol":"BTC-CLP",
      "currency":"CLP",
      "product":"BTC",
      "bid":"1000000.00000000",
      "ask":"1000000.00000000"
    }, {
      "symbol":"BTC-HKD",
      "currency":"HKD",
      "product":"BTC",
      "bid":"1752.96293766",
      "ask":"1770.31900635"
    }, {
      "symbol":"BTC-PHP",
      "currency":"PHP",
      "product":"BTC",
      "bid":"10052.88670407",
      "ask":"10151.44441686"
    }, {
      "symbol":"BTC-THB",
      "currency":"THB",
      "product":"BTC",
      "bid":"7219.55778736",
      "ask":"7365.40743964"
    }, {
      "symbol":"BTC-TWD",
      "currency":"TWD",
      "product":"BTC",
      "bid":"7032.31067175",
      "ask":"7102.63377847"
    }
  ]
}
```

```json
{
  "market":{
    "symbol":"BTC-PHP",
    "currency":"PHP",
    "product":"BTC",
    "bid":"9911.31691110",
    "ask":"10008.48668473"
  }
}
```
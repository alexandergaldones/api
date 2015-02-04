# Quote API

Quotes can be directly accessed from this API, in addition to the `buyquote`
and `sellorder` endpoints. This API is the preferred way to access
multi-currency quotes, such as BTC-PHP or BTC-THB.

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
quoting for BTC to PHP, THB, HKD, or TWD.

#### Endpoint

https://quote.coins.ph/v1/markets

#### HTTP Method

**GET**

#### Fields

* **symbol** - Market symbol, such as BTC-PHP and BTC-THB.
* **currency** - Fiat currency symbol. This is the currency the user will use to pay for the product.
* **product** - Product of converting fiat. This is the thing that the user wants to obtain.
* **bid** - The amount of currency that the user would get when a unit of product is sold. For instance, the user would get 9800 PHP when they sell 1 BTC. Take note that the rate fluctuates.
* **ask** - The amount of currency to buy a unit of product. For instance, it would cost 10000 PHP to buy 1 BTC. Take note that the rate fluctuates.

#### Example Responses

URL: https://quote.coins.ph/v1/markets

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

URL: https://quote.coins.ph/v1/markets/BTC-PHP

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
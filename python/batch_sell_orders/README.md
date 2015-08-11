# Batch create sell orders

This is a command line utility that allows posting sell orders by batch.
The expected input file is a csv file, which contains a heading row followed
by the sell orders to post.

## Requirements

* python2.7
* requests

python2.7 is expected to be installed in the system. To install the other
requirements, run `pip install requirements.txt` while inside this directory.
Feel free to decide whether to use a virtual environment or not.

## Usage

Create a `config.json` file in the same directory as the script. The file should
contain your api key and api secret, like so:

```
{
    "api_key": "your_api_key",
    "api_secret": "your_api_secret"
}
```

Invoke the command as `python batch_sell_orders.py file_name.csv`, where
`file_name.csv` is the input file to be processed.

```
$ python batch_sell_orders.py

usage: batch_sell_orders.py [-h] [--config CONFIG] filename
```

## CSV file format

The csv file should have the first line as a header that describes the fields
contained in each column:

```
currency,amount,payment_outlet,pay_with_wallet,bank_account_name,bank_account_number
```

With this header, the rest of the contents should look like the following:

```
PHP,100,bpi,PBTC,John Doe,1234567890
PHP,150,bdo,PBTC,Alice Wonderland,0987654321
```

This will form request bodies as:

```
{
    "currency": "PHP",
    "amount": "100",
    "payment_outlet": "bpi",
    "pay_with_wallet": "PBTC",
    "bank_account_name": "John Doe",
    "bank_account_number": "1234567890"
}
```

The order of the headers do not matter, as long as the contents of it's representative
columns are correct. For example, consider the following header:


```
code,amount,currency,payment_outlet,bank_account_name,pay_with_wallet,bank_account_number
```

The contents should represent the column they belong to:

```
1234,100,PHP,bpi,John Doe,PBTC,1234567890
```

To form the correct request body:

```
{
    "code": "1234",
    "amount": "100",
    "currency": "PHP",
    "payment_outlet": "bpi",
    "bank_account_name": "John Doe",
    "pay_with_wallet": "PBTC",
    "bank_account_number": "1234567890"
}
```

## API docs

The sell order api is documented [here](http://api.coins.asia/docs/sellorder)

## Disclaimer

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.

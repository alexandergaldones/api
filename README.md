API Examples
==============

Examples for how to use the Coins.ph API are provided in this repository. Additionally, API docs can be found at [the documentation page](http://coinsph.github.io/api). For issues, feature requests, and suggestions, please file an [issue](https://github.com/coinsph/api/issues).

## Easily Send Bitcoin from your Coins.ph Wallet

First Set your Coins Key and Secret you can get these at the
[API Dashboard](https://coins.ph/user/api).

Install requirements and export your keys
```bash
pip install -r requirements.txt
 export COINS_API_KEY=[your API key]
 export COINS_API_SECRET=[your secret]
```

To send funds using the command line utility just run out of the /python directory:
```bash
python sendbitcoin.py coffeefund@coins.ph 0.001
```
You can send to a bitcoin address, email address or even a phone number.

## Contributing

Please feel free to contribute examples of how to use the API for different languages. If a language is not yet in the root project directory, please create a directory and name it with the language that the examples in that directory use. For instance:

```
.gitignore
README.md
python/
  hmac.py
  oauth.py
java/
  hmac.java
  oauth.java
... and so on
```

For each example, please include a link (as a comment/docstring) to the documentation page that it implements.

## License

API Examples are MIT licensed.

The MIT License __(MIT)__

Copyright © 2014 coins.ph

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files __(the "Software")__, to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.

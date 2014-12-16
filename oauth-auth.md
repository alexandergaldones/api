# OAuth2

Coins API can use OAuth2 to authenticate requests as legitimate and for authorization. Popular social networks as well as other web heavyweights use OAuth2. If you do not wish to use your API secret to execute requests in behalf of a user, we recommend using this method.

## Enabling OAuth2

Using [Coins API Dashboard](https://coins.ph/user/api) (_login required_) you can get the necessary OAuth2 tokens to configure your application and begin using our API.

> If you're making a mobile or browser-based app, make sure to never place the client secret in the hands of your user.

> You can (and really, should ASAP) regenerate a new secret if the old one leaks out.

## Scopes

OAuth2 requires the use of scopes. Each scope represents a feature in the API. In order to use a feature, the scope associated with that feature should be enabled in your application. Please make sure to select at least one scope, as applications without any scope can only interact with our quotes API.

These are the currently available scopes:

* **buyorder** - Allows an application to use the Buy Order API
* **sellorder** - Allows an application to use the Sell Order and Send Money APIs
* **history** - Allows an application to use the Transaction History APIs, which are also under Buy Order and Sell Order

You can always reauthorize with the user if you need a larger scope, so please prefer using low-scope tokens as much as possible.

## Application Authorization Flow

OAuth2 requires the developer to ask for user permissions before the application can make API calls. This is only done once, and then every time the token needs to be refreshed.

Direct your users to the url `http://coins.ph/user/api/authorize` with the following query parameters:

* **client_id** - Select `show` on your chosen application's [API Access](https://coins.ph/user/api) dashboard. This is the API Key as displayed on the dialog.
* **response_type** - Can either be `token` or `code`. `token` is used for client-side flows, while `code` is used for server-side flows.
* **scope** (optional) - Can be used to customize the scope of the token to be created. When not provided, the token will default to the scopes provided in the [API Access](https://coins.ph/user/api) page. Multiple scopes can be provided by separating each scope with a `+`, like so: `buyorder+sellorder+history`.
* **redirect_uri** (optional) - Can be used to redirect the user to a different page than the one provided in the [API Access](https://coins.ph/user/api) page.

A common example of a url for requesting user permission is as follows:

```
https://coins.ph/user/api/authorize?client_id=yourclientid&response_type=token
```

Once a user approves your application, the user will be redirected to the `redirect_uri` you provided. The `redirect_uri` will contain the following parameters appended to the url:

* **access_token** - The token to be attached to each request to prove authentication.
* **token_type** - The type of token returned.
* **state** - The scopes of the provided token.

The parameters are not appended to the url as GET parameters (ie. first parameter prefixed with a `?`). Instead, the first parameter is prefixed with a `#`. This prevents our servers from logging the access token. It also means that you must use custom application logic to retrieve the access token.

### Client Side Flow

This flow is commonly used for applications that store the token in the client. Follow the steps described in [Application Authorization Flow](oauth-auth.html#application-authorization-flow). Once you retrieve the `access_token`, it can be used by adding this HTTP header for every API call:

```
Authorization: Bearer youraccesstoken
```

#### Client Side Flow Example

Example of a common client-side flow:

1. Direct the user to https://coins.ph/user/api/authorize?client_id=yourclientid&response_type=token
2. User selects "Allow"
3. User is redirected to http://yourredirecturl.com/#access_token=someaccesstoken&token_type=Bearer&state=&scope=buyorder+sellorder+history
4. Client application retrieves the token from the url
5. Client application can now initiate an API call, with the header `Authorization: Bearer someaccesstoken` for each API call.

### Server Side Flow

This flow is commonly used for applications that can't store the token in the client. The developer's application server is responsible for keeping track of its client's tokens. To use this flow, follow the steps described in Application Authorization Flow, with the `response_type` parameter with the value `code`. The user will then be redirected to the `redirect_uri` you have provided, but instead of having an `access_token` parameter, it will have `code` attached.

Additionally, The `code` is used by the application server to retrieve an access token for a user. The `code` can only be used once per user. The application server can retrieve an `access_token` for the user by doing a POST request to the `/user/oathtoken` endpoint with the following parameters:

* **client_id** - Select `show` on your chosen application's API Access dashboard. This is the API Key as displayed on the dialog.
* **client_secret** - Select `show` on your chosen application's API Access dashboard. This is Secret as displayed on the dialog.
* **code** - The `code` retrieved from the `redirect_uri`
* **grant_type** - `authorization_code` is used to retrieve an access token.
* **redirect_uri** - The `redirect_uri` as defined in your chosen application's API Access dashboard.

#### Access Token

Upon completing the request, your application server should receive a json response with the key `access_token`, which could then be used for subsequent API calls by including it in an Authorization HTTP header:

```
Authorization: Bearer useraccesstoken
```

#### Refresh Token

In addition to the `access_token` being returned from the `/user/oauthtoken` endpoint, the json response also contains a `refresh_token` which can be used for getting a new `access_token`. This is usually used for getting a new `access_token` once it expires, or for invalidating the current `access_token` in exchange for a new one.

Using the `refresh_token` is almost the same as using `code` to obtain an `access_token`. Issue a POST request to the same endpoint, `/user/oauthtoken`, with the following parameters:

* **client_id** - Select `show` on your chosen application's API Access dashboard. This is the API Key as displayed on the dialog.
* **client_secret** - Select `show` on your chosen application's API Access dashboard. This is Secret as displayed on the dialog.
* **refresh_token** - The `refresh_token` retrieved from the previous POST request to `/user/oauthtoken`.
* **grant_type** - `refresh_token` is used to use the `refresh_token` to retrieve a new access token.
* **redirect_uri** - The `redirect_uri` as defined in your chosen application's API Access dashboard.

#### Server Side Flow Example

Example of a common server-side flow:

1. Direct the user to https://coins.ph/user/api/authorize?client_id=yourclientid&response_type=code&grant_type=authorization_code
2. User selects "Allow"
3. User is redirected to http://yourredirecturl.com/?code=somecode
4. Client application retrieves the token from the url and sends it to the application server.
5. Application server initiates a POST request to https://coins.ph/user/oauthtoken with an HTTP Content-Type header of `application/x-www-form-urlencoded`
6. The oauthtoken endopint responds with a json that contains the key `access_token`
7. Application server stores this token in behalf of the user.
8. The application server can now initiate API calls in behalf of the user, with the header `Authorization: Bearer useraccesstoken` for each API call.

## Initiating API calls with OAuth2

Once the user or your application server has the `access_token` an API call can be made with the following required HTTP headers:

* Authorization - Authorization type followed by the access token ie. `Bearer token`
* nonce - A number that can only be used once per user. See [Authentication](auth.html#use-a-nonce)

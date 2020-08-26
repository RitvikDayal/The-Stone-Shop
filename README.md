# The Stone Shop

<style>
.grid-container {
  display: grid;
  grid-template-columns: 1fr 1fr 1fr;
  grid-template-rows: 1fr 1fr;
  gap: 1px 1px;
  grid-template-areas: "home shop cart" "side-cart checkout .";
}

.home { grid-area: home; }

.shop { grid-area: shop; }

.cart { grid-area: cart; }

.side-cart { grid-area: side-cart; }

.checkout { grid-area: checkout; }
</style>

<p style="text-align:center; font-size:16px;">
<b>A Django Ecommerce web app to sell stone products.</b>
</p>

<img src="screenshots/home.png">

>The stone shop template comes with the following funtionalities:-
- Add Products with details such as image, name, price tags etc.

- A visitor can shop without creating an account but will need one to checkout.

- The shop currently support singler seller.

- Paypal Integration.

- Password Reset Functionality.

- Customer Registration.

> Used Cookies for Anonymous user interaction functionality.

Credits:- 
Images used are copyright freee, royalty free images from pexels.com and manyt other sources. The theme used was developed by TheWayShop.

## Enjoy Some ScreenShots
---
<div class="grid-container">

<div class="home">![](screenshots/home-1.png)</div>

<div class="shop">![](screenshots/shop.png)</div>

<div class="cart">![](screenshots/cart.png)</div>

<div class="side-cart">![](screenshots/side-cart.png)</div>

<div class="checkout">![](screenshots/checkout.png)</div>

</div>

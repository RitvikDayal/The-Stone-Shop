function getCookie(name){
    // getting all the cookies from
    var cookieArr = document.cookie.split(";");

    // looping through all cookies to find ours
    for(var i=0; i < cookieArr.length; i++){
        var cookiePair = cookieArr[i].split("=");

        // removing starting whitepace and comparing names
        if(name == cookiePair[0].trim()){
            // Decoding cookie value and return
            return decodeURIComponent(cookiePair[1]);
        }
    }

    return null; //if cookie not found
}

var cart = JSON.parse(getCookie('stone_shop_user'))

if (cart == undefined) {
    cart = {}
    console.log('Cart was created!')
    document.cookie = 'cart='+ JSON.stringify(cart)+";domain=;path=/"
}

console.log('Cart: ',cart);


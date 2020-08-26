var shipping = '{{order.shipping}}'

var total = '{{order.get_cart_total|floatformat:2}}'

var form = document.getElementById('checkout-address')

form.addEventListener('submit', function(e){
    e.preventDefault()
    console.log('Form Submitted!!')
})

if(shipping == 'False'){
    document.getElementById('checkout-address').innerHTML = '<h2>The items are digital, No Billing Address Required</h2><br><h1>Thankyou for shopping @ The Stone Shop</h1>'
}

document.getElementById('make-payment').addEventListener('click', function(e){
    submitFormData()
})

function submitFormData(){
    console.log('Payment Button Clicked');

    var userFormData = {
        'firstName' : null,
        'lastName' : null,
        'email' : null,
        'username' : null,
        'total': total,
    }

    var shippingInfo = {
        'address' : null,
        'address2': null,
        'country': null,
        'state' : null,
        'zip': null,
    }

    if(shipping != 'False'){
         
        //User Information
        userFormData.firstName = form.firstname.value;
        userFormData.lastName = form.lastname.value;
        userFormData.email = form.email.value;
        userFormData.username = form.username.value;

        //Shipping Information
        shippingInfo.address = form.address.value;
        shippingInfo.address2 = form.address2.value;
        shippingInfo.country = form.country.value;
        shippingInfo.state = form.state.value;
        shippingInfo.zip = form.zip.value;

    }

    var url = "/process_order/"
    fetch(url,{
        method: 'POST',
        headers:{
            'content-Type':'application/json',
            'X-CSRFToken':csrftoken,
        },
        body:JSON.stringify({'form':userFormData, 'shipping':shippingInfo})
    })

    .then((response) => response.json())
    .then((data) => {
        console.log('Success: ',data);
        alert('transaction completed');
        window.location.href = "{% url 'home' %}"
    })

}
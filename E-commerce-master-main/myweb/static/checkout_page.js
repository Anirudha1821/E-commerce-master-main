    if (localStorage.getItem('cart') == null) {
        var cart = {};
    } else {
        cart = JSON.parse(localStorage.getItem('cart'));
    }
    console.log(cart);
    var sum = 0;
    if ($.isEmptyObject(cart)) {
        // If object is empty
        mystr = "<li>Cart is empty.</li>"
        $('#items').append(mystr);
    }

    for (item in cart) {
        let name = cart[item][1];
        let qty = cart[item][0];
        sum = sum + qty;
        mystr = ` <li>${name} <br> Quantity 
                    ${qty}
                        </li>`
        $('#items').append(mystr);
    }
    document.getElementById('cart').innerHTML = sum;

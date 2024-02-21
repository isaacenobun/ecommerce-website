// Handle image clicks
var ProductImg = document.getElementById('product-img');
var SmallImg = document.getElementsByClassName('small-img');

for (let i = 0; i < SmallImg.length; i++) {
    SmallImg[i].onclick = function(event) {
        ProductImg.src = event.target.src;
    };
}

// Handle input subtotal change
var inputValues = document.getElementsByClassName('inputValue');
var subTotals = document.getElementsByClassName('subTotal');
var totalSubTotalElement = document.getElementById('subTotal-Total');
var taxElement = document.getElementById('Tax');
var totalElement = document.getElementById('Total')

for (let i = 0; i < inputValues.length; i++) {
    inputValues[i].addEventListener('input', function(event) {
        var totalSubTotal = 0.00;
        for (let j = 0; j < inputValues.length; j++) {
            var newValue = parseFloat(inputValues[j].value);
            if (!isNaN(newValue) && newValue >= 0) {
                subTotals[j].innerText = `$${(newValue * 50).toFixed(2)}`;
                totalSubTotal += newValue * 50;
            } else {
                subTotals[j].innerText = subTotals[j].innerText;
            }
        }
        totalSubTotalElement.innerText = `$${totalSubTotal.toFixed(2)}`;
        taxElement.innerText = `$${(totalSubTotal*0.1).toFixed(2)}`;
        totalElement.innerText = `$${(totalSubTotal.toFixed(2)-(totalSubTotal*0.1).toFixed(2)).toFixed(2)}`;
    });
}

// Handle Login and Register toggle
var login = document.getElementById('login')
var register = document.getElementById('register')
var indicator = document.getElementById('Indicator')
var loginForm = document.getElementById('LoginForm')
var regForm = document.getElementById('RegForm')

login.addEventListener('click', function(){
    indicator.style.transform = 'translateX(0px)';
    loginForm.style.transform = 'translateX(300px)';
    regForm.style.transform = 'translateX(300px)';
    regForm.style.opacity = '0'
    loginForm.style.opacity = '1'
});

register.addEventListener('click', function(){
    indicator.style.transform = 'translateX(100px)';
    loginForm.style.transform = 'translateX(0)';
    regForm.style.transform = 'translateX(0)';
    regForm.style.opacity = '1'
    loginForm.style.opacity = '0'
});
console.log('js loaded');
let notify = document.getElementById('calculate');
notify.addEventListener('click',function(){
    let height = document.getElementById('height').value;
    let weight = document.getElementById('weight').value;
    let age = document.getElementById('age').value;
    let gender = document.querySelector('input[name="gender"]:checked').value;
    let cuongdo = document.querySelector('input[name="cuongdo"]:checked').value;
    if(gender == "male")
    {
        bmr = 66 + (13.75 * parseInt(weight)) + (5 * parseInt(height)) - (6.7 * parseInt(age));
    }
    else
    {
        bmr = 655 + (9.6 * parseInt(weight)) + (1.8 * parseInt(height)) -  (4.7 * parseInt(age));
    }
    if(cuongdo == 1.2)
    {
        rmr = parseInt(bmr) * 1.2;
    }
    else if(cuongdo == 1.375)
    {
        rmr = parseInt(bmr) * 1.375;
    }
    else if(cuongdo == 1.45)
    {
        rmr = parseInt(bmr) * 1.45;
    }
    else if(cuongdo == 1.75)
    {
        rmr = parseInt(bmr) * 1.75;
    }
    else if(cuongdo == 1.95)
    {
        rmr = parseInt(bmr) * 1.95;
    }
    console.log(height);
    document.getElementById('result').innerHTML = 'BMR bạn là: '+ bmr +" calories. RMR của bạn cần thiết là: "+rmr+" calories";
    console.log('click')
});
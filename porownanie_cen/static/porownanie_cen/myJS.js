
function myFunction() {

  if (document.getElementById("result")){
    var len = document.getElementById("result").rows[0].cells.length;
    var num_kontrahenci = document.getElementById("result").rows[0].cells.length;
    var prefix=''
    var prefix_low = 'lowest_'
    var rows = (document.getElementById('result').getElementsByTagName("tbody")[0].getElementsByClassName("row_result").length);
    var n=1;
    var r=1;
    var lowest_sum = document.getElementById('lowest_sum').textContent;
    var lowest_prices_sum = 0;
    var all_prices = [];

    console.log(rows);

    for( var j=r; j<=rows; j++){

      for(var i=n; i<=len; i++){
        var tocheck = document.getElementById(prefix + i).textContent;
        var element = document.getElementById(prefix_low + j).textContent;
        if(element == tocheck){
          var change = document.getElementById(i);
          change.classList.remove("bg-dark");
          change.classList.add("bg-success");
        }
      }
      n = i;
      len+=num_kontrahenci;
      price_txt = document.getElementById(prefix_low + j).textContent;

      if(price_txt){
        price_float = parseFloat(price_txt);
      } else{
        price_float = 0;
      }
      lowest_prices_sum += price_float;

    }
    var price_to_show = document.getElementById('lowest_sum');
    price_to_show.innerHTML= lowest_prices_sum.toFixed(2);

    n=1;
    r=1;
    len = document.getElementById("result").rows[0].cells.length;

    for(var j=r; j<=rows; j++){
      for(var i=n; i<=len; i++){
        var tocheck = document.getElementById(prefix + i).textContent;
        if (tocheck =='N/A'){
          all_prices.push(0);
        } else{
          price = parseFloat(tocheck);
          all_prices.push(price);
        }
      }
      n = i;
      len+=num_kontrahenci;
    }


    len = document.getElementById("result").rows[0].cells.length;
    kontrahent_price_sum = 0;


    for(var n=0; n<len; n++ ){

      for(var i=n; i<=all_prices.length-1;i=i+num_kontrahenci){

        kontrahent_price_sum+=all_prices[i]

      }
      var kontrahent_price_sum_to_show = document.getElementById('cena_kontrahent_' + (n+1));
      kontrahent_price_sum_to_show.innerHTML = kontrahent_price_sum.toFixed(2);
      kontrahent_price_sum = 0;
    }
  }
}

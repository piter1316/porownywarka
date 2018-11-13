
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

function copy(){
    iter = 0;
    var rows = document.getElementById('prices').getElementsByTagName("tbody")[0].getElementsByTagName("tr").length;
    var cells = document.getElementById('prices').getElementsByTagName("tbody")[0].getElementsByTagName("td").length;
    var len = document.getElementById("prices").rows[0].cells.length;
    var toCopy ='';
    var iter = 0;
    for( var j=1; j<=rows; j++){
       for(var i=iter; i<len+1; i++){
       var text = document.getElementById("prices").getElementsByTagName("tbody")[0].getElementsByTagName("td")[i].innerText;
       text = text.replace('\t','')

       if(i!=iter+2){
        toCopy+=text+'\t';
       }else{
        toCopy+=text;
       }
      }
      iter=i;
      len+=3;
      toCopy+='\n';
    }
    var toCopyArea = document.getElementById("copy");
    toCopyArea.innerHTML=toCopy;
    toCopyArea.select();
    document.execCommand("copy");
    var copyButton = document.getElementById("copyButton");
    $(copyButton).attr('data-original-title', 'Skopiowano!!!')
    .tooltip('show');
    setTimeout(function(){
        $(copyButton).attr('data-original-title', 'Kopiuj do Schowka')
        .tooltip('show').delay(2000).tooltip('hide');
    },2000);
}

$(function () {
  $('[data-toggle="tooltip"]').tooltip()
})


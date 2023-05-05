window.onload = function() {
   podp = document.getElementById('podp');
   otpi = document.getElementById('otpi');
   console.log(podp);
   console.log(otpi);

   if(otpi != null){
        podp.remove()
   }

  };

function eventSign(postId, userId, token){
//console.log(postId, userId, token);
const formData = new FormData();
let xhr = new XMLHttpRequest();
    xhr.open('POST','/add/');
	xhr.setRequestHeader('X-CSRFToken', token);
//	xhr.setRequestHeader("Content-type", "multipart/form-data");
    formData.append("userId", userId);
    formData.append("postId", postId);
    xhr.send(formData);
}

function eventDelete(postId, userId, token){
console.log(postId, userId, token);
const formData = new FormData();
let xhr = new XMLHttpRequest();
    xhr.open('POST','/del/');
	xhr.setRequestHeader('X-CSRFToken', token);
    formData.append("userId", userId);
    formData.append("postId", postId);
    xhr.send(formData);
}

function getPdf(){
let xhr = new XMLHttpRequest();
    xhr.open('GET','/pdf/');
	xhr.setRequestHeader('Content-type', 'application/x-www-form-urlencoded');
	xhr.responseType = "document";
    xhr.send();
}



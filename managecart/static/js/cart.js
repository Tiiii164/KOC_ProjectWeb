function plus(){
    var t=document.getElementById("textbox").value;
    document.getElementById("textbox").value=parseInt(t)+1;
}
function minus(){
    var t=document.getElementById("textbox").value;
    if(parseInt(t)>1){
        document.getElementById("textbox").value=parseInt(t)-1;
    }
}
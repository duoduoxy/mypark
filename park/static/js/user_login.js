window.onload = function(){
    var form = $("form")[0];
    inputs = $(form).find("input");
    form.addEventListener("submit", function(e){
        if(inputs[1].value == ""){
            $("#error_input").css("display", "block");
            $("#error_input").text("请输入用户名");
            setTimeout(function(){
                $("#error_input").css("display", "none");
            },1000);
            e.preventDefault();
        }else if(inputs[2].value == ""){
            $("#error_input").css("display", "block");
            $("#error_input").text("请输入密码");
            setTimeout(function(){
                $("#error_input").css("display", "none");
            },1000);
            e.preventDefault();
        }
    },false);
}
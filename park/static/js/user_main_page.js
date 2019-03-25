window.onload = function(){
    $.post("get_notification", function(data){
        $("#notification").find("marquee").text(data);
    } );
}

function to_info(){
    window.location.href = "to_info";
}
function to_park(){
    if($("#pay_state").text()=="余额不足"){
        $("#warn_message").text("你本月尚未支付停车费用,已暂停停车业务");
        $("#warn_message").css("display", "block");
        setTimeout(function(){
            $("#warn_message").css("display", "none");
        },1000);
    }else{
        window.location.href = "to_park";
    }
}
function to_charge(){
    window.location.href = "to_charge";
}
function to_comment(){
    if("0"==$("#is_owner").text()){
        $("#warn_message").text("抱歉非业主暂时不能评论");
        $("#warn_message").css("display", "block");
        setTimeout(function(){
            $("#warn_message").css("display", "none");
        }, 1000);
    }else{
        window.location.href="to_comment";
    }
}
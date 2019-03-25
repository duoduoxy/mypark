window.onload = function(){
    $.post("get_balance",{"id": $("#user_id").text()}, function(data){
        $("#balance").text(data);
    });
    if("1"==$("#is_owner").text()){
        $.post("get_position", {"id":$("#user_id").text()}, function(data){
        $("#position").text(data);
        });
        $("#status").text("业主");

    }else{
        $("#status").text("非业主");
        $("#position").text("无固定车位");
    }
}
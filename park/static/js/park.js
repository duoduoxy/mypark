var position = "";
var state = "";
window.onload = function(){
    $.post("get_user_parkinfo", {"user_id":$("#user_id").text()}, function(data){
        position = data;
        state = data;
    });
    get_position_state();
    if("1"==$("#is_owner").text()){
        $.post("get_position", {"id": $("#user_id").text()}, function(data){
           position = data;
           $("#banner").text("您的专属停车位为"+position + ",请点击该停车位停车.");
           change_position_color();
        });
    }else{
        $("#banner").text("请点击未使用停车位停车.");
    }
    $("#way1").on("change", function(){
        if($(this).val()!=""){
            upload();
        }
    });
}

function upload(){
    var form_data = new FormData();
    var file_info = $("#way1")[0].files[0];
    form_data.append("file", file_info);
    $.ajax({
        url: 'pic_upload',
        type: 'POST',
        data: form_data,
        processData:false,
        contentType:false,
        success: function(data){
            $("#way2").val(data);
        }
    });
}

function change_position_color(){
    imgs = $(".group_position").find("img");
    $.each(imgs, function(n,value){
        if(value.alt==position){
            $(value).css("border-color", "red");
            return;
        }
    });
}

function get_position_state(){
$.post("get_parkinfo", function(data){
        $.each(data, function(n, value){
            if(value["isBusy"]=="no"){
                if(value["parkID"]=="A"){
                    $("#group_a").append("<img onclick='to_park(this)' class='img-thumbnail' src='/static/image/car.jpg' alt='" + value["parkID"] + value["positionID"] +
                     "' align='" + value["isBind"] + "' />" );
                }else if(value["parkID"]=="B"){
                    $("#group_b").append("<img onclick='to_park(this)' class='img-thumbnail' src='/static/image/car.jpg' alt='" + value["parkID"] + value["positionID"] +
                     "' align='" + value["isBind"] + "' />" );
                }else{
                    $("#group_c").append("<img onclick='to_park(this)' class='img-thumbnail' src='/static/image/car.jpg' alt='" + value["parkID"] + value["positionID"] +
                     "' align='" + value["isBind"] + "' />" );
                }
            }else{
                if(value["parkID"]=="A"){
                                    $("#group_a").append("<img onclick='to_park(this)' class='img-thumbnail' src='/static/image/using_car.jpg' alt='" + value["parkID"] + value["positionID"] +
                     "' align='" + value["isBind"] + "' />" );
                }else if(value["parkID"]=="B"){
                                   $("#group_b").append("<img onclick='to_park(this)' class='img-thumbnail' src='/static/image/using_car.jpg' alt='" + value["parkID"] + value["positionID"] +
                     "' align='" + value["isBind"] + "' />" );
                }else{
                                    $("#group_c").append("<img onclick='to_park(this)' class='img-thumbnail' src='/static/image/using_car.jpg' alt='" + value["parkID"] + value["positionID"] +
                     "' align='" + value["isBind"] + "' />" );
                }
            }
        })
    },"json");
}

function to_park(obj){
    if($(obj)[0].src.indexOf("using_car")!=-1){
        return;
    }else{
        if($(obj)[0].alt==position){
            parking();
            return;
        }else{
            if($(obj)[0].align=="yes"){
                $("#warn_message").text("业主专用车位");
                $("#warn_message").css("display", "block");
                setTimeout(function(){
                    $("#warn_message").css("display", "none");
                },1000);
                return;
            }
            if(state==""){
                position = $(obj)[0].alt;
                parking();
            }
        }
    }
}

function parking(){
    $("#parking").modal("show");
}

function confirm_park(){
    if($("#way2").val()==""){
        return;
    }
    $.post("once_park", {"user_id":$("#user_id").text()}, function(data){
        if(data=="success"){
               $.post("confirm_park",{"position":position, "user_id":$("#user_id").text(), "car_id":$("#way2").val(), "is_owner": $("#is_owner").text()}, function(data){
               if(data=="success"){
                $("#parking").modal("hide");
                imgs = $(".group_position").find("img");
                $.each(imgs, function(n,value){
                    if(value.alt==position){
                        $(value)[0].src="/static/image/using_car.jpg";
                        state = "parking";
                    }
                });
               }
            });
        }else{
            $("#warn_message").text("每位用户只能占用一个停车位");
            $("warn_message").css("display", "block");
            setTimeout(function(){
                $("#warn_message").css("display", "none");
            },1000);
        }
    });

}

function finish(){
    console.log("click");
    imgs = $(".group_position").find("img");
    $.each(imgs, function(n, value){
        if(value.alt==position&&($(value)[0].src.indexOf("using_car")!=-1)){
            $.post("finish", {"position":position, "user_id":$("#user_id").text(), "is_owner":$("#is_owner").text()}, function(data){
                if(data=="success"){
                    $(value)[0].src="/static/image/car.jpg";
                }else if(data.indexOf("余额")!=-1){
                    $("#warn_message").text(data);
                    $("#warn_message").css("display", "block");
                    setTimeout(function(){
                        $("#warn_message").css("display", "none");
                    },1000);
                }else if(data.indexOf("消费")!=-1){
                    $(value)[0].src="/static/image/car.jpg";
                    $("#warn_message").text(data);
                        $("#warn_message").css("display", "block");
                        setTimeout(function(){
                            $("#warn_message").css("display", "none");
                        },1000);
                    state = "";
                }
            })
        }
    });
}


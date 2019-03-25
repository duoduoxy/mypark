var hygiene = 5;
var platform = 5;
var service = 5;
function change_star(obj){
    if($(obj)[0].src.indexOf("grey_heart")!=-1){
        $(obj).attr("src", "/static/image/yellow_heart.jpg");
    }else{
        $(obj).attr("src", "/static/image/grey_heart.jpg");
    }
    count_star();
    show_comment();

}

function show_comment(){
    if(hygiene==5){
        $("#hygiene").text("很好");
    }else if(hygiene==4){
        $("#hygiene").text("好");
    }else if(hygiene == 3){
        $("#hygiene").text("较好");
    }else if(hygiene == 2){
        $("#hygiene").text("较差");
    }else if(hygiene ==1){
        $("#hygiene").text("差");
    }else{
        $("#hygiene").text("很差");
    }

    if(service==5){
        $("#service").text("很好");
    }else if(service==4){
        $("#service").text("好");
    }else if(service == 3){
        $("#service").text("较好");
    }else if(service == 2){
        $("#service").text("较差");
    }else if(service ==1){
        $("#service").text("差");
    }else{
        $("#service").text("很差");
    }

    if(platform==5){
        $("#platform").text("很好");
    }else if(platform==4){
        $("#platform").text("好");
    }else if(platform == 3){
        $("#platform").text("较好");
    }else if(platform == 2){
        $("#platform").text("较差");
    }else if(platform ==1){
        $("#platform").text("差");
    }else{
        $("#platform").text("很差");
    }
}

function count_star(){
    hygiene = 0;
    platform = 0;
    service = 0;
    $.each($("#star1").find("img"), function(n, value){
        value = value.src;
        if(value.indexOf("yellow_heart")!=-1){
            hygiene ++;
        }
    });
    $.each($("#star2").find("img"), function(n, value){
        value = value.src;
        if(value.indexOf("yellow_heart")!=-1){
            service++;
        }
    });
    $.each($("#star3").find("img"), function(n,value){
        value = value.src;
        if(value.indexOf("yellow_heart")!=-1){
            platform++;
        }
    });

}

function submit_comment(){
    $.post("submit_comment", {"hygiene":hygiene, "service":service, "platform":platform , "comment_content":$("#comment_content").val(), "user_id":$("#user_id").text()},
    function(data){
        if("success"==data){
            $("#submit_result").css("display","block");
            $("#submit_result").text("评价提交成功");
            $("#comment_content").val("");
            setTimeout(function(){
                $("#submit_result").css("display", "none");
            },1000);
        }
    });
}
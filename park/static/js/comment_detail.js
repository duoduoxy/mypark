window.onload = function(){
    $.post("get_comment_detail",{"id": $("#id").text()}, function(data){
        $("#content").text(data);
    })
}

function ans_comment(){
    $.post("ans_comment", {"id": $("#id").text(),
    "content": $("#answer_comment").val()
    }, function (data){
        $("#answer_result").text(data);
        $("#answer_result").css("display", "block");
        $("#answer_comment").val("");
        setTimeout(function(){
            $("#answer_result").css("display", "none");
        }, 1000);
    })
}

function getQueryVariable(variable)
{
       var query = window.location.search.substring(1);
       var vars = query.split("&");
       for (var i=0;i<vars.length;i++) {
               var pair = vars[i].split("=");
               if(pair[0] == variable){return pair[1];}
       }
       return(false);
}
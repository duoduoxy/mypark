window.onload = function(){
    $("#banner").width(document.documentElement.clientWidth);
    $("#function").width(document.documentElement.clientWidth);
    $("body").height(document.documentElement.clientHeight);
    init_show();
    $("#content_for_message").css("display", "block");
}

function change_tab(obj, id){
    $(".tab").css("color", "#333333");
    $(obj).css("color", "#FFF68F");
    init_show();
    if(id == 1){
        $("#content_for_message").css("display", "block");
    }else if(id == 2){
        $("#content_for_comment").css("display", "block");
        clear_comment();
        get_comment();
    }else if(id == 3){
        clear_parkinfo();
        get_parkinfo();
        $("#message_for_position").css("display", "block");
    }
}

function clear_comment(){
    $("tr").remove(".row_comment");
}

function clear_parkinfo(){
    $("#group_a").empty();
    $("#group_b").empty();
    $("#group_c").empty();
    $("#fill1").empty();
    $("#fill2").empty();
    $("#fill3").empty();
}

function get_parkinfo(){
    $.post("get_parkinfo", function(data){
        $.each(data, function(n, value){
            if(value["isBusy"]=="no"){
                if(value["parkID"]=="A"){
                    $("#group_a").append("<img class='img-thumbnail' src='/static/image/car.jpg'/>");
                }else if(value["parkID"]=="B"){
                    $("#group_b").append("<img class='img-thumbnail' src='/static/image/car.jpg'/>");
                }else{
                    $("#group_c").append("<img class='img-thumbnail' src='/static/image/car.jpg'/>");
                }
            }else{
                if(value["parkID"]=="A"){
                    $("#group_a").append("<img class='img-thumbnail' src='/static/image/using_car.jpg'/>");
                }else if(value["parkID"]=="B"){
                    $("#group_b").append("<img class='img-thumbnail' src='/static/image/using_car.jpg'/>");
                }else{
                    $("#group_c").append("<img class='img-thumbnail' src='/static/image/using_car.jpg'/>");
                }
            }
        })
        fill_group(data);
    },
    "json")
}

function fill_group(data){
    var num_group_a=0;
    var num_use_a=0;
    var num_group_b=0;
    var num_use_b=0;
    var num_group_c=0;
    var num_use_c=0;
    $.each(data, function(n, value){
        if(value["parkID"]=="A"){
            num_group_a++;
            if(value["isBusy"]=="yes"){
                num_use_a++;
            }
        }else if(value["parkID"]=="B"){
            num_group_b++;
            if(value["isBusy"]=="yes"){
                num_use_b++;
            }
        }else{
            num_group_c++;
            if(value["isBusy"]=="yes"){
                num_use_c++;
            }
        }
    });
    $("#fill1").append("<td>A</td><td>"+ num_group_a + "</td><td>" + num_use_a + "</td><td><font onclick='add_position(1)' class='glyphicon glyphicon-plus'></font></td>")
    $("#fill2").append("<td>B</td><td>"+ num_group_b + "</td><td>" + num_use_b + "</td><td><font onclick='add_position(2)' class='glyphicon glyphicon-plus'></font></td>")
    $("#fill3").append("<td>C</td><td>"+ num_group_c + "</td><td>" + num_use_c + "</td><td><font onclick='add_position(3)' class='glyphicon glyphicon-plus'></font></td>")
}

function add_position(group){
    var flag;
    if(group == 1)
        flag = 'A';
    else if(group == 2)
        flag = 'B';
    else
        flag = 'C';
    $.post("add_position",
    {"group": flag},
    function (data){
        clear_parkinfo();
        get_parkinfo();
    })
}

function del_position(){
    $.post("del_position", {"parkID":$("#select_group").val(),"positionID":$("#position_id").val()},
    function(data){
        $("#del_result").text(data);
        $("#del_result").css("display", "block");
        $("#position_id").val("");
        clear_parkinfo();
        get_parkinfo();
        setTimeout(function(){
            $("#del_result").css("display", "none");
            $("#delete_position").modal("hide");
        },1000);
    });
}

function get_comment(){
    $.post("get_comment", function(data){
        $.each(data, function(n, value){
                $("#comment").append(
                    "<tr class='row_comment' onclick='view_comment(this)'><td>" + value['id'] + "</td><td>" + value['username'] + "</td><td>" + value['time'] + "</td><td>" + value['state'] + "</td></tr>"
                )
         })
    },
    "json"
    );
}

function view_comment(obj){
    var id = obj.cells[0].innerHTML;
    window.location.href="comment_detail?id=" + id;
}

function exit_system(){
    $.post("exit_system", function(data){
        window.location.href=data;
    });
}

function publish_notification(){
    var title = $("#message_title").val().trim();
    var content = $("#message_content").val().trim();
    if(""==title){
        alert("Please input notification title!");
        return;
    }
    if(""==content){
        alert("Please input notification content!");
        return;
    }
    $.post("publish_notification",
    {
        title: title,
        content: content
    },
    function(data){
        if("success" == data){
            $("#message_title").val("");
            $("#message_content").val("");
            $("#publish_result").css("display", "block");
            $("#publish_result").text("通知已发布！");
            setTimeout(
            function(){
                $("#publish_result").css("display", "none");
            },1000)
        }
    }
    )

}

function show_manage_page(){
    if($("#manage_group").css("display").trim()=="none"){
        $("#manage_group").css("display", "block");
        $(".group_position").css("display", "none");
    }else{
        $("#manage_group").css("display", "none");
        $(".group_position").css("display", "block");
    }
}



function init_show(){
    $("#content_for_message").css("display", "none");
    $("#content_for_comment").css("display", "none");
    $("#message_for_position").css("display", "none");
}
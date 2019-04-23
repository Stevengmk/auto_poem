
$("#test_hide").click(function () {
    // var data_flask = $("#flask").serialize()
    var data_flask = $("#flask_hide").val()
    var get_data = {"usr":data_flask}
    $.ajax({
        url:"/hide",
        type:"GET",
        dataType:"json",
        async:true,
        data:get_data,
        success:function (result) {
            console.log(result)
            document.getElementById("result_hide").innerText = result
        },
        error:function (XMLHttpRequest,textStatus,errorThrown) {
            alert(XMLHttpRequest.status)
            alert(XMLHttpRequest.readyState)
            alert(textStatus)
        }
    });
})


$("#test_fir").click(function () {
    // var data_flask = $("#flask").serialize()
    var data_flask = $("#flask_fir").val()
    var get_data = {"usr":data_flask}
    $.ajax({
        url:"/fir",
        type:"GET",
        dataType:"json",
        async:true,
        data:get_data,
        success:function (result) {
            // alert(data_flask)
            console.log(result)
            // $("#result").html("<p>"+result+"<p>")
            document.getElementById("result_fir").innerText = result
        },
        error:function (XMLHttpRequest,textStatus,errorThrown) {
            alert(XMLHttpRequest.status)
            alert(XMLHttpRequest.readyState)
            alert(textStatus)
        }
    });
})


$("#test_sen").click(function () {
    // var data_flask = $("#flask").serialize()
    var data_flask = $("#flask_sen").val()
    var get_data = {"usr":data_flask}
    $.ajax({
        // url:"{{url_for('testController')}}",
        url:"/sen",
        type:"GET",
        dataType:"json",
        async:true,
        // data:{test:$("#test_flask").serialize()},
        // data:$('form').serialize(),
        // data:{usr:$("#flask").val()},
        data:get_data,
        // data:data_flask,
        success:function (result) {
            // alert(data_flask)
            console.log(result)
            // $("#result").html("<p>"+result+"<p>")
            document.getElementById("result_sen").innerText = result
        },
        error:function (XMLHttpRequest,textStatus,errorThrown) {
            alert(XMLHttpRequest.status)
            alert(XMLHttpRequest.readyState)
            alert(textStatus)
        }
    });
})



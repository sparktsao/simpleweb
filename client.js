$("#data").change(function(){
    var testdata = $("#data").val();
    $.ajax({
  	  type: "POST",
	  url: "users/spark",
	  data: {'data':testdata},
	  cache: false,
	  success: function(data){
	     $("#resultarea").text(data);
             if(data.split("\n").slice(-1)>0.5)
             {
                document.getElementById("score").style.background='red';
                document.getElementById("score").innerHTML = "Dangerous, score:"+data.split("\n").slice(-1);
                console.log(data.split("\n").slice(-1));
             }
             else
             {
                document.getElementById("score").style.background='green';
                document.getElementById("score").innerHTML = data.split("\n").slice(-1);
                console.log(data.split("\n").slice(-1));
             }
	  }
	});

  });

$("#data").mouseenter(function(){
    $("#data").css("background-color", "yellow");
});
$("#data").mouseleave(function(){
    $("#data").css("background-color", "white");
});

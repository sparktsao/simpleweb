$("#data").change(function(){
    //#var myusername = document.getElementById("login").elements["username"].value;
    var testdata = $("#data").val();
    $.ajax({
  	  type: "POST",
	  url: "users/spark",
	  data: {'data':testdata},
	  cache: false,
	  success: function(data){
	     $("#resultarea").text(data);
	  }
	});

  });


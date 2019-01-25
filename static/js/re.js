function call(data_g){  

    const url='/dhishnya/authenticate/';
    var dr; 
    

    $.ajax({
        type:'POST',
        url: url,
        dataType:'text',        
        data:data_g,
        success:handleSuccess,
        error:handleError,
        async:false,
        timeout:500
    });

    function handleSuccess(data_r) { 
        dr=JSON.parse(data_r);
    }
    

    if (dr.repeat>0)
    {
        return null;

    }else if(dr.status==200){
        return true;


    }
    else if(dr.status==201){
        return false;

    }



    function handleError(){
        asforclock.hide();
        voiforclock.hide();
        alert("Check your internet connection");  

    }

}

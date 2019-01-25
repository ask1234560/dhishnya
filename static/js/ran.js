$("document").ready(function(){
    var count;
    var lc=$("#count");
    var arr=[3263,2532,1244,1200,1100,1044,896,585,442,324,310,280,267];
    var i=0;
   
    
    rand=function(){
        
        count=arr[i];
        i+=1;
        if(count>0){
        lc[0].innerHTML=count;
           }
        
        
    }



  

});
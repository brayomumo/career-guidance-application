$( "#myform" ).submit(function( event ) {
    alert( "Handler for .submit() called." );
    event.preventDefault();
    var maths = parseInt($('#maths').val());
    var english = parseInt($('#english').val());
    var kiswahili = parseInt($('#kiswahili').val());
    var physics = parseInt($('#physics').val());
    var biology = parseInt($('#biology').val());
    var history = parseInt($('#history').val());
    var geography = parseInt($('#geography').val());
    var chemistry = parseInt($('#chemistry').val());
    var agriculture = parseInt($('#agri').val());
    var business = parseInt($('#bs').val());
    var comp = parseInt($('#comp').val());
    var french = parseInt($('#french').val());
    var cre = parseInt($('#cre').val());
    
    var subjects= [maths,english,kiswahili,physics,chemistry,biology,business,geography,history,comp,french,cre,agriculture]
    var sum = 0
    // console.log()
    for (var i =0; i<subjects.length;i++){
        var sub =   (subjects[i])
        // console.log(sub)
        sum += sub
    }
    //choosing 4 main subjects
    var x = 0 //where x is sum of 4 main subjects

    
  
    var lang = Math.max(  (english),   (kiswahili))
    
    var science  = Math.max(  (physics),   (chemistry),   (biology))
    
    var humanity = Math.max(  (geography),   (history),   (cre))
    var matechnicals = Math.max(  (french),   (comp),   (business),   (agriculture))
    var Element4 = 0
    if(humanity > matechnicals){
        Element4 = humanity
    }
    else {
        Element4 = matechnicals
    }
    
    x = lang +science+Element4 + maths
    console.log(x)
    //calculating cluster points
    var y = sum
    var cluster = Math.sqrt((x/48 )* (y/84)) * 48
    cluster = cluster.toFixed(3)
    // console.log(cluster)
    var Turl = "/cutoffpoints" + cluster
    $.ajax({
        url: Turl ,
        method: 'GET',

        // send selected data to the responseOnClick method which is in views.py
        data: {
            'cutoff': cluster
        }, // 'id' will be used in request.GET.get('id') which is in views.py, $(this).val() is selected item, 
        success: function (data) {
            console.log(data);}
        })

    
  });
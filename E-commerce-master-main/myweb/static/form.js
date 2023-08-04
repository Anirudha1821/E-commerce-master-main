var click=0;

$(".next").click(function(){
    click++;
    if(click===1){
        $(".page_one, .page_three , .page_four").attr({style:"display : none"});
        $(".page_two").attr({style:"display : show"});
    }
    else if(click===2){
        $(".page_one, .page_two , .page_four").attr({style:"display : none"});
        $(".page_three").attr({style:"display : show"});
    }
    else if(click===3){
        $(".page_one, .page_two , .page_three").attr({style:"display : none"});
        $(".page_four").attr({style:"display : show"});
    }
})

$(".prev").click(function(){
    click--;
    if(click==0){
        $(".page_two, .page_three , .page_four").attr({style:"display : none"});
        $(".page_one").attr({style:"display : show"});
    }
    else if(click===1){
        $(".page_one, .page_three , .page_four").attr({style:"display : none"});
        $(".page_two").attr({style:"display : show"});
    }
    else if(click===2){
        $(".page_one, .page_two , .page_four").attr({style:"display : none"});
        $(".page_three").attr({style:"display : show"});
    }
})
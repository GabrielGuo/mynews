/**
 * 首页轮播图JS
 */
//利用JS选择器和图片的循环出现
$(function(){
	var numpic = $('#slidelist li').size()-1;
	var nownow = 0;
	var inout = 0;
	var TT = 0;
	var SPEED = 4000;		//轮播的时间

	$('#slidelist li').eq(0).siblings('li').css({'display':'none'}); // 初始化除了第一个其他显示为None

	var ulstart = '<ul id="pagination" class="ad_show slidebar">',
		ulcontent = '',
		ulend = '</ul>';
	ADDLI();
	var pagination = $('#pagination a');		//定义指向哪号标签
	var paginationwidth = $('#pagination').width();
	//$('#pagination').css('margin-left',(0-paginationwidth));
	
	pagination.eq(0).addClass('on');
		
	function ADDLI(){	//统计有多少张广告位
		for(var i = 0; i <= numpic; i++){
			ulcontent += '<a class="" href="#">' +  (i+1) +  '</a>';
		}
		
		$('#slidelist').after(ulstart + ulcontent + ulend);
	}

	pagination.on('click',DOTCHANGE);
	
	function DOTCHANGE(){
		
		var changenow = $(this).index();
		
		$('#slidelist li').eq(nownow).css('z-index','39');
		$('#slidelist li').eq(changenow).css({'z-index':'38'}).show();
		pagination.eq(changenow).addClass('on').siblings('a').removeClass('on');
		$('#slidelist li').eq(nownow).fadeOut(400,function(){$('#slidelist li').eq(changenow).fadeIn(500);});
		nownow = changenow;
	}
	
	pagination.mouseenter(function(){
		inout = 1;
	});
	
	pagination.mouseleave(function(){
		inout = 0;
	});
	
	function GOGO(){	//循环加一的显示图片
		var NN = nownow+1;
		if( inout == 1 ){
			} else {
			if(nownow < numpic){
			$('#slidelist li').eq(nownow).css('z-index','39');
			$('#slidelist li').eq(NN).css({'z-index':'38'}).show();
			pagination.eq(NN).addClass('on').siblings('a').removeClass('on');
			$('#slidelist li').eq(nownow).fadeOut(400,function(){$('#slidelist li').eq(NN).fadeIn(500);});
			nownow += 1;
			//fedein 显示出来 fedeout离开

		}else{
			NN = 0;
			$('#slidelist li').eq(nownow).css('z-index','39');
			$('#slidelist li').eq(NN).stop(true,true).css({'z-index':'38'}).show();
			$('#slidelist li').eq(nownow).fadeOut(400,function(){$('#slidelist li').eq(0).fadeIn(500);});
			pagination.eq(NN).addClass('on').siblings('a').removeClass('on');

			nownow=0;

			}
		}
		TT = setTimeout(GOGO, SPEED);
	}
	
	TT = setTimeout(GOGO, SPEED);
});


/*
 * @Autor: Wentao Lin
 * @Description: 
 * @Date: 2020-12-23 19:18:54
 * @LastEditTime: 2020-12-30 16:17:23
 * @LastEditors: Wentao Lin
 */

$(function() {
	document.getElementById("loginBntId").onclick = function() {
        if ($("#loginBntId").attr('target') == '0') {
            $('#loginModalId').modal('show');
        }
        else if ($("#loginBntId").attr('target') == '1') {
            $.cookie('username', '');
            $("#loginBntId").attr('target','0');
            location.replace("/");
        }
	}
});



$(window).ready(function(){
	//获取浏览器高度
	var h = $(window).width();
	if(h < 992 && h >= 768) {//浏览器小于500px时，标签选择器所选标签消失
        $("#search-input").fadeOut(0);
        $("#search-link").attr('href', "/search_page")
        $("#search-button").attr('value',"Search page")
	}else{
        $("#search-input").fadeIn(0);//id为title的元素1秒内显示
        $("#search-link").attr('href', "#")
        $("#search-button").attr('value',"Search")
        $(function() {
            document.getElementById("search-button").onclick = function() {
                alert("The search function is not implemented yet")
            }
        });
	}
});

$(window).ready(function() {
    $('.search-btn').on('click', function () {
        alert("The search function is not implemented yet")
    })
});

$(window).resize(function(){
	//获取浏览器高度
	var h = $(window).width();
	if(h < 992 && h >= 768) {//浏览器小于500px时，标签选择器所选标签消失
        $("#search-input").fadeOut(0);
        $("#search-link").attr('href', "/search_page")
        $("#search-button").attr('value',"Search page")
	}else{
        $("#search-input").fadeIn(0);//id为title的元素1秒内显示
        $("#search-link").attr('href', "#")
        $("#search-button").attr('value',"Search")
        $(function() {
            document.getElementById("search-button").onclick = function() {
                alert("The search function is not implemented yet")
            }
        });
	}
})

$(document).ready(function(){
    if($.cookie("isClose") != 'yes'){
        var winWid = $(window).width()/2 - $('.alert_windows').width()/2;
        var winHig = $(window).height()/2 - $('.alert_windows').height()/2;
        // $(".alert_windows").css({"left":winWid,"top":-winHig*2});	//自上而下滑出
        $(".alert_windows").show();
        $(".alert_windows").animate({"left":winWid,"top":winHig},1000);
        $(".alert_windows  .cookie-header").click(function(){
            $(this).parent().fadeOut(500);
            //以天为单位
            // $.cookie("isClose",'yes',{ expires:1/8640});//测试十秒
            $.cookie("isClose",'yes',{ expires:1});//一天
        });
    }
});

$(document).ready(function(){
    if($.cookie("username") != '' && $.cookie("username") != null){
        $("#loginBntId").text('Logout');
        $("#loginBntId").attr('target','1');
    };
});

// $(document).ready(function(){
//     if($.cookie('variable_name')==null){
//         $("#loginBntId").text('Signin');
//     };
// });

$(document).ready(function () {
    $('.click').on('click', function () {
        $('.click').removeClass('active_address');
        $(this).addClass('active_address');
    });
});

$(window).load(function () {
    var list = $('.price')
    var number = 0
    list.each(function(){
        number += parseInt($(this).children().last().text())
    })
    $(".class-show").children().last().text(number)
});

$(document).ready(function () {
    $('.plus_button').on('click', function () {
        var id = $(this).attr('id')
        id = '#' + id
        var number = parseInt($(id).prev().text())
        number = number + 1
        $(id).prev().text(number)
        var price = parseInt($(".class-show").children().last().text())
        price += parseInt($(id).parent().prev().prev().children().last().text())
        $(".class-show").children().last().text(price)
    });
});

$(document).ready(function () {
    $('.minus_button').on('click', function () {
        var id = $(this).attr('id')
        id = '#' + id
        var number = parseInt($(id).next().text())
        if (number > 0) {
            number = number - 1
            var price = parseInt($(".class-show").children().last().text())
            price -= parseInt($(id).parent().prev().prev().children().last().text())
            $(".class-show").children().last().text(price)
        }
        $(id).next().text(number)
        if (number == 0) {
            $(id).prev().click()
        }
    });
});


function bindEmailCaptchaClick(){
     $('#captcha-btn').click(function (event) {
         var $this = $(this);
         event.preventDefault();
         var email = $('input[name=email]').val();
         if (!email) {
             zlalert.alertInfoToast('请输入邮箱！');
             return;
         }
         $.ajax({
             url :'/auth/captcha/email?email='+ email,
             method : "GET",
             success : function (result) {
                 var code = result['code'];
                 if (code == 200) {
                     var countdown = 60;
                    //取消点击事件
                     $this.off("click");
                     var timer = setInterval(function () {
                         $this.text(countdown + '秒后重新发送');
                         countdown--;
                         if (countdown <= 0) {
                            //清除定时器
                             clearInterval(timer);
                            //修改文字
                             $this.text('发送验证码');
                            //重新绑定事件
                             bindEmailCaptchaClick();
                         }
                         }, 1000);
                     alert('邮件验证码发送成功！');
                 } else {
                     zlalert.alertInfoToast(result['message']);
                }
            },
             fail : function (error) {
                 console.log(error);
            }
        })
    });
}

$(function () {
    bindEmailCaptchaClick();
})
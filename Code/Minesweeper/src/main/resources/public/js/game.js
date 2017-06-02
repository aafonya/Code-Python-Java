/**
 * Created by judit on 01.06.17.
 */
/**
 * Created by tahin on 2017.05.03..
 */
$ (document).ready(function () {
    $('div[id^="button"]').click(function(){
        var id = this.id.substring(6,this.id.length);
        $.ajax({url: "/index/" + id, success: function(result){
            console.log(result);
            $('#'+this.id).text(result);
            //$('#'+this.id).remove();

        }});
    });
});
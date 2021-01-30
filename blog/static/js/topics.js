var getPosts = function(e) {
    $.get(
        $(this).attr("data-url"),
            {
                topics: this.textContent.substring(1)
            },
        function(data, status, xhr) {
//            window.location.href = data.url;
            console.log(data.posts);
            var text = '';
            var i;
        //    for(i = 0; i < data.post_cnt; i++) {
        //        text += "<a href='javascript:void(0);' class='topic link'>&ensp;</a>"
        //    }
        },
        "json"
    );

}

document.querySelectorAll('.topic').forEach(div =>
    div.onclick = getPosts
)

$(document).ready(function(e) {
    getPosts(e);
})

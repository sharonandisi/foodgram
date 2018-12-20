like = (id) => {
    $("#likeicon" + id).addClass("liked")
    $("#likespan" + id).text(newLikes)

}

dislike = (id) => {
    $("#likeicon" + id).removeClass("liked")
    $("#likespan" + id).text(newLikes)

}

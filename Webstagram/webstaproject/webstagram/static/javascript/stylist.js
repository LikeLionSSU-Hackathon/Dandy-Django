const list=document.getElementsByClassName('stylist_list');

for(let i=0;i<list.length;i++){
    list[i].addEventListener("click",function(){
        alert("선택되었습니다.");
    });
}
function showDate(id1,id2, id3){
    var slide = document.getElementById(id1)
    var slideValue = document.getElementById(id2).innerHTML = parseInt(slide.value) +1
    var OutputView = document.getElementById(id2).innerHTML = months[slide.value]
    var mLIST = document.getElementById(id3).getElementsByTagName('li')
    var mLI = Object.values(mLIST)
    for (var obj of mLI){
        if (obj.value == slideValue){
            obj.style.opacity = '1'
            obj.style.transform  = 'scale(1.25)'
        }
        else{ obj.style.opacity = '.5'
        obj.style.transform  = 'scale(1)'}
    }
}

const months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];
var d = new Date();
const currentMONTH = d.getMonth()
function loadData(){
    document.getElementsByName('month').forEach((value)=>{
        if (value.className == 'slider')
            value.defaultValue = currentMONTH
        else value.defaultValue = months[d.getMonth()]
    })
    document.querySelectorAll('.monthli').forEach((ul)=>{
        ul.children.item(currentMONTH).style.opacity = '1'
        ul.children.item(currentMONTH).style.transform  = 'scale(1.25)'
    })
}
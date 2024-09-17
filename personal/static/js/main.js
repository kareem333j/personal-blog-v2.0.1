window.onload = ()=>{
    let links = document.querySelectorAll(".navbar .navbar-nav li a");
let navbar_btn_open = document.querySelector(".navbar .open");
let navbar_btn_close = document.querySelector(".navbar .close");

navbar_btn_open.onclick = ()=>{
    navbar_btn_close.style = "display:block";
    navbar_btn_open.style = "display:none";
}
navbar_btn_close.onclick = ()=>{
    navbar_btn_close.style = "display:none";
    navbar_btn_open.style = "display:block";
}
links.forEach(
    (ele) => {
        ele.onclick = ()=>{
            // delete active
            links.forEach(
                (ele)=>{
                     ele.classList.remove("active");
                }
            );
            // active new link
           ele.classList.add("active");
        }
    }
);

focusDiv = document.querySelector('.focus-div');

// search
let search = document.querySelector('.search-div');
let search_form = document.querySelector('.search');
let search_sugestions = document.querySelector('.search .sugestions');
let search_input = document.querySelector('.search-div input');
let search_results = document.querySelectorAll('.search .sugestions .result');

// search suggestion

search_input.addEventListener('input',(e)=>{
    search.classList.add("active");
    search_sugestions.classList.add("active");
    if(e.target.value == ""){
        search.classList.remove("active");
        search_sugestions.classList.remove("active");
    }
    getSuggestions(e.target.value);
});

document.addEventListener('keyup',(e)=>{
    if(e.ctrlKey && e.key === "/"){
        search_input.focus();
    }
});
function getSuggestions(data){
    url = '/search_suggestions/';
    fetch(url,{
        method: 'POST',
        headers: {
            "Content-Type": "application/json",
            'X-CSRFToken':csrftoken
        },
        body: JSON.stringify({'data':data})
    })
    .then((response)=>response.json())
    .then((data)=>{ 
        [...search_sugestions.children].map((e)=>{
            e.remove();
        })
        createSuggestions(data);
        // suggestionClick();
    });
}
function createSuggestions(data){
    if (data['results'].length == 0){
        search.classList.remove("active");
        search_sugestions.classList.remove("active");
    }else{
        for(let i = 0; i < data['results'].length; ++i){
            if(data['results'][i].type == 'user'){
                createSuggUser(data, i);
                suggestionClick_any();
            }
            else if(data['results'][i].type == 'comment'){
                createSuggComment(data, i);
                suggestionClick_any();
            }
            else if(data['results'][i].type == 'project'){
                createSuggProject(data, i);
                suggestionClick_any();
            }
            else if(data['results'][i].type == 'last_searches'){
                createSuggLast(data, i);
            }
        }
    }
}
function createSuggUser(data,i){
    let resultDiv = document.createElement('a');
    let IconDiv = document.createElement('div');
    let img = document.createElement('img');
    let dataDiv = document.createElement('div');
    let h4 = document.createElement('h4');
    let p = document.createElement('p');

    resultDiv.className = 'result result-sug d-flex gap-2 align-items-start';
    resultDiv.href = `/profile/${data['results'][i].id}/`;
    p.className = 'text-black-50';
    IconDiv.className = 'icon-div';
    dataDiv.className = 'data d-flex flex-column justify-content-start align-items-start';

    h4.innerHTML = data['results'][i].full_name;
    p.innerHTML = `@${data['results'][i].username}`;
    resultDiv.setAttribute('data-id', data['results'][i].id);
    resultDiv.setAttribute('data-type', 'user');
    img.src = `${data['results'][i].img}`;

    resultDiv.appendChild(IconDiv);
    resultDiv.appendChild(dataDiv);
    dataDiv.appendChild(h4);
    dataDiv.appendChild(p);
    IconDiv.appendChild(img);
    search_sugestions.appendChild(resultDiv);
}
function createSuggComment(data,i){
    let resultDiv = document.createElement('a');
    let IconDiv = document.createElement('div');
    let dataDiv = document.createElement('div');
    let h4 = document.createElement('h4');
    let p = document.createElement('p');

    resultDiv.className = 'result result-sug d-flex gap-2 align-items-start';
    p.className = 'text-black-50 text-start';
    IconDiv.className = 'icon-div';
    IconDiv.innerHTML = '<i class="fa-solid fa-comment"></i>';
    dataDiv.className = 'data d-flex flex-column justify-content-start align-items-start';
    
    h4.innerHTML = data['results'][i].full_name;
    p.innerHTML = `${data['results'][i].comment}`;
    resultDiv.setAttribute('data-id', data['results'][i].id);
    resultDiv.setAttribute('data-type', 'comment');
    resultDiv.href = `/profile/${data['results'][i].user_id}/#comment-${data['results'][i].id}`;

    resultDiv.appendChild(IconDiv);
    resultDiv.appendChild(dataDiv);
    dataDiv.appendChild(h4);
    dataDiv.appendChild(p);
    search_sugestions.appendChild(resultDiv);
}
function createSuggProject(data,i){
    let resultDiv = document.createElement('a');
    let IconDiv = document.createElement('div');
    let dataDiv = document.createElement('div');
    let h4 = document.createElement('h4');
    let p = document.createElement('p');

    resultDiv.className = 'result d-flex gap-2 align-items-start';
    p.className = 'text-black-50 text-start';
    IconDiv.className = 'icon-div';
    IconDiv.innerHTML = '<i class="fa-solid fa-file-shield"></i>';
    dataDiv.className = 'data d-flex flex-column justify-content-start align-items-start';
    
    h4.innerHTML = data['results'][i].full_name;
    p.innerHTML = `${data['results'][i].description}`;
    resultDiv.setAttribute('data-id', data['results'][i].id);
    resultDiv.setAttribute('data-type', 'project');
    resultDiv.href = `/project/${data['results'][i].id}`;

    resultDiv.appendChild(IconDiv);
    resultDiv.appendChild(dataDiv);
    dataDiv.appendChild(h4);
    dataDiv.appendChild(p);
    search_sugestions.appendChild(resultDiv);
}
function createSuggLast(data,i){
    let resultDiv = document.createElement('div');
    let IconDiv = document.createElement('div');
    let dataDiv = document.createElement('div');
    let p = document.createElement('p');
    // let deleteBtn = document.createElement('a');

    resultDiv.className = 'result last-searches d-flex gap-2 align-items-start';
    p.className = 'text-black-50 text-start';
    p.style = 'font-size:1.1em';
    IconDiv.className = 'icon-div';
    IconDiv.innerHTML = '<i class="fa-solid fa-clock-rotate-left"></i>';
    dataDiv.className = 'data d-flex flex-column justify-content-start align-items-start';
    // deleteBtn.className = 'delete-results-btn';
    
    p.innerHTML = `${data['results'][i].content}`;
    // deleteBtn.innerHTML = '<i class="fa-solid fa-xmark"></i>';
    resultDiv.setAttribute('data-id', data['results'][i].id);
    // deleteBtn.setAttribute('data-id', data['results'][i].id)

    resultDiv.appendChild(IconDiv);
    resultDiv.appendChild(dataDiv);
    dataDiv.appendChild(p);
    // dataDiv.appendChild(deleteBtn);
    search_sugestions.appendChild(resultDiv);

    let lastSearches = document.querySelectorAll('.last-searches');
    suggestionClick_last(lastSearches);
}
function suggestionClick_last(elements){
    [...elements].map((e)=>{
        e.onclick = ()=>{
            search_input.value = e.children[1].children[0].textContent;
            search_form.submit();
        }
    });
}
function suggestionClick_any(){
    let elements = document.querySelectorAll('.result-sug');
    [...elements].map((e)=>{
        e.onclick = ()=>{
            if(e.dataset.type === 'user'){
                console.log('user: ',e.dataset.id);
                
            }
            if(e.dataset.type === 'comment'){
                console.log('comment: ',e.dataset.id);
            }
        }
    });
}

window.document.addEventListener('click', (e)=>{
    if(!e.target.classList.contains('search-div') && !e.target.parentElement.classList.contains('search-div')){
        search.classList.remove("active");
        search_sugestions.classList.remove("active");
    }
});
search_input.onfocus = ()=>{
    focusDiv.style.display = "flex";
    search.style = "z-index: 999";
    search_sugestions.style = "z-index: 999";
    document.querySelector("body").style = "overflow:hidden;";
}
focusDiv.onclick = ()=>{
    focusDiv.style = "display:none !important";
    search.style = "z-index: 2";
    search_sugestions.style = "z-index: 2";
    document.querySelector("body").style = "overflow:auto;";
};




// scrolling

let section = document.querySelector(".sec1");
let navbar = document.querySelector(".navbar");
let navDropDown = document.querySelector(".drop-profile ul");
let navDropLink = document.querySelectorAll(".drop-profile ul li a");

// go up btn and other when scroll
let btnUp = document.createElement("button");
let btnTxt = document.createTextNode("UP");
btnUp.appendChild(btnTxt);
btnUp.className = "btnUp";
document.body.appendChild(btnUp);
btnUp.style.cssText = "display:none;background-color: black;position: fixed;bottom: 20px;right: 20px;padding: 5px 10px;color: #fff;border: 0;cursor: pointer;border-radius:10px;font-size:1.3em";
btnUp.innerHTML = '<i class="fa-solid fa-circle-arrow-up"></i>';

if(window.scrollY < section.offsetTop+70){
    navbar_btn_open.onclick = ()=>{
        activeNavStyleOnScroll();
    }
    navbar_btn_close.onclick = ()=>{
        deActiveNavStyleOnScroll();
    }
}
window.onscroll = function(){
    if(window.scrollY >= section.offsetTop+70){
        activeNavStyleOnScroll();
    }
    if(window.scrollY < section.offsetTop+70){
        deActiveNavStyleOnScroll();
        navbar_btn_open.onclick = ()=>{
            activeNavStyleOnScroll();
        }
        navbar_btn_close.onclick = ()=>{
            deActiveNavStyleOnScroll();
        }
    }
}

function activeNavStyleOnScroll(){
    navbar.style = "box-shadow: 0 0 20px #181f2b;position: fixed;width:100%;z-index:999;background-color:rgba(34, 34, 34, 0.85)";
    btnUp.style.cssText = "display:block;background-color: black;position: fixed;bottom: 20px;right: 20px;padding: 5px 10px;color: #fff;border: 0;cursor: pointer;border-radius:10px;font-size:1.3em";
    if(navDropDown){
                navDropDown.style = "background-color:rgba(34, 34, 34, 0.85);";
        for(let i =0; i < navDropLink.length; i++){
            navDropLink[i].style = 'color:#fff';
        }  
    }
}
function deActiveNavStyleOnScroll(){
    navbar.style = "box-shadow: 0";
    btnUp.style.cssText = "display:block";
    if(navDropDown){
        navDropDown.style = "background-color:#fff;";
        for(let i =0; i < navDropLink.length; i++){
            navDropLink[i].style = 'color:#000';
        }
    }
}

btnUp.onclick = ()=>{
    window.scrollTo({
        top:0,
        behavior: 'smooth'
    });
}


// var typed = new Typed('#text', {
//     strings: ['> Web Developer', '> Full Stack', '> Django Developer'],
//     typeSpeed: 50,
//     backSpeed:100,
//     backDelay:1000,
//     loop:true
// });


// Aos

const observer = new IntersectionObserver(
    (entries)=>{
        entries.forEach(
            (entry)=>{
                if(entry.isIntersecting){
                    entry.target.classList.add('show');
                }/*else{
                    entry.target.classList.remove('show');
                }*/
            }
        );
    }
);

const hiddenElement = document.querySelectorAll('.hidden');
hiddenElement.forEach(
    (el)=>{
        observer.observe(el)
    }
);

}



// comment more
let moreBtn = document.querySelectorAll(".user-comment .more-comment");
let moreCommentDiv = document.querySelectorAll(".more-content");
moreBtn.forEach((e)=>{
    e.addEventListener("click", (ele)=>{
        moreCommentDiv.forEach((e)=>{
            e.classList.remove("active");
        });
        e.nextElementSibling.classList.add("active");
    });
    
});

document.addEventListener("click",(ele)=>{
    if(ele.target.id == "more-i" || ele.target.id == "more-btn"){
    }else{
        moreCommentDiv.forEach((e)=>{
            e.classList.remove("active");
        });
    }
});


// project imgs
let sectionView = document.querySelector(".section-view");
let sectionDivImg = document.querySelectorAll(".section-view .imgs-div .img");
let nextBtn = document.querySelector(".section-view .next");
let prevBtn = document.querySelector(".section-view .prev");
if(sectionView){
    // view project action
    let viewBtns = document.querySelectorAll(".data-pro .view-project");
    let exitProjectView = document.querySelector(".section-view .exit-project");
    viewBtns.forEach((e)=>{
        e.onclick = ()=>{
            sectionView.style = "display:flex;opacity:1;";
            sectionView.style.transform = "translateX(0%)";
        }
    });
        exitProjectView.onclick = function(){
            sectionView.style = "display:flex;opacity:0;";
            sectionView.style.transform = "translateX(-100%)";
        };
    
    let counter = 1;
    setInterval(()=>{
        document.querySelector(".img-counter h3").innerHTML = `${counter}/${sectionDivImg.length}`;
    },1);
    nextBtn.addEventListener("click",()=>{
        let activeNow = document.querySelector(".section-view .imgs-div .img.active");
        sectionDivImg.forEach((e)=>{
            e.classList.remove("active");
        });
        if(counter < sectionDivImg.length){
            counter++;
            activeNow.nextElementSibling.classList.add("active");
        }else{
            sectionDivImg[0].classList.add("active");
            counter = 1;
        }
    });
    prevBtn.onclick = ()=>{
        let activeNow = document.querySelector(".section-view .imgs-div .img.active");
        sectionDivImg.forEach((e)=>{
            e.classList.remove("active");
        });
        if(counter > 1){
            counter--;
            activeNow.previousElementSibling.classList.add("active");
        }else{
            sectionDivImg[sectionDivImg.length-1].classList.add("active");
            counter = sectionDivImg.length;
        }
    }
}

projectImgs = [];
let viewProject = document.querySelectorAll(".view-project");

viewProject.forEach((e)=>{
    e.addEventListener("click",(ele)=>{
        var projectId = ele.target.dataset.id;
        projectData(projectId);
    });
});

function projectData(projectId){
    var url = '/view_project/';

    fetch(url, {
        method: "POST",
        headers: {
            'content-type':'application/json',
            'X-CSRFToken':csrftoken,
        },
        body: JSON.stringify({'projectId':projectId})
    })

    .then((Response)=>{
        return Response.json()
    })

    .then((data)=>{
        dataCome = data.split(',');
        let proImgs = document.querySelectorAll('.section-view img');
        for(let i=0 ;i <proImgs.length; i++){
            proImgs[i].src = `/images/${dataCome[i]}`;
        }
    })
}

function getToken(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
  }
  const csrftoken = getToken('csrftoken');


let loading = '';
let loadMoreBtn = '';
let category = '';
$(document).ready(function(){

$("#q").on('keyup', function (e) {
        if (e.key === 'Enter' || e.keyCode === 13) {
            searchProduct(lang);
        }
    });

$("#q-mobile-123").on('keyup', function (e) {
        if (e.key === 'Enter' || e.keyCode === 13) {
            searchProductMobile(lang);
        }
    });
document.getElementsByClassName('index-video').play();


});

if (lang==='en'){
    loadMoreBtn = '<button onclick="loadMoreProduct()" type="submit" class="btn btn-primary load-more-btn" id="load-more-btn">\n' +
        '            more products\n' +
        '        </button>';

    loading = '<button type="submit" class="btn btn-primary load-more-btn" id="spinner-btn">\n' +
        '            <span class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span>\n' +
        '            loading... \n' +
        '        </button>';
}else{

    loadMoreBtn = '<button onclick="loadMoreProduct()" type="submit" class="btn btn-primary load-more-btn" id="load-more-btn">\n' +
        '            محصولات بیشتر\n' +
        '        </button>';

    loading = '<button type="submit" class="btn btn-primary load-more-btn" id="spinner-btn">\n' +
        '            <span class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span>\n' +
        '            ...لودینگ\n' +
        '        </button>';
}



function loadMoreProduct() {
    let lol = document.getElementById("lol");
    const sort = $('#sort').find(":selected").val();
    const lengths = $('.col-5').length;
    let value = ''
    if (category !== ''){
        let selectBox = document.getElementById(`${category}`);
        value = selectBox.options[selectBox.selectedIndex].value;
    }
    $.ajax({
        url: '/products/load-more/',
        data: {
            sort: sort,
            lengths: lengths,
            state: category,
            value:value
        },
        datatype: 'json',
        method: 'GET',
        beforeSend: function () {
            lol.innerHTML = loading ;
        },
        success: function (res) {
            if (res.status === 'success') {
                lol.innerHTML = loadMoreBtn;
                $('#product-ajax').append(res.data);
            } else {
                lol.classList.remove('lol');
                lol.classList.add('self-alert');
                lol.innerHTML = 'محصول دیگری وجود ندارد';
            }

        }
    });
}

function filterProduct2(cat, lang){
    let spinner = document.getElementById('spinner-middle');
    let load_more_btn = document.getElementById('load-more-btn');
    const sort = $('#sort').find(":selected").val();
    let productAjax = document.getElementById("container");
    let lol = document.getElementById("lol");


    let value = '';
    if(cat !== ''){
        let selectBox = document.getElementById(`${cat}`);
        value = selectBox.options[selectBox.selectedIndex].value;
        category = cat;
    }else {
        cat = category;
        let selectBox = document.getElementById(`${cat}`);
        value = selectBox.options[selectBox.selectedIndex].value;
    }


    $.ajax({
        url: '/products/filter/',
        data: {
            state:cat,
            value:value,
            sort:sort
        },
        datatype: 'json',
        method: 'GET',
        beforeSend: function () {
            load_more_btn.classList.remove('dis-n');
            productAjax.classList.add("filter-blur");
            lol.classList.add("filter-blur");
            spinner.classList.remove('dis-n');

        },
        success: function (res) {
            let text = '';
            if(lang==='en'){
                text = 'all';
            }else if(lang === 'fa'){
                 text = 'همه';
            }else {
                text = 'الجميع';
            }
            productAjax.classList.remove("filter-blur");
            lol.classList.remove("filter-blur");
            spinner.classList.add('dis-n');
            if (cat === "simpleBag"){
                $('span.current:eq(2)').text(`${text}`);
                $('span.current:eq(0)').text(`${text}`);

            }else if(cat === "productType"){
                $('span.current:eq(0)').text(`${text}`);
                $('span.current:eq(1)').text(`${text}`);
            }else if(cat === "stockBag"){
                 $('span.current:eq(1)').text(`${text}`);
                 $('span.current:eq(2)').text(`${text}`);
            }

            $('#product-ajax').html(res.data);
        }
    });


}




function filterProductIndex(cat, lang){
    let spinner = document.getElementById('spinner-middle');
    let lol = document.getElementById("lol");
    const sort = $('#sort').find(":selected").val();
    let value = ''
    if(cat !== ''){
        let selectBox = document.getElementById(`${cat}`);
        value = selectBox.options[selectBox.selectedIndex].value;
        category = cat;
    }else {
        cat = category;
        let selectBox = document.getElementById(`${cat}`);
        value = selectBox.options[selectBox.selectedIndex].value;
    }


    $.ajax({
        url: '/products/filter/',
        data: {
            state:cat,
            value:value,
            sort:sort
        },
        datatype: 'json',
        method: 'GET',
        beforeSend: function () {

            $(".col-5").each(function (index, item) {
                this.parentNode.removeChild(this);
            });
            spinner.classList.remove('dis-n');
        },
        success: function (res) {
            let text = '';
            if(lang==='en'){
                text = 'all';
            }else if(lang === 'fa'){
                 text = 'همه';
            }else {
                text = 'الجميع';
            }
            spinner.classList.add('dis-n');
            if (cat === "simpleBag"){
                $('span.current:eq(2)').text(`${text}`);
                $('span.current:eq(0)').text(`${text}`);

            }else if(cat === "productType"){
                $('span.current:eq(0)').text(`${text}`);
                $('span.current:eq(1)').text(`${text}`);
            }else if(cat === "stockBag"){
                 $('span.current:eq(1)').text(`${text}`);
                 $('span.current:eq(2)').text(`${text}`);
            }

            $('#product-ajax').html(res.data);
        }
    });


}

function searchProduct(lang) {
    const q = document.getElementById('q');

    $.ajax({
        url: '/products/search/',
        data: {
            q:q.value
        },
        datatype: 'json',
        method: 'GET',
        beforeSend: function () {

        },
        success: function (res) {
                if(res.status === 'success'){
                    $('#main').html(res.data);
                }else {
                    q.classList.add('self-red');
                    if(lang === 'fa'){
                        q.placeholder = 'کلمه ای وارد نکردید!';
                    }else if(lang === 'en'){
                        q.placeholder = 'no any words to search!';
                    }else {
                        q.placeholder = 'أنت لم تدخل كلمة واحدة !';
                    }
                }

        }
    });
}
function searchProductMobile(lang){
    const q = document.getElementById('q-mobile-123');
    console.log(q);
    $.ajax({
        url: '/products/search/',
        data: {
            q:q.value
        },
        datatype: 'json',
        method: 'GET',
        beforeSend: function () {

        },
        success: function (res) {
                if(res.status === 'success'){
                    $('#main').html(res.data);
                }else {
                    console.log(q.value);
                    q.classList.add('self-red');
                    if(lang === 'fa'){
                        q.placeholder = 'کلمه ای وارد نکردید!';
                    }else if(lang === 'en'){
                        q.placeholder = 'no any words to search!';
                    }else {
                        q.placeholder = 'أنت لم تدخل كلمة واحدة !';
                    }
                }

        }
    });
}

document.addEventListener('DOMContentLoaded', function() {
            var scrollLink = document.getElementById('scrollLink');
            scrollLink.addEventListener('click', function(e) {
                e.preventDefault();
                var targetId = this.getAttribute('href').substring(1);
                var targetElement = document.getElementById(targetId);
                var offsetTop = targetElement.offsetTop;

                // Smooth scroll animation
                window.scrollTo({
                    top: offsetTop,
                    behavior: 'smooth'
                });
            });
        });

document.addEventListener('DOMContentLoaded', function() {
            var scrollLink = document.getElementById('scrollLink2');
            scrollLink.addEventListener('click', function(e) {
                e.preventDefault();
                const popup = document.getElementById("popup");
                popup.classList.remove("active");
                var targetId = this.getAttribute('href').substring(1);
                var targetElement = document.getElementById(targetId);
                var offsetTop = targetElement.offsetTop;

                // Smooth scroll animation
                window.scrollTo({
                    top: offsetTop,
                    behavior: 'smooth'
                });
            });
        });


document.addEventListener('DOMContentLoaded', function() {
            var scrollLink = document.getElementById('scrollLink3');
            scrollLink.addEventListener('click', function(e) {
                e.preventDefault();
                var targetId = this.getAttribute('href').substring(1);
                var targetElement = document.getElementById(targetId);
                var offsetTop = targetElement.offsetTop;

                // Smooth scroll animation
                window.scrollTo({
                    top: offsetTop,
                    behavior: 'smooth'
                });
            });
        });


// new
document.addEventListener('DOMContentLoaded', function() {
            var scrollLink = document.getElementById('scrollLink5');
            scrollLink.addEventListener('click', function(e) {
                e.preventDefault();
                var targetId = this.getAttribute('href').substring(1);
                var targetElement = document.getElementById(targetId);
                var offsetTop = targetElement.offsetTop;

                // Smooth scroll animation
                window.scrollTo({
                    top: offsetTop,
                    behavior: 'smooth'
                });
            });
        });

function indexVideo(){
    const video = document.querySelector('.index-video');
        if (video.paused) {
          video.play();
        } else {
          video.pause();
        }
}
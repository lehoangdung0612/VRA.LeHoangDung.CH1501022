(function($) {
    Dropzone.options.formUpload = {
        maxFiles: 1,
        acceptedFiles: "image/*",
        init: function() {
            this.on("success", function(file, data) {
                setTimeout(function () {
                    initImageViewer(data);
                }, 500);
            });
        }
    };

    function initLazyLoad() {
        var bLazy = new Blazy({
            offset: 1000,
            success: function(element){
                setTimeout(function(){
                    $(element).closest('.loading').removeClass('loading')
                }, 100);
            }
        });
    }

    function initJcrop(element) {
        $(element).Jcrop({
            boxWidth: 600,
            onChange: recCoords,
            onSelect: recCoords
        });
    }

    function handleFormAction() {
        if ($('#search-frm').data('ajax-search')) {
            ///search by call ajax to Python API
            $('#btn-submit').on('click', function (e) {
                e.preventDefault();
                var template =  '<div id="search-container">' +
                                    '<a id="back-to-search" href="/">&larr; Back to search</a>' + 
                                    '<h4>Showing results of {0} images</h4>' + 
                                    '<ol class="list" type="1">{1}</ol>' +
                                '</div>';
                $.ajax({
                    method: 'get',
                    url: $('#search-frm').attr('action'),
                    data: $('#search-frm').serialize(),
                    timeout: 5000,
                    beforeSend: function () {
                        $('body').append('<div class="overlay"><div class="spinner"></div></div>');
                    },
                    success: function (result, status) {
                        if (result.data) {
                            var list = [];
                            for (var i = 0; i < result.data.length; i++) {
                                list.push(
                                    '<li class="image loading">' + 
                                        '<div class="content">' + 
                                            '<a class="link" href="/detail?id=' + encodeURIComponent(result.data[i].image) +
                                                '<img class="b-lazy" src="data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==" data-src="' + result.data[i].image + '">' +
                                            '</a>' + 
                                            '<div class="score">Score = ' + result.data[i].score + '</div>' +
                                        '</div>' +
                                    '</li>'
                                );
                            }
                            template = template.replace('{0}', result.data.length);
                            template = template.replace('{1}', list.join(''));
                            $('#img-container').html(template);
                            initLazyLoad();
                        } else {
                            $('#img-container').html('<h4>' + result.error + '</h4>');
                        }
                        $('.overlay').remove();
                    },
                    error: function (jqXHR , status, e) {
                        if (status === 'timeout') {
                            $('#btn-submit').click();
                        }
                    }
                });
            });
        } else {
            ///search by submiting form to Python API
            $('#search-frm').on('submit', function () {
                $('body').append('<div class="overlay"><div class="spinner"></div></div>');
            });
        }
    }

    function initImageViewer(data) {
        if ($('#formUpload').data('external-upload')) {
            ///upload data to Python host
            $('#image-viewer img').attr('src', data.fileSrc);
            $('#query').val(data.fileName);
            $('.viewer').show();
            $('.form-upload').hide();
        } else {
            ///upload data to this host
            $('#img-container').html(data);
        }

        initJcrop($('#image-viewer img'));
        handleFormAction();
    }

    function recCoords (c) {
        $('#crop-x').val(Math.round(c.x));
        $('#crop-y').val(Math.round(c.y));
        $('#crop-w').val(Math.round(c.w));
        $('#crop-h').val(Math.round(c.h));
    }
    
    function updateMainHeight() {
        var winHeight = $(window).height();
        if ($('body').height() < winHeight) {
            $('#main-content').css('minHeight', winHeight - $('#header').height() - $('#footer').height());
        }
    }

    updateMainHeight();
    initLazyLoad();
    initJcrop($('#image-viewer img:visible'));
    handleFormAction();

    setTimeout(function () {
        updateMainHeight();
    }, 2000);

    $(window).on('resize', function () {
        updateMainHeight();
    });

}(window.jQuery));
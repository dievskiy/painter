$.getScript("static/js/canvas-drawing.js", function () {

    const DEFAULT_COLOR = [39, 108, 184];
    const $canvas = $('#canvas-container');
    const $publish = $("#publish");
    let published = false;

    const cfd = new CanvasFreeDrawing.default({
        elementId: 'cfd',
        width: $canvas.width(),
        height: $canvas.height(),
        showWarnings: true,
    });
    $(window).resize(function () {
        var width = $canvas.width();
        var height = $canvas.height();
        $("#cfd").css({"height": height + "px", "width": width + "px"});
    });

    cfd.setDrawingColor(DEFAULT_COLOR);

    // init color picker
    $('#color-picker').spectrum({
        type: "color",
        move: function (c) {
            let rgb = c.toRgb();
            cfd.setDrawingColor([rgb.r, rgb.g, rgb.b, rgb.a]);
        }
    });

    $('.sp-replacer')[0].classList.add("w-50");
    $('.sp-replacer')[0].classList.add("m-2");

    $('#clear').click(function (event) {
        cfd.clear()
    });
    $('#undo').click(function (event) {
        cfd.undo()
    });
    $('#redo').click(function (event) {
        cfd.redo()
    });

    $publish.click(function (event) {
        // $(this).html("<img src='{{ url_for('static', filename='img/loading.gif') }}'>");
        if (published) return;
        $(this).html('<img src="../../static/img/loading.gif">');
        let image = cfd.save();
        $.ajax({
            url: "/api/v1/publish",
            type: "POST",
            data: JSON.stringify({data: image}),
            contentType: "application/json; charset=utf-8",
            dataType: "json",
        }).done(function (data) {
            published = true;
            $publish[0].firstChild.remove();
            $publish.html('<input class="p-0 input-group-text input-group" value="' + data['_link'] + '"/>');
        })
    });
});

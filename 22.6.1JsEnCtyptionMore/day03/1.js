function get_data(t, e) {
    var n;
    s.info("Start session");
    var r = i.Utils.encryptSessions(JSON.stringify(N));
    $.ajax({
        type: "POST",
        url: (null === (n = i.Utils.getClientConfig()) || void 0 === n ? void 0 : n.baseUrl) + "/api/v1/sessions",
        beforeSend: function (t) {
            t.setRequestHeader("Fetch-Mode", navigator.userAgent),
                t.setRequestHeader("etag", k)
        },
        xhrFields: {
            withCredentials: !0
        },
        crossDomain: !0,
        data: JSON.stringify({
            data: r
        }),
        contentType: "application/json; charset=utf-8",
        dataType: "json"
    }).done((function (e) {
            t(e)
        }
    )).fail((function (t, n, r) {
            e({
                _type: "network",
                status: t.status,
                text: t.responseText
            })
        }
    ))
}
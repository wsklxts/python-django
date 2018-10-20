/**
 * Created by Administrator on 2018/10/11.
 */
function parseString(str, obj) {
    Object.keys(obj).forEach(function (key) {
        str = str.replace(/\{\{(.*?)\}\}/g, function (m, k) {
                return obj[k.trim()]
            }
        )
    })
    return str;
}
$.getUrlParam = function (name) {
    var reg = new RegExp("(^|&)" + name + "=([^&]*)(&|$)");
    var r = window.location.search.substr(1).match(reg);
    if (r != null) return unescape(r[2]);
    return null;
}
var url = "http://127.0.0.1:8899/"






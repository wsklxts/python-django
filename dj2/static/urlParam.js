  function changeURLArg(url, arg, arg_val) {
        /// <summary>
        /// url参数替换值
        /// </summary>
        /// <param name="url">目标url </param>
        /// <param name="arg">需要替换的参数名称</param>
        ///<param name="arg_val">替换后的参数的值</param>
        /// <returns>参数替换后的url </returns>
        var pattern = arg + '=([^&]*)';
        var replaceText = arg + '=' + arg_val;
        if (url.match(pattern)) {
            var tmp = '/(' + arg + '=)([^&]*)/gi';
            tmp = url.replace(eval(tmp), replaceText);
            return tmp;
        } else {
            if (url.match('[\?]')) {
                return url + '&' + replaceText;
            } else {
                return url + '?' + replaceText;
            }
        }
        return url + '\n' + arg + '\n' + arg_val;
    }
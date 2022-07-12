function get_result(result) {
    if (result && result.retcode === 0) {
        me.setServerTime(result.servertime);
        me.nonce = result.nonce;
        me.rsaPubkey = result.pubkey;
        me.rsakv = result.rsakv;
        pcid = result.pcid;
        preloginTime = (new Date()).getTime() - preloginTimeStart - (parseInt(result.exectime, 10) || 0)
    }
    if (typeof callback == "function") {
        callback(result)
    }
}
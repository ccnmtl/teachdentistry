function getVisibleViewport() {
    var viewportwidth;
    var viewportheight;
    
    // the more standards compliant browsers (mozilla/netscape/opera/IE7) use window.innerWidth and window.innerHeight
    if (typeof window.innerWidth != 'undefined') {
         viewportwidth = window.innerWidth;
         viewportheight = window.innerHeight;
    } else if (typeof document.documentElement !== 'undefined' &&
         typeof document.documentElement.clientWidth !=
        'undefined' && document.documentElement.clientWidth !== 0) {
        // IE6 in standards compliant mode (i.e. with a valid doctype as the first line in the document)
        viewportwidth = document.documentElement.clientWidth;
        viewportheight = document.documentElement.clientHeight;
    } else {
        // older versions of IE
        viewportwidth = document.getElementsByTagName('body')[0].clientWidth;
        viewportheight = document.getElementsByTagName('body')[0].clientHeight;
    }
    
    return { height: viewportheight -
                (30 + document.getElementById("masthead").clientHeight +
                        document.getElementById("primarynav").clientHeight),
             width: viewportwidth };
}
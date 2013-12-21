<!doctype html>
<html class="no-js" lang="en">

<head>
    <meta charset="utf-8" />
    <title>MyBitcoind</title>
    <link rel="stylesheet" href="/static/css/foundation.css" />
    <link rel="stylesheet" href="/static/css/css.css" />
    <script src="/static/js/modernizr.js"></script>
</head>

<body>
    <nav class="top-bar" data-topbar>
        <ul class="title-area">
            <li class="name">
                <h1><a href="#">MyBitcoind</a></h1> 
            </li>
            <li class="toggle-topbar menu-icon"><a href="#"><span>Menu</span></a>
            </li>
        </ul>
        <section class="top-bar-section">
            <ul class="right">
                <li class="divider"></li>
                <li>
                    <a href="#" class="bold">Balance: {{ balance }}฿</a>
                </li>
            </ul>
            <ul class="left">
                <li class="has-dropdown">
                    <a href="#">Addresses</a>
                        <ul class="dropdown">
                            <li><a href="/addresses/list/">Address List</a></li>
                            <li><a href="/addresses/unspent/">Unspent Outputs</a></li>
                            <li><a href="/addresses/received/">Received</a></li>
                        </ul>
                    </li>
                </li>
            </ul>
            <ul class="left">
                <li class="has-dropdown">
                    <a href="#">Import</a>
                        <ul class="dropdown">
                            <li><a href="/import/list/">List</a></li>
                            <li><a href="/import/wallet/">Wallet</a></li>
                        </ul>
                    </li>
                </li>
            </ul>
        </section>
    </nav>

    <div class="row">
        <div class="large-12 medium-12 columns">
            %include
        </div>
    </div>

    <script src="/static/js/jquery.js"></script>
    <script src="/static/js/foundation.min.js"></script>
    <script src="/static/js/stupidtable.min.js"></script>
    <script>
        $(document).foundation();
        $(".sortable").stupidtable();
    </script>
</body>

</html>

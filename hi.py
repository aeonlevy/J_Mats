from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import pandas as pd
import requests
import csv

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)  # Use headless=True if needed
    page = browser.new_page()
    page.goto("https://tokyofashion.com/photos/?location=Harajuku")  # Change to your target website
    page.wait_for_load_state("networkidle")  # Wait until the page fully loads
    print(page.content())  # Extract HTML content
    browser.close()

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)  # Use headless=True if needed
    page = browser.new_page()
    page.goto("https://tokyofashion.com/photos/?location=Shibuya")  # Change to your target website
    page.wait_for_load_state("networkidle")  # Wait until the page fully loads
    print(page.content())  # Extract HTML content
    browser.close()
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)  # Use headless=True if needed
    page = browser.new_page()
    page.goto("https://tokyofashion.com/photos/?location=Shinjuku")  # Change to your target website
    page.wait_for_load_state("networkidle")  # Wait until the page fully loads
    print(page.content())  # Extract HTML content
    browser.close()



html = """<!DOCTYPE html><html lang="en-US"><head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<link rel="preload" href="https://tokyofashion.com/wp-content/themes/tokyofashion/fonts/fontawesome-webfont.woff2?v=4.7.0" as="font" type="font/woff2" crossorigin=""><link rel="profile" href="https://gmpg.org/xfn/11">

	<link media="all" href="https://tokyofashion.com/wp-content/cache/autoptimize/css/autoptimize_f035207383e8e457d3776c8597bfc517.css" rel="stylesheet"><title>Shibuya Japanese Street Fashion Photos – Tokyo Fashion</title>
<meta name="robots" content="max-image-preview:large">
	
	<link href="https://fonts.gstatic.com" crossorigin="anonymous" rel="preconnect">
<link rel="alternate" type="application/rss+xml" title="Tokyo Fashion » Feed" href="https://tokyofashion.com/feed/">
<link rel="alternate" type="application/rss+xml" title="Tokyo Fashion » Comments Feed" href="https://tokyofashion.com/comments/feed/">
<link rel="alternate" type="application/rss+xml" title="Tokyo Fashion » Tokyo Street Fashion Photos Comments Feed" href="https://tokyofashion.com/photos/feed/">











<script src="https://tokyofashion.com/wp-includes/js/jquery/jquery.min.js?ver=3.7.1" id="jquery-core-js"></script>




<script id="responsive-lightbox-js-before">
var rlArgs = {"script":"magnific","selector":"lightbox","customEvents":"","activeGalleries":true,"disableOn":0,"midClick":true,"preloader":true,"closeOnContentClick":true,"closeOnBgClick":true,"closeBtnInside":true,"showCloseBtn":true,"enableEscapeKey":true,"alignTop":false,"fixedContentPos":"auto","fixedBgPos":"auto","autoFocusLast":true,"woocommerce_gallery":false,"ajaxurl":"https:\/\/tokyofashion.com\/wp-admin\/admin-ajax.php","nonce":"26d353d815","preview":false,"postId":1308,"scriptExtension":false};
</script>

<link rel="https://api.w.org/" href="https://tokyofashion.com/wp-json/"><link rel="alternate" title="JSON" type="application/json" href="https://tokyofashion.com/wp-json/wp/v2/pages/1308"><link rel="EditURI" type="application/rsd+xml" title="RSD" href="https://tokyofashion.com/xmlrpc.php?rsd">
<meta name="generator" content="WordPress 6.7.2">
<link rel="canonical" href="https://tokyofashion.com/photos/">
<link rel="shortlink" href="https://tokyofashion.com/?p=1308">
<link rel="alternate" title="oEmbed (JSON)" type="application/json+oembed" href="https://tokyofashion.com/wp-json/oembed/1.0/embed?url=https%3A%2F%2Ftokyofashion.com%2Fphotos%2F">
<link rel="alternate" title="oEmbed (XML)" type="text/xml+oembed" href="https://tokyofashion.com/wp-json/oembed/1.0/embed?url=https%3A%2F%2Ftokyofashion.com%2Fphotos%2F&amp;format=xml">
<link rel="pingback" href="https://tokyofashion.com/xmlrpc.php">		
		</head>

<body class="home">
<div class="header-menu_mob">
    <nav role="navigation">
        <div class="menu-main-container"><ul id="Main" class="menu"><li id="menu-item-94790" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-home menu-item-94790"><a href="https://tokyofashion.com/">Home</a></li>
<li id="menu-item-94791" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-94791"><a href="https://tokyofashion.com/articles/">Articles</a></li>
<li id="menu-item-94792" class="menu-item menu-item-type-post_type menu-item-object-page current-menu-item page_item page-item-1308 current_page_item menu-item-94792"><a href="https://tokyofashion.com/photos/" aria-current="page">Street Photos</a></li>
<li id="menu-item-94793" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-94793"><a href="https://tokyofashion.com/brands/">Brands</a></li>
<li id="menu-item-94794" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-94794"><a href="https://tokyofashion.com/fashion-map/">Fashion Map</a></li>
<li id="menu-item-94795" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-94795"><a href="https://tokyofashion.com/music/">Music</a></li>
</ul></div>    </nav>
    <div class="header-menu_close fa fa-times"></div>
</div>
<div class="main-wrapper">
    <header role="banner" class="header">
        <div class="inner-wrapper header-wrapper">
            <div class="header-block">
                <div class="header-logo logo">
                    	<a href="https://tokyofashion.com/" class="custom-logo-link" rel="home"><noscript><img width="245" height="118" src="https://tokyofashion.com/wp-content/uploads/2021/03/cropped-logo-1.gif" class="custom-logo" alt="Tokyo Fashion" decoding="async" /></noscript><img width="245" height="118" src="https://tokyofashion.com/wp-content/uploads/2021/03/cropped-logo-1.gif" data-src="https://tokyofashion.com/wp-content/uploads/2021/03/cropped-logo-1.gif" class="custom-logo lazyloaded" alt="Tokyo Fashion" decoding="async"></a>                </div>
                <div class="header-menu">
                    <nav role="navigation">
                        <button class="menu-toggle" aria-controls="primary-menu" aria-expanded="false">Primary Menu</button>
                        <div class="menu-main-container"><ul id="Main" class="menu"><li class="menu-item menu-item-type-post_type menu-item-object-page menu-item-home menu-item-94790"><a href="https://tokyofashion.com/">Home</a></li>
<li class="menu-item menu-item-type-post_type menu-item-object-page menu-item-94791"><a href="https://tokyofashion.com/articles/">Articles</a></li>
<li class="menu-item menu-item-type-post_type menu-item-object-page current-menu-item page_item page-item-1308 current_page_item menu-item-94792"><a href="https://tokyofashion.com/photos/" aria-current="page">Street Photos</a></li>
<li class="menu-item menu-item-type-post_type menu-item-object-page menu-item-94793"><a href="https://tokyofashion.com/brands/">Brands</a></li>
<li class="menu-item menu-item-type-post_type menu-item-object-page menu-item-94794"><a href="https://tokyofashion.com/fashion-map/">Fashion Map</a></li>
<li class="menu-item menu-item-type-post_type menu-item-object-page menu-item-94795"><a href="https://tokyofashion.com/music/">Music</a></li>
</ul></div>                    </nav>
                </div>
            </div>
            <div class="header-block">
                <div class="header-sandwich fa fa-bars"></div>
                <div class="header-block_inner">
                    <div class="header-social">
                        <ul>
                            <li><a href="https://www.facebook.com/TokyoFashion" class="fa fa-facebook" target="_blank"></a></li>
                            <li><a href="https://twitter.com/tokyofashion" class="fa fa-twitter" target="_blank"></a></li>
                            <li><a href="https://feeds.feedburner.com/TokyoFashion" class="fa fa-rss" target="_blank"></a></li>
                            <li><a href="https://feedburner.google.com/fb/a/mailverify?uri=TokyoFashion&amp;loc=en_US" class="fa fa-envelope" target="_blank"></a></li>
                        </ul>
                    </div>
                    <div class="header-search">
                        <a href="#" title="Search" class="header-search_link fa fa-search"></a>
                        <div class="header-search_overlay">
                            <form method="get" class="search-form" action="https://tokyofashion.com/">
                                <label>
                                    <span class="screen-reader-text">Search for:</span>
                                    <input type="search" class="search-field" placeholder="Type and hit enter..." value="" name="s" title="Search for:">
                                </label>
                                <button type="submit" class="search-submit"><i class="fa fa-search"></i></button>
                            </form>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </header>

<div id="content">
		  <main role="main" class="main-content">
                <div class="inner-wrapper main-inner_wrapper">
                    <div class="content-left">
					<a class="backlink" href="https://tokyofashion.com/photos/">« Back to Recent Tokyo Street Fashion photos</a><br><br>
					<div 7="" class="contentpanel bm-half">
						<h2 class="contentpaneltitle">Shibuya Japanese Street Fashion Photos<!--  --></h2>
						<div class="photos-block"><ul class="photos-list">	<li>
				<a href="https://tokyofashion.com/japanese-fashion-beauty-vintage-kimono-street-style-tokyo/" class="photo" title="Japanese Fashion &amp; Beauty TikToker in Vintage Kimono Street Style in Shibuya, Tokyo">
			<noscript><img src="https://tokyofashion.com/wp-content/uploads/2021/09/2021-09-04-001-002-NK-Harajuku-DZ7-0853.jpg" alt="Japanese Fashion &amp; Beauty TikToker in Vintage Kimono Street Style in Shibuya, Tokyo" width="140" height="180" loading="lazy"></noscript><img class=" lazyloaded" src="https://tokyofashion.com/wp-content/uploads/2021/09/2021-09-04-001-002-NK-Harajuku-DZ7-0853.jpg" data-src="https://tokyofashion.com/wp-content/uploads/2021/09/2021-09-04-001-002-NK-Harajuku-DZ7-0853.jpg" alt="Japanese Fashion &amp; Beauty TikToker in Vintage Kimono Street Style in Shibuya, Tokyo" width="140" height="180" loading="lazy">
		</a>
	</li>
	<li>
				<a href="https://tokyofashion.com/handmade-japanese-kimono-street-tokyo-coming-of-age-day/" class="photo" title="Handmade Japanese Kimono on the Street in Tokyo For Coming of Age Day">
			<noscript><img src="https://tokyofashion.com/wp-content/uploads/2020/01/Handmade-Kimono-Street-Style-Tokyo-20200113DZ77082.jpg" alt="Handmade Japanese Kimono on the Street in Tokyo For Coming of Age Day" width="140" height="180" loading="lazy"></noscript><img class=" lazyloaded" src="https://tokyofashion.com/wp-content/uploads/2020/01/Handmade-Kimono-Street-Style-Tokyo-20200113DZ77082.jpg" data-src="https://tokyofashion.com/wp-content/uploads/2020/01/Handmade-Kimono-Street-Style-Tokyo-20200113DZ77082.jpg" alt="Handmade Japanese Kimono on the Street in Tokyo For Coming of Age Day" width="140" height="180" loading="lazy">
		</a>
	</li>
	<li>
				<a href="https://tokyofashion.com/tokyo-streetwear-zara-never-mind-the-xu-snakeskin-pants-choker-chain-attagirl/" class="photo" title="All Black Tokyo Streetwear Style w/ Zara, Never Mind the XU Snakeskin Pants, Choker w/ Body Chain &amp; Attagirl Lace-Up Shoes">
			<noscript><img src="https://tokyofashion.com/wp-content/uploads/2019/05/NK-2019-04-08-010-001-Harajuku-DZ7-0955-2.jpg" alt="All Black Tokyo Streetwear Style w/ Zara, Never Mind the XU Snakeskin Pants, Choker w/ Body Chain &amp; Attagirl Lace-Up Shoes" width="140" height="180" loading="lazy"></noscript><img class=" lazyloaded" src="https://tokyofashion.com/wp-content/uploads/2019/05/NK-2019-04-08-010-001-Harajuku-DZ7-0955-2.jpg" data-src="https://tokyofashion.com/wp-content/uploads/2019/05/NK-2019-04-08-010-001-Harajuku-DZ7-0955-2.jpg" alt="All Black Tokyo Streetwear Style w/ Zara, Never Mind the XU Snakeskin Pants, Choker w/ Body Chain &amp; Attagirl Lace-Up Shoes" width="140" height="180" loading="lazy">
		</a>
	</li>
	<li>
				<a href="https://tokyofashion.com/tokyo-styles-twin-braids-furry-hat-elcasion-vintage-suit-gucci-fjallraven-kanken-george-cox/" class="photo" title="Tokyo Streetwear Styles w/ Twin Braids, Furry Hat, Elcasion Vintage Suit, Gucci Rings, Fjallraven Kanken Backpack &amp; George Cox Creepers">
			<noscript><img src="https://tokyofashion.com/wp-content/uploads/2019/05/NK-2019-04-08-017-001-Harajuku-DZ7-1156.jpg" alt="Tokyo Streetwear Styles w/ Twin Braids, Furry Hat, Elcasion Vintage Suit, Gucci Rings, Fjallraven Kanken Backpack &amp; George Cox Creepers" width="140" height="180" loading="lazy"></noscript><img class=" lazyloaded" src="https://tokyofashion.com/wp-content/uploads/2019/05/NK-2019-04-08-017-001-Harajuku-DZ7-1156.jpg" data-src="https://tokyofashion.com/wp-content/uploads/2019/05/NK-2019-04-08-017-001-Harajuku-DZ7-1156.jpg" alt="Tokyo Streetwear Styles w/ Twin Braids, Furry Hat, Elcasion Vintage Suit, Gucci Rings, Fjallraven Kanken Backpack &amp; George Cox Creepers" width="140" height="180" loading="lazy">
		</a>
	</li>
	<li>
				<a href="https://tokyofashion.com/kawaii-tokyo-girls-street-styles-purple-hair-leopard-coat-rrr-vintage-checkered-skirt/" class="photo" title="Kawaii Tokyo Girls Street Styles w/ Purple Hair, WEGO Leopard Coat, RRR Vintage Blazer, Checkered Skirt">
			<noscript><img src="https://tokyofashion.com/wp-content/uploads/2019/05/NK-2019-04-08-013-001-Harajuku-DZ7-1037-3.jpg" alt="Kawaii Tokyo Girls Street Styles w/ Purple Hair, WEGO Leopard Coat, RRR Vintage Blazer, Checkered Skirt" width="140" height="180" loading="lazy"></noscript><img class=" lazyloaded" src="https://tokyofashion.com/wp-content/uploads/2019/05/NK-2019-04-08-013-001-Harajuku-DZ7-1037-3.jpg" data-src="https://tokyofashion.com/wp-content/uploads/2019/05/NK-2019-04-08-013-001-Harajuku-DZ7-1037-3.jpg" alt="Kawaii Tokyo Girls Street Styles w/ Purple Hair, WEGO Leopard Coat, RRR Vintage Blazer, Checkered Skirt" width="140" height="180" loading="lazy">
		</a>
	</li>
	<li>
				<a href="https://tokyofashion.com/street-styles-two-tone-hair-leopard-hat-faith-tokyo-pleather-pants-marine-serre-kirsch/" class="photo" title="Japanese Street Styles w/ Two-Tone Hair, Leopard Hat, Faith Tokyo Pleather Pants, Gallerie, Marine Serre, Kirsch, Guess &amp; Yosuke">
			<noscript><img src="https://tokyofashion.com/wp-content/uploads/2019/05/NK-2019-04-08-015-001-Harajuku-DZ7-1088.jpg" alt="Japanese Street Styles w/ Two-Tone Hair, Leopard Hat, Faith Tokyo Pleather Pants, Gallerie, Marine Serre, Kirsch, Guess &amp; Yosuke" width="140" height="180" loading="lazy"></noscript><img class=" lazyloaded" src="https://tokyofashion.com/wp-content/uploads/2019/05/NK-2019-04-08-015-001-Harajuku-DZ7-1088.jpg" data-src="https://tokyofashion.com/wp-content/uploads/2019/05/NK-2019-04-08-015-001-Harajuku-DZ7-1088.jpg" alt="Japanese Street Styles w/ Two-Tone Hair, Leopard Hat, Faith Tokyo Pleather Pants, Gallerie, Marine Serre, Kirsch, Guess &amp; Yosuke" width="140" height="180" loading="lazy">
		</a>
	</li>
	<li>
				<a href="https://tokyofashion.com/layered-ruffles-tokyo-street-fashion-w-birdcage-veil-belts-kinji-vintage-yosuke/" class="photo" title="Layered Ruffles Tokyo Street Fashion w/ Birdcage Veil, Sheer Blouse, Multiple Belts, Kinji Vintage &amp; Yosuke Boots">
			<noscript><img src="https://tokyofashion.com/wp-content/uploads/2019/05/NK-2019-04-08-014-003-Harajuku-DZ7-1075-2.jpg" alt="Layered Ruffles Tokyo Street Fashion w/ Birdcage Veil, Sheer Blouse, Multiple Belts, Kinji Vintage &amp; Yosuke Boots" width="140" height="180" loading="lazy"></noscript><img class=" lazyloaded" src="https://tokyofashion.com/wp-content/uploads/2019/05/NK-2019-04-08-014-003-Harajuku-DZ7-1075-2.jpg" data-src="https://tokyofashion.com/wp-content/uploads/2019/05/NK-2019-04-08-014-003-Harajuku-DZ7-1075-2.jpg" alt="Layered Ruffles Tokyo Street Fashion w/ Birdcage Veil, Sheer Blouse, Multiple Belts, Kinji Vintage &amp; Yosuke Boots" width="140" height="180" loading="lazy">
		</a>
	</li>
	<li>
				<a href="https://tokyofashion.com/tokyo-style-colorful-bob-hairstyle-bubbles-lace-top-corset-pleated-skirt/" class="photo" title="Tokyo Streetwear Style w/ Colorful Bob Hairstyle, Bubbles Lace Top, Plaid Corset Top, Pleated Skirt &amp; Platform Heels">
			<noscript><img src="https://tokyofashion.com/wp-content/uploads/2019/05/NK-2019-04-08-008-001-Harajuku-DZ7-0902-2.jpg" alt="Tokyo Streetwear Style w/ Colorful Bob Hairstyle, Bubbles Lace Top, Plaid Corset Top, Pleated Skirt &amp; Platform Heels" width="140" height="180" loading="lazy"></noscript><img class=" lazyloaded" src="https://tokyofashion.com/wp-content/uploads/2019/05/NK-2019-04-08-008-001-Harajuku-DZ7-0902-2.jpg" data-src="https://tokyofashion.com/wp-content/uploads/2019/05/NK-2019-04-08-008-001-Harajuku-DZ7-0902-2.jpg" alt="Tokyo Streetwear Style w/ Colorful Bob Hairstyle, Bubbles Lace Top, Plaid Corset Top, Pleated Skirt &amp; Platform Heels" width="140" height="180" loading="lazy">
		</a>
	</li>
	<li>
				<a href="https://tokyofashion.com/tokyo-streetwear-metal-vampire-fangs-myob-pink-house-kobinai/" class="photo" title="Pink Tokyo Streetwear Styles w/ Metal Vampire Fangs, M.Y.O.B., Pink House, Kobinai &amp; Vivienne Westwood,">
			<noscript><img src="https://tokyofashion.com/wp-content/uploads/2019/05/NK-2019-04-08-007-001-Harajuku-DZ7-0854.jpg" alt="Pink Tokyo Streetwear Styles w/ Metal Vampire Fangs, M.Y.O.B., Pink House, Kobinai &amp; Vivienne Westwood," width="140" height="180" loading="lazy"></noscript><img class=" lazyloaded" src="https://tokyofashion.com/wp-content/uploads/2019/05/NK-2019-04-08-007-001-Harajuku-DZ7-0854.jpg" data-src="https://tokyofashion.com/wp-content/uploads/2019/05/NK-2019-04-08-007-001-Harajuku-DZ7-0854.jpg" alt="Pink Tokyo Streetwear Styles w/ Metal Vampire Fangs, M.Y.O.B., Pink House, Kobinai &amp; Vivienne Westwood," width="140" height="180" loading="lazy">
		</a>
	</li>
	<li>
				<a href="https://tokyofashion.com/acid-wash-denim-snakeskin-print-street-styles-tokyo-evris-one-spo-rasvoa/" class="photo" title="Acid Wash Denim &amp; Snakeskin Print Street Styles in Tokyo w/ Evris, One Spo, Rasvoa, WEGO, Dickies &amp; New Balance">
			<noscript><img src="https://tokyofashion.com/wp-content/uploads/2019/05/NK-2019-04-08-004-002-Harajuku-DZ7-0731-2.jpg" alt="Acid Wash Denim &amp; Snakeskin Print Street Styles in Tokyo w/ Evris, One Spo, Rasvoa, WEGO, Dickies &amp; New Balance" width="140" height="180" loading="lazy"></noscript><img class=" lazyloaded" src="https://tokyofashion.com/wp-content/uploads/2019/05/NK-2019-04-08-004-002-Harajuku-DZ7-0731-2.jpg" data-src="https://tokyofashion.com/wp-content/uploads/2019/05/NK-2019-04-08-004-002-Harajuku-DZ7-0731-2.jpg" alt="Acid Wash Denim &amp; Snakeskin Print Street Styles in Tokyo w/ Evris, One Spo, Rasvoa, WEGO, Dickies &amp; New Balance" width="140" height="180" loading="lazy">
		</a>
	</li>
	<li>
				<a href="https://tokyofashion.com/x-girl-japan-suit-street-style-vantan-fashion-school-tokyo/" class="photo" title="X-Girl Japan Suit Street Style at Vantan Fashion School Entrance Ceremony in Tokyo">
			<noscript><img src="https://tokyofashion.com/wp-content/uploads/2019/04/Vantan-XGirl-Street-Fashion-Tokyo-20190408DZ70780.jpg" alt="X-Girl Japan Suit Street Style at Vantan Fashion School Entrance Ceremony in Tokyo" width="140" height="180" loading="lazy"></noscript><img class=" lazyloaded" src="https://tokyofashion.com/wp-content/uploads/2019/04/Vantan-XGirl-Street-Fashion-Tokyo-20190408DZ70780.jpg" data-src="https://tokyofashion.com/wp-content/uploads/2019/04/Vantan-XGirl-Street-Fashion-Tokyo-20190408DZ70780.jpg" alt="X-Girl Japan Suit Street Style at Vantan Fashion School Entrance Ceremony in Tokyo" width="140" height="180" loading="lazy">
		</a>
	</li>
	<li>
				<a href="https://tokyofashion.com/aqua-hair-faux-fur-myob-zara-kimono-dior/" class="photo" title="Vantan Students in Aqua Hair, Faux Fur Coat, Kimono Dress, MYOB, Zara, Dior, H&amp;M, (ME) Harajuku &amp; Anna Sui Quilted Bag">
			<noscript><img src="https://tokyofashion.com/wp-content/uploads/2019/05/NK-2019-04-08-001-001-Harajuku-DZ7-0600.jpg" alt="Vantan Students in Aqua Hair, Faux Fur Coat, Kimono Dress, MYOB, Zara, Dior, H&amp;M, (ME) Harajuku &amp; Anna Sui Quilted Bag" width="140" height="180" loading="lazy"></noscript><img class=" lazyloaded" src="https://tokyofashion.com/wp-content/uploads/2019/05/NK-2019-04-08-001-001-Harajuku-DZ7-0600.jpg" data-src="https://tokyofashion.com/wp-content/uploads/2019/05/NK-2019-04-08-001-001-Harajuku-DZ7-0600.jpg" alt="Vantan Students in Aqua Hair, Faux Fur Coat, Kimono Dress, MYOB, Zara, Dior, H&amp;M, (ME) Harajuku &amp; Anna Sui Quilted Bag" width="140" height="180" loading="lazy">
		</a>
	</li>
	<li>
				<a href="https://tokyofashion.com/fashion-student-designer-in-blue-hair-black-mask-flat-paisley-print-quilted-dress-platform-sequin-boots/" class="photo" title="Fashion Student &amp; Designer in Blue Hair, Black Mask, Flat Paisley Print Quilted Dress &amp; Platform Sequin Boots">
			<noscript><img src="https://tokyofashion.com/wp-content/uploads/2019/05/NK-2019-04-08-002-001-Harajuku-DZ7-0647-2.jpg" alt="Fashion Student &amp; Designer in Blue Hair, Black Mask, Flat Paisley Print Quilted Dress &amp; Platform Sequin Boots" width="140" height="180" loading="lazy"></noscript><img class=" lazyloaded" src="https://tokyofashion.com/wp-content/uploads/2019/05/NK-2019-04-08-002-001-Harajuku-DZ7-0647-2.jpg" data-src="https://tokyofashion.com/wp-content/uploads/2019/05/NK-2019-04-08-002-001-Harajuku-DZ7-0647-2.jpg" alt="Fashion Student &amp; Designer in Blue Hair, Black Mask, Flat Paisley Print Quilted Dress &amp; Platform Sequin Boots" width="140" height="180" loading="lazy">
		</a>
	</li>
	<li>
				<a href="https://tokyofashion.com/chic-womens-suit-fashion-in-shibuya-w-dark-lipstick-orange-suit-waist-bag-leopard-print-creepers/" class="photo" title="Chic Women's Suit Fashion in Shibuya w/ Dark Lipstick, Orange Suit, Waist Bag &amp; Leopard Print Creepers">
			<noscript><img src="https://tokyofashion.com/wp-content/uploads/2019/05/NK-2019-04-08-003-001-Harajuku-DZ7-0697-2.jpg" alt="Chic Women&#039;s Suit Fashion in Shibuya w/ Dark Lipstick, Orange Suit, Waist Bag &amp; Leopard Print Creepers" width="140" height="180" loading="lazy"></noscript><img class=" lazyloaded" src="https://tokyofashion.com/wp-content/uploads/2019/05/NK-2019-04-08-003-001-Harajuku-DZ7-0697-2.jpg" data-src="https://tokyofashion.com/wp-content/uploads/2019/05/NK-2019-04-08-003-001-Harajuku-DZ7-0697-2.jpg" alt="Chic Women's Suit Fashion in Shibuya w/ Dark Lipstick, Orange Suit, Waist Bag &amp; Leopard Print Creepers" width="140" height="180" loading="lazy">
		</a>
	</li>
	<li>
				<a href="https://tokyofashion.com/all-black-street-fashion-w-platinum-blonde-hair-cape-coat-maxi-skirt-w-lace-panel-anna-sui-bag-a-dr-martens-boots/" class="photo" title="All Black Street Fashion w/ Platinum Blonde Hair, Cape Coat, Maxi Skirt w/ Lace Panel, Anna Sui Bag &amp;a Dr. Martens Boots">
			<noscript><img src="https://tokyofashion.com/wp-content/uploads/2019/05/NK-2019-04-08-006-001-Harajuku-DZ7-0823.jpg" alt="All Black Street Fashion w/ Platinum Blonde Hair, Cape Coat, Maxi Skirt w/ Lace Panel, Anna Sui Bag &amp;a Dr. Martens Boots" width="140" height="180" loading="lazy"></noscript><img class=" lazyloaded" src="https://tokyofashion.com/wp-content/uploads/2019/05/NK-2019-04-08-006-001-Harajuku-DZ7-0823.jpg" data-src="https://tokyofashion.com/wp-content/uploads/2019/05/NK-2019-04-08-006-001-Harajuku-DZ7-0823.jpg" alt="All Black Street Fashion w/ Platinum Blonde Hair, Cape Coat, Maxi Skirt w/ Lace Panel, Anna Sui Bag &amp;a Dr. Martens Boots" width="140" height="180" loading="lazy">
		</a>
	</li>
	<li>
				<a href="https://tokyofashion.com/fashion-student-with-aqua-streaked-hair-black-lipstick-shield-visor-sunglasses-oh-pearl-satin-blazer-rrr-metallic-pants-drawstring-backpack-patent-platforms/" class="photo" title="Fashion Student with Aqua-Streaked Hair, Black Lipstick, Shield Visor Sunglasses, Oh Pearl Satin Blazer, RRR Metallic Pants, Drawstring Backpack &amp; Patent Platforms">
			<noscript><img src="https://tokyofashion.com/wp-content/uploads/2019/05/NK-2019-04-08-009-001-Harajuku-DZ7-0920.jpg" alt="Fashion Student with Aqua-Streaked Hair, Black Lipstick, Shield Visor Sunglasses, Oh Pearl Satin Blazer, RRR Metallic Pants, Drawstring Backpack &amp; Patent Platforms" width="140" height="180" loading="lazy"></noscript><img class="lazyload" src="data:image/svg+xml,%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20viewBox=%220%200%20140%20180%22%3E%3C/svg%3E" data-src="https://tokyofashion.com/wp-content/uploads/2019/05/NK-2019-04-08-009-001-Harajuku-DZ7-0920.jpg" alt="Fashion Student with Aqua-Streaked Hair, Black Lipstick, Shield Visor Sunglasses, Oh Pearl Satin Blazer, RRR Metallic Pants, Drawstring Backpack &amp; Patent Platforms" width="140" height="180" loading="lazy">
		</a>
	</li>
	<li>
				<a href="https://tokyofashion.com/three-fashion-students-in-vivienne-westwood-demonia-bubbles-forever21-spica-bershka/" class="photo" title="Three Fashion Students in Vivienne Westwood, Demonia, Bubbles, Forever21, Spica &amp; Bershka">
			<noscript><img src="https://tokyofashion.com/wp-content/uploads/2019/05/NK-2019-04-08-011-001-Harajuku-DZ7-0982-1.jpg" alt="Three Fashion Students in Vivienne Westwood, Demonia, Bubbles, Forever21, Spica &amp; Bershka" width="140" height="180" loading="lazy"></noscript><img class="lazyload" src="data:image/svg+xml,%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20viewBox=%220%200%20140%20180%22%3E%3C/svg%3E" data-src="https://tokyofashion.com/wp-content/uploads/2019/05/NK-2019-04-08-011-001-Harajuku-DZ7-0982-1.jpg" alt="Three Fashion Students in Vivienne Westwood, Demonia, Bubbles, Forever21, Spica &amp; Bershka" width="140" height="180" loading="lazy">
		</a>
	</li>
	<li>
				<a href="https://tokyofashion.com/mens-street-fashion-w-ombre-purple-hair-christopher-nemeth-oversized-blazer-comme-des-garcons-t-shirt-gucci-leather-loafers/" class="photo" title="Mens Street Fashion w/ Ombre Purple Hair, Christopher Nemeth, Oversized Blazer, Comme des Garcons T-Shirt &amp; Gucci Leather Loafers">
			<noscript><img src="https://tokyofashion.com/wp-content/uploads/2019/05/NK-2019-04-08-012-001-Harajuku-DZ7-0999-2.jpg" alt="Mens Street Fashion w/ Ombre Purple Hair, Christopher Nemeth, Oversized Blazer, Comme des Garcons T-Shirt &amp; Gucci Leather Loafers" width="140" height="180" loading="lazy"></noscript><img class="lazyload" src="data:image/svg+xml,%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20viewBox=%220%200%20140%20180%22%3E%3C/svg%3E" data-src="https://tokyofashion.com/wp-content/uploads/2019/05/NK-2019-04-08-012-001-Harajuku-DZ7-0999-2.jpg" alt="Mens Street Fashion w/ Ombre Purple Hair, Christopher Nemeth, Oversized Blazer, Comme des Garcons T-Shirt &amp; Gucci Leather Loafers" width="140" height="180" loading="lazy">
		</a>
	</li>
	<li>
				<a href="https://tokyofashion.com/purple-hair-floral-print-dress-drug-honey-damask-print-skirt-4c-faith-tokyo-dr-martens-boots/" class="photo" title="Purple Hair, Floral Print Dress, Drug Honey Damask Print Skirt, 4C°, Faith Tokyo &amp; Dr. Martens Boots">
			<noscript><img src="https://tokyofashion.com/wp-content/uploads/2019/05/NK-2019-04-08-016-001-Harajuku-DZ7-1130-2.jpg" alt="Purple Hair, Floral Print Dress, Drug Honey Damask Print Skirt, 4C°, Faith Tokyo &amp; Dr. Martens Boots" width="140" height="180" loading="lazy"></noscript><img class="lazyload" src="data:image/svg+xml,%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20viewBox=%220%200%20140%20180%22%3E%3C/svg%3E" data-src="https://tokyofashion.com/wp-content/uploads/2019/05/NK-2019-04-08-016-001-Harajuku-DZ7-1130-2.jpg" alt="Purple Hair, Floral Print Dress, Drug Honey Damask Print Skirt, 4C°, Faith Tokyo &amp; Dr. Martens Boots" width="140" height="180" loading="lazy">
		</a>
	</li>
	<li>
				<a href="https://tokyofashion.com/birdcage-veil-headpiece-vivienne-westood-john-lawrence-sullivan-me-harajuku-dr-martens-boots/" class="photo" title="Birdcage Veil Headpiece, Vivienne Westood, John Lawrence Sullivan, (ME) Harajuku &amp; Dr. Martens Boots">
			<noscript><img src="https://tokyofashion.com/wp-content/uploads/2019/05/NK-2019-04-08-018-001-Harajuku-DZ7-1197-3.jpg" alt="Birdcage Veil Headpiece, Vivienne Westood, John Lawrence Sullivan, (ME) Harajuku &amp; Dr. Martens Boots" width="140" height="180" loading="lazy"></noscript><img class="lazyload" src="data:image/svg+xml,%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20viewBox=%220%200%20140%20180%22%3E%3C/svg%3E" data-src="https://tokyofashion.com/wp-content/uploads/2019/05/NK-2019-04-08-018-001-Harajuku-DZ7-1197-3.jpg" alt="Birdcage Veil Headpiece, Vivienne Westood, John Lawrence Sullivan, (ME) Harajuku &amp; Dr. Martens Boots" width="140" height="180" loading="lazy">
		</a>
	</li>
	<li>
				<a href="https://tokyofashion.com/japanese-rapper-in-dapper-street-fashion-w-agnes-b-homme-plaid-blazer-button-fly-pants-zara-sneakers-leather-satchel/" class="photo" title="Japanese Rapper in Dapper Street Fashion w/ Agnes B Homme Plaid Blazer, Button Fly Pants, Zara Sneakers &amp; Leather Satchel">
			<noscript><img src="https://tokyofashion.com/wp-content/uploads/2019/05/NK-2019-04-08-019-001-Harajuku-DZ7-1247-3.jpg" alt="Japanese Rapper in Dapper Street Fashion w/ Agnes B Homme Plaid Blazer, Button Fly Pants, Zara Sneakers &amp; Leather Satchel" width="140" height="180" loading="lazy"></noscript><img class="lazyload" src="data:image/svg+xml,%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20viewBox=%220%200%20140%20180%22%3E%3C/svg%3E" data-src="https://tokyofashion.com/wp-content/uploads/2019/05/NK-2019-04-08-019-001-Harajuku-DZ7-1247-3.jpg" alt="Japanese Rapper in Dapper Street Fashion w/ Agnes B Homme Plaid Blazer, Button Fly Pants, Zara Sneakers &amp; Leather Satchel" width="140" height="180" loading="lazy">
		</a>
	</li>
	<li>
				<a href="https://tokyofashion.com/hijabi-tokyo-street-style-pink-zara-suit-chanel-sneakers/" class="photo" title="Hijabi Tokyo Street Style w/ Pink Zara Suit, Fendi Bag &amp; Pink Chanel Sneakers">
			<noscript><img src="https://tokyofashion.com/wp-content/uploads/2019/04/Pink-Suit-Chanel-Sneakers-Shibuya-20190407DZ70561.jpg" alt="Hijabi Tokyo Street Style w/ Pink Zara Suit, Fendi Bag &amp; Pink Chanel Sneakers" width="140" height="180" loading="lazy"></noscript><img class="lazyload" src="data:image/svg+xml,%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20viewBox=%220%200%20140%20180%22%3E%3C/svg%3E" data-src="https://tokyofashion.com/wp-content/uploads/2019/04/Pink-Suit-Chanel-Sneakers-Shibuya-20190407DZ70561.jpg" alt="Hijabi Tokyo Street Style w/ Pink Zara Suit, Fendi Bag &amp; Pink Chanel Sneakers" width="140" height="180" loading="lazy">
		</a>
	</li>
	<li>
				<a href="https://tokyofashion.com/tokyo-drag-queen-the-street-shibuya/" class="photo" title="Tokyo Drag Queen on the Street in Shibuya">
			<noscript><img src="https://tokyofashion.com/wp-content/uploads/2019/04/Tokyo-Queen-Style-20190321DZ71459.jpg" alt="Tokyo Drag Queen on the Street in Shibuya" width="140" height="180" loading="lazy"></noscript><img class="lazyload" src="data:image/svg+xml,%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20viewBox=%220%200%20140%20180%22%3E%3C/svg%3E" data-src="https://tokyofashion.com/wp-content/uploads/2019/04/Tokyo-Queen-Style-20190321DZ71459.jpg" alt="Tokyo Drag Queen on the Street in Shibuya" width="140" height="180" loading="lazy">
		</a>
	</li>
	<li>
				<a href="https://tokyofashion.com/vintage-pastel-street-style-in-shibuya-w-long-quilted-coat-knit-sweater-ruffle-dress-velcro-sneakers-sling-bag/" class="photo" title="Vintage Pastel Street Style in Shibuya w/ Long Quilted Coat, Knit Sweater, Ruffle Dress, Velcro Sneakers &amp; Sling Bag">
			<noscript><img src="https://tokyofashion.com/wp-content/uploads/2019/02/NK-2019-01-14-004-001-Harajuku-DZ7-7148.jpg" alt="Vintage Pastel Street Style in Shibuya w/ Long Quilted Coat, Knit Sweater, Ruffle Dress, Velcro Sneakers &amp; Sling Bag" width="140" height="180" loading="lazy"></noscript><img class="lazyload" src="data:image/svg+xml,%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20viewBox=%220%200%20140%20180%22%3E%3C/svg%3E" data-src="https://tokyofashion.com/wp-content/uploads/2019/02/NK-2019-01-14-004-001-Harajuku-DZ7-7148.jpg" alt="Vintage Pastel Street Style in Shibuya w/ Long Quilted Coat, Knit Sweater, Ruffle Dress, Velcro Sneakers &amp; Sling Bag" width="140" height="180" loading="lazy">
		</a>
	</li>
	<li>
				<a href="https://tokyofashion.com/tokyo-menswear-street-style-w-blunt-bob-cropped-blazer-faith-tokyo-hoodie-forever21-flared-pants-zara-shoes/" class="photo" title="Tokyo Menswear Street Style w/ Blunt Bob, Cropped Blazer, Faith Tokyo Hoodie, Forever21 Flared Pants &amp; Zara Shoes">
			<noscript><img src="https://tokyofashion.com/wp-content/uploads/2019/02/NK-2019-01-14-003-001-Harajuku-DZ7-7120.jpg" alt="Tokyo Menswear Street Style w/ Blunt Bob, Cropped Blazer, Faith Tokyo Hoodie, Forever21 Flared Pants &amp; Zara Shoes" width="140" height="180" loading="lazy"></noscript><img class="lazyload" src="data:image/svg+xml,%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20viewBox=%220%200%20140%20180%22%3E%3C/svg%3E" data-src="https://tokyofashion.com/wp-content/uploads/2019/02/NK-2019-01-14-003-001-Harajuku-DZ7-7120.jpg" alt="Tokyo Menswear Street Style w/ Blunt Bob, Cropped Blazer, Faith Tokyo Hoodie, Forever21 Flared Pants &amp; Zara Shoes" width="140" height="180" loading="lazy">
		</a>
	</li>
	<li>
				<a href="https://tokyofashion.com/kyoto-pop-icon-kawaii-japanese-monster-girl-asachill-w-pink-bob-joyrich-sheer-top/" class="photo" title="Kyoto Pop Icon &amp; Kawaii Japanese Monster Girl Asachill w/ Pink Bob, JOYRICH Sheer Top, Faux Fur Stole &amp; Zine Boom Box Bag">
			<noscript><img src="https://tokyofashion.com/wp-content/uploads/2019/02/NK-2019-01-14-001-001-Harajuku-DZ7-6963.jpg" alt="Kyoto Pop Icon &amp; Kawaii Japanese Monster Girl Asachill w/ Pink Bob, JOYRICH Sheer Top, Faux Fur Stole &amp; Zine Boom Box Bag" width="140" height="180" loading="lazy"></noscript><img class="lazyload" src="data:image/svg+xml,%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20viewBox=%220%200%20140%20180%22%3E%3C/svg%3E" data-src="https://tokyofashion.com/wp-content/uploads/2019/02/NK-2019-01-14-001-001-Harajuku-DZ7-6963.jpg" alt="Kyoto Pop Icon &amp; Kawaii Japanese Monster Girl Asachill w/ Pink Bob, JOYRICH Sheer Top, Faux Fur Stole &amp; Zine Boom Box Bag" width="140" height="180" loading="lazy">
		</a>
	</li>
	<li>
				<a href="https://tokyofashion.com/kawaii-japanese-kimono-style-rainbow-hair-furifu-kimono-6dokidoki/" class="photo" title="Kawaii Japanese Kimono Style w/ Rainbow Pixie Hair, FuriFu Kimono, 6%DOKIDOKI, Hoyajuku &amp; Disturbia Clothing Platforms">
			<noscript><img src="https://tokyofashion.com/wp-content/uploads/2019/02/NK-2019-01-14-005-001-Harajuku-DZ7-6880_1.jpg" alt="Kawaii Japanese Kimono Style w/ Rainbow Pixie Hair, FuriFu Kimono, 6%DOKIDOKI, Hoyajuku &amp; Disturbia Clothing Platforms" width="140" height="180" loading="lazy"></noscript><img class="lazyload" src="data:image/svg+xml,%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20viewBox=%220%200%20140%20180%22%3E%3C/svg%3E" data-src="https://tokyofashion.com/wp-content/uploads/2019/02/NK-2019-01-14-005-001-Harajuku-DZ7-6880_1.jpg" alt="Kawaii Japanese Kimono Style w/ Rainbow Pixie Hair, FuriFu Kimono, 6%DOKIDOKI, Hoyajuku &amp; Disturbia Clothing Platforms" width="140" height="180" loading="lazy">
		</a>
	</li>
	<li>
				<a href="https://tokyofashion.com/shibuya-streetwear-style-w-braided-updo-microwave-ruffle-sleeve-jacket-skirt-over-floral-print-pants-thibaut-fuzzy-heels-lhp-heart-bag/" class="photo" title="Shibuya Streetwear Style w/ Braided Updo, Microwave Ruffle Sleeve Jacket, Skirt Over Floral Print Pants, Thibaut Fuzzy Heels &amp; LHP Heart Bag">
			<noscript><img src="https://tokyofashion.com/wp-content/uploads/2019/02/NK-2019-01-14-002-001-Harajuku-DZ7-7065_1.jpg" alt="Shibuya Streetwear Style w/ Braided Updo, Microwave Ruffle Sleeve Jacket, Skirt Over Floral Print Pants, Thibaut Fuzzy Heels &amp; LHP Heart Bag" width="140" height="180" loading="lazy"></noscript><img class="lazyload" src="data:image/svg+xml,%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20viewBox=%220%200%20140%20180%22%3E%3C/svg%3E" data-src="https://tokyofashion.com/wp-content/uploads/2019/02/NK-2019-01-14-002-001-Harajuku-DZ7-7065_1.jpg" alt="Shibuya Streetwear Style w/ Braided Updo, Microwave Ruffle Sleeve Jacket, Skirt Over Floral Print Pants, Thibaut Fuzzy Heels &amp; LHP Heart Bag" width="140" height="180" loading="lazy">
		</a>
	</li>
	<li>
				<a href="https://tokyofashion.com/color-coordinated-tokyo-street-style-cute-plush-dr-martens/" class="photo" title="Yellow &amp; Black Color-Coordinated Tokyo Street Style w/ Cute Plush Bag, Spinns &amp; Dr. Martens">
			<noscript><img src="https://tokyofashion.com/wp-content/uploads/2018/06/NK-2018-05-06-014-001-Harajuku-D58-4928_1.jpg" alt="Yellow &amp; Black Color-Coordinated Tokyo Street Style w/ Cute Plush Bag, Spinns &amp; Dr. Martens" width="140" height="180" loading="lazy"></noscript><img class="lazyload" src="data:image/svg+xml,%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20viewBox=%220%200%20140%20180%22%3E%3C/svg%3E" data-src="https://tokyofashion.com/wp-content/uploads/2018/06/NK-2018-05-06-014-001-Harajuku-D58-4928_1.jpg" alt="Yellow &amp; Black Color-Coordinated Tokyo Street Style w/ Cute Plush Bag, Spinns &amp; Dr. Martens" width="140" height="180" loading="lazy">
		</a>
	</li>
	<li>
				<a href="https://tokyofashion.com/shironuri-minori-shibuya-aqua-silver/" class="photo" title="Shironuri Minori on the Street in Shibuya at Night Wearing Aqua &amp; Silver">
			<noscript><img src="https://tokyofashion.com/wp-content/uploads/2017/07/Minori-Shironuri-Shibuya-20170506DSC5844.jpg" alt="Shironuri Minori on the Street in Shibuya at Night Wearing Aqua &amp; Silver" width="140" height="180" loading="lazy"></noscript><img class="lazyload" src="data:image/svg+xml,%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20viewBox=%220%200%20140%20180%22%3E%3C/svg%3E" data-src="https://tokyofashion.com/wp-content/uploads/2017/07/Minori-Shironuri-Shibuya-20170506DSC5844.jpg" alt="Shironuri Minori on the Street in Shibuya at Night Wearing Aqua &amp; Silver" width="140" height="180" loading="lazy">
		</a>
	</li>
	<li>
				<a href="https://tokyofashion.com/avant-garde-japanese-street-style-comme-des-garcons-porter/" class="photo" title="Avant-garde Japanese Street Style w/ Comme Des Garcons, Porter, Ambush &amp; Chrome Hearts">
			<noscript><img src="https://tokyofashion.com/wp-content/uploads/2017/06/Comme-Des-Garcons-Japanese-Streetwear-20170617DSC4683.jpg" alt="Avant-garde Japanese Street Style w/ Comme Des Garcons, Porter, Ambush &amp; Chrome Hearts" width="140" height="180" loading="lazy"></noscript><img class="lazyload" src="data:image/svg+xml,%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20viewBox=%220%200%20140%20180%22%3E%3C/svg%3E" data-src="https://tokyofashion.com/wp-content/uploads/2017/06/Comme-Des-Garcons-Japanese-Streetwear-20170617DSC4683.jpg" alt="Avant-garde Japanese Street Style w/ Comme Des Garcons, Porter, Ambush &amp; Chrome Hearts" width="140" height="180" loading="lazy">
		</a>
	</li>
	<li>
				<a href="https://tokyofashion.com/colorful-vintage-japanese-street-styles-w-powerpuff-girls-kinji-harajuku/" class="photo" title="Colorful Vintage Japanese Street Styles w/ PowerPuff Girls, Kinji Harajuku &amp; Little Sunny Bite">
			<noscript><img src="https://tokyofashion.com/wp-content/uploads/2017/06/Monaca-Harajuku-Power-Puff-Girls-20170506DSC6104.jpg" alt="Colorful Vintage Japanese Street Styles w/ PowerPuff Girls, Kinji Harajuku &amp; Little Sunny Bite" width="140" height="180" loading="lazy"></noscript><img class="lazyload" src="data:image/svg+xml,%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20viewBox=%220%200%20140%20180%22%3E%3C/svg%3E" data-src="https://tokyofashion.com/wp-content/uploads/2017/06/Monaca-Harajuku-Power-Puff-Girls-20170506DSC6104.jpg" alt="Colorful Vintage Japanese Street Styles w/ PowerPuff Girls, Kinji Harajuku &amp; Little Sunny Bite" width="140" height="180" loading="lazy">
		</a>
	</li>
	<li>
				<a href="https://tokyofashion.com/comme-des-garcons-yohji-yamamoto-balenciaga-tokyo/" class="photo" title="Comme Des Garcons, Yohji Yamamoto &amp; Balenciaga Tokyo Street Fashion">
			<noscript><img src="https://tokyofashion.com/wp-content/uploads/2017/05/Yohji-Yamamoto-Comme-Des-Garcons-Shibuya-20170506DSC5974.jpg" alt="Comme Des Garcons, Yohji Yamamoto &amp; Balenciaga Tokyo Street Fashion" width="140" height="180" loading="lazy"></noscript><img class="lazyload" src="data:image/svg+xml,%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20viewBox=%220%200%20140%20180%22%3E%3C/svg%3E" data-src="https://tokyofashion.com/wp-content/uploads/2017/05/Yohji-Yamamoto-Comme-Des-Garcons-Shibuya-20170506DSC5974.jpg" alt="Comme Des Garcons, Yohji Yamamoto &amp; Balenciaga Tokyo Street Fashion" width="140" height="180" loading="lazy">
		</a>
	</li>
	<li>
				<a href="https://tokyofashion.com/shibuya-guy-hat-plaid-shirt-jacket/" class="photo" title="Shibuya Guy in Hat, WEGO Plaid Shirt Jacket, Skinny Jeans &amp; Clutch Bag">
			<noscript><img src="https://tokyofashion.com/wp-content/uploads/2016/01/TK-2015-10-16-011-001-Harajuku.jpg" alt="Shibuya Guy in Hat, WEGO Plaid Shirt Jacket, Skinny Jeans &amp; Clutch Bag" width="140" height="180" loading="lazy"></noscript><img class="lazyload" src="data:image/svg+xml,%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20viewBox=%220%200%20140%20180%22%3E%3C/svg%3E" data-src="https://tokyofashion.com/wp-content/uploads/2016/01/TK-2015-10-16-011-001-Harajuku.jpg" alt="Shibuya Guy in Hat, WEGO Plaid Shirt Jacket, Skinny Jeans &amp; Clutch Bag" width="140" height="180" loading="lazy">
		</a>
	</li>
	<li>
				<a href="https://tokyofashion.com/stylish-tokyo-all-black-yohji-yamamoto-moschino/" class="photo" title="Stylish Tokyo Duo in All Black w/ Yohji Yamamoto, Alexander Wang, Saint Laurent &amp; Moschino">
			<noscript><img src="https://tokyofashion.com/wp-content/uploads/2015/11/TK-2015-10-12-021-001-Harajuku.jpg" alt="Stylish Tokyo Duo in All Black w/ Yohji Yamamoto, Alexander Wang, Saint Laurent &amp; Moschino" width="140" height="180" loading="lazy"></noscript><img class="lazyload" src="data:image/svg+xml,%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20viewBox=%220%200%20140%20180%22%3E%3C/svg%3E" data-src="https://tokyofashion.com/wp-content/uploads/2015/11/TK-2015-10-12-021-001-Harajuku.jpg" alt="Stylish Tokyo Duo in All Black w/ Yohji Yamamoto, Alexander Wang, Saint Laurent &amp; Moschino" width="140" height="180" loading="lazy">
		</a>
	</li>
	<li>
				<a href="https://tokyofashion.com/shibuya-girls-crop-top-monomania-unif-emoda/" class="photo" title="Shibuya Girls in Quilted Crop Top, Monomania, UNIF, Emoda &amp; Shelter">
			<noscript><img src="https://tokyofashion.com/wp-content/uploads/2015/11/TK-2015-10-12-022-001-Harajuku.jpg" alt="Shibuya Girls in Quilted Crop Top, Monomania, UNIF, Emoda &amp; Shelter" width="140" height="180" loading="lazy"></noscript><img class="lazyload" src="data:image/svg+xml,%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20viewBox=%220%200%20140%20180%22%3E%3C/svg%3E" data-src="https://tokyofashion.com/wp-content/uploads/2015/11/TK-2015-10-12-022-001-Harajuku.jpg" alt="Shibuya Girls in Quilted Crop Top, Monomania, UNIF, Emoda &amp; Shelter" width="140" height="180" loading="lazy">
		</a>
	</li>
	<li>
				<a href="https://tokyofashion.com/shibuya-halloween-party-pictures-video-15/" class="photo" title="Shibuya Halloween Party 2015 - Pictures &amp; Video!">
			<noscript><img src="https://tokyofashion.com/wp-content/uploads/2015/11/20151030_DSC_2203.jpg" alt="Shibuya Halloween Party 2015 - Pictures &amp; Video!" width="140" height="180" loading="lazy"></noscript><img class="lazyload" src="data:image/svg+xml,%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20viewBox=%220%200%20140%20180%22%3E%3C/svg%3E" data-src="https://tokyofashion.com/wp-content/uploads/2015/11/20151030_DSC_2203.jpg" alt="Shibuya Halloween Party 2015 - Pictures &amp; Video!" width="140" height="180" loading="lazy">
		</a>
	</li>
	<li>
				<a href="https://tokyofashion.com/halloween-eve-japan-costume-pictures/" class="photo" title="Halloween Eve in Japan - 150 Halloween Costume Pictures">
			<noscript><img src="https://tokyofashion.com/wp-content/uploads/2015/10/Halloween-in-Japan-Shibuya-15-10-30-065.jpg" alt="Halloween Eve in Japan - 150 Halloween Costume Pictures" width="140" height="180" loading="lazy"></noscript><img class="lazyload" src="data:image/svg+xml,%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20viewBox=%220%200%20140%20180%22%3E%3C/svg%3E" data-src="https://tokyofashion.com/wp-content/uploads/2015/10/Halloween-in-Japan-Shibuya-15-10-30-065.jpg" alt="Halloween Eve in Japan - 150 Halloween Costume Pictures" width="140" height="180" loading="lazy">
		</a>
	</li>
	<li>
				<a href="https://tokyofashion.com/dark-tokyo-street-style-fetis-demonia/" class="photo" title="Dark Tokyo Street Style w/ Black Lipstick, Fetis &amp; Demonia Boots">
			<noscript><img src="https://tokyofashion.com/wp-content/uploads/2015/10/Demonia-Fetis-Uniqlo-Shibuya-20151017DSC9857.jpg" alt="Dark Tokyo Street Style w/ Black Lipstick, Fetis &amp; Demonia Boots" width="140" height="180" loading="lazy"></noscript><img class="lazyload" src="data:image/svg+xml,%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20viewBox=%220%200%20140%20180%22%3E%3C/svg%3E" data-src="https://tokyofashion.com/wp-content/uploads/2015/10/Demonia-Fetis-Uniqlo-Shibuya-20151017DSC9857.jpg" alt="Dark Tokyo Street Style w/ Black Lipstick, Fetis &amp; Demonia Boots" width="140" height="180" loading="lazy">
		</a>
	</li>
	<li>
				<a href="https://tokyofashion.com/rocket-platform-boots-rick-owens-shibuya/" class="photo" title="Rocket Platform Boots, Rick Owens, 101 Dalmatians Remake Top &amp; Vintage Fashion in Shibuya">
			<noscript><img src="https://tokyofashion.com/wp-content/uploads/2015/10/Barrack-Room-GVGV-Shibuya-20151024DSC0099.jpg" alt="Rocket Platform Boots, Rick Owens, 101 Dalmatians Remake Top &amp; Vintage Fashion in Shibuya" width="140" height="180" loading="lazy"></noscript><img class="lazyload" src="data:image/svg+xml,%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20viewBox=%220%200%20140%20180%22%3E%3C/svg%3E" data-src="https://tokyofashion.com/wp-content/uploads/2015/10/Barrack-Room-GVGV-Shibuya-20151024DSC0099.jpg" alt="Rocket Platform Boots, Rick Owens, 101 Dalmatians Remake Top &amp; Vintage Fashion in Shibuya" width="140" height="180" loading="lazy">
		</a>
	</li>
</ul><br style="clear:both;"></div>							<div class="navigation">
																	<div class="navleft">
										<a href="https://tokyofashion.com/photos/?location=Shibuya&amp;start=40">« Show Older Shibuya Photos</a>
									</div>
																							</div>
							<div id="photonav" align="center">
								<a href="https://tokyofashion.com/photos/?location=Shibuya&amp;month=3&amp;years=2025">Browse Shibuya Photos By Month
								</a>
							</div>
					</div> <!-- .contentpanel -->
				</div>
				
<aside role="complementary" class="sidebar">
	
		<section id="recent-posts-2" class="widget widget_recent_entries">
		<h2 class="widget-title">Recent Posts</h2>
		<ul>
											<li>
					<a href="https://tokyofashion.com/korean-street-style-harajuku-japan-metal-glove-thug-club-fashion/">Korean Street Style in Harajuku, Japan w/ Giant Metal Glove &amp; Thug Club Fashion</a>
									</li>
											<li>
					<a href="https://tokyofashion.com/japanese-clown-street-style-harajuku-w-hello-kitty-shironuri-makeup-room-shoes/">Japanese Clown-Inspired Street Style in Harajuku w/ Hello Kitty, Shironuri Makeup &amp; Room Shoes</a>
									</li>
											<li>
					<a href="https://tokyofashion.com/japanese-gothic-tattoo-artist-vivienne-westwood-harajuku-tokyo/">Japanese Gothic Tattoo Artist Wearing Vivienne Westwood on the Street in Harajuku, Tokyo</a>
									</li>
											<li>
					<a href="https://tokyofashion.com/japanese-visual-kei-harajuku-asakura-garo-opanchu-usagi/">Japanese Visual Kei Singer in Harajuku w/ Kawaii Pink, Asakura Garo &amp; Opanchu Usagi</a>
									</li>
											<li>
					<a href="https://tokyofashion.com/japanese-dancer-hime-hairstyle-harajuku-street-style-not-conventional-yosuke-boots/">Japanese Dancer w/ Hime Hairstyle in All Black Harajuku Street Style, Not Conventional &amp; Yosuke Boots</a>
									</li>
					</ul>

		</section><section id="linkcat-415" class="widget widget_links"><h2 class="widget-title">Fashion Brands</h2>
	<ul class="xoxo blogroll">
<li><a href="http://www.virtualjapan.com/wiki/A_Bathing_Ape" rel="noopener" title="BAPE" target="_blank">A Bathing Ape</a></li>
<li><a href="http://www.virtualjapan.com/wiki/AS_KNOW_AS_de_base" rel="noopener" title="AS KNOW AS" target="_blank">AS KNOW AS</a></li>
<li><a href="http://www.virtualjapan.com/wiki/Ato_%28fashion_brand%29" rel="noopener" title="Ato Japan" target="_blank">Ato</a></li>
<li><a href="http://www.virtualjapan.com/wiki/Billionaire_Boys_Club" rel="noopener" title="Billionaire Boys Club" target="_blank">Billionaire Boys Club</a></li>
<li><a href="http://www.virtualjapan.com/wiki/Chisato_Tsumori" rel="noopener" title="Chisato Tsumori" target="_blank">Chisato Tsumori</a></li>
<li><a href="http://www.virtualjapan.com/wiki/Comme_des_Garcons" rel="noopener" title="Comme des Garcons" target="_blank">Comme des Garcons</a></li>
<li><a href="http://www.virtualjapan.com/wiki/Edwin" rel="noopener" title="Edwin Jeans" target="_blank">Edwin</a></li>
<li><a href="http://www.virtualjapan.com/wiki/Frapbois" rel="noopener" title="Frapbois" target="_blank">Frapbois</a></li>
<li><a href="http://www.virtualjapan.com/wiki/Hysteric_Glamour" rel="noopener" title="Hysteric Glamour" target="_blank">Hysteric Glamour</a></li>
<li><a href="http://www.virtualjapan.com/wiki/Limi_Feu" rel="noopener" title="Limi Feu" target="_blank">Limi Feu</a></li>
<li><a href="http://www.virtualjapan.com/wiki/Mercibeaucoup" rel="noopener" title="Mercibeaucoup" target="_blank">Mercibeaucoup</a></li>
<li><a href="http://www.virtualjapan.com/wiki/N.Hoolywood" rel="noopener" title="N.Hoolywood" target="_blank">N.Hoolywood</a></li>
<li><a href="http://www.virtualjapan.com/wiki/Samantha_Thavasa" rel="noopener" title="Samantha Thavasa" target="_blank">Samantha Thavasa</a></li>
<li><a href="http://www.virtualjapan.com/wiki/The_Viridi-anne" rel="noopener" title="The Viridi-anne" target="_blank">The Viridi-anne</a></li>

	</ul>
</section>
</aside><!-- #secondary -->
			</div>
          </main>
	</div><!-- #content -->
<footer role="contentinfo" class="footer">
    <div class="inner-wrapper footer-wrapper">
        <div class="footer-main">
            <div class="footer-menu">
                <button class="menu-toggle" aria-controls="primary-menu" aria-expanded="false">Primary Menu</button>
                <div class="menu-footer-container"><ul id="Footer" class="menu"><li id="menu-item-94796" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-home menu-item-94796"><a href="https://tokyofashion.com/">Home</a></li>
<li id="menu-item-94797" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-94797"><a href="https://tokyofashion.com/articles/">Articles</a></li>
<li id="menu-item-94798" class="menu-item menu-item-type-post_type menu-item-object-page current-menu-item page_item page-item-1308 current_page_item menu-item-94798"><a href="https://tokyofashion.com/photos/" aria-current="page">Street Photos</a></li>
<li id="menu-item-94799" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-94799"><a href="https://tokyofashion.com/brands/">Brands</a></li>
<li id="menu-item-94800" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-94800"><a href="https://tokyofashion.com/forum/">Forum</a></li>
<li id="menu-item-94801" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-94801"><a href="https://tokyofashion.com/fashion-map/">Fashion Map</a></li>
<li id="menu-item-94802" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-94802"><a href="https://tokyofashion.com/music/">Music</a></li>
<li id="menu-item-94803" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-94803"><a href="https://tokyofashion.com/contests/">Contests</a></li>
<li id="menu-item-94804" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-94804"><a href="https://tokyofashion.com/contributors/">About</a></li>
</ul></div>            </div>
            <div class="footer-logo logo">
                <noscript><img width="148" height="72" src="/wp-content/themes/tokyofashion/img/footer-logo.gif" alt="Logo"></noscript><img class="lazyload" width="148" height="72" src="data:image/svg+xml,%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20viewBox=%220%200%20148%2072%22%3E%3C/svg%3E" data-src="/wp-content/themes/tokyofashion/img/footer-logo.gif" alt="Logo">
            </div>
        </div>
        <div class="footer-copyright">
            <p>Copyright 2000-2021 TokyoFashion.com. All rights reserved. <a href="#">Privacy Policy</a></p>
        </div>
    </div>
</footer>
</div>

<noscript><style>.lazyload{display:none;}</style></noscript><script data-noptimize="1">window.lazySizesConfig=window.lazySizesConfig||{};window.lazySizesConfig.loadMode=1;</script><script async="" data-noptimize="1" src="https://tokyofashion.com/wp-content/plugins/autoptimize/classes/external/js/lazysizes.min.js?ao_version=3.1.13"></script>





<script defer="" src="https://tokyofashion.com/wp-content/cache/autoptimize/js/autoptimize_4c77f180cca5754b3c917b64152ec93e.js"></script><script>(function(){function c(){var b=a.contentDocument||a.contentWindow.document;if(b){var d=b.createElement('script');d.innerHTML="window.__CF$cv$params={r:'9201e50d9f798242',t:'MTc0MTkzNTYzMy4wMDAwMDA='};var a=document.createElement('script');a.nonce='';a.src='/cdn-cgi/challenge-platform/scripts/jsd/main.js';document.getElementsByTagName('head')[0].appendChild(a);";b.getElementsByTagName('head')[0].appendChild(d)}}if(document.body){var a=document.createElement('iframe');a.height=1;a.width=1;a.style.position='absolute';a.style.top=0;a.style.left=0;a.style.border='none';a.style.visibility='hidden';document.body.appendChild(a);if('loading'!==document.readyState)c();else if(window.addEventListener)document.addEventListener('DOMContentLoaded',c);else{var e=document.onreadystatechange||function(){};document.onreadystatechange=function(b){e(b);'loading'!==document.readyState&&(document.onreadystatechange=e,c())}}}})();</script><iframe height="1" width="1" style="position: absolute; top: 0px; left: 0px; border: none; visibility: hidden;"></iframe><script defer="" src="https://static.cloudflareinsights.com/beacon.min.js/vcd15cbe7772f49c399c6a5babf22c1241717689176015" integrity="sha512-ZpsOmlRQV6y907TI0dKBHq9Md29nnaEIPlkf84rnaERnq6zvWvPUqr2ft8M1aS28oN72PdrCzSjY4U6VaAw1EQ==" data-cf-beacon="{&quot;rayId&quot;:&quot;9201e50d9f798242&quot;,&quot;serverTiming&quot;:{&quot;name&quot;:{&quot;cfExtPri&quot;:true,&quot;cfL4&quot;:true,&quot;cfSpeedBrain&quot;:true,&quot;cfCacheStatus&quot;:true}},&quot;version&quot;:&quot;2025.1.0&quot;,&quot;token&quot;:&quot;a4577270ad5a4bf19902742d028d2a2b&quot;}" crossorigin="anonymous"></script>





</body></html>"""  # Replace this with your actual HTML data

soup = BeautifulSoup(html, "html.parser")


data = []
for link in soup.find_all("a", href=True):  
    title = link.get_text(strip=True)
    url = link["href"]
    
    # Find image inside the link (if available)
    img_tag = link.find("img")
    img_url = img_tag["src"] if img_tag else "No Image"
    
    data.append([title, url, img_url])

 
csv_file = "shibuyatrends.csv"
with open(csv_file, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Title", "Link", "Image URL"])
    writer.writerows(data)

print(f"shibuya")




html = """<!DOCTYPE html><html lang="en-US"><head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<link rel="preload" href="https://tokyofashion.com/wp-content/themes/tokyofashion/fonts/fontawesome-webfont.woff2?v=4.7.0" as="font" type="font/woff2" crossorigin=""><link rel="profile" href="https://gmpg.org/xfn/11">

	<link media="all" href="https://tokyofashion.com/wp-content/cache/autoptimize/css/autoptimize_f035207383e8e457d3776c8597bfc517.css" rel="stylesheet"><title>Shinjuku Japanese Street Fashion Photos – Tokyo Fashion</title>
<meta name="robots" content="max-image-preview:large">
	
	<link href="https://fonts.gstatic.com" crossorigin="anonymous" rel="preconnect">
<link rel="alternate" type="application/rss+xml" title="Tokyo Fashion » Feed" href="https://tokyofashion.com/feed/">
<link rel="alternate" type="application/rss+xml" title="Tokyo Fashion » Comments Feed" href="https://tokyofashion.com/comments/feed/">
<link rel="alternate" type="application/rss+xml" title="Tokyo Fashion » Tokyo Street Fashion Photos Comments Feed" href="https://tokyofashion.com/photos/feed/">











<script src="https://tokyofashion.com/wp-includes/js/jquery/jquery.min.js?ver=3.7.1" id="jquery-core-js"></script>




<script id="responsive-lightbox-js-before">
var rlArgs = {"script":"magnific","selector":"lightbox","customEvents":"","activeGalleries":true,"disableOn":0,"midClick":true,"preloader":true,"closeOnContentClick":true,"closeOnBgClick":true,"closeBtnInside":true,"showCloseBtn":true,"enableEscapeKey":true,"alignTop":false,"fixedContentPos":"auto","fixedBgPos":"auto","autoFocusLast":true,"woocommerce_gallery":false,"ajaxurl":"https:\/\/tokyofashion.com\/wp-admin\/admin-ajax.php","nonce":"26d353d815","preview":false,"postId":1308,"scriptExtension":false};
</script>

<link rel="https://api.w.org/" href="https://tokyofashion.com/wp-json/"><link rel="alternate" title="JSON" type="application/json" href="https://tokyofashion.com/wp-json/wp/v2/pages/1308"><link rel="EditURI" type="application/rsd+xml" title="RSD" href="https://tokyofashion.com/xmlrpc.php?rsd">
<meta name="generator" content="WordPress 6.7.2">
<link rel="canonical" href="https://tokyofashion.com/photos/">
<link rel="shortlink" href="https://tokyofashion.com/?p=1308">
<link rel="alternate" title="oEmbed (JSON)" type="application/json+oembed" href="https://tokyofashion.com/wp-json/oembed/1.0/embed?url=https%3A%2F%2Ftokyofashion.com%2Fphotos%2F">
<link rel="alternate" title="oEmbed (XML)" type="text/xml+oembed" href="https://tokyofashion.com/wp-json/oembed/1.0/embed?url=https%3A%2F%2Ftokyofashion.com%2Fphotos%2F&amp;format=xml">
<link rel="pingback" href="https://tokyofashion.com/xmlrpc.php">		
		</head>

<body class="home">
<div class="header-menu_mob">
    <nav role="navigation">
        <div class="menu-main-container"><ul id="Main" class="menu"><li id="menu-item-94790" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-home menu-item-94790"><a href="https://tokyofashion.com/">Home</a></li>
<li id="menu-item-94791" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-94791"><a href="https://tokyofashion.com/articles/">Articles</a></li>
<li id="menu-item-94792" class="menu-item menu-item-type-post_type menu-item-object-page current-menu-item page_item page-item-1308 current_page_item menu-item-94792"><a href="https://tokyofashion.com/photos/" aria-current="page">Street Photos</a></li>
<li id="menu-item-94793" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-94793"><a href="https://tokyofashion.com/brands/">Brands</a></li>
<li id="menu-item-94794" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-94794"><a href="https://tokyofashion.com/fashion-map/">Fashion Map</a></li>
<li id="menu-item-94795" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-94795"><a href="https://tokyofashion.com/music/">Music</a></li>
</ul></div>    </nav>
    <div class="header-menu_close fa fa-times"></div>
</div>
<div class="main-wrapper">
    <header role="banner" class="header">
        <div class="inner-wrapper header-wrapper">
            <div class="header-block">
                <div class="header-logo logo">
                    	<a href="https://tokyofashion.com/" class="custom-logo-link" rel="home"><noscript><img width="245" height="118" src="https://tokyofashion.com/wp-content/uploads/2021/03/cropped-logo-1.gif" class="custom-logo" alt="Tokyo Fashion" decoding="async" /></noscript><img width="245" height="118" src="https://tokyofashion.com/wp-content/uploads/2021/03/cropped-logo-1.gif" data-src="https://tokyofashion.com/wp-content/uploads/2021/03/cropped-logo-1.gif" class="custom-logo lazyloaded" alt="Tokyo Fashion" decoding="async"></a>                </div>
                <div class="header-menu">
                    <nav role="navigation">
                        <button class="menu-toggle" aria-controls="primary-menu" aria-expanded="false">Primary Menu</button>
                        <div class="menu-main-container"><ul id="Main" class="menu"><li class="menu-item menu-item-type-post_type menu-item-object-page menu-item-home menu-item-94790"><a href="https://tokyofashion.com/">Home</a></li>
<li class="menu-item menu-item-type-post_type menu-item-object-page menu-item-94791"><a href="https://tokyofashion.com/articles/">Articles</a></li>
<li class="menu-item menu-item-type-post_type menu-item-object-page current-menu-item page_item page-item-1308 current_page_item menu-item-94792"><a href="https://tokyofashion.com/photos/" aria-current="page">Street Photos</a></li>
<li class="menu-item menu-item-type-post_type menu-item-object-page menu-item-94793"><a href="https://tokyofashion.com/brands/">Brands</a></li>
<li class="menu-item menu-item-type-post_type menu-item-object-page menu-item-94794"><a href="https://tokyofashion.com/fashion-map/">Fashion Map</a></li>
<li class="menu-item menu-item-type-post_type menu-item-object-page menu-item-94795"><a href="https://tokyofashion.com/music/">Music</a></li>
</ul></div>                    </nav>
                </div>
            </div>
            <div class="header-block">
                <div class="header-sandwich fa fa-bars"></div>
                <div class="header-block_inner">
                    <div class="header-social">
                        <ul>
                            <li><a href="https://www.facebook.com/TokyoFashion" class="fa fa-facebook" target="_blank"></a></li>
                            <li><a href="https://twitter.com/tokyofashion" class="fa fa-twitter" target="_blank"></a></li>
                            <li><a href="https://feeds.feedburner.com/TokyoFashion" class="fa fa-rss" target="_blank"></a></li>
                            <li><a href="https://feedburner.google.com/fb/a/mailverify?uri=TokyoFashion&amp;loc=en_US" class="fa fa-envelope" target="_blank"></a></li>
                        </ul>
                    </div>
                    <div class="header-search">
                        <a href="#" title="Search" class="header-search_link fa fa-search"></a>
                        <div class="header-search_overlay">
                            <form method="get" class="search-form" action="https://tokyofashion.com/">
                                <label>
                                    <span class="screen-reader-text">Search for:</span>
                                    <input type="search" class="search-field" placeholder="Type and hit enter..." value="" name="s" title="Search for:">
                                </label>
                                <button type="submit" class="search-submit"><i class="fa fa-search"></i></button>
                            </form>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </header>

<div id="content">
		  <main role="main" class="main-content">
                <div class="inner-wrapper main-inner_wrapper">
                    <div class="content-left">
					<a class="backlink" href="https://tokyofashion.com/photos/">« Back to Recent Tokyo Street Fashion photos</a><br><br>
					<div 7="" class="contentpanel bm-half">
						<h2 class="contentpaneltitle">Shinjuku Japanese Street Fashion Photos<!--  (and other areas) --></h2>
						<div class="photos-block"><ul class="photos-list">	<li>
				<a href="https://tokyofashion.com/tokyo-girls-street-styles-the-shining-twins-necktie-berrycupide-mono-comme-ca-rrr-vintage/" class="photo" title="Tokyo Girls Street Styles w/ The Shining Twins, Leather Jacket, Necktie, Berrycupide, Mono Comme Ca, RRR &amp; Vintage">
			<noscript><img src="https://tokyofashion.com/wp-content/uploads/2019/11/NK-2019-11-04-015-001-Bunka-DZ7-1169.jpg" alt="Tokyo Girls Street Styles w/ The Shining Twins, Leather Jacket, Necktie, Berrycupide, Mono Comme Ca, RRR &amp; Vintage" width="140" height="180" loading="lazy"></noscript><img class=" lazyloaded" src="https://tokyofashion.com/wp-content/uploads/2019/11/NK-2019-11-04-015-001-Bunka-DZ7-1169.jpg" data-src="https://tokyofashion.com/wp-content/uploads/2019/11/NK-2019-11-04-015-001-Bunka-DZ7-1169.jpg" alt="Tokyo Girls Street Styles w/ The Shining Twins, Leather Jacket, Necktie, Berrycupide, Mono Comme Ca, RRR &amp; Vintage" width="140" height="180" loading="lazy">
		</a>
	</li>
	<li>
				<a href="https://tokyofashion.com/chic-tokyo-vintage-street-style-green-top-black-dress-zara-shoes/" class="photo" title="Chic Tokyo Vintage Street Style w/ Green Top, Black Dress &amp; Zara Shoes">
			<noscript><img src="https://tokyofashion.com/wp-content/uploads/2019/11/NK-2019-11-04-045-001-Bunka-DZ7-2466_1.jpg" alt="Chic Tokyo Vintage Street Style w/ Green Top, Black Dress &amp; Zara Shoes" width="140" height="180" loading="lazy"></noscript><img class=" lazyloaded" src="https://tokyofashion.com/wp-content/uploads/2019/11/NK-2019-11-04-045-001-Bunka-DZ7-2466_1.jpg" data-src="https://tokyofashion.com/wp-content/uploads/2019/11/NK-2019-11-04-045-001-Bunka-DZ7-2466_1.jpg" alt="Chic Tokyo Vintage Street Style w/ Green Top, Black Dress &amp; Zara Shoes" width="140" height="180" loading="lazy">
		</a>
	</li>
	<li>
				<a href="https://tokyofashion.com/mixed-prints-tokyo-street-style-tibal-coat-desigual-tripp-nyc-new-rock/" class="photo" title="Mixed Prints Tokyo Street Style w/ Tibal Coat, Desigual, Tripp NYC &amp; New Rock">
			<noscript><img src="https://tokyofashion.com/wp-content/uploads/2019/11/NK-2019-11-04-021-001-Bunka-DZ7-1444.jpg" alt="Mixed Prints Tokyo Street Style w/ Tibal Coat, Desigual, Tripp NYC &amp; New Rock" width="140" height="180" loading="lazy"></noscript><img class=" lazyloaded" src="https://tokyofashion.com/wp-content/uploads/2019/11/NK-2019-11-04-021-001-Bunka-DZ7-1444.jpg" data-src="https://tokyofashion.com/wp-content/uploads/2019/11/NK-2019-11-04-021-001-Bunka-DZ7-1444.jpg" alt="Mixed Prints Tokyo Street Style w/ Tibal Coat, Desigual, Tripp NYC &amp; New Rock" width="140" height="180" loading="lazy">
		</a>
	</li>
	<li>
				<a href="https://tokyofashion.com/japanese-streetwear-styles-hat-goggles-remake-fashion-esc-studio-civarize-calvin-klein-dr-martens/" class="photo" title="Japanese Streetwear Styles w/ Furry Hat, Goggles, Remake Fashion, Layered Belts, ESC Studio, Civarize, Calvin Klein, Leather Briefcase &amp; Dr. Martens">
			<noscript><img src="https://tokyofashion.com/wp-content/uploads/2019/11/NK-2019-11-04-020-001-Bunka-DZ7-1393.jpg" alt="Japanese Streetwear Styles w/ Furry Hat, Goggles, Remake Fashion, Layered Belts, ESC Studio, Civarize, Calvin Klein, Leather Briefcase &amp; Dr. Martens" width="140" height="180" loading="lazy"></noscript><img class=" lazyloaded" src="https://tokyofashion.com/wp-content/uploads/2019/11/NK-2019-11-04-020-001-Bunka-DZ7-1393.jpg" data-src="https://tokyofashion.com/wp-content/uploads/2019/11/NK-2019-11-04-020-001-Bunka-DZ7-1393.jpg" alt="Japanese Streetwear Styles w/ Furry Hat, Goggles, Remake Fashion, Layered Belts, ESC Studio, Civarize, Calvin Klein, Leather Briefcase &amp; Dr. Martens" width="140" height="180" loading="lazy">
		</a>
	</li>
	<li>
				<a href="https://tokyofashion.com/tokyo-style-heihei-plaid-bow-dress-g2-vinyl-record-bag/" class="photo" title="Tokyo Teen Style w/ HEIHEI Plaid Bow Dress, Beret, Lace Socks &amp; G2? Vinyl Record Bag">
			<noscript><img src="https://tokyofashion.com/wp-content/uploads/2019/11/NK-2019-11-04-029-001-Bunka-DZ7-1774-2_1.jpg" alt="Tokyo Teen Style w/ HEIHEI Plaid Bow Dress, Beret, Lace Socks &amp; G2? Vinyl Record Bag" width="140" height="180" loading="lazy"></noscript><img class=" lazyloaded" src="https://tokyofashion.com/wp-content/uploads/2019/11/NK-2019-11-04-029-001-Bunka-DZ7-1774-2_1.jpg" data-src="https://tokyofashion.com/wp-content/uploads/2019/11/NK-2019-11-04-029-001-Bunka-DZ7-1774-2_1.jpg" alt="Tokyo Teen Style w/ HEIHEI Plaid Bow Dress, Beret, Lace Socks &amp; G2? Vinyl Record Bag" width="140" height="180" loading="lazy">
		</a>
	</li>
	<li>
				<a href="https://tokyofashion.com/bunka-fashion-college-students-lace-headdress-birdcage-veil-hat-lace-gloves-teddy-bear-backpack-panama-boy-irregular-choice/" class="photo" title="Bunka Fashion College Students' Street Styles w/ Lace Headdress, Birdcage Veil Hat, Lace Gloves, Teddy Bear Backpack, Panama Boy, Slit Skirt, Himiko &amp; Irregular Choice Shoes">
			<noscript><img src="https://tokyofashion.com/wp-content/uploads/2019/11/NK-2019-11-03-028-002-Harajuku-DZ7-0346-3.jpg" alt="Bunka Fashion College Students&#039; Street Styles w/ Lace Headdress, Birdcage Veil Hat, Lace Gloves, Teddy Bear Backpack, Panama Boy, Slit Skirt, Himiko &amp; Irregular Choice Shoes" width="140" height="180" loading="lazy"></noscript><img class=" lazyloaded" src="https://tokyofashion.com/wp-content/uploads/2019/11/NK-2019-11-03-028-002-Harajuku-DZ7-0346-3.jpg" data-src="https://tokyofashion.com/wp-content/uploads/2019/11/NK-2019-11-03-028-002-Harajuku-DZ7-0346-3.jpg" alt="Bunka Fashion College Students' Street Styles w/ Lace Headdress, Birdcage Veil Hat, Lace Gloves, Teddy Bear Backpack, Panama Boy, Slit Skirt, Himiko &amp; Irregular Choice Shoes" width="140" height="180" loading="lazy">
		</a>
	</li>
	<li>
				<a href="https://tokyofashion.com/tjapanese-model-tokyo-keisuke-yoshida-harness-pleated-pants/" class="photo" title="Teen Japanese Model in Tokyo w/ Keisuke Yoshida, Harness, Pleated Pants &amp; Boots">
			<noscript><img src="https://tokyofashion.com/wp-content/uploads/2019/11/NK-2019-11-04-016-001-Bunka-DZ7-1242-copy.jpg" alt="Teen Japanese Model in Tokyo w/ Keisuke Yoshida, Harness, Pleated Pants &amp; Boots" width="140" height="180" loading="lazy"></noscript><img class=" lazyloaded" src="https://tokyofashion.com/wp-content/uploads/2019/11/NK-2019-11-04-016-001-Bunka-DZ7-1242-copy.jpg" data-src="https://tokyofashion.com/wp-content/uploads/2019/11/NK-2019-11-04-016-001-Bunka-DZ7-1242-copy.jpg" alt="Teen Japanese Model in Tokyo w/ Keisuke Yoshida, Harness, Pleated Pants &amp; Boots" width="140" height="180" loading="lazy">
		</a>
	</li>
	<li>
				<a href="https://tokyofashion.com/tokyo-girl-vintage-street-style-tattoos-office-kiko-pinnap/" class="photo" title="All Black Tokyo Girl Vintage Street Style w/ Tattoos, Hare, DKNY, Office Kiko &amp; Pinnap">
			<noscript><img src="https://tokyofashion.com/wp-content/uploads/2019/11/NK-2019-11-04-036-001-Bunka-DZ7-2091-2_1.jpg" alt="All Black Tokyo Girl Vintage Street Style w/ Tattoos, Hare, DKNY, Office Kiko &amp; Pinnap" width="140" height="180" loading="lazy"></noscript><img class=" lazyloaded" src="https://tokyofashion.com/wp-content/uploads/2019/11/NK-2019-11-04-036-001-Bunka-DZ7-2091-2_1.jpg" data-src="https://tokyofashion.com/wp-content/uploads/2019/11/NK-2019-11-04-036-001-Bunka-DZ7-2091-2_1.jpg" alt="All Black Tokyo Girl Vintage Street Style w/ Tattoos, Hare, DKNY, Office Kiko &amp; Pinnap" width="140" height="180" loading="lazy">
		</a>
	</li>
	<li>
				<a href="https://tokyofashion.com/tokyo-colorful-street-styles-furry-cap-wide-brim-hat-knit-beanie-vivienne-westwood-vintage-handmade/" class="photo" title="Tokyo Girls in Colorful Street Styles w/ Furry Cap, Wide Brim Hat, Knit Beanie, Vivienne Westwood, Calico, Vintage &amp; Handmade Fashion">
			<noscript><img src="https://tokyofashion.com/wp-content/uploads/2019/11/NK-2019-11-04-030-001-Bunka-DZ7-1808.jpg" alt="Tokyo Girls in Colorful Street Styles w/ Furry Cap, Wide Brim Hat, Knit Beanie, Vivienne Westwood, Calico, Vintage &amp; Handmade Fashion" width="140" height="180" loading="lazy"></noscript><img class=" lazyloaded" src="https://tokyofashion.com/wp-content/uploads/2019/11/NK-2019-11-04-030-001-Bunka-DZ7-1808.jpg" data-src="https://tokyofashion.com/wp-content/uploads/2019/11/NK-2019-11-04-030-001-Bunka-DZ7-1808.jpg" alt="Tokyo Girls in Colorful Street Styles w/ Furry Cap, Wide Brim Hat, Knit Beanie, Vivienne Westwood, Calico, Vintage &amp; Handmade Fashion" width="140" height="180" loading="lazy">
		</a>
	</li>
	<li>
				<a href="https://tokyofashion.com/tokyo-boylesque-dancer-styles-dolly-noire-polo-ralph-lauren-anatometal/" class="photo" title="Matching Tokyo Boylesque Dancer Street Styles w/ Dolly Noire, Cookman, Polo Ralph Lauren, Adidas &amp; Anatometal">
			<noscript><img src="https://tokyofashion.com/wp-content/uploads/2019/11/NK-2019-11-04-004-001-Bunka-DZ7-0717_1.jpg" alt="Matching Tokyo Boylesque Dancer Street Styles w/ Dolly Noire, Cookman, Polo Ralph Lauren, Adidas &amp; Anatometal" width="140" height="180" loading="lazy"></noscript><img class=" lazyloaded" src="https://tokyofashion.com/wp-content/uploads/2019/11/NK-2019-11-04-004-001-Bunka-DZ7-0717_1.jpg" data-src="https://tokyofashion.com/wp-content/uploads/2019/11/NK-2019-11-04-004-001-Bunka-DZ7-0717_1.jpg" alt="Matching Tokyo Boylesque Dancer Street Styles w/ Dolly Noire, Cookman, Polo Ralph Lauren, Adidas &amp; Anatometal" width="140" height="180" loading="lazy">
		</a>
	</li>
	<li>
				<a href="https://tokyofashion.com/nile-perch-tokyo-street-style-two-tone-hair-gingham-dress-mickey-mouse-bag-yosuke/" class="photo" title="Nile Perch Tokyo Street Style w/ Half Color Braids, Handmade Headdress, Hair Pompoms, Gingham Dress, Mickey Mouse Bag &amp; Yosuke Creepers">
			<noscript><img src="https://tokyofashion.com/wp-content/uploads/2019/11/NK-2019-11-04-040-001-Bunka-DZ7-2254.jpg" alt="Nile Perch Tokyo Street Style w/ Half Color Braids, Handmade Headdress, Hair Pompoms, Gingham Dress, Mickey Mouse Bag &amp; Yosuke Creepers" width="140" height="180" loading="lazy"></noscript><img class=" lazyloaded" src="https://tokyofashion.com/wp-content/uploads/2019/11/NK-2019-11-04-040-001-Bunka-DZ7-2254.jpg" data-src="https://tokyofashion.com/wp-content/uploads/2019/11/NK-2019-11-04-040-001-Bunka-DZ7-2254.jpg" alt="Nile Perch Tokyo Street Style w/ Half Color Braids, Handmade Headdress, Hair Pompoms, Gingham Dress, Mickey Mouse Bag &amp; Yosuke Creepers" width="140" height="180" loading="lazy">
		</a>
	</li>
	<li>
				<a href="https://tokyofashion.com/monochrome-tokyo-menswear-styles-spiky-hair-handmade-cuff-u-dresser-hm-yosuke/" class="photo" title="Monochrome Tokyo Menswear Styles w/ Spiky Hair, Handmade Cuff, U Dresser, H&amp;M, Yosuke &amp; Dolls Kill">
			<noscript><img src="https://tokyofashion.com/wp-content/uploads/2019/11/NK-2019-11-04-011-001-Bunka-DZ7-1047.jpg" alt="Monochrome Tokyo Menswear Styles w/ Spiky Hair, Handmade Cuff, U Dresser, H&amp;M, Yosuke &amp; Dolls Kill" width="140" height="180" loading="lazy"></noscript><img class=" lazyloaded" src="https://tokyofashion.com/wp-content/uploads/2019/11/NK-2019-11-04-011-001-Bunka-DZ7-1047.jpg" data-src="https://tokyofashion.com/wp-content/uploads/2019/11/NK-2019-11-04-011-001-Bunka-DZ7-1047.jpg" alt="Monochrome Tokyo Menswear Styles w/ Spiky Hair, Handmade Cuff, U Dresser, H&amp;M, Yosuke &amp; Dolls Kill" width="140" height="180" loading="lazy">
		</a>
	</li>
	<li>
				<a href="https://tokyofashion.com/japanese-street-styles-pink-bob-two-tone-hair-hats-nile-perch-vintage-suit-kirby-bag-swankiss/" class="photo" title="Japanese Street Styles w/ Pink Bob, Two-Tone Hair, Hats, Nile Perch, Vintage Suit, Kirby Bag, Vivienne Westwood, Alice and the Pirates, Yosuke &amp; Swankiss">
			<noscript><img src="https://tokyofashion.com/wp-content/uploads/2019/11/NK-2019-11-04-006-001-Bunka-DZ7-0839-3_1.jpg" alt="Japanese Street Styles w/ Pink Bob, Two-Tone Hair, Hats, Nile Perch, Vintage Suit, Kirby Bag, Vivienne Westwood, Alice and the Pirates, Yosuke &amp; Swankiss" width="140" height="180" loading="lazy"></noscript><img class=" lazyloaded" src="https://tokyofashion.com/wp-content/uploads/2019/11/NK-2019-11-04-006-001-Bunka-DZ7-0839-3_1.jpg" data-src="https://tokyofashion.com/wp-content/uploads/2019/11/NK-2019-11-04-006-001-Bunka-DZ7-0839-3_1.jpg" alt="Japanese Street Styles w/ Pink Bob, Two-Tone Hair, Hats, Nile Perch, Vintage Suit, Kirby Bag, Vivienne Westwood, Alice and the Pirates, Yosuke &amp; Swankiss" width="140" height="180" loading="lazy">
		</a>
	</li>
	<li>
				<a href="https://tokyofashion.com/vivienne-westwood-tokyo-street-fashion-wide-brim-hat-leopard-print-coat-rocking-horse-shoes/" class="photo" title="Vivienne Westwood Tokyo Street Fashion w/ Wide Brim Hat, Leopard Print Coat, Cardigan, Ruffle Blouse, Leather Briefcase &amp; Rocking Horse Shoes">
			<noscript><img src="https://tokyofashion.com/wp-content/uploads/2019/11/NK-2019-11-04-044-001-Bunka-DZ7-2420-2_1.jpg" alt="Vivienne Westwood Tokyo Street Fashion w/ Wide Brim Hat, Leopard Print Coat, Cardigan, Ruffle Blouse, Leather Briefcase &amp; Rocking Horse Shoes" width="140" height="180" loading="lazy"></noscript><img class=" lazyloaded" src="https://tokyofashion.com/wp-content/uploads/2019/11/NK-2019-11-04-044-001-Bunka-DZ7-2420-2_1.jpg" data-src="https://tokyofashion.com/wp-content/uploads/2019/11/NK-2019-11-04-044-001-Bunka-DZ7-2420-2_1.jpg" alt="Vivienne Westwood Tokyo Street Fashion w/ Wide Brim Hat, Leopard Print Coat, Cardigan, Ruffle Blouse, Leather Briefcase &amp; Rocking Horse Shoes" width="140" height="180" loading="lazy">
		</a>
	</li>
	<li>
				<a href="https://tokyofashion.com/japanese-styles-sexy-necklace-pink-panther-fkta-gallerie-tokyo-versace/" class="photo" title="Japanese Street Styles w/ SEXY Necklace, Pink Panther, FKTA, Gallerie Tokyo &amp; Versace">
			<noscript><img src="https://tokyofashion.com/wp-content/uploads/2019/11/NK-2019-11-03-016-001-Harajuku-DZ7-9893-2.jpg" alt="Japanese Street Styles w/ SEXY Necklace, Pink Panther, FKTA, Gallerie Tokyo &amp; Versace" width="140" height="180" loading="lazy"></noscript><img class=" lazyloaded" src="https://tokyofashion.com/wp-content/uploads/2019/11/NK-2019-11-03-016-001-Harajuku-DZ7-9893-2.jpg" data-src="https://tokyofashion.com/wp-content/uploads/2019/11/NK-2019-11-03-016-001-Harajuku-DZ7-9893-2.jpg" alt="Japanese Street Styles w/ SEXY Necklace, Pink Panther, FKTA, Gallerie Tokyo &amp; Versace" width="140" height="180" loading="lazy">
		</a>
	</li>
	<li>
				<a href="https://tokyofashion.com/tokyo-style-bambron-butterfly-wings-suit-chain-painted-shoes/" class="photo" title="Tokyo Street Style w/ BamBron Embellished Butterfly Wings Suit, Chain Necklaces &amp; Painted Shoes">
			<noscript><img src="https://tokyofashion.com/wp-content/uploads/2019/11/NK-2019-11-03-026-001-Harajuku-DZ7-0264.jpg" alt="Tokyo Street Style w/ BamBron Embellished Butterfly Wings Suit, Chain Necklaces &amp; Painted Shoes" width="140" height="180" loading="lazy"></noscript><img class="lazyload" src="data:image/svg+xml,%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20viewBox=%220%200%20140%20180%22%3E%3C/svg%3E" data-src="https://tokyofashion.com/wp-content/uploads/2019/11/NK-2019-11-03-026-001-Harajuku-DZ7-0264.jpg" alt="Tokyo Street Style w/ BamBron Embellished Butterfly Wings Suit, Chain Necklaces &amp; Painted Shoes" width="140" height="180" loading="lazy">
		</a>
	</li>
	<li>
				<a href="https://tokyofashion.com/tokyo-street-fashion-purple-hair-gold-crown-vinyl-mini-dress-office-kiko-boots/" class="photo" title="Colorful Tokyo Street Fashion w/ Purple Hair, Gold Crown, Vinyl Mini Dress, Gallerie &amp; Office Kiko Patent Boots">
			<noscript><img src="https://tokyofashion.com/wp-content/uploads/2019/11/NK-2019-11-04-043-001-Bunka-DZ7-2370_1.jpg" alt="Colorful Tokyo Street Fashion w/ Purple Hair, Gold Crown, Vinyl Mini Dress, Gallerie &amp; Office Kiko Patent Boots" width="140" height="180" loading="lazy"></noscript><img class="lazyload" src="data:image/svg+xml,%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20viewBox=%220%200%20140%20180%22%3E%3C/svg%3E" data-src="https://tokyofashion.com/wp-content/uploads/2019/11/NK-2019-11-04-043-001-Bunka-DZ7-2370_1.jpg" alt="Colorful Tokyo Street Fashion w/ Purple Hair, Gold Crown, Vinyl Mini Dress, Gallerie &amp; Office Kiko Patent Boots" width="140" height="180" loading="lazy">
		</a>
	</li>
	<li>
				<a href="https://tokyofashion.com/bunka-fashion-college-colorful-vintage-street-style-w-red-dress-spring-heel-sneakers-shinkirou-bag/" class="photo" title="Bunka Fashion College Colorful Vintage Street Style w/ Red Dress, Spring Heel Sneakers &amp; Shinkirou Bag">
			<noscript><img src="https://tokyofashion.com/wp-content/uploads/2019/11/NK-2019-11-04-025-001-Bunka-DZ7-1611_1.jpg" alt="Bunka Fashion College Colorful Vintage Street Style w/ Red Dress, Spring Heel Sneakers &amp; Shinkirou Bag" width="140" height="180" loading="lazy"></noscript><img class="lazyload" src="data:image/svg+xml,%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20viewBox=%220%200%20140%20180%22%3E%3C/svg%3E" data-src="https://tokyofashion.com/wp-content/uploads/2019/11/NK-2019-11-04-025-001-Bunka-DZ7-1611_1.jpg" alt="Bunka Fashion College Colorful Vintage Street Style w/ Red Dress, Spring Heel Sneakers &amp; Shinkirou Bag" width="140" height="180" loading="lazy">
		</a>
	</li>
	<li>
				<a href="https://tokyofashion.com/tokyo-street-styles-twin-knit-hat-houndstooth-dress-floral-prints-pink-house-bed-jw-ford/" class="photo" title="Red Tokyo Street Styles w/ Twin Buns, Knit Hat, Houndstooth Belted Dress, Floral Prints, Handmade Fashion, Pink House &amp; Bed JW Ford">
			<noscript><img src="https://tokyofashion.com/wp-content/uploads/2019/11/NK-2019-11-04-033-001-Bunka-DZ7-1951-2.jpg" alt="Red Tokyo Street Styles w/ Twin Buns, Knit Hat, Houndstooth Belted Dress, Floral Prints, Handmade Fashion, Pink House &amp; Bed JW Ford" width="140" height="180" loading="lazy"></noscript><img class="lazyload" src="data:image/svg+xml,%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20viewBox=%220%200%20140%20180%22%3E%3C/svg%3E" data-src="https://tokyofashion.com/wp-content/uploads/2019/11/NK-2019-11-04-033-001-Bunka-DZ7-1951-2.jpg" alt="Red Tokyo Street Styles w/ Twin Buns, Knit Hat, Houndstooth Belted Dress, Floral Prints, Handmade Fashion, Pink House &amp; Bed JW Ford" width="140" height="180" loading="lazy">
		</a>
	</li>
	<li>
				<a href="https://tokyofashion.com/colorful-hair-sailor-moon-tokyo-street-styles-twin-tails-handmade-fashion-tokyo-bopper/" class="photo" title="Colorful Hair &amp; Sailor Moon Tokyo Street Styles w/ Purple Hair, Green Twin Tails, Handmade Fashion, Tokyo Bopper &amp; Dr. Martens">
			<noscript><img src="https://tokyofashion.com/wp-content/uploads/2019/11/NK-2019-11-04-039-001-Bunka-DZ7-2184_1-1.jpg" alt="Colorful Hair &amp; Sailor Moon Tokyo Street Styles w/ Purple Hair, Green Twin Tails, Handmade Fashion, Tokyo Bopper &amp; Dr. Martens" width="140" height="180" loading="lazy"></noscript><img class="lazyload" src="data:image/svg+xml,%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20viewBox=%220%200%20140%20180%22%3E%3C/svg%3E" data-src="https://tokyofashion.com/wp-content/uploads/2019/11/NK-2019-11-04-039-001-Bunka-DZ7-2184_1-1.jpg" alt="Colorful Hair &amp; Sailor Moon Tokyo Street Styles w/ Purple Hair, Green Twin Tails, Handmade Fashion, Tokyo Bopper &amp; Dr. Martens" width="140" height="180" loading="lazy">
		</a>
	</li>
	<li>
				<a href="https://tokyofashion.com/tokyo-street-style-dries-van-noten-robe-de-chambre-comme-des-garcons-aska-masuda-christopher-nemeth/" class="photo" title="Bunka Fashion College Tokyo Street Style w/ Dries Van Noten, Robe de Chambre Comme des Garcons, Bed J.W. Ford, Aska Masuda &amp; Christopher Nemeth">
			<noscript><img src="https://tokyofashion.com/wp-content/uploads/2019/11/NK-2019-11-04-022-001-Bunka-DZ7-1482.jpg" alt="Bunka Fashion College Tokyo Street Style w/ Dries Van Noten, Robe de Chambre Comme des Garcons, Bed J.W. Ford, Aska Masuda &amp; Christopher Nemeth" width="140" height="180" loading="lazy"></noscript><img class="lazyload" src="data:image/svg+xml,%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20viewBox=%220%200%20140%20180%22%3E%3C/svg%3E" data-src="https://tokyofashion.com/wp-content/uploads/2019/11/NK-2019-11-04-022-001-Bunka-DZ7-1482.jpg" alt="Bunka Fashion College Tokyo Street Style w/ Dries Van Noten, Robe de Chambre Comme des Garcons, Bed J.W. Ford, Aska Masuda &amp; Christopher Nemeth" width="140" height="180" loading="lazy">
		</a>
	</li>
	<li>
				<a href="https://tokyofashion.com/gothic-japanese-steampunk-fashion-face-mask-bonnet-floral-headpiece/" class="photo" title="Gothic Japanese Steampunk Fashion w/ Face Mask, Bonnet, Floral Headpiece, Ruffle Shirt, Asymmetrical Skirt &amp; Boots">
			<noscript><img src="https://tokyofashion.com/wp-content/uploads/2019/11/NK-2019-11-04-003-001-Bunka-DZ7-0694-2_1.jpg" alt="Gothic Japanese Steampunk Fashion w/ Face Mask, Bonnet, Floral Headpiece, Ruffle Shirt, Asymmetrical Skirt &amp; Boots" width="140" height="180" loading="lazy"></noscript><img class="lazyload" src="data:image/svg+xml,%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20viewBox=%220%200%20140%20180%22%3E%3C/svg%3E" data-src="https://tokyofashion.com/wp-content/uploads/2019/11/NK-2019-11-04-003-001-Bunka-DZ7-0694-2_1.jpg" alt="Gothic Japanese Steampunk Fashion w/ Face Mask, Bonnet, Floral Headpiece, Ruffle Shirt, Asymmetrical Skirt &amp; Boots" width="140" height="180" loading="lazy">
		</a>
	</li>
	<li>
				<a href="https://tokyofashion.com/tokyo-street-style-vintage-belted-jacket-with-shoulder-pads-open-the-door-demonia/" class="photo" title="Red &amp; Black Tokyo Street Style w/ Vintage Belted Jacket With Shoulder Pads, Open The Door Bag &amp; Demonia Platforms">
			<noscript><img src="https://tokyofashion.com/wp-content/uploads/2019/11/NK-2019-11-04-002-001-Bunka-DZ7-0669-copy.jpg" alt="Red &amp; Black Tokyo Street Style w/ Vintage Belted Jacket With Shoulder Pads, Open The Door Bag &amp; Demonia Platforms" width="140" height="180" loading="lazy"></noscript><img class="lazyload" src="data:image/svg+xml,%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20viewBox=%220%200%20140%20180%22%3E%3C/svg%3E" data-src="https://tokyofashion.com/wp-content/uploads/2019/11/NK-2019-11-04-002-001-Bunka-DZ7-0669-copy.jpg" alt="Red &amp; Black Tokyo Street Style w/ Vintage Belted Jacket With Shoulder Pads, Open The Door Bag &amp; Demonia Platforms" width="140" height="180" loading="lazy">
		</a>
	</li>
	<li>
				<a href="https://tokyofashion.com/painted-mind-infection-fashion-tokyo-trench-coat-skeletons-kimono-givenchy-gucci/" class="photo" title="Hand Painted Mind Infection Street Fashion in Tokyo w/ Trench Coat, Skeletons Kimono, Givenchy, Gucci &amp; Dr. Martens">
			<noscript><img src="https://tokyofashion.com/wp-content/uploads/2019/11/NK-2019-11-03-027-001-Harajuku-DZ7-0283-2_1.jpg" alt="Hand Painted Mind Infection Street Fashion in Tokyo w/ Trench Coat, Skeletons Kimono, Givenchy, Gucci &amp; Dr. Martens" width="140" height="180" loading="lazy"></noscript><img class="lazyload" src="data:image/svg+xml,%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20viewBox=%220%200%20140%20180%22%3E%3C/svg%3E" data-src="https://tokyofashion.com/wp-content/uploads/2019/11/NK-2019-11-03-027-001-Harajuku-DZ7-0283-2_1.jpg" alt="Hand Painted Mind Infection Street Fashion in Tokyo w/ Trench Coat, Skeletons Kimono, Givenchy, Gucci &amp; Dr. Martens" width="140" height="180" loading="lazy">
		</a>
	</li>
	<li>
				<a href="https://tokyofashion.com/tokyo-street-styles-perverze-maison-margiela-belly-button-kiki-koenji-new-rock-faith-tokyo/" class="photo" title="Tokyo Teen Street Styles w/ Perverze Faux Fur Coat, Maison Margiela, Belly Button, Kiki Koenji, New Rock &amp; Faith Tokyo">
			<noscript><img src="https://tokyofashion.com/wp-content/uploads/2019/11/NK-2019-11-03-025-001-Harajuku-DZ7-0189.jpg" alt="Tokyo Teen Street Styles w/ Perverze Faux Fur Coat, Maison Margiela, Belly Button, Kiki Koenji, New Rock &amp; Faith Tokyo" width="140" height="180" loading="lazy"></noscript><img class="lazyload" src="data:image/svg+xml,%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20viewBox=%220%200%20140%20180%22%3E%3C/svg%3E" data-src="https://tokyofashion.com/wp-content/uploads/2019/11/NK-2019-11-03-025-001-Harajuku-DZ7-0189.jpg" alt="Tokyo Teen Street Styles w/ Perverze Faux Fur Coat, Maison Margiela, Belly Button, Kiki Koenji, New Rock &amp; Faith Tokyo" width="140" height="180" loading="lazy">
		</a>
	</li>
	<li>
				<a href="https://tokyofashion.com/minimalist-tokyo-street-styles-ombre-hair-gemini-tale-harness-vivienne-westwood-john-lawrence-sullivan/" class="photo" title="Minimalist Tokyo Street Styles w/ Ombre Hair, Gemini Tale Harness, Vivienne Westwood Coat, John Lawrence Sullivan &amp; Vintage Fashion">
			<noscript><img src="https://tokyofashion.com/wp-content/uploads/2019/11/NK-2019-11-03-032-001-Harajuku-DZ7-0505.jpg" alt="Minimalist Tokyo Street Styles w/ Ombre Hair, Gemini Tale Harness, Vivienne Westwood Coat, John Lawrence Sullivan &amp; Vintage Fashion" width="140" height="180" loading="lazy"></noscript><img class="lazyload" src="data:image/svg+xml,%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20viewBox=%220%200%20140%20180%22%3E%3C/svg%3E" data-src="https://tokyofashion.com/wp-content/uploads/2019/11/NK-2019-11-03-032-001-Harajuku-DZ7-0505.jpg" alt="Minimalist Tokyo Street Styles w/ Ombre Hair, Gemini Tale Harness, Vivienne Westwood Coat, John Lawrence Sullivan &amp; Vintage Fashion" width="140" height="180" loading="lazy">
		</a>
	</li>
	<li>
				<a href="https://tokyofashion.com/pink-handmade-kawaii-style-tulle-gingham-pinafore-quilted-bag-fuzzy-hat-wc-tokyo-bopper/" class="photo" title="Pink Handmade Kawaii Japanese Street Style w/ Tulle Blouse, Gingham Pinafore, Quilted Bag, Fuzzy Hat, WC &amp; Tokyo Bopper">
			<noscript><img src="https://tokyofashion.com/wp-content/uploads/2019/11/NK-2019-11-03-017-001-Harajuku-DZ7-9950.jpg" alt="Pink Handmade Kawaii Japanese Street Style w/ Tulle Blouse, Gingham Pinafore, Quilted Bag, Fuzzy Hat, WC &amp; Tokyo Bopper" width="140" height="180" loading="lazy"></noscript><img class="lazyload" src="data:image/svg+xml,%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20viewBox=%220%200%20140%20180%22%3E%3C/svg%3E" data-src="https://tokyofashion.com/wp-content/uploads/2019/11/NK-2019-11-03-017-001-Harajuku-DZ7-9950.jpg" alt="Pink Handmade Kawaii Japanese Street Style w/ Tulle Blouse, Gingham Pinafore, Quilted Bag, Fuzzy Hat, WC &amp; Tokyo Bopper" width="140" height="180" loading="lazy">
		</a>
	</li>
	<li>
				<a href="https://tokyofashion.com/the-ivy-tokyo-mother-daughter-street-styles-floral-earrings-vintage-denim-tegteg-verdy-puchu-monster-backpack/" class="photo" title="The Ivy Tokyo Mother &amp; Daughter Street Styles w/ Floral Earrings, Vintage Studded Denim Jacket, TEGTEG Sweater, Flared Pants &amp; Verdy x Puchu Monster Backpack">
			<noscript><img src="https://tokyofashion.com/wp-content/uploads/2019/11/NK-2019-11-03-003-001-Harajuku-DZ7-9463_1.jpg" alt="The Ivy Tokyo Mother &amp; Daughter Street Styles w/ Floral Earrings, Vintage Studded Denim Jacket, TEGTEG Sweater, Flared Pants &amp; Verdy x Puchu Monster Backpack" width="140" height="180" loading="lazy"></noscript><img class="lazyload" src="data:image/svg+xml,%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20viewBox=%220%200%20140%20180%22%3E%3C/svg%3E" data-src="https://tokyofashion.com/wp-content/uploads/2019/11/NK-2019-11-03-003-001-Harajuku-DZ7-9463_1.jpg" alt="The Ivy Tokyo Mother &amp; Daughter Street Styles w/ Floral Earrings, Vintage Studded Denim Jacket, TEGTEG Sweater, Flared Pants &amp; Verdy x Puchu Monster Backpack" width="140" height="180" loading="lazy">
		</a>
	</li>
	<li>
				<a href="https://tokyofashion.com/bunka-fashion-college-street-styles-oversized-sunglasses-furry-coat-chanel-quilted-bag-tabi-boots/" class="photo" title="Bunka Fashion College Street Styles w/ Oversized Sunglasses, Cloche Hat, Furry Coat, Textured Eyelet Jacket, Chanel Quilted Bag &amp; Tabi Boots">
			<noscript><img src="https://tokyofashion.com/wp-content/uploads/2019/11/NK-2019-11-03-009-001-Harajuku-DZ7-9679.jpg" alt="Bunka Fashion College Street Styles w/ Oversized Sunglasses, Cloche Hat, Furry Coat, Textured Eyelet Jacket, Chanel Quilted Bag &amp; Tabi Boots" width="140" height="180" loading="lazy"></noscript><img class="lazyload" src="data:image/svg+xml,%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20viewBox=%220%200%20140%20180%22%3E%3C/svg%3E" data-src="https://tokyofashion.com/wp-content/uploads/2019/11/NK-2019-11-03-009-001-Harajuku-DZ7-9679.jpg" alt="Bunka Fashion College Street Styles w/ Oversized Sunglasses, Cloche Hat, Furry Coat, Textured Eyelet Jacket, Chanel Quilted Bag &amp; Tabi Boots" width="140" height="180" loading="lazy">
		</a>
	</li>
	<li>
				<a href="https://tokyofashion.com/tokyo-streetwear-lad-musician-comme-des-garcons-homme-plus-dttk-dulcamara-margiela-alexander-wang/" class="photo" title="Tokyo Streetwear Styles w/ LAD Musician, Comme des Garcons Homme Plus, D.TT.K Puffer Coat, Dulcamara, Maison Margiela &amp; Alexander Wang">
			<noscript><img src="https://tokyofashion.com/wp-content/uploads/2019/11/NK-2019-11-03-001-001-Harajuku-DZ7-9383-2_1.jpg" alt="Tokyo Streetwear Styles w/ LAD Musician, Comme des Garcons Homme Plus, D.TT.K Puffer Coat, Dulcamara, Maison Margiela &amp; Alexander Wang" width="140" height="180" loading="lazy"></noscript><img class="lazyload" src="data:image/svg+xml,%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20viewBox=%220%200%20140%20180%22%3E%3C/svg%3E" data-src="https://tokyofashion.com/wp-content/uploads/2019/11/NK-2019-11-03-001-001-Harajuku-DZ7-9383-2_1.jpg" alt="Tokyo Streetwear Styles w/ LAD Musician, Comme des Garcons Homme Plus, D.TT.K Puffer Coat, Dulcamara, Maison Margiela &amp; Alexander Wang" width="140" height="180" loading="lazy">
		</a>
	</li>
	<li>
				<a href="https://tokyofashion.com/handmade-tokyo-street-style-bunka-fashion-college-yohji-yamamoto-margiela/" class="photo" title="Handmade Tokyo Street Style at Bunka Fashion College w/ Yohji Yamamoto, Margiela &amp; Vivienne Westwood">
			<noscript><img src="https://tokyofashion.com/wp-content/uploads/2019/11/Bunka-Fashion-College-Street-Style-20191104DZ72057.jpg" alt="Handmade Tokyo Street Style at Bunka Fashion College w/ Yohji Yamamoto, Margiela &amp; Vivienne Westwood" width="140" height="180" loading="lazy"></noscript><img class="lazyload" src="data:image/svg+xml,%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20viewBox=%220%200%20140%20180%22%3E%3C/svg%3E" data-src="https://tokyofashion.com/wp-content/uploads/2019/11/Bunka-Fashion-College-Street-Style-20191104DZ72057.jpg" alt="Handmade Tokyo Street Style at Bunka Fashion College w/ Yohji Yamamoto, Margiela &amp; Vivienne Westwood" width="140" height="180" loading="lazy">
		</a>
	</li>
	<li>
				<a href="https://tokyofashion.com/plaid-tokyo-streetwear-styles-w-plaid-headpiece-shimamura-furry-monster-jacket-plaid-collar-jun-takahashi-winged-backpack-demonia-caged-platforms/" class="photo" title="Plaid Tokyo Streetwear Styles w/ Plaid Headpiece, Shimamura Furry Monster Jacket, Plaid Collar, Jun Takahashi, Winged Backpack &amp; Demonia Caged Platforms">
			<noscript><img src="https://tokyofashion.com/wp-content/uploads/2019/11/NK-2019-11-04-034-001-Bunka-DZ7-1990.jpg" alt="Plaid Tokyo Streetwear Styles w/ Plaid Headpiece, Shimamura Furry Monster Jacket, Plaid Collar, Jun Takahashi, Winged Backpack &amp; Demonia Caged Platforms" width="140" height="180" loading="lazy"></noscript><img class="lazyload" src="data:image/svg+xml,%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20viewBox=%220%200%20140%20180%22%3E%3C/svg%3E" data-src="https://tokyofashion.com/wp-content/uploads/2019/11/NK-2019-11-04-034-001-Bunka-DZ7-1990.jpg" alt="Plaid Tokyo Streetwear Styles w/ Plaid Headpiece, Shimamura Furry Monster Jacket, Plaid Collar, Jun Takahashi, Winged Backpack &amp; Demonia Caged Platforms" width="140" height="180" loading="lazy">
		</a>
	</li>
	<li>
				<a href="https://tokyofashion.com/all-white-fashion-w-twin-pink-tails-red-eye-makeup-ruffle-headpiece-atelier-pierrot-metamorphose-temps-de-fille-pink-bags-axes-femme-wedges/" class="photo" title="All White Fashion w/ Twin Pink Tails, Red Eye Makeup, Ruffle Headpiece, Atelier Pierrot, Metamorphose Temps De Fille, Pink Bags &amp; Axes Femme Wedges">
			<noscript><img src="https://tokyofashion.com/wp-content/uploads/2019/11/NK-2019-11-04-028-001-Bunka-DZ7-1739.jpg" alt="All White Fashion w/ Twin Pink Tails, Red Eye Makeup, Ruffle Headpiece, Atelier Pierrot, Metamorphose Temps De Fille, Pink Bags &amp; Axes Femme Wedges" width="140" height="180" loading="lazy"></noscript><img class="lazyload" src="data:image/svg+xml,%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20viewBox=%220%200%20140%20180%22%3E%3C/svg%3E" data-src="https://tokyofashion.com/wp-content/uploads/2019/11/NK-2019-11-04-028-001-Bunka-DZ7-1739.jpg" alt="All White Fashion w/ Twin Pink Tails, Red Eye Makeup, Ruffle Headpiece, Atelier Pierrot, Metamorphose Temps De Fille, Pink Bags &amp; Axes Femme Wedges" width="140" height="180" loading="lazy">
		</a>
	</li>
	<li>
				<a href="https://tokyofashion.com/colorful-head-scarf-baby-the-stars-shine-bright-dress-kinji-knit-blazer-rrr-shirt-iro-wo-matoue-vivienne-westwood-satchel-bags-dr-martens/" class="photo" title="Colorful Head Scarf, Baby The Stars Shine Bright Dress, Kinji Knit Blazer, RRR Shirt, Iro Wo Matoue, Vivienne Westwood, Satchel Bags &amp; Dr. Martens">
			<noscript><img src="https://tokyofashion.com/wp-content/uploads/2019/11/NK-2019-11-04-024-001-Bunka-DZ7-1559_1.jpg" alt="Colorful Head Scarf, Baby The Stars Shine Bright Dress, Kinji Knit Blazer, RRR Shirt, Iro Wo Matoue, Vivienne Westwood, Satchel Bags &amp; Dr. Martens" width="140" height="180" loading="lazy"></noscript><img class="lazyload" src="data:image/svg+xml,%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20viewBox=%220%200%20140%20180%22%3E%3C/svg%3E" data-src="https://tokyofashion.com/wp-content/uploads/2019/11/NK-2019-11-04-024-001-Bunka-DZ7-1559_1.jpg" alt="Colorful Head Scarf, Baby The Stars Shine Bright Dress, Kinji Knit Blazer, RRR Shirt, Iro Wo Matoue, Vivienne Westwood, Satchel Bags &amp; Dr. Martens" width="140" height="180" loading="lazy">
		</a>
	</li>
	<li>
				<a href="https://tokyofashion.com/tokyo-monochrome-streetwear-styles-w-cat-eye-sunglasses-belted-corset-harley-davidson-dyog-cropped-top-gallerie-zara-hm-bershka-forever21-demonia-converse/" class="photo" title="Tokyo Monochrome Streetwear Styles w/ Cat Eye Sunglasses, Belted Corset, Harley Davidson, DYOG Cropped Top, Gallerie, Zara, H&amp;M, Bershka, Forever21, Demonia &amp; Converse">
			<noscript><img src="https://tokyofashion.com/wp-content/uploads/2019/11/NK-2019-11-04-018-001-Bunka-DZ7-1296-2.jpg" alt="Tokyo Monochrome Streetwear Styles w/ Cat Eye Sunglasses, Belted Corset, Harley Davidson, DYOG Cropped Top, Gallerie, Zara, H&amp;M, Bershka, Forever21, Demonia &amp; Converse" width="140" height="180" loading="lazy"></noscript><img class="lazyload" src="data:image/svg+xml,%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20viewBox=%220%200%20140%20180%22%3E%3C/svg%3E" data-src="https://tokyofashion.com/wp-content/uploads/2019/11/NK-2019-11-04-018-001-Bunka-DZ7-1296-2.jpg" alt="Tokyo Monochrome Streetwear Styles w/ Cat Eye Sunglasses, Belted Corset, Harley Davidson, DYOG Cropped Top, Gallerie, Zara, H&amp;M, Bershka, Forever21, Demonia &amp; Converse" width="140" height="180" loading="lazy">
		</a>
	</li>
	<li>
				<a href="https://tokyofashion.com/bunka-fashion-college-street-style-w-lee-jacket-digawell-shirt-us-army-pants/" class="photo" title="Bunka Fashion College Street Style w/ Lee Jacket, Digawell Shirt &amp; US Army Pants">
			<noscript><img src="https://tokyofashion.com/wp-content/uploads/2019/11/NK-2019-11-04-042-001-Bunka-DZ7-2327.jpg" alt="Bunka Fashion College Street Style w/ Lee Jacket, Digawell Shirt &amp; US Army Pants" width="140" height="180" loading="lazy"></noscript><img class="lazyload" src="data:image/svg+xml,%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20viewBox=%220%200%20140%20180%22%3E%3C/svg%3E" data-src="https://tokyofashion.com/wp-content/uploads/2019/11/NK-2019-11-04-042-001-Bunka-DZ7-2327.jpg" alt="Bunka Fashion College Street Style w/ Lee Jacket, Digawell Shirt &amp; US Army Pants" width="140" height="180" loading="lazy">
		</a>
	</li>
	<li>
				<a href="https://tokyofashion.com/bunka-fashion-college-handmade-flower-bag/" class="photo" title="Bunka Fashion College Handmade &amp; Vintage Street Fashion w/ Leopard Print Dress &amp; Flower Bag">
			<noscript><img src="https://tokyofashion.com/wp-content/uploads/2019/11/NK-2019-11-04-041-001-Bunka-DZ7-2293.jpg" alt="Bunka Fashion College Handmade &amp; Vintage Street Fashion w/ Leopard Print Dress &amp; Flower Bag" width="140" height="180" loading="lazy"></noscript><img class="lazyload" src="data:image/svg+xml,%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20viewBox=%220%200%20140%20180%22%3E%3C/svg%3E" data-src="https://tokyofashion.com/wp-content/uploads/2019/11/NK-2019-11-04-041-001-Bunka-DZ7-2293.jpg" alt="Bunka Fashion College Handmade &amp; Vintage Street Fashion w/ Leopard Print Dress &amp; Flower Bag" width="140" height="180" loading="lazy">
		</a>
	</li>
	<li>
				<a href="https://tokyofashion.com/all-black-rick-owens-street-fashion-w-skinny-pants-platform-boots-chains/" class="photo" title="All Black Rick Owens Street Fashion w/ Skinny Pants, Platform Boots &amp; Chains">
			<noscript><img src="https://tokyofashion.com/wp-content/uploads/2019/11/NK-2019-11-04-038-001-Bunka-DZ7-2153.jpg" alt="All Black Rick Owens Street Fashion w/ Skinny Pants, Platform Boots &amp; Chains" width="140" height="180" loading="lazy"></noscript><img class="lazyload" src="data:image/svg+xml,%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20viewBox=%220%200%20140%20180%22%3E%3C/svg%3E" data-src="https://tokyofashion.com/wp-content/uploads/2019/11/NK-2019-11-04-038-001-Bunka-DZ7-2153.jpg" alt="All Black Rick Owens Street Fashion w/ Skinny Pants, Platform Boots &amp; Chains" width="140" height="180" loading="lazy">
		</a>
	</li>
	<li>
				<a href="https://tokyofashion.com/tokyo-street-style-w-graffiti-coat-colorful-platform-shoes-beret-man-g-demonia-kobinai/" class="photo" title="Tokyo Street Style w/ Graffiti Coat, Colorful Platform Shoes, Beret, Man G, Demonia &amp; Kobinai">
			<noscript><img src="https://tokyofashion.com/wp-content/uploads/2019/11/NK-2019-11-04-037-001-Bunka-DZ7-2119.jpg" alt="Tokyo Street Style w/ Graffiti Coat, Colorful Platform Shoes, Beret, Man G, Demonia &amp; Kobinai" width="140" height="180" loading="lazy"></noscript><img class="lazyload" src="data:image/svg+xml,%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20viewBox=%220%200%20140%20180%22%3E%3C/svg%3E" data-src="https://tokyofashion.com/wp-content/uploads/2019/11/NK-2019-11-04-037-001-Bunka-DZ7-2119.jpg" alt="Tokyo Street Style w/ Graffiti Coat, Colorful Platform Shoes, Beret, Man G, Demonia &amp; Kobinai" width="140" height="180" loading="lazy">
		</a>
	</li>
	<li>
				<a href="https://tokyofashion.com/vintage-street-styles-w-tokyo-bopper-lily-brown-acne-studios-gucci/" class="photo" title="Vintage Street Styles w/ Tokyo Bopper, Lily Brown, Acne Studios &amp; Gucci">
			<noscript><img src="https://tokyofashion.com/wp-content/uploads/2019/11/NK-2019-11-04-032-001-Bunka-DZ7-1907.jpg" alt="Vintage Street Styles w/ Tokyo Bopper, Lily Brown, Acne Studios &amp; Gucci" width="140" height="180" loading="lazy"></noscript><img class="lazyload" src="data:image/svg+xml,%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20viewBox=%220%200%20140%20180%22%3E%3C/svg%3E" data-src="https://tokyofashion.com/wp-content/uploads/2019/11/NK-2019-11-04-032-001-Bunka-DZ7-1907.jpg" alt="Vintage Street Styles w/ Tokyo Bopper, Lily Brown, Acne Studios &amp; Gucci" width="140" height="180" loading="lazy">
		</a>
	</li>
</ul><br style="clear:both;"></div>							<div class="navigation">
																	<div class="navleft">
										<a href="https://tokyofashion.com/photos/?location=Shinjuku&amp;start=40">« Show Older Shinjuku Photos</a>
									</div>
																							</div>
							<div id="photonav" align="center">
								<a href="https://tokyofashion.com/photos/?location=Shinjuku&amp;month=3&amp;years=2025">Browse Shinjuku Photos By Month
								</a>
							</div>
					</div> <!-- .contentpanel -->
				</div>
				
<aside role="complementary" class="sidebar">
	
		<section id="recent-posts-2" class="widget widget_recent_entries">
		<h2 class="widget-title">Recent Posts</h2>
		<ul>
											<li>
					<a href="https://tokyofashion.com/korean-street-style-harajuku-japan-metal-glove-thug-club-fashion/">Korean Street Style in Harajuku, Japan w/ Giant Metal Glove &amp; Thug Club Fashion</a>
									</li>
											<li>
					<a href="https://tokyofashion.com/japanese-clown-street-style-harajuku-w-hello-kitty-shironuri-makeup-room-shoes/">Japanese Clown-Inspired Street Style in Harajuku w/ Hello Kitty, Shironuri Makeup &amp; Room Shoes</a>
									</li>
											<li>
					<a href="https://tokyofashion.com/japanese-gothic-tattoo-artist-vivienne-westwood-harajuku-tokyo/">Japanese Gothic Tattoo Artist Wearing Vivienne Westwood on the Street in Harajuku, Tokyo</a>
									</li>
											<li>
					<a href="https://tokyofashion.com/japanese-visual-kei-harajuku-asakura-garo-opanchu-usagi/">Japanese Visual Kei Singer in Harajuku w/ Kawaii Pink, Asakura Garo &amp; Opanchu Usagi</a>
									</li>
											<li>
					<a href="https://tokyofashion.com/japanese-dancer-hime-hairstyle-harajuku-street-style-not-conventional-yosuke-boots/">Japanese Dancer w/ Hime Hairstyle in All Black Harajuku Street Style, Not Conventional &amp; Yosuke Boots</a>
									</li>
					</ul>

		</section><section id="linkcat-415" class="widget widget_links"><h2 class="widget-title">Fashion Brands</h2>
	<ul class="xoxo blogroll">
<li><a href="http://www.virtualjapan.com/wiki/A_Bathing_Ape" rel="noopener" title="BAPE" target="_blank">A Bathing Ape</a></li>
<li><a href="http://www.virtualjapan.com/wiki/AS_KNOW_AS_de_base" rel="noopener" title="AS KNOW AS" target="_blank">AS KNOW AS</a></li>
<li><a href="http://www.virtualjapan.com/wiki/Ato_%28fashion_brand%29" rel="noopener" title="Ato Japan" target="_blank">Ato</a></li>
<li><a href="http://www.virtualjapan.com/wiki/Billionaire_Boys_Club" rel="noopener" title="Billionaire Boys Club" target="_blank">Billionaire Boys Club</a></li>
<li><a href="http://www.virtualjapan.com/wiki/Chisato_Tsumori" rel="noopener" title="Chisato Tsumori" target="_blank">Chisato Tsumori</a></li>
<li><a href="http://www.virtualjapan.com/wiki/Comme_des_Garcons" rel="noopener" title="Comme des Garcons" target="_blank">Comme des Garcons</a></li>
<li><a href="http://www.virtualjapan.com/wiki/Edwin" rel="noopener" title="Edwin Jeans" target="_blank">Edwin</a></li>
<li><a href="http://www.virtualjapan.com/wiki/Frapbois" rel="noopener" title="Frapbois" target="_blank">Frapbois</a></li>
<li><a href="http://www.virtualjapan.com/wiki/Hysteric_Glamour" rel="noopener" title="Hysteric Glamour" target="_blank">Hysteric Glamour</a></li>
<li><a href="http://www.virtualjapan.com/wiki/Limi_Feu" rel="noopener" title="Limi Feu" target="_blank">Limi Feu</a></li>
<li><a href="http://www.virtualjapan.com/wiki/Mercibeaucoup" rel="noopener" title="Mercibeaucoup" target="_blank">Mercibeaucoup</a></li>
<li><a href="http://www.virtualjapan.com/wiki/N.Hoolywood" rel="noopener" title="N.Hoolywood" target="_blank">N.Hoolywood</a></li>
<li><a href="http://www.virtualjapan.com/wiki/Samantha_Thavasa" rel="noopener" title="Samantha Thavasa" target="_blank">Samantha Thavasa</a></li>
<li><a href="http://www.virtualjapan.com/wiki/The_Viridi-anne" rel="noopener" title="The Viridi-anne" target="_blank">The Viridi-anne</a></li>

	</ul>
</section>
</aside><!-- #secondary -->
			</div>
          </main>
	</div><!-- #content -->
<footer role="contentinfo" class="footer">
    <div class="inner-wrapper footer-wrapper">
        <div class="footer-main">
            <div class="footer-menu">
                <button class="menu-toggle" aria-controls="primary-menu" aria-expanded="false">Primary Menu</button>
                <div class="menu-footer-container"><ul id="Footer" class="menu"><li id="menu-item-94796" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-home menu-item-94796"><a href="https://tokyofashion.com/">Home</a></li>
<li id="menu-item-94797" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-94797"><a href="https://tokyofashion.com/articles/">Articles</a></li>
<li id="menu-item-94798" class="menu-item menu-item-type-post_type menu-item-object-page current-menu-item page_item page-item-1308 current_page_item menu-item-94798"><a href="https://tokyofashion.com/photos/" aria-current="page">Street Photos</a></li>
<li id="menu-item-94799" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-94799"><a href="https://tokyofashion.com/brands/">Brands</a></li>
<li id="menu-item-94800" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-94800"><a href="https://tokyofashion.com/forum/">Forum</a></li>
<li id="menu-item-94801" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-94801"><a href="https://tokyofashion.com/fashion-map/">Fashion Map</a></li>
<li id="menu-item-94802" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-94802"><a href="https://tokyofashion.com/music/">Music</a></li>
<li id="menu-item-94803" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-94803"><a href="https://tokyofashion.com/contests/">Contests</a></li>
<li id="menu-item-94804" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-94804"><a href="https://tokyofashion.com/contributors/">About</a></li>
</ul></div>            </div>
            <div class="footer-logo logo">
                <noscript><img width="148" height="72" src="/wp-content/themes/tokyofashion/img/footer-logo.gif" alt="Logo"></noscript><img class="lazyload" width="148" height="72" src="data:image/svg+xml,%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20viewBox=%220%200%20148%2072%22%3E%3C/svg%3E" data-src="/wp-content/themes/tokyofashion/img/footer-logo.gif" alt="Logo">
            </div>
        </div>
        <div class="footer-copyright">
            <p>Copyright 2000-2021 TokyoFashion.com. All rights reserved. <a href="#">Privacy Policy</a></p>
        </div>
    </div>
</footer>
</div>

<noscript><style>.lazyload{display:none;}</style></noscript><script data-noptimize="1">window.lazySizesConfig=window.lazySizesConfig||{};window.lazySizesConfig.loadMode=1;</script><script async="" data-noptimize="1" src="https://tokyofashion.com/wp-content/plugins/autoptimize/classes/external/js/lazysizes.min.js?ao_version=3.1.13"></script>





<script defer="" src="https://tokyofashion.com/wp-content/cache/autoptimize/js/autoptimize_4c77f180cca5754b3c917b64152ec93e.js"></script><script>(function(){function c(){var b=a.contentDocument||a.contentWindow.document;if(b){var d=b.createElement('script');d.innerHTML="window.__CF$cv$params={r:'9201e5221fa2c96a',t:'MTc0MTkzNTYzNy4wMDAwMDA='};var a=document.createElement('script');a.nonce='';a.src='/cdn-cgi/challenge-platform/scripts/jsd/main.js';document.getElementsByTagName('head')[0].appendChild(a);";b.getElementsByTagName('head')[0].appendChild(d)}}if(document.body){var a=document.createElement('iframe');a.height=1;a.width=1;a.style.position='absolute';a.style.top=0;a.style.left=0;a.style.border='none';a.style.visibility='hidden';document.body.appendChild(a);if('loading'!==document.readyState)c();else if(window.addEventListener)document.addEventListener('DOMContentLoaded',c);else{var e=document.onreadystatechange||function(){};document.onreadystatechange=function(b){e(b);'loading'!==document.readyState&&(document.onreadystatechange=e,c())}}}})();</script><iframe height="1" width="1" style="position: absolute; top: 0px; left: 0px; border: none; visibility: hidden;"></iframe><script defer="" src="https://static.cloudflareinsights.com/beacon.min.js/vcd15cbe7772f49c399c6a5babf22c1241717689176015" integrity="sha512-ZpsOmlRQV6y907TI0dKBHq9Md29nnaEIPlkf84rnaERnq6zvWvPUqr2ft8M1aS28oN72PdrCzSjY4U6VaAw1EQ==" data-cf-beacon="{&quot;rayId&quot;:&quot;9201e5221fa2c96a&quot;,&quot;serverTiming&quot;:{&quot;name&quot;:{&quot;cfExtPri&quot;:true,&quot;cfL4&quot;:true,&quot;cfSpeedBrain&quot;:true,&quot;cfCacheStatus&quot;:true}},&quot;version&quot;:&quot;2025.1.0&quot;,&quot;token&quot;:&quot;a4577270ad5a4bf19902742d028d2a2b&quot;}" crossorigin="anonymous"></script>





</body></html>"""  # Replace this with your actual HTML data

soup = BeautifulSoup(html, "html.parser")


data = []
for link in soup.find_all("a", href=True):  
    title = link.get_text(strip=True)
    url = link["href"]
    
    # Find image inside the link (if available)
    img_tag = link.find("img")
    img_url = img_tag["src"] if img_tag else "No Image"
    
    data.append([title, url, img_url])


csv_file = "shinjukutrends.csv"
with open(csv_file, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Title", "Link", "Image URL"])
    writer.writerows(data)

print(f"shinjuku")



html = """<!DOCTYPE html><html lang="en-US"><head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<link rel="preload" href="https://tokyofashion.com/wp-content/themes/tokyofashion/fonts/fontawesome-webfont.woff2?v=4.7.0" as="font" type="font/woff2" crossorigin=""><link rel="profile" href="https://gmpg.org/xfn/11">

	<link media="all" href="https://tokyofashion.com/wp-content/cache/autoptimize/css/autoptimize_f035207383e8e457d3776c8597bfc517.css" rel="stylesheet"><title>Harajuku Japanese Street Fashion Photos – Tokyo Fashion</title>
<meta name="robots" content="max-image-preview:large">
	
	<link href="https://fonts.gstatic.com" crossorigin="anonymous" rel="preconnect">
<link rel="alternate" type="application/rss+xml" title="Tokyo Fashion » Feed" href="https://tokyofashion.com/feed/">
<link rel="alternate" type="application/rss+xml" title="Tokyo Fashion » Comments Feed" href="https://tokyofashion.com/comments/feed/">
<link rel="alternate" type="application/rss+xml" title="Tokyo Fashion » Tokyo Street Fashion Photos Comments Feed" href="https://tokyofashion.com/photos/feed/">











<script src="https://tokyofashion.com/wp-includes/js/jquery/jquery.min.js?ver=3.7.1" id="jquery-core-js"></script>




<script id="responsive-lightbox-js-before">
var rlArgs = {"script":"magnific","selector":"lightbox","customEvents":"","activeGalleries":true,"disableOn":0,"midClick":true,"preloader":true,"closeOnContentClick":true,"closeOnBgClick":true,"closeBtnInside":true,"showCloseBtn":true,"enableEscapeKey":true,"alignTop":false,"fixedContentPos":"auto","fixedBgPos":"auto","autoFocusLast":true,"woocommerce_gallery":false,"ajaxurl":"https:\/\/tokyofashion.com\/wp-admin\/admin-ajax.php","nonce":"26d353d815","preview":false,"postId":1308,"scriptExtension":false};
</script>

<link rel="https://api.w.org/" href="https://tokyofashion.com/wp-json/"><link rel="alternate" title="JSON" type="application/json" href="https://tokyofashion.com/wp-json/wp/v2/pages/1308"><link rel="EditURI" type="application/rsd+xml" title="RSD" href="https://tokyofashion.com/xmlrpc.php?rsd">
<meta name="generator" content="WordPress 6.7.2">
<link rel="canonical" href="https://tokyofashion.com/photos/">
<link rel="shortlink" href="https://tokyofashion.com/?p=1308">
<link rel="alternate" title="oEmbed (JSON)" type="application/json+oembed" href="https://tokyofashion.com/wp-json/oembed/1.0/embed?url=https%3A%2F%2Ftokyofashion.com%2Fphotos%2F">
<link rel="alternate" title="oEmbed (XML)" type="text/xml+oembed" href="https://tokyofashion.com/wp-json/oembed/1.0/embed?url=https%3A%2F%2Ftokyofashion.com%2Fphotos%2F&amp;format=xml">
<link rel="pingback" href="https://tokyofashion.com/xmlrpc.php">		
		</head>

<body class="home">
<div class="header-menu_mob">
    <nav role="navigation">
        <div class="menu-main-container"><ul id="Main" class="menu"><li id="menu-item-94790" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-home menu-item-94790"><a href="https://tokyofashion.com/">Home</a></li>
<li id="menu-item-94791" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-94791"><a href="https://tokyofashion.com/articles/">Articles</a></li>
<li id="menu-item-94792" class="menu-item menu-item-type-post_type menu-item-object-page current-menu-item page_item page-item-1308 current_page_item menu-item-94792"><a href="https://tokyofashion.com/photos/" aria-current="page">Street Photos</a></li>
<li id="menu-item-94793" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-94793"><a href="https://tokyofashion.com/brands/">Brands</a></li>
<li id="menu-item-94794" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-94794"><a href="https://tokyofashion.com/fashion-map/">Fashion Map</a></li>
<li id="menu-item-94795" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-94795"><a href="https://tokyofashion.com/music/">Music</a></li>
</ul></div>    </nav>
    <div class="header-menu_close fa fa-times"></div>
</div>
<div class="main-wrapper">
    <header role="banner" class="header">
        <div class="inner-wrapper header-wrapper">
            <div class="header-block">
                <div class="header-logo logo">
                    	<a href="https://tokyofashion.com/" class="custom-logo-link" rel="home"><noscript><img width="245" height="118" src="https://tokyofashion.com/wp-content/uploads/2021/03/cropped-logo-1.gif" class="custom-logo" alt="Tokyo Fashion" decoding="async" /></noscript><img width="245" height="118" src="https://tokyofashion.com/wp-content/uploads/2021/03/cropped-logo-1.gif" data-src="https://tokyofashion.com/wp-content/uploads/2021/03/cropped-logo-1.gif" class="custom-logo lazyloaded" alt="Tokyo Fashion" decoding="async"></a>                </div>
                <div class="header-menu">
                    <nav role="navigation">
                        <button class="menu-toggle" aria-controls="primary-menu" aria-expanded="false">Primary Menu</button>
                        <div class="menu-main-container"><ul id="Main" class="menu"><li class="menu-item menu-item-type-post_type menu-item-object-page menu-item-home menu-item-94790"><a href="https://tokyofashion.com/">Home</a></li>
<li class="menu-item menu-item-type-post_type menu-item-object-page menu-item-94791"><a href="https://tokyofashion.com/articles/">Articles</a></li>
<li class="menu-item menu-item-type-post_type menu-item-object-page current-menu-item page_item page-item-1308 current_page_item menu-item-94792"><a href="https://tokyofashion.com/photos/" aria-current="page">Street Photos</a></li>
<li class="menu-item menu-item-type-post_type menu-item-object-page menu-item-94793"><a href="https://tokyofashion.com/brands/">Brands</a></li>
<li class="menu-item menu-item-type-post_type menu-item-object-page menu-item-94794"><a href="https://tokyofashion.com/fashion-map/">Fashion Map</a></li>
<li class="menu-item menu-item-type-post_type menu-item-object-page menu-item-94795"><a href="https://tokyofashion.com/music/">Music</a></li>
</ul></div>                    </nav>
                </div>
            </div>
            <div class="header-block">
                <div class="header-sandwich fa fa-bars"></div>
                <div class="header-block_inner">
                    <div class="header-social">
                        <ul>
                            <li><a href="https://www.facebook.com/TokyoFashion" class="fa fa-facebook" target="_blank"></a></li>
                            <li><a href="https://twitter.com/tokyofashion" class="fa fa-twitter" target="_blank"></a></li>
                            <li><a href="https://feeds.feedburner.com/TokyoFashion" class="fa fa-rss" target="_blank"></a></li>
                            <li><a href="https://feedburner.google.com/fb/a/mailverify?uri=TokyoFashion&amp;loc=en_US" class="fa fa-envelope" target="_blank"></a></li>
                        </ul>
                    </div>
                    <div class="header-search">
                        <a href="#" title="Search" class="header-search_link fa fa-search"></a>
                        <div class="header-search_overlay">
                            <form method="get" class="search-form" action="https://tokyofashion.com/">
                                <label>
                                    <span class="screen-reader-text">Search for:</span>
                                    <input type="search" class="search-field" placeholder="Type and hit enter..." value="" name="s" title="Search for:">
                                </label>
                                <button type="submit" class="search-submit"><i class="fa fa-search"></i></button>
                            </form>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </header>

<div id="content">
		  <main role="main" class="main-content">
                <div class="inner-wrapper main-inner_wrapper">
                    <div class="content-left">
					<a class="backlink" href="https://tokyofashion.com/photos/">« Back to Recent Tokyo Street Fashion photos</a><br><br>
					<div 7="" class="contentpanel bm-half">
						<h2 class="contentpaneltitle">Harajuku Japanese Street Fashion Photos<!--  --></h2>
						<div class="photos-block"><ul class="photos-list">	<li>
				<a href="https://tokyofashion.com/korean-street-style-harajuku-japan-metal-glove-thug-club-fashion/" class="photo" title="Korean Street Style in Harajuku, Japan w/ Giant Metal Glove &amp; Thug Club Fashion">
			<noscript><img src="https://tokyofashion.com/wp-content/uploads/2024/10/2024-09-21-Harajuku-NK-002-008-0141.jpg" alt="Korean Street Style in Harajuku, Japan w/ Giant Metal Glove &amp; Thug Club Fashion" width="140" height="180" loading="lazy"></noscript><img class=" lazyloaded" src="https://tokyofashion.com/wp-content/uploads/2024/10/2024-09-21-Harajuku-NK-002-008-0141.jpg" data-src="https://tokyofashion.com/wp-content/uploads/2024/10/2024-09-21-Harajuku-NK-002-008-0141.jpg" alt="Korean Street Style in Harajuku, Japan w/ Giant Metal Glove &amp; Thug Club Fashion" width="140" height="180" loading="lazy">
		</a>
	</li>
	<li>
				<a href="https://tokyofashion.com/japanese-clown-street-style-harajuku-w-hello-kitty-shironuri-makeup-room-shoes/" class="photo" title="Japanese Clown-Inspired Street Style in Harajuku w/ Hello Kitty, Shironuri Makeup &amp; Room Shoes">
			<noscript><img src="https://tokyofashion.com/wp-content/uploads/2024/09/2024-05-25-Harajuku-NK-011-001-1213.jpg" alt="Japanese Clown-Inspired Street Style in Harajuku w/ Hello Kitty, Shironuri Makeup &amp; Room Shoes" width="140" height="180" loading="lazy"></noscript><img class=" lazyloaded" src="https://tokyofashion.com/wp-content/uploads/2024/09/2024-05-25-Harajuku-NK-011-001-1213.jpg" data-src="https://tokyofashion.com/wp-content/uploads/2024/09/2024-05-25-Harajuku-NK-011-001-1213.jpg" alt="Japanese Clown-Inspired Street Style in Harajuku w/ Hello Kitty, Shironuri Makeup &amp; Room Shoes" width="140" height="180" loading="lazy">
		</a>
	</li>
	<li>
				<a href="https://tokyofashion.com/japanese-gothic-tattoo-artist-vivienne-westwood-harajuku-tokyo/" class="photo" title="Japanese Gothic Tattoo Artist Wearing Vivienne Westwood on the Street in Harajuku, Tokyo">
			<noscript><img src="https://tokyofashion.com/wp-content/uploads/2023/06/2023-06-11-012-002-NK-Harajuku-0771.jpg" alt="Japanese Gothic Tattoo Artist Wearing Vivienne Westwood on the Street in Harajuku, Tokyo" width="140" height="180" loading="lazy"></noscript><img class=" lazyloaded" src="https://tokyofashion.com/wp-content/uploads/2023/06/2023-06-11-012-002-NK-Harajuku-0771.jpg" data-src="https://tokyofashion.com/wp-content/uploads/2023/06/2023-06-11-012-002-NK-Harajuku-0771.jpg" alt="Japanese Gothic Tattoo Artist Wearing Vivienne Westwood on the Street in Harajuku, Tokyo" width="140" height="180" loading="lazy">
		</a>
	</li>
	<li>
				<a href="https://tokyofashion.com/japanese-visual-kei-harajuku-asakura-garo-opanchu-usagi/" class="photo" title="Japanese Visual Kei Singer in Harajuku w/ Kawaii Pink, Asakura Garo &amp; Opanchu Usagi">
			<noscript><img src="https://tokyofashion.com/wp-content/uploads/2023/05/2023-05-20-017-001-NK-Harajuku-1631.jpg" alt="Japanese Visual Kei Singer in Harajuku w/ Kawaii Pink, Asakura Garo &amp; Opanchu Usagi" width="140" height="180" loading="lazy"></noscript><img class=" lazyloaded" src="https://tokyofashion.com/wp-content/uploads/2023/05/2023-05-20-017-001-NK-Harajuku-1631.jpg" data-src="https://tokyofashion.com/wp-content/uploads/2023/05/2023-05-20-017-001-NK-Harajuku-1631.jpg" alt="Japanese Visual Kei Singer in Harajuku w/ Kawaii Pink, Asakura Garo &amp; Opanchu Usagi" width="140" height="180" loading="lazy">
		</a>
	</li>
	<li>
				<a href="https://tokyofashion.com/japanese-dancer-hime-hairstyle-harajuku-street-style-not-conventional-yosuke-boots/" class="photo" title="Japanese Dancer w/ Hime Hairstyle in All Black Harajuku Street Style, Not Conventional &amp; Yosuke Boots">
			<noscript><img src="https://tokyofashion.com/wp-content/uploads/2023/05/2023-04-30-025-002-NK-Harajuku-2359.jpg" alt="Japanese Dancer w/ Hime Hairstyle in All Black Harajuku Street Style, Not Conventional &amp; Yosuke Boots" width="140" height="180" loading="lazy"></noscript><img class=" lazyloaded" src="https://tokyofashion.com/wp-content/uploads/2023/05/2023-04-30-025-002-NK-Harajuku-2359.jpg" data-src="https://tokyofashion.com/wp-content/uploads/2023/05/2023-04-30-025-002-NK-Harajuku-2359.jpg" alt="Japanese Dancer w/ Hime Hairstyle in All Black Harajuku Street Style, Not Conventional &amp; Yosuke Boots" width="140" height="180" loading="lazy">
		</a>
	</li>
	<li>
				<a href="https://tokyofashion.com/japanese-designer-custom-headpiece-armani-wide-short-pants-kagari-yusuki-platform-boots/" class="photo" title="Japanese Designer in Custom Headpiece, Armani Jacket, Wide Short Pants, Kagari Yusuki Bag &amp; Platform Boots">
			<noscript><img src="https://tokyofashion.com/wp-content/uploads/2023/04/2023-04-09-008-011-NK-Harajuku-7-2-0932.jpg" alt="Japanese Designer in Custom Headpiece, Armani Jacket, Wide Short Pants, Kagari Yusuki Bag &amp; Platform Boots" width="140" height="180" loading="lazy"></noscript><img class=" lazyloaded" src="https://tokyofashion.com/wp-content/uploads/2023/04/2023-04-09-008-011-NK-Harajuku-7-2-0932.jpg" data-src="https://tokyofashion.com/wp-content/uploads/2023/04/2023-04-09-008-011-NK-Harajuku-7-2-0932.jpg" alt="Japanese Designer in Custom Headpiece, Armani Jacket, Wide Short Pants, Kagari Yusuki Bag &amp; Platform Boots" width="140" height="180" loading="lazy">
		</a>
	</li>
	<li>
				<a href="https://tokyofashion.com/japanese-cyber-y2k-street-style-pleated-jacket-harajuku/" class="photo" title="Japanese Cyber/Y2K Street Style With Pleated Jacket in Harajuku">
			<noscript><img src="https://tokyofashion.com/wp-content/uploads/2023/03/20230226_7_2_0182.jpg" alt="Japanese Cyber/Y2K Street Style With Pleated Jacket in Harajuku" width="140" height="180" loading="lazy"></noscript><img class=" lazyloaded" src="https://tokyofashion.com/wp-content/uploads/2023/03/20230226_7_2_0182.jpg" data-src="https://tokyofashion.com/wp-content/uploads/2023/03/20230226_7_2_0182.jpg" alt="Japanese Cyber/Y2K Street Style With Pleated Jacket in Harajuku" width="140" height="180" loading="lazy">
		</a>
	</li>
	<li>
				<a href="https://tokyofashion.com/japanese-denim-man-street-style-handmade-jeans-harajuku/" class="photo" title="Japanese &quot;Denim Man&quot; Street Style w/ Handmade Jeans Outfit &amp; Denim Mask in Harajuku">
			<noscript><img src="https://tokyofashion.com/wp-content/uploads/2023/03/2023-02-25-006-007-NK-Harajuku-0438.jpg" alt="Japanese &quot;Denim Man&quot; Street Style w/ Handmade Jeans Outfit &amp; Denim Mask in Harajuku" width="140" height="180" loading="lazy"></noscript><img class=" lazyloaded" src="https://tokyofashion.com/wp-content/uploads/2023/03/2023-02-25-006-007-NK-Harajuku-0438.jpg" data-src="https://tokyofashion.com/wp-content/uploads/2023/03/2023-02-25-006-007-NK-Harajuku-0438.jpg" alt="Japanese &quot;Denim Man&quot; Street Style w/ Handmade Jeans Outfit &amp; Denim Mask in Harajuku" width="140" height="180" loading="lazy">
		</a>
	</li>
	<li>
				<a href="https://tokyofashion.com/harajuku-college-vintage-cropped-blazer-toga-pants-boots/" class="photo" title="Harajuku College Student in Vintage Cropped Blazer, Toga Pants, Vintage Accessories &amp; Vintage Boots">
			<noscript><img src="https://tokyofashion.com/wp-content/uploads/2022/04/2022-04-16-025-003-NK-Harajuku-1942.jpg" alt="Harajuku College Student in Vintage Cropped Blazer, Toga Pants, Vintage Accessories &amp; Vintage Boots" width="140" height="180" loading="lazy"></noscript><img class=" lazyloaded" src="https://tokyofashion.com/wp-content/uploads/2022/04/2022-04-16-025-003-NK-Harajuku-1942.jpg" data-src="https://tokyofashion.com/wp-content/uploads/2022/04/2022-04-16-025-003-NK-Harajuku-1942.jpg" alt="Harajuku College Student in Vintage Cropped Blazer, Toga Pants, Vintage Accessories &amp; Vintage Boots" width="140" height="180" loading="lazy">
		</a>
	</li>
	<li>
				<a href="https://tokyofashion.com/japanese-college-student-vintage-track-suit-1984-cassette-player-hat-shoes/" class="photo" title="Japanese College Student in Vintage Track Suit w/ 1984 Cassette Player, Hat &amp; Pointy Shoes">
			<noscript><img src="https://tokyofashion.com/wp-content/uploads/2022/04/2022-04-16-027-001-NK-Harajuku-2062.jpg" alt="Japanese College Student in Vintage Track Suit w/ 1984 Cassette Player, Hat &amp; Pointy Shoes" width="140" height="180" loading="lazy"></noscript><img class=" lazyloaded" src="https://tokyofashion.com/wp-content/uploads/2022/04/2022-04-16-027-001-NK-Harajuku-2062.jpg" data-src="https://tokyofashion.com/wp-content/uploads/2022/04/2022-04-16-027-001-NK-Harajuku-2062.jpg" alt="Japanese College Student in Vintage Track Suit w/ 1984 Cassette Player, Hat &amp; Pointy Shoes" width="140" height="180" loading="lazy">
		</a>
	</li>
	<li>
				<a href="https://tokyofashion.com/limi-feu-marine-serre-vivienne-westwood-rocking-horse-boots-harajuku/" class="photo" title="LIMI Feu Ribbon Dress, Marine Serre &amp; Vivienne Westwood Rocking Horse Boots in Harajuku">
			<noscript><img src="https://tokyofashion.com/wp-content/uploads/2022/04/2022-04-17-002-004-NK-Harajuku-0114.jpg" alt="LIMI Feu Ribbon Dress, Marine Serre &amp; Vivienne Westwood Rocking Horse Boots in Harajuku" width="140" height="180" loading="lazy"></noscript><img class=" lazyloaded" src="https://tokyofashion.com/wp-content/uploads/2022/04/2022-04-17-002-004-NK-Harajuku-0114.jpg" data-src="https://tokyofashion.com/wp-content/uploads/2022/04/2022-04-17-002-004-NK-Harajuku-0114.jpg" alt="LIMI Feu Ribbon Dress, Marine Serre &amp; Vivienne Westwood Rocking Horse Boots in Harajuku" width="140" height="180" loading="lazy">
		</a>
	</li>
	<li>
				<a href="https://tokyofashion.com/vintage-harajuku-style-wide-brim-hat-1980s-jacket-sailor-pants-boots/" class="photo" title="Green Vintage Harajuku Street Style w/ Wide Brim Hat, 1980s Jacket, Sailor Pants &amp; Vintage Boots">
			<noscript><img src="https://tokyofashion.com/wp-content/uploads/2022/04/2022-04-16-015-004-NK-Harajuku-1125.jpg" alt="Green Vintage Harajuku Street Style w/ Wide Brim Hat, 1980s Jacket, Sailor Pants &amp; Vintage Boots" width="140" height="180" loading="lazy"></noscript><img class=" lazyloaded" src="https://tokyofashion.com/wp-content/uploads/2022/04/2022-04-16-015-004-NK-Harajuku-1125.jpg" data-src="https://tokyofashion.com/wp-content/uploads/2022/04/2022-04-16-015-004-NK-Harajuku-1125.jpg" alt="Green Vintage Harajuku Street Style w/ Wide Brim Hat, 1980s Jacket, Sailor Pants &amp; Vintage Boots" width="140" height="180" loading="lazy">
		</a>
	</li>
	<li>
				<a href="https://tokyofashion.com/japanese-kawaii-harajuku-yellow-hair-buffalo-monster-30cm-platforms-loose-socks/" class="photo" title="Japanese Kawaii Idol in Harajuku w/ Yellow Hair, Buffalo &quot;Monster&quot; 30cm Platforms, Loose Socks &amp; Takuya Angel Bag">
			<noscript><img src="https://tokyofashion.com/wp-content/uploads/2022/04/2022-04-10-007-008-NK-Harajuku-0426.jpg" alt="Japanese Kawaii Idol in Harajuku w/ Yellow Hair, Buffalo &quot;Monster&quot; 30cm Platforms, Loose Socks &amp; Takuya Angel Bag" width="140" height="180" loading="lazy"></noscript><img class=" lazyloaded" src="https://tokyofashion.com/wp-content/uploads/2022/04/2022-04-10-007-008-NK-Harajuku-0426.jpg" data-src="https://tokyofashion.com/wp-content/uploads/2022/04/2022-04-10-007-008-NK-Harajuku-0426.jpg" alt="Japanese Kawaii Idol in Harajuku w/ Yellow Hair, Buffalo &quot;Monster&quot; 30cm Platforms, Loose Socks &amp; Takuya Angel Bag" width="140" height="180" loading="lazy">
		</a>
	</li>
	<li>
				<a href="https://tokyofashion.com/monochrome-harajuku-style-knit-cap-stussy-bag-loose-socks-crocs/" class="photo" title="Monochrome Harajuku Street Style w/ Knit Cap, Stussy Tote Bag, Loose Socks &amp; Crocs">
			<noscript><img src="https://tokyofashion.com/wp-content/uploads/2022/04/2022-04-09-007-002-NK-Harajuku-0407.jpg" alt="Monochrome Harajuku Street Style w/ Knit Cap, Stussy Tote Bag, Loose Socks &amp; Crocs" width="140" height="180" loading="lazy"></noscript><img class=" lazyloaded" src="https://tokyofashion.com/wp-content/uploads/2022/04/2022-04-09-007-002-NK-Harajuku-0407.jpg" data-src="https://tokyofashion.com/wp-content/uploads/2022/04/2022-04-09-007-002-NK-Harajuku-0407.jpg" alt="Monochrome Harajuku Street Style w/ Knit Cap, Stussy Tote Bag, Loose Socks &amp; Crocs" width="140" height="180" loading="lazy">
		</a>
	</li>
	<li>
				<a href="https://tokyofashion.com/harajuku-street-style-chuocho-tactical-craft-horns-ikumi-tripp-nyc/" class="photo" title="Dark Harajuku Street Style w/ Chuocho Tactical Craft Horns, Ikumi, Tripp NYC Strap Pants &amp; Nike Sneakers">
			<noscript><img src="https://tokyofashion.com/wp-content/uploads/2022/04/2022-01-29-020-008-NK-Harajuku-DZ7-1656.jpg" alt="Dark Harajuku Street Style w/ Chuocho Tactical Craft Horns, Ikumi, Tripp NYC Strap Pants &amp; Nike Sneakers" width="140" height="180" loading="lazy"></noscript><img class=" lazyloaded" src="https://tokyofashion.com/wp-content/uploads/2022/04/2022-01-29-020-008-NK-Harajuku-DZ7-1656.jpg" data-src="https://tokyofashion.com/wp-content/uploads/2022/04/2022-01-29-020-008-NK-Harajuku-DZ7-1656.jpg" alt="Dark Harajuku Street Style w/ Chuocho Tactical Craft Horns, Ikumi, Tripp NYC Strap Pants &amp; Nike Sneakers" width="140" height="180" loading="lazy">
		</a>
	</li>
	<li>
				<a href="https://tokyofashion.com/harajuku-mother-daughter-the-ivy-tokyo-earrings-sailor-moon-mikio-sakabe/" class="photo" title="Harajuku Mother &amp; Daughter w/ The Ivy Tokyo Earrings, Sailor Moon, fäfä, Sister Jane &amp; Mikio Sakabe">
			<noscript><img src="https://tokyofashion.com/wp-content/uploads/2022/03/2021-06-06-024-001-Harajuku-NK-DZ7-0014.jpg" alt="Harajuku Mother &amp; Daughter w/ The Ivy Tokyo Earrings, Sailor Moon, fäfä, Sister Jane &amp; Mikio Sakabe" width="140" height="180" loading="lazy"></noscript><img class="lazyload" src="data:image/svg+xml,%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20viewBox=%220%200%20140%20180%22%3E%3C/svg%3E" data-src="https://tokyofashion.com/wp-content/uploads/2022/03/2021-06-06-024-001-Harajuku-NK-DZ7-0014.jpg" alt="Harajuku Mother &amp; Daughter w/ The Ivy Tokyo Earrings, Sailor Moon, fäfä, Sister Jane &amp; Mikio Sakabe" width="140" height="180" loading="lazy">
		</a>
	</li>
	<li>
				<a href="https://tokyofashion.com/dog-harajuku-cropped-jacket-tripp-nyc-pants-new-rock-boots/" class="photo" title="Dog Harajuku Cropped Jacket Street Style w/ Tripp NYC Pants &amp; New Rock Metal Boots">
			<noscript><img src="https://tokyofashion.com/wp-content/uploads/2022/03/2022-03-06-028-002-NK-Harajuku-3176.jpg" alt="Dog Harajuku Cropped Jacket Street Style w/ Tripp NYC Pants &amp; New Rock Metal Boots" width="140" height="180" loading="lazy"></noscript><img class="lazyload" src="data:image/svg+xml,%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20viewBox=%220%200%20140%20180%22%3E%3C/svg%3E" data-src="https://tokyofashion.com/wp-content/uploads/2022/03/2022-03-06-028-002-NK-Harajuku-3176.jpg" alt="Dog Harajuku Cropped Jacket Street Style w/ Tripp NYC Pants &amp; New Rock Metal Boots" width="140" height="180" loading="lazy">
		</a>
	</li>
	<li>
				<a href="https://tokyofashion.com/japanese-idol-tattoos-piercings-sheer-fashion-boots-harajuku/" class="photo" title="Japanese Idol w/ Tattoos &amp; Piercings Wearing Sheer Fashion &amp; Boots in Harajuku">
			<noscript><img src="https://tokyofashion.com/wp-content/uploads/2022/03/2022-03-05-014-001-NK-Harajuku-0815.jpg" alt="Japanese Idol w/ Tattoos &amp; Piercings Wearing Sheer Fashion &amp; Boots in Harajuku" width="140" height="180" loading="lazy"></noscript><img class="lazyload" src="data:image/svg+xml,%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20viewBox=%220%200%20140%20180%22%3E%3C/svg%3E" data-src="https://tokyofashion.com/wp-content/uploads/2022/03/2022-03-05-014-001-NK-Harajuku-0815.jpg" alt="Japanese Idol w/ Tattoos &amp; Piercings Wearing Sheer Fashion &amp; Boots in Harajuku" width="140" height="180" loading="lazy">
		</a>
	</li>
	<li>
				<a href="https://tokyofashion.com/japanese-john-lawrence-sullivan-paul-smith-vintage-fashion-ships-japan/" class="photo" title="Japanese Student in Harajuku w/ John Lawrence Sullivan, Paul Smith, Vintage Fashion &amp; Ships Japan">
			<noscript><img src="https://tokyofashion.com/wp-content/uploads/2022/03/2022-02-12-006-001-NK-Harajuku-0307.jpg" alt="Japanese Student in Harajuku w/ John Lawrence Sullivan, Paul Smith, Vintage Fashion &amp; Ships Japan" width="140" height="180" loading="lazy"></noscript><img class="lazyload" src="data:image/svg+xml,%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20viewBox=%220%200%20140%20180%22%3E%3C/svg%3E" data-src="https://tokyofashion.com/wp-content/uploads/2022/03/2022-02-12-006-001-NK-Harajuku-0307.jpg" alt="Japanese Student in Harajuku w/ John Lawrence Sullivan, Paul Smith, Vintage Fashion &amp; Ships Japan" width="140" height="180" loading="lazy">
		</a>
	</li>
	<li>
				<a href="https://tokyofashion.com/japanese-youtuber-harajuku-corduroy-pants-the-tote-bag-marc-jacobs/" class="photo" title="Japanese YouTuber in Harajuku w/ Vintage Street Style, Corduroy Pants &amp; The Tote Bag by Marc Jacobs">
			<noscript><img src="https://tokyofashion.com/wp-content/uploads/2022/02/2022-02-26-003-002-NK-Harajuku-0315.jpg" alt="Japanese YouTuber in Harajuku w/ Vintage Street Style, Corduroy Pants &amp; The Tote Bag by Marc Jacobs" width="140" height="180" loading="lazy"></noscript><img class="lazyload" src="data:image/svg+xml,%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20viewBox=%220%200%20140%20180%22%3E%3C/svg%3E" data-src="https://tokyofashion.com/wp-content/uploads/2022/02/2022-02-26-003-002-NK-Harajuku-0315.jpg" alt="Japanese YouTuber in Harajuku w/ Vintage Street Style, Corduroy Pants &amp; The Tote Bag by Marc Jacobs" width="140" height="180" loading="lazy">
		</a>
	</li>
	<li>
				<a href="https://tokyofashion.com/japanese-vintage-street-style-bob-hairstyle-oversized-jacket-scarf-belt-boots/" class="photo" title="Japanese Vintage Street Style w/ Bob Hairstyle, Oversized Jacket, Scarf Belt &amp; Boots">
			<noscript><img src="https://tokyofashion.com/wp-content/uploads/2022/02/2022-02-20-005-001-NK-Harajuku-0248.jpg" alt="Japanese Vintage Street Style w/ Bob Hairstyle, Oversized Jacket, Scarf Belt &amp; Boots" width="140" height="180" loading="lazy"></noscript><img class="lazyload" src="data:image/svg+xml,%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20viewBox=%220%200%20140%20180%22%3E%3C/svg%3E" data-src="https://tokyofashion.com/wp-content/uploads/2022/02/2022-02-20-005-001-NK-Harajuku-0248.jpg" alt="Japanese Vintage Street Style w/ Bob Hairstyle, Oversized Jacket, Scarf Belt &amp; Boots" width="140" height="180" loading="lazy">
		</a>
	</li>
	<li>
				<a href="https://tokyofashion.com/japanese-giant-bow-faux-fur-jacket-pink-harajuku/" class="photo" title="Japanese Model w/ Giant Bow, Faux Fur Jacket, BPM150 &amp; Pink Accents in Harajuku">
			<noscript><img src="https://tokyofashion.com/wp-content/uploads/2022/02/2022-01-22-006-004-NK-Harajuku-0504.jpg" alt="Japanese Model w/ Giant Bow, Faux Fur Jacket, BPM150 &amp; Pink Accents in Harajuku" width="140" height="180" loading="lazy"></noscript><img class="lazyload" src="data:image/svg+xml,%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20viewBox=%220%200%20140%20180%22%3E%3C/svg%3E" data-src="https://tokyofashion.com/wp-content/uploads/2022/02/2022-01-22-006-004-NK-Harajuku-0504.jpg" alt="Japanese Model w/ Giant Bow, Faux Fur Jacket, BPM150 &amp; Pink Accents in Harajuku" width="140" height="180" loading="lazy">
		</a>
	</li>
	<li>
				<a href="https://tokyofashion.com/oversized-japanese-street-style-harajuku-cotobuki-koenji/" class="photo" title="Oversized Japanese Street Style in Harajuku w/ Cotobuki Koenji Coat &amp; Cotobuki Wide Pants">
			<noscript><img src="https://tokyofashion.com/wp-content/uploads/2022/02/2022-02-05-003-008-NK-Harajuku-0216.jpg" alt="Oversized Japanese Street Style in Harajuku w/ Cotobuki Koenji Coat &amp; Cotobuki Wide Pants" width="140" height="180" loading="lazy"></noscript><img class="lazyload" src="data:image/svg+xml,%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20viewBox=%220%200%20140%20180%22%3E%3C/svg%3E" data-src="https://tokyofashion.com/wp-content/uploads/2022/02/2022-02-05-003-008-NK-Harajuku-0216.jpg" alt="Oversized Japanese Street Style in Harajuku w/ Cotobuki Koenji Coat &amp; Cotobuki Wide Pants" width="140" height="180" loading="lazy">
		</a>
	</li>
	<li>
				<a href="https://tokyofashion.com/comme-des-garcons-martin-margiela-handmade-fashion-harajuku/" class="photo" title="Comme Des Garcons, Martin Margiela &amp; Handmade Fashion on the Street in Harajuku, Tokyo">
			<noscript><img src="https://tokyofashion.com/wp-content/uploads/2022/02/2022-02-05-004-001-NK-Harajuku-0285.jpg" alt="Comme Des Garcons, Martin Margiela &amp; Handmade Fashion on the Street in Harajuku, Tokyo" width="140" height="180" loading="lazy"></noscript><img class="lazyload" src="data:image/svg+xml,%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20viewBox=%220%200%20140%20180%22%3E%3C/svg%3E" data-src="https://tokyofashion.com/wp-content/uploads/2022/02/2022-02-05-004-001-NK-Harajuku-0285.jpg" alt="Comme Des Garcons, Martin Margiela &amp; Handmade Fashion on the Street in Harajuku, Tokyo" width="140" height="180" loading="lazy">
		</a>
	</li>
	<li>
				<a href="https://tokyofashion.com/futuristic-japanese-style-balmung-chloma-leg-covers-mikio-sakabe-shoes/" class="photo" title="Futuristic Japanese Street Style w/ Balmung Jacket, Chloma Leg Covers &amp; Mikio Sakabe Shoes">
			<noscript><img src="https://tokyofashion.com/wp-content/uploads/2022/02/2021-12-11-022-004-NK-Harajuku-DZ7-2119.jpg" alt="Futuristic Japanese Street Style w/ Balmung Jacket, Chloma Leg Covers &amp; Mikio Sakabe Shoes" width="140" height="180" loading="lazy"></noscript><img class="lazyload" src="data:image/svg+xml,%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20viewBox=%220%200%20140%20180%22%3E%3C/svg%3E" data-src="https://tokyofashion.com/wp-content/uploads/2022/02/2021-12-11-022-004-NK-Harajuku-DZ7-2119.jpg" alt="Futuristic Japanese Street Style w/ Balmung Jacket, Chloma Leg Covers &amp; Mikio Sakabe Shoes" width="140" height="180" loading="lazy">
		</a>
	</li>
	<li>
				<a href="https://tokyofashion.com/retro-fashion-tokyo-four-buttons-japan-suit-bespoke-shirt-ramuda-ichihara-umbrella/" class="photo" title="Retro 1930s &amp; 1940s Fashion in Tokyo w/ Four Buttons Japan Suit, Bespoke Shirt &amp; Ramuda Ichihara Umbrella">
			<noscript><img src="https://tokyofashion.com/wp-content/uploads/2022/01/2021-12-11-001-001-NK-Harajuku-DZ7-0001.jpg" alt="Retro 1930s &amp; 1940s Fashion in Tokyo w/ Four Buttons Japan Suit, Bespoke Shirt &amp; Ramuda Ichihara Umbrella" width="140" height="180" loading="lazy"></noscript><img class="lazyload" src="data:image/svg+xml,%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20viewBox=%220%200%20140%20180%22%3E%3C/svg%3E" data-src="https://tokyofashion.com/wp-content/uploads/2022/01/2021-12-11-001-001-NK-Harajuku-DZ7-0001.jpg" alt="Retro 1930s &amp; 1940s Fashion in Tokyo w/ Four Buttons Japan Suit, Bespoke Shirt &amp; Ramuda Ichihara Umbrella" width="140" height="180" loading="lazy">
		</a>
	</li>
	<li>
				<a href="https://tokyofashion.com/harajuku-girl-faux-fur-coat-cyborglabo-mask-leg-covers-demonia/" class="photo" title="Harajuku Girl in Faux Fur Coat, CyborgLabo Face Mask, Cutout Top, Miniskirt, Leg Covers &amp; Demonia Platform Shoes">
			<noscript><img src="https://tokyofashion.com/wp-content/uploads/2022/01/2022-01-22-016-003-NK-Harajuku-1480.jpg" alt="Harajuku Girl in Faux Fur Coat, CyborgLabo Face Mask, Cutout Top, Miniskirt, Leg Covers &amp; Demonia Platform Shoes" width="140" height="180" loading="lazy"></noscript><img class="lazyload" src="data:image/svg+xml,%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20viewBox=%220%200%20140%20180%22%3E%3C/svg%3E" data-src="https://tokyofashion.com/wp-content/uploads/2022/01/2022-01-22-016-003-NK-Harajuku-1480.jpg" alt="Harajuku Girl in Faux Fur Coat, CyborgLabo Face Mask, Cutout Top, Miniskirt, Leg Covers &amp; Demonia Platform Shoes" width="140" height="180" loading="lazy">
		</a>
	</li>
	<li>
				<a href="https://tokyofashion.com/japanese-hosts-street-styles-harajuku-yohji-yamamoto-luis-saint-laurent/" class="photo" title="Japanese Hosts Street Styles in Harajuku w/ Yohji Yamamoto, Lui's, Saint Laurent, Dior, Marc Jacobs &amp; Chrome Hearts">
			<noscript><img src="https://tokyofashion.com/wp-content/uploads/2022/01/2021-12-11-031-105-NK-Harajuku-DZ7-3632.jpg" alt="Japanese Hosts Street Styles in Harajuku w/ Yohji Yamamoto, Lui&#039;s, Saint Laurent, Dior, Marc Jacobs &amp; Chrome Hearts" width="140" height="180" loading="lazy"></noscript><img class="lazyload" src="data:image/svg+xml,%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20viewBox=%220%200%20140%20180%22%3E%3C/svg%3E" data-src="https://tokyofashion.com/wp-content/uploads/2022/01/2021-12-11-031-105-NK-Harajuku-DZ7-3632.jpg" alt="Japanese Hosts Street Styles in Harajuku w/ Yohji Yamamoto, Lui's, Saint Laurent, Dior, Marc Jacobs &amp; Chrome Hearts" width="140" height="180" loading="lazy">
		</a>
	</li>
	<li>
				<a href="https://tokyofashion.com/harajuku-pink-hairstyle-chanel-leg-warmers-spiked-crocs/" class="photo" title="Harajuku Girl w/ Pink Streaked Hairstyle, Chanel Plush Bag, Leg Warmers &amp; Spiked Crocs">
			<noscript><img src="https://tokyofashion.com/wp-content/uploads/2022/01/2022-01-16-011-001-NK-Harajuku.jpg" alt="Harajuku Girl w/ Pink Streaked Hairstyle, Chanel Plush Bag, Leg Warmers &amp; Spiked Crocs" width="140" height="180" loading="lazy"></noscript><img class="lazyload" src="data:image/svg+xml,%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20viewBox=%220%200%20140%20180%22%3E%3C/svg%3E" data-src="https://tokyofashion.com/wp-content/uploads/2022/01/2022-01-16-011-001-NK-Harajuku.jpg" alt="Harajuku Girl w/ Pink Streaked Hairstyle, Chanel Plush Bag, Leg Warmers &amp; Spiked Crocs" width="140" height="180" loading="lazy">
		</a>
	</li>
	<li>
				<a href="https://tokyofashion.com/kimono-twintails-hairstyle-on-the-street-in-harajuku/" class="photo" title="RinRin Doll Wearing a Kimono &amp; Twintails Hairstyle on The Street in Harajuku">
			<noscript><img src="https://tokyofashion.com/wp-content/uploads/2022/01/2021-01-11-007-005-NK-Harajuku-DZ7-2795.jpg" alt="RinRin Doll Wearing a Kimono &amp; Twintails Hairstyle on The Street in Harajuku" width="140" height="180" loading="lazy"></noscript><img class="lazyload" src="data:image/svg+xml,%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20viewBox=%220%200%20140%20180%22%3E%3C/svg%3E" data-src="https://tokyofashion.com/wp-content/uploads/2022/01/2021-01-11-007-005-NK-Harajuku-DZ7-2795.jpg" alt="RinRin Doll Wearing a Kimono &amp; Twintails Hairstyle on The Street in Harajuku" width="140" height="180" loading="lazy">
		</a>
	</li>
	<li>
				<a href="https://tokyofashion.com/harajuku-girl-colorful-hand-painted-japanese-street-style/" class="photo" title="Harajuku Girl in Colorful Hand-Painted Coming of Age Day Japanese Street Style">
			<noscript><img src="https://tokyofashion.com/wp-content/uploads/2022/01/2022-01-08-019-002-NK-Harajuku-1531.jpg" alt="Harajuku Girl in Colorful Hand-Painted Coming of Age Day Japanese Street Style" width="140" height="180" loading="lazy"></noscript><img class="lazyload" src="data:image/svg+xml,%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20viewBox=%220%200%20140%20180%22%3E%3C/svg%3E" data-src="https://tokyofashion.com/wp-content/uploads/2022/01/2022-01-08-019-002-NK-Harajuku-1531.jpg" alt="Harajuku Girl in Colorful Hand-Painted Coming of Age Day Japanese Street Style" width="140" height="180" loading="lazy">
		</a>
	</li>
	<li>
				<a href="https://tokyofashion.com/japanese-fashion-designer-harajuku-dimmoire-extra-long-sleeves-alexander-mcqueen-demonia/" class="photo" title="Japanese Fashion Designer in Harajuku w/ DimMoire Extra Long Sleeves Sweater, Alexander McQueen &amp; Demonia Platform Boots">
			<noscript><img src="https://tokyofashion.com/wp-content/uploads/2022/01/2021-12-26-022-003-NK-Harajuku-1690.jpg" alt="Japanese Fashion Designer in Harajuku w/ DimMoire Extra Long Sleeves Sweater, Alexander McQueen &amp; Demonia Platform Boots" width="140" height="180" loading="lazy"></noscript><img class="lazyload" src="data:image/svg+xml,%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20viewBox=%220%200%20140%20180%22%3E%3C/svg%3E" data-src="https://tokyofashion.com/wp-content/uploads/2022/01/2021-12-26-022-003-NK-Harajuku-1690.jpg" alt="Japanese Fashion Designer in Harajuku w/ DimMoire Extra Long Sleeves Sweater, Alexander McQueen &amp; Demonia Platform Boots" width="140" height="180" loading="lazy">
		</a>
	</li>
	<li>
				<a href="https://tokyofashion.com/takuya-angel-kimono-vivienne-westwood-yosuke-style/" class="photo" title="Takuya Angel Kimono, Vivienne Westwood, Fuzzy Ears and Yosuke Street Style in Harajuku, Japan">
			<noscript><img src="https://tokyofashion.com/wp-content/uploads/2021/12/2021-12-05-003-001-NK-Harajuku-DZ7-0220.jpg" alt="Takuya Angel Kimono, Vivienne Westwood, Fuzzy Ears and Yosuke Street Style in Harajuku, Japan" width="140" height="180" loading="lazy"></noscript><img class="lazyload" src="data:image/svg+xml,%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20viewBox=%220%200%20140%20180%22%3E%3C/svg%3E" data-src="https://tokyofashion.com/wp-content/uploads/2021/12/2021-12-05-003-001-NK-Harajuku-DZ7-0220.jpg" alt="Takuya Angel Kimono, Vivienne Westwood, Fuzzy Ears and Yosuke Street Style in Harajuku, Japan" width="140" height="180" loading="lazy">
		</a>
	</li>
	<li>
				<a href="https://tokyofashion.com/harajuku-bunny-ikumi-furry-hat-blazer-plaid-skirt-platforms/" class="photo" title="Harajuku Girl w/ Bunny in IKUMI Furry Hat, Red Blazer, Plaid Mini Skirt, Fishnets, and Platforms">
			<noscript><img src="https://tokyofashion.com/wp-content/uploads/2021/12/20211225_DZ7_0541.jpg" alt="Harajuku Girl w/ Bunny in IKUMI Furry Hat, Red Blazer, Plaid Mini Skirt, Fishnets, and Platforms" width="140" height="180" loading="lazy"></noscript><img class="lazyload" src="data:image/svg+xml,%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20viewBox=%220%200%20140%20180%22%3E%3C/svg%3E" data-src="https://tokyofashion.com/wp-content/uploads/2021/12/20211225_DZ7_0541.jpg" alt="Harajuku Girl w/ Bunny in IKUMI Furry Hat, Red Blazer, Plaid Mini Skirt, Fishnets, and Platforms" width="140" height="180" loading="lazy">
		</a>
	</li>
	<li>
				<a href="https://tokyofashion.com/purple-twintails-merry-jenny-amavel-majestic-legon-6dokidoki/" class="photo" title="Purple Twintails &amp; Merry Jenny Japanese Street Style w/ Amavel, Majestic Legon &amp; 6%DOKIDOKI">
			<noscript><img src="https://tokyofashion.com/wp-content/uploads/2021/12/2021-12-19-029-001-NK-Harajuku_2168.jpg" alt="Purple Twintails &amp; Merry Jenny Japanese Street Style w/ Amavel, Majestic Legon &amp; 6%DOKIDOKI" width="140" height="180" loading="lazy"></noscript><img class="lazyload" src="data:image/svg+xml,%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20viewBox=%220%200%20140%20180%22%3E%3C/svg%3E" data-src="https://tokyofashion.com/wp-content/uploads/2021/12/2021-12-19-029-001-NK-Harajuku_2168.jpg" alt="Purple Twintails &amp; Merry Jenny Japanese Street Style w/ Amavel, Majestic Legon &amp; 6%DOKIDOKI" width="140" height="180" loading="lazy">
		</a>
	</li>
	<li>
				<a href="https://tokyofashion.com/twintail-fringe-dog-harajuku-orb-bag-game-boy-micro/" class="photo" title="Harajuku Guy w/ Twintail Hairstyle, Vintage Fringe Jacket, Dog Harajuku Skirt, Orb Bag &amp; Game Boy Micro">
			<noscript><img src="https://tokyofashion.com/wp-content/uploads/2021/12/2021-12-11-010-005-NK-Harajuku-0915.jpg" alt="Harajuku Guy w/ Twintail Hairstyle, Vintage Fringe Jacket, Dog Harajuku Skirt, Orb Bag &amp; Game Boy Micro" width="140" height="180" loading="lazy"></noscript><img class="lazyload" src="data:image/svg+xml,%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20viewBox=%220%200%20140%20180%22%3E%3C/svg%3E" data-src="https://tokyofashion.com/wp-content/uploads/2021/12/2021-12-11-010-005-NK-Harajuku-0915.jpg" alt="Harajuku Guy w/ Twintail Hairstyle, Vintage Fringe Jacket, Dog Harajuku Skirt, Orb Bag &amp; Game Boy Micro" width="140" height="180" loading="lazy">
		</a>
	</li>
	<li>
				<a href="https://tokyofashion.com/harajuku-girl-plaid-oversized-blazer-vintage-pants-converse/" class="photo" title="Harajuku Girl in Plaid on Plaid w/ Oversized Blazer, Vintage Plaid Pants &amp; Converse Sneakers">
			<noscript><img src="https://tokyofashion.com/wp-content/uploads/2021/12/2021-12-11-004-001-NK-Harajuku-0365.jpg" alt="Harajuku Girl in Plaid on Plaid w/ Oversized Blazer, Vintage Plaid Pants &amp; Converse Sneakers" width="140" height="180" loading="lazy"></noscript><img class="lazyload" src="data:image/svg+xml,%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20viewBox=%220%200%20140%20180%22%3E%3C/svg%3E" data-src="https://tokyofashion.com/wp-content/uploads/2021/12/2021-12-11-004-001-NK-Harajuku-0365.jpg" alt="Harajuku Girl in Plaid on Plaid w/ Oversized Blazer, Vintage Plaid Pants &amp; Converse Sneakers" width="140" height="180" loading="lazy">
		</a>
	</li>
	<li>
				<a href="https://tokyofashion.com/harajuku-girl-cat-ears-tokyo-cropped-jacket-fashion-yosuke/" class="photo" title="Harajuku Girl w/ Cat Ears in &quot;Tokyo&quot; Cropped Jacket, Resale Fashion &amp; Yosuke Platform Shoes">
			<noscript><img src="https://tokyofashion.com/wp-content/uploads/2021/12/2021-12-11-015-002-NK-Harajuku-1409.jpg" alt="Harajuku Girl w/ Cat Ears in &quot;Tokyo&quot; Cropped Jacket, Resale Fashion &amp; Yosuke Platform Shoes" width="140" height="180" loading="lazy"></noscript><img class="lazyload" src="data:image/svg+xml,%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20viewBox=%220%200%20140%20180%22%3E%3C/svg%3E" data-src="https://tokyofashion.com/wp-content/uploads/2021/12/2021-12-11-015-002-NK-Harajuku-1409.jpg" alt="Harajuku Girl w/ Cat Ears in &quot;Tokyo&quot; Cropped Jacket, Resale Fashion &amp; Yosuke Platform Shoes" width="140" height="180" loading="lazy">
		</a>
	</li>
	<li>
				<a href="https://tokyofashion.com/harajuku-handmade-remake-street-style-platform-boots/" class="photo" title="Harajuku Guy in Handmade Remake Street Style w/ Oversized Sleeves, Gold Chains &amp; Platform Boots">
			<noscript><img src="https://tokyofashion.com/wp-content/uploads/2021/12/2021-11-13-008-005-NK-Harajuku-0846.jpg" alt="Harajuku Guy in Handmade Remake Street Style w/ Oversized Sleeves, Gold Chains &amp; Platform Boots" width="140" height="180" loading="lazy"></noscript><img class="lazyload" src="data:image/svg+xml,%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20viewBox=%220%200%20140%20180%22%3E%3C/svg%3E" data-src="https://tokyofashion.com/wp-content/uploads/2021/12/2021-11-13-008-005-NK-Harajuku-0846.jpg" alt="Harajuku Guy in Handmade Remake Street Style w/ Oversized Sleeves, Gold Chains &amp; Platform Boots" width="140" height="180" loading="lazy">
		</a>
	</li>
	<li>
				<a href="https://tokyofashion.com/japanese-gothic-lolita-harajuku-marble-fashion-moi-meme-moitie/" class="photo" title="Japanese Gothic Lolita in Harajuku w/ Marble Fashion, Moi-Meme-Moitie, Current Mood &amp; Demonia">
			<noscript><img src="https://tokyofashion.com/wp-content/uploads/2021/12/2021-10-09-007-005-NK-Harajuku-DZ7-0648.jpg" alt="Japanese Gothic Lolita in Harajuku w/ Marble Fashion, Moi-Meme-Moitie, Current Mood &amp; Demonia" width="140" height="180" loading="lazy"></noscript><img class="lazyload" src="data:image/svg+xml,%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20viewBox=%220%200%20140%20180%22%3E%3C/svg%3E" data-src="https://tokyofashion.com/wp-content/uploads/2021/12/2021-10-09-007-005-NK-Harajuku-DZ7-0648.jpg" alt="Japanese Gothic Lolita in Harajuku w/ Marble Fashion, Moi-Meme-Moitie, Current Mood &amp; Demonia" width="140" height="180" loading="lazy">
		</a>
	</li>
</ul><br style="clear:both;"></div>							<div class="navigation">
																	<div class="navleft">
										<a href="https://tokyofashion.com/photos/?location=Harajuku&amp;start=40">« Show Older Harajuku Photos</a>
									</div>
																							</div>
							<div id="photonav" align="center">
								<a href="https://tokyofashion.com/photos/?location=Harajuku&amp;month=3&amp;years=2025">Browse Harajuku Photos By Month
								</a>
							</div>
					</div> <!-- .contentpanel -->
				</div>
				
<aside role="complementary" class="sidebar">
	
		<section id="recent-posts-2" class="widget widget_recent_entries">
		<h2 class="widget-title">Recent Posts</h2>
		<ul>
											<li>
					<a href="https://tokyofashion.com/korean-street-style-harajuku-japan-metal-glove-thug-club-fashion/">Korean Street Style in Harajuku, Japan w/ Giant Metal Glove &amp; Thug Club Fashion</a>
									</li>
											<li>
					<a href="https://tokyofashion.com/japanese-clown-street-style-harajuku-w-hello-kitty-shironuri-makeup-room-shoes/">Japanese Clown-Inspired Street Style in Harajuku w/ Hello Kitty, Shironuri Makeup &amp; Room Shoes</a>
									</li>
											<li>
					<a href="https://tokyofashion.com/japanese-gothic-tattoo-artist-vivienne-westwood-harajuku-tokyo/">Japanese Gothic Tattoo Artist Wearing Vivienne Westwood on the Street in Harajuku, Tokyo</a>
									</li>
											<li>
					<a href="https://tokyofashion.com/japanese-visual-kei-harajuku-asakura-garo-opanchu-usagi/">Japanese Visual Kei Singer in Harajuku w/ Kawaii Pink, Asakura Garo &amp; Opanchu Usagi</a>
									</li>
											<li>
					<a href="https://tokyofashion.com/japanese-dancer-hime-hairstyle-harajuku-street-style-not-conventional-yosuke-boots/">Japanese Dancer w/ Hime Hairstyle in All Black Harajuku Street Style, Not Conventional &amp; Yosuke Boots</a>
									</li>
					</ul>

		</section><section id="linkcat-415" class="widget widget_links"><h2 class="widget-title">Fashion Brands</h2>
	<ul class="xoxo blogroll">
<li><a href="http://www.virtualjapan.com/wiki/A_Bathing_Ape" rel="noopener" title="BAPE" target="_blank">A Bathing Ape</a></li>
<li><a href="http://www.virtualjapan.com/wiki/AS_KNOW_AS_de_base" rel="noopener" title="AS KNOW AS" target="_blank">AS KNOW AS</a></li>
<li><a href="http://www.virtualjapan.com/wiki/Ato_%28fashion_brand%29" rel="noopener" title="Ato Japan" target="_blank">Ato</a></li>
<li><a href="http://www.virtualjapan.com/wiki/Billionaire_Boys_Club" rel="noopener" title="Billionaire Boys Club" target="_blank">Billionaire Boys Club</a></li>
<li><a href="http://www.virtualjapan.com/wiki/Chisato_Tsumori" rel="noopener" title="Chisato Tsumori" target="_blank">Chisato Tsumori</a></li>
<li><a href="http://www.virtualjapan.com/wiki/Comme_des_Garcons" rel="noopener" title="Comme des Garcons" target="_blank">Comme des Garcons</a></li>
<li><a href="http://www.virtualjapan.com/wiki/Edwin" rel="noopener" title="Edwin Jeans" target="_blank">Edwin</a></li>
<li><a href="http://www.virtualjapan.com/wiki/Frapbois" rel="noopener" title="Frapbois" target="_blank">Frapbois</a></li>
<li><a href="http://www.virtualjapan.com/wiki/Hysteric_Glamour" rel="noopener" title="Hysteric Glamour" target="_blank">Hysteric Glamour</a></li>
<li><a href="http://www.virtualjapan.com/wiki/Limi_Feu" rel="noopener" title="Limi Feu" target="_blank">Limi Feu</a></li>
<li><a href="http://www.virtualjapan.com/wiki/Mercibeaucoup" rel="noopener" title="Mercibeaucoup" target="_blank">Mercibeaucoup</a></li>
<li><a href="http://www.virtualjapan.com/wiki/N.Hoolywood" rel="noopener" title="N.Hoolywood" target="_blank">N.Hoolywood</a></li>
<li><a href="http://www.virtualjapan.com/wiki/Samantha_Thavasa" rel="noopener" title="Samantha Thavasa" target="_blank">Samantha Thavasa</a></li>
<li><a href="http://www.virtualjapan.com/wiki/The_Viridi-anne" rel="noopener" title="The Viridi-anne" target="_blank">The Viridi-anne</a></li>

	</ul>
</section>
</aside><!-- #secondary -->
			</div>
          </main>
	</div><!-- #content -->
<footer role="contentinfo" class="footer">
    <div class="inner-wrapper footer-wrapper">
        <div class="footer-main">
            <div class="footer-menu">
                <button class="menu-toggle" aria-controls="primary-menu" aria-expanded="false">Primary Menu</button>
                <div class="menu-footer-container"><ul id="Footer" class="menu"><li id="menu-item-94796" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-home menu-item-94796"><a href="https://tokyofashion.com/">Home</a></li>
<li id="menu-item-94797" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-94797"><a href="https://tokyofashion.com/articles/">Articles</a></li>
<li id="menu-item-94798" class="menu-item menu-item-type-post_type menu-item-object-page current-menu-item page_item page-item-1308 current_page_item menu-item-94798"><a href="https://tokyofashion.com/photos/" aria-current="page">Street Photos</a></li>
<li id="menu-item-94799" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-94799"><a href="https://tokyofashion.com/brands/">Brands</a></li>
<li id="menu-item-94800" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-94800"><a href="https://tokyofashion.com/forum/">Forum</a></li>
<li id="menu-item-94801" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-94801"><a href="https://tokyofashion.com/fashion-map/">Fashion Map</a></li>
<li id="menu-item-94802" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-94802"><a href="https://tokyofashion.com/music/">Music</a></li>
<li id="menu-item-94803" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-94803"><a href="https://tokyofashion.com/contests/">Contests</a></li>
<li id="menu-item-94804" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-94804"><a href="https://tokyofashion.com/contributors/">About</a></li>
</ul></div>            </div>
            <div class="footer-logo logo">
                <noscript><img width="148" height="72" src="/wp-content/themes/tokyofashion/img/footer-logo.gif" alt="Logo"></noscript><img class="lazyload" width="148" height="72" src="data:image/svg+xml,%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20viewBox=%220%200%20148%2072%22%3E%3C/svg%3E" data-src="/wp-content/themes/tokyofashion/img/footer-logo.gif" alt="Logo">
            </div>
        </div>
        <div class="footer-copyright">
            <p>Copyright 2000-2021 TokyoFashion.com. All rights reserved. <a href="#">Privacy Policy</a></p>
        </div>
    </div>
</footer>
</div>

<noscript><style>.lazyload{display:none;}</style></noscript><script data-noptimize="1">window.lazySizesConfig=window.lazySizesConfig||{};window.lazySizesConfig.loadMode=1;</script><script async="" data-noptimize="1" src="https://tokyofashion.com/wp-content/plugins/autoptimize/classes/external/js/lazysizes.min.js?ao_version=3.1.13"></script>





<script defer="" src="https://tokyofashion.com/wp-content/cache/autoptimize/js/autoptimize_4c77f180cca5754b3c917b64152ec93e.js"></script><script>(function(){function c(){var b=a.contentDocument||a.contentWindow.document;if(b){var d=b.createElement('script');d.innerHTML="window.__CF$cv$params={r:'9201829a0d14c94a',t:'MTc0MTkzMTYwMS4wMDAwMDA='};var a=document.createElement('script');a.nonce='';a.src='/cdn-cgi/challenge-platform/scripts/jsd/main.js';document.getElementsByTagName('head')[0].appendChild(a);";b.getElementsByTagName('head')[0].appendChild(d)}}if(document.body){var a=document.createElement('iframe');a.height=1;a.width=1;a.style.position='absolute';a.style.top=0;a.style.left=0;a.style.border='none';a.style.visibility='hidden';document.body.appendChild(a);if('loading'!==document.readyState)c();else if(window.addEventListener)document.addEventListener('DOMContentLoaded',c);else{var e=document.onreadystatechange||function(){};document.onreadystatechange=function(b){e(b);'loading'!==document.readyState&&(document.onreadystatechange=e,c())}}}})();</script><iframe height="1" width="1" style="position: absolute; top: 0px; left: 0px; border: none; visibility: hidden;"></iframe><script defer="" src="https://static.cloudflareinsights.com/beacon.min.js/vcd15cbe7772f49c399c6a5babf22c1241717689176015" integrity="sha512-ZpsOmlRQV6y907TI0dKBHq9Md29nnaEIPlkf84rnaERnq6zvWvPUqr2ft8M1aS28oN72PdrCzSjY4U6VaAw1EQ==" data-cf-beacon="{&quot;rayId&quot;:&quot;9201829a0d14c94a&quot;,&quot;serverTiming&quot;:{&quot;name&quot;:{&quot;cfExtPri&quot;:true,&quot;cfL4&quot;:true,&quot;cfSpeedBrain&quot;:true,&quot;cfCacheStatus&quot;:true}},&quot;version&quot;:&quot;2025.1.0&quot;,&quot;token&quot;:&quot;a4577270ad5a4bf19902742d028d2a2b&quot;}" crossorigin="anonymous"></script>





</body></html>"""  # Replace this with your actual HTML data

soup = BeautifulSoup(html, "html.parser")

 
data = []
for link in soup.find_all("a", href=True):  
    title = link.get_text(strip=True)
    url = link["href"]
    
    # Find image inside the link (if available)
    img_tag = link.find("img")
    img_url = img_tag["src"] if img_tag else "No Image"
    
    data.append([title, url, img_url])


csv_file = "harujuku_trends.csv"
with open(csv_file, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Title", "Link", "Image URL"])
    writer.writerows(data)



import requests
from PIL import Image
from io import BytesIO
import os
import pandas as pd
os.makedirs("fashion_images", exist_ok=True)

# Load CSV
df = pd.read_csv("harujuku_trends.csv")
df = pd.read_csv("shibuyatrends.csv")
df = pd.read_csv("shinjukutrends.csv")

# Download images
for index, row in df.iterrows():
    try:
        response = requests.get(row["image"])
        img = Image.open(BytesIO(response.content))
        img.save(f"fashion_images/image_{index}.jpg")
    except:
        continue

print("Images downloaded successfully!")



import sqlite3
import pandas as pd

# Connect to SQLite (or create DB if it doesn’t exist)
conn = sqlite3.connect("fashion_trends.db")
cursor = conn.cursor()

# Create a table
cursor.execute("""
CREATE TABLE IF NOT EXISTS fashion (
    id INTEGER PRIMARY KEY,
    title TEXT,
    link TEXT,
    image_url TEXT
)
""")

# Insert data
df = pd.read_csv("harujuku_trends.csv")
df = pd.read_csv("shinjukutrends.csv")
df = pd.read_csv("shibuyatrends.csv")
df.to_sql("fashion", conn, if_exists="replace", index=False)

print("Data stored in database ")






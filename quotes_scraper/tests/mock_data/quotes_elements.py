quote_element_1 = """
			<div class="quote mediumText ">
  <div class="quoteDetails ">
        <a class="leftAlignedImage" href="/author/show/1221698.Neil_Gaiman">
      <img alt="Neil Gaiman" src="https://images.gr-assets.com/authors/1234150163p2/1221698.jpg" />
</a>
<div class="quoteText">
      &ldquo;Fairy tales are more than true: not because they tell us that dragons exist, but because they tell us that dragons can be beaten.&rdquo;
  <br>  &#8213;
  <span class="authorOrTitle">
    Neil Gaiman,
  </span>
    <span id=quote_book_link_17061>
      <a class="authorOrTitle" href="/work/quotes/2834844">Coraline</a>
    </span>
    

  
<script type="text/javascript" charset="utf-8">
//<![CDATA[  

  function submitShelfLink(unique_id, book_id, shelf_id, shelf_name, submit_form, exclusive) {
    var checkbox_id = 'shelf_name_' + unique_id + '_' + shelf_id;
    var element = document.getElementById(checkbox_id)

    var checked = element.checked
    if (checked && exclusive) {
      // can't uncheck a radio by clicking it!
      return
    }
    if(document.getElementById("savingMessage")){
      Element.show('savingMessage')
    }
    var element_id = 'shelfInDropdownName_' + unique_id + '_' + shelf_id;
    Element.update(element_id, "saving...");
    if (submit_form) {
      Element.hide('shelfDropdown_' + unique_id)
      var form = document.getElementById('addBookForm' + book_id)
      if (form) {
        form.shelf.value = shelf_name
        form.onsubmit()
      }
    }
    else {
      var action = checked ? 'remove' : ''
      element.checked = !element.checked
      new Ajax.Request('/shelf/add_to_shelf', {asynchronous:true, evalScripts:true, onSuccess:function(request){shelfSubmitted(request, book_id, checkbox_id, element_id, unique_id, shelf_name)}, parameters:'book_id=' + book_id + '&name=' + shelf_name + '&a=' + action + '&authenticity_token=' + encodeURIComponent('rzKb78xtiJAjWR24v66jzFsRoVYzS65CiXNRysgLEhDhDEqNGo1bqSMCnJUIds62VykL70uMXfSZ4H9daG6mxQ==')})
    }
  }

  function shelfSubmitted(request, book_id, checkbox_id, element_id, unique_id, shelf_name) {
    Element.update('shelfListfalse_' + book_id, request.responseText)
    afterShelfSave(checkbox_id, element_id, unique_id, shelf_name.escapeHTML())
  }

  function refreshGroupBox(group_id, book_id) {
    new Ajax.Updater('addGroupBooks' + book_id + '', '/group/add_book_box', {asynchronous:true, evalScripts:true, onSuccess:function(request){refreshGroupBoxComplete(request, book_id);}, parameters:'id=' + group_id + '&book_id=' + book_id + '&refresh=true' + '&authenticity_token=' + encodeURIComponent('pzOENkvIcr0od02mHgBjJfnpFX8V3Iyt8UMbbwpf2BrpDVVUnSihhCgszIup2A5f9dG/xm0bfxvh0DX4qjpszw==')})
  }
//]]>
</script>


<script>
//<![CDATA[
      var newTip = new Tip($('quote_book_link_17061'), "\n\n  <h2><a class=\"readable bookTitle\" href=\"https://www.goodreads.com/book/show/17061.Coraline?from_choice=false&amp;from_home_module=false\">Coraline<\/a><\/h2>\n\n      <div>\n        by <a class=\"authorName\" href=\"/author/show/1221698.Neil_Gaiman\">Neil Gaiman<\/a><span title=\"Goodreads Author!\">*<\/span>\n      <\/div>\n\n          <div class=\"smallText uitext darkGreyText\">\n            <span class=\"minirating\"><span class=\"stars staticStars notranslate\"><span size=\"12x12\" class=\"staticStar p10\"><\/span><span size=\"12x12\" class=\"staticStar p10\"><\/span><span size=\"12x12\" class=\"staticStar p10\"><\/span><span size=\"12x12\" class=\"staticStar p10\"><\/span><span size=\"12x12\" class=\"staticStar p3\"><\/span><\/span> 4.06 avg rating &mdash; 556,924 ratings<\/span>            &mdash; published 2002\n          <\/div>\n\n    <div class=\"addBookTipDescription\">\n      \n<span id=\"freeTextContainer13687441555565652198\">The day after they moved in, Coraline went exploring....\n\nIn Coraline&apos;s family&apos;s new flat are twenty-one windows and fourteen doors. Thirteen of the doors open and close. \n\nThe fourteenth is locked, and on the other side is only a brick wall, until t<\/span>\n  <span id=\"freeText13687441555565652198\" style=\"display:none\">The day after they moved in, Coraline went exploring....\n\nIn Coraline\'s family\'s new flat are twenty-one windows and fourteen doors. Thirteen of the doors open and close. \n\nThe fourteenth is locked, and on the other side is only a brick wall, until the day Coraline unlocks the door to find a passage to another flat in another house just like her own. \n\nOnly it\'s different. \n\nAt first, things seem marvelous in the other flat. The food is better. The toy box is filled with wind-up angels that flutter around the bedroom, books whose pictures writhe and crawl and shimmer, little dinosaur skulls that chatter their teeth. But there\'s another mother, and another father, and they want Coraline to stay with them and be their little girl. They want to change her and never let her go. \n\nOther children are trapped there as well, lost souls behind the mirrors. Coraline is their only hope of rescue. She will have to fight with all her wits and all the tools she can find if she is to save the lost children, her ordinary life, and herself. \n\nCritically acclaimed and award-winning author Neil Gaiman will delight readers with his first novel for all ages.<\/span>\n  <a data-text-id=\"13687441555565652198\" href=\"#\" onclick=\"swapContent(\$(this));; return false;\">...more<\/a>\n\n    <\/div>\n\n      <div class=\'wtrButtonContainer wtrSignedOut\' id=\'1_book_17061\'>\n<div class=\'wtrUp wtrLeft\'>\n<form action=\"/shelf/add_to_shelf\" accept-charset=\"UTF-8\" method=\"post\"><input name=\"utf8\" type=\"hidden\" value=\"&#x2713;\" /><input type=\"hidden\" name=\"authenticity_token\" value=\"05UvnNTM3my9g/R8+GEOyjTSvRYyyE9fd/KclmjYsN6dq/7+AiwNVb3YdVFPuWOwOOoXr0oPvOlnYbIByL0ECw==\" />\n<input type=\"hidden\" name=\"book_id\" id=\"book_id\" value=\"17061\" />\n<input type=\"hidden\" name=\"name\" id=\"name\" value=\"to-read\" />\n<input type=\"hidden\" name=\"unique_id\" id=\"unique_id\" value=\"1_book_17061\" />\n<input type=\"hidden\" name=\"wtr_new\" id=\"wtr_new\" value=\"true\" />\n<input type=\"hidden\" name=\"from_choice\" id=\"from_choice\" value=\"false\" />\n<input type=\"hidden\" name=\"from_home_module\" id=\"from_home_module\" value=\"false\" />\n<input type=\"hidden\" name=\"ref\" id=\"ref\" value=\"\" class=\"wtrLeftUpRef\" />\n<input type=\"hidden\" name=\"existing_review\" id=\"existing_review\" value=\"false\" class=\"wtrExisting\" />\n<input type=\"hidden\" name=\"page_referrer\" id=\"page_referrer\" value=\"https://www.goodreads.com/quotes/search?utf8=%E2%9C%93&amp;q=jeffrey+archer&amp;commit=Search\" />\n<input type=\"hidden\" name=\"page_url\" id=\"page_url\" value=\"/quotes/search\" />\n<button class=\'wtrToRead\' type=\'submit\'>\n<span class=\'progressTrigger\'>Want to Read<\/span>\n<span class=\'progressIndicator\'>saving…<\/span>\n<\/button>\n<\/form>\n\n<\/div>\n\n<div class=\'wtrRight wtrUp\'>\n<form class=\"hiddenShelfForm\" action=\"/shelf/add_to_shelf\" accept-charset=\"UTF-8\" method=\"post\"><input name=\"utf8\" type=\"hidden\" value=\"&#x2713;\" /><input type=\"hidden\" name=\"authenticity_token\" value=\"JwePcQ81BUa78l5GZvHiP+1xNhd88Z4BuluwAEahz+lpOV4T2dXWf7up32vRKY9F4UmcrgQ2bbeqyJ6X5sR7PA==\" />\n<input type=\"hidden\" name=\"unique_id\" id=\"unique_id\" value=\"1_book_17061\" />\n<input type=\"hidden\" name=\"book_id\" id=\"book_id\" value=\"17061\" />\n<input type=\"hidden\" name=\"a\" id=\"a\" />\n<input type=\"hidden\" name=\"name\" id=\"name\" />\n<input type=\"hidden\" name=\"from_choice\" id=\"from_choice\" value=\"false\" />\n<input type=\"hidden\" name=\"from_home_module\" id=\"from_home_module\" value=\"false\" />\n<input type=\"hidden\" name=\"page_referrer\" id=\"page_referrer\" value=\"https://www.goodreads.com/quotes/search?utf8=%E2%9C%93&amp;q=jeffrey+archer&amp;commit=Search\" />\n<input type=\"hidden\" name=\"page_url\" id=\"page_url\" value=\"/quotes/search\" />\n<\/form>\n\n<button class=\'wtrShelfButton\'><\/button>\n<div class=\'wtrShelfMenu\'>\n<ul class=\'wtrExclusiveShelves\'>\n<li><button class=\'wtrExclusiveShelf\' name=\'name\' type=\'submit\' value=\'to-read\'>\n<span class=\'progressTrigger\'>Want to Read<\/span>\n<img alt=\"saving…\" class=\"progressIndicator\" src=\"https://s.gr-assets.com/assets/loading-trans-ced157046184c3bc7c180ffbfc6825a4.gif\" />\n<\/button>\n<\/li>\n<li><button class=\'wtrExclusiveShelf\' name=\'name\' type=\'submit\' value=\'currently-reading\'>\n<span class=\'progressTrigger\'>Currently Reading<\/span>\n<img alt=\"saving…\" class=\"progressIndicator\" src=\"https://s.gr-assets.com/assets/loading-trans-ced157046184c3bc7c180ffbfc6825a4.gif\" />\n<\/button>\n<\/li>\n<li><button class=\'wtrExclusiveShelf\' name=\'name\' type=\'submit\' value=\'read\'>\n<span class=\'progressTrigger\'>Read<\/span>\n<img alt=\"saving…\" class=\"progressIndicator\" src=\"https://s.gr-assets.com/assets/loading-trans-ced157046184c3bc7c180ffbfc6825a4.gif\" />\n<\/button>\n<\/li>\n<\/ul>\n<\/div>\n<\/div>\n\n<div class=\'ratingStars wtrRating\'>\n<div class=\'starsErrorTooltip hidden\'>\nError rating book. Refresh and try again.\n<\/div>\n<div class=\'myRating uitext greyText\'>Rate this book<\/div>\n<div class=\'clearRating uitext\'>Clear rating<\/div>\n<div class=\"stars\" data-resource-id=\"17061\" data-user-id=\"0\" data-submit-url=\"/review/rate/17061?page_referrer=https%3A%2F%2Fwww.goodreads.com%2Fquotes%2Fsearch%3Futf8%3D%25E2%259C%2593%26q%3Djeffrey%2Barcher%26commit%3DSearch&page_url=%2Fquotes%2Fsearch&rate_books_page=false&stars_click=false&wtr_button_id=1_book_17061\" data-rating=\"0\"><a class=\"star off\" title=\"did not like it\" href=\"#\" ref=\"\">1 of 5 stars<\/a><a class=\"star off\" title=\"it was ok\" href=\"#\" ref=\"\">2 of 5 stars<\/a><a class=\"star off\" title=\"liked it\" href=\"#\" ref=\"\">3 of 5 stars<\/a><a class=\"star off\" title=\"really liked it\" href=\"#\" ref=\"\">4 of 5 stars<\/a><a class=\"star off\" title=\"it was amazing\" href=\"#\" ref=\"\">5 of 5 stars<\/a><\/div>\n<\/div>\n\n<\/div>\n\n\n\n\n", { style: 'addbook', stem: 'leftMiddle', hook: { tip: 'leftMiddle', target: 'rightMiddle' }, offset: { x: 5, y: 0 }, hideOn: false, width: 400, hideAfter: 0.05, delay: 0.35 });
      $('quote_book_link_17061').observe('prototip:shown', function() {
        if (this.up('#box')) {
          $$('div.prototip').each(function(i){i.setStyle({zIndex: $('box').getStyle('z-index')})});
        } else {
          $$('div.prototip').each(function(i){i.setStyle({zIndex: 6000})});
        }
      });

      newTip['wrapper'].addClassName('prototipAllowOverflow');

        $('quote_book_link_17061').observe('prototip:shown', function () {
          $$('div.prototip').each(function (e) {
            if ($('quote_book_link_17061').hasClassName('ignored')) {
              e.setStyle({'display': 'none'});
              return;
            }
            e.setStyle({'overflow': 'visible'});
          });
        });
      $('quote_book_link_17061').observe('prototip:hidden', function () {
        $$('span.elementTwo').each(function (e) {
          if (e.getStyle('display') !== 'none') {
            var lessLink = e.next();
            swapContent(lessLink);
          }
        });
      });

//]]>
</script>

</div>


<div class="quoteFooter">
   <div class="greyText smallText left">
     tags:
       <a href="/quotes/tag/books">books</a>,
       <a href="/quotes/tag/dragons">dragons</a>,
       <a href="/quotes/tag/fairy-tales">fairy-tales</a>,
       <a href="/quotes/tag/inspirational">inspirational</a>,
       <a href="/quotes/tag/paraphrasing-g-k-chesterton">paraphrasing-g-k-chesterton</a>
   </div>
   <div class="right">
     <a class="smallText" title="View this quote" href="/quotes/17764-fairy-tales-are-more-than-true-not-because-they-tell">43913 likes</a>
   </div>
</div>

  </div>
    <div class="action">
        <a class="gr-button gr-button--small" rel="nofollow" href="/user/new">Like</a>
    </div>
  <br class="clear"/>
</div>"""

quote_element_2 = """

	<div class="quote mediumText last">
  <div class="quoteDetails ">
        <a class="leftAlignedImage" href="/author/show/1221698.Neil_Gaiman">
      <img alt="Neil Gaiman" src="https://images.gr-assets.com/authors/1234150163p2/1221698.jpg" />
</a>
<div class="quoteText">
      &ldquo;Tomorrow may be hell, but today was a good writing day, and on the good writing days nothing else matters.&rdquo;
  <br>  &#8213;
  <span class="authorOrTitle">
    Neil Gaiman
  </span>
</div>


<div class="quoteFooter">
   <div class="greyText smallText left">
     tags:
       <a href="/quotes/tag/writing">writing</a>
   </div>
   <div class="right">
     <a class="smallText" title="View this quote" href="/quotes/21831-tomorrow-may-be-hell-but-today-was-a-good-writing">3064 likes</a>
   </div>
</div>

  </div>
    <div class="action">
        <a class="gr-button gr-button--small" rel="nofollow" href="/user/new">Like</a>
    </div>
  <br class="clear"/>
</div>


"""

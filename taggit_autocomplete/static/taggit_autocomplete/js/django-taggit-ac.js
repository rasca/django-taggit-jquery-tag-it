(function($) {
    $(document).ready(function() {
        $('.django-taggit-ac').each(function() {
            var $elem = $(this);
            $elem.tagit({
                caseSensitive: false,
                tagSource: function(search, showChoices) {
                    options = this;
                    $.getJSON($elem.data('src'), {
                        q: search.term.toLowerCase()
                    }, function(data) {
                        showChoices(options._subtractArray(data, options.assignedTags()));
                    });
                }
            });
        });
    });
})(jQuery);

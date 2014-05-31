Pull Quote - Markdown Plugin 
==================================

#### Pull Quote ####

[Pull Quotes][pq] are seen in magazines to draw the attention of the reader to important excerpts of the article. This extension can be used as a Markdown plugin or in a [Pelican site][pelican], to easily implement pull quotes.

The left half of the figure below shows the markdown syntax and the right half shows the corresponding web page. The generated HTML markup is quite clean and non-repetitive as CSS3 is used. But note that the excerpt is an exact copy of the body text and shown quite close to it.

![side by side comparison](https://raw.githubusercontent.com/arocks/markdown-pullquote/master/side-by-side.png) 

[pq]: http://en.wikipedia.org/wiki/Pull_quote

### Usage ###

Usage instructions as applicable to [Pelican][pelican].

Copy the `mdx_pullquote` directory into the `plugins` directory inside your pelican project.

Next open your `pelicanconf.py` and add `'pullquote'` to the `MD_EXTENSIONS` list, as follows:

``` python

    MD_EXTENSIONS = ['codehilite', 'pullquote']
```

Finally, ensure that your site's CSS recognises and display the pull quote correctly. There are several ways of achieving this. A sample CSS code could be:

``` css

    div[data-pullquote]:before, span[data-pullquote]:before {
	    content: attr(data-pullquote);
        display: block;
	    float: right;
	    width: 200px;
	    margin: 0 0 0.5em 30px;
	    padding: 0;
	    font-size: 1.5em;
	    line-height: 1.4em;

        font-style: italic;
        text-align: left;
        color: #0000AA;
    }

```

Now, you are all set!

To use pulldown in your markdown posts, you will need to use markdown's hyperlink syntax with `+` symbol instead of the URL. For e.g.

```markdown

	This text is before the quote. I would say,[this part 
    will appear as a pull quote](+). This text is after the quote.  
    
```

### License ###

This content is released under the (http://opensource.org/licenses/MIT) MIT License.

[pelican]: http://docs.getpelican.com/en/latest/

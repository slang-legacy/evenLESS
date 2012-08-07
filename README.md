evenLESS
========

evenLESS is an indentation-based language which compiles into [LESS](http://lesscss.org/). It follows the exact same syntax as properly formatted LESS, except it does not need curly braces or semi-colins. For example, this evenLESS code:

```scss
@import "lib.css"

.border-radius(@radius: 5px) //a parametric mixin
	border-radius: @radius
	-moz-border-radius: @radius
	color: @radius

//a comment on its own line

#header
	.border-radius(4px)

	.nav // nested!
		color: #000

/*a css style comment*/

div span, p span, nav span{ //some real css (evenLESS can parse this too)
    font-size: 18px;
}

.button
	.border-radius
```

...is compiled into this LESS code:

```scss
@import "lib.css";

.border-radius(@radius: 5px){//a parametric mixin
	border-radius: @radius;
	-moz-border-radius: @radius;
	color: @radius;}

//a comment on its own line

#header{
	.border-radius(4px);

	.nav{// nested!
		color: #000;}}

/*a css style comment*/

div span, p span, nav span{//some real css (evenLESS can parse this too)
	font-size: 18px;}


.button{
	.border-radius;}
```

...which gets compiled into normal CSS like LESS code always is.

This indentation-based syntax helps make code more concise and is good for people who already properly indent code, because it uses these indentations in place of the regular characters (curly braces & semicolons) to make a much lighter syntax.

##Usage

In python you can use:

```python
import evenless

print evenless.compile("""
@color: #4D926F

#header
	color: @color

h2
	color: @color
""")
```


##Features
 - can be mixed with regular LESS (and obviously, CSS) so long as it is properly indented
 - line-to-line conversion (so all lines match up between the source and original)
 - (**NOT IMPLEMENTED YET**) console interface which replaces lessc with same functionality, but for evenLESS
 - evenLESS can be compiled into either LESS (to use in the client-side LESS compiler, or another LESS compiler), or automatically into CSS
 - fully compatible with all versions of CSS, as well as browser specific extensions
 - evenLESS syntax works with existing LESS syntax highlighting


##Notes
 - Technically the outputted LESS should have the curly braces at the end of blocks be on their own lines. However, they are added to the end of the last line in the block to insure that line numbers are not changed between the source and the original (so the line numbers in error messages match up). If you want the output to be more readable then you can pass it through a LESS formatter.
 - evenLESS is tab-indented (no spaces, until compatibility is added for this)
evenLESS
========

##Update
As of now, I've stopped working on evenLESS. It was a fun project, and is probably still useful because of it's backwards compatibility with LESS. However, I really like [Stylus](https://github.com/LearnBoost/stylus) more, so I have very little motivation to continue developing this.

If somebody else wants to take this over, go ahead. I'll even link this repo to your fork if you email me.

-------------------------------------

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

evenLESS_code = """
@color: #4D926F

#header
	color: @color

h2
	color: @color
"""

print evenless.compile(evenLESS_code)
```

or this more robust example which prints out errors if they are raised, which is useful for debugging syntax errors:

```python
try:
	print evenless.compile(evenLESS_code)
except evenless.CalledProcessError as error:
	print error.output  # print out explanation of error (same as the one returned by lessc)

```


##Features
 - can be mixed with regular LESS (and obviously, CSS) so long as it is properly indented
 - line-to-line conversion, so all lines match up between the source and original
 - (**NOT IMPLEMENTED YET**) console interface which replaces lessc with same functionality, but for evenLESS
 - evenLESS can be compiled into either LESS (to use in the client-side LESS compiler, or another LESS compiler), or automatically into CSS
 - fully compatible with all versions of CSS, as well as browser specific extensions
 - evenLESS syntax works with existing LESS syntax highlighting


##Notes
 - Technically the outputted LESS should have the curly braces at the end of blocks be on their own lines (if it were formatted properly). However, they are added to the end of the last line in the block to insure that line numbers are not changed between the source and the original (so the line numbers in error messages match up). If you want the output to be more readable then you can pass it through a LESS formatter.
 - evenLESS is tab-indented (no spaces, until compatibility is added for this)
 - If you are just looking to compile LESS using python, checkout the `compile_LESS()` function in this module; it implements a full interface for interacting with lessc and can be used independently from the evenLESS compiler. Thus, it is useful even if you are not using evenLESS.
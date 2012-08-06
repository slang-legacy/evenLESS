evenLESS
=========

evenLESS is a indentation-based language which compiles into LESS. It follows the exact same syntax as properly formatted LESS, except it has no curly braces or semi-colins. For example, this evenLESS code: 

	@import "lib.css"

	.border-radius (@radius: 5px) //a parametric mixin
		border-radius: @radius
		-moz-border-radius: @radius
		color: @radius

	//a comment on its own line

	#header
		.border-radius(4px)

		#header // nested!
			.border-radius(4px)

	/*a multi-
	line
	comment*/

	.button
		.border-radius

...is compiled into this LESS code:

	@import "lib.css";

	.border-radius (@radius: 5px){//a parametric mixin
		border-radius: @radius;
		-moz-border-radius: @radius;
		color: @radius;}

	//a comment on its own line

	#header{
		.border-radius(4px);

		#header{// nested!
			.border-radius(4px);}}

	/*a multi-
	line
	comment*/

	.button{
		.border-radius;}

...which gets compiled into normal CSS like LESS code always is.

This indentation-based syntax helps make code more concise and is good for people who already properly indent code, because it uses these indentations in place of the regular characters (curly braces & semicolons) to make a much lighter syntax.

##Usage

In python you can use:

	import evenless

	print evenless.compile("""
	@color: #4D926F

	#header
		color: @color

	h2
		color: @color
	""")


##Features
 - line-to-line conversion (so all lines match up between the source and original)
 - evenLESS syntax works with existing LESS syntax highlighting
 - (**NOT IMPLEMENTED YET**) console interface which replaces lessc with same functionality, but for evenLESS
 - evenLESS can be compiled into either LESS (to use in the client-side LESS compiler, or another LESS compiler), or automatically into CSS
 - fully compatible with all versions of CSS, as well as browser specific extensions


##Notes
 - Technically the outputted LESS should have the curly brackets at the end of blocks be on their own lines. However, they are added to the end of the last line in the block to insure that line numbers are not changed between the source and the original (so the line numbers in error messages match up). If you want the output to be more readable then you can pass it through a LESS formatter.



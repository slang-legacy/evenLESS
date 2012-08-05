LESSplus
=========

LESS+ is a compiler which takes indentation-based LESS and outputs regular LESS. For example, this LESS+ code: 

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

The syntax of indentation based LESS (called LESS+) is the same as properly formatted LESS, just without any curly braces or semicolons (similar to the syntax of SASS). This helps make code more concise and is good for people who already properly indent code, because it uses these indentations in place of the regular characters (curly braces & semicolons) to make a lighter syntax.

##Usage

In python you can use:

	import lessplus

	print lessplus.compile("""
	@color: #4D926F

	#header
		color: @color

	h2
		color: @color
	""")


##Features
 - line-to-line conversion (so all lines match up between the source and original)
 - LESS+ syntax works with existing LESS syntax highlighting
 - (**NOT IMPLEMENTED YET**) console interface which replaces lessc with same functionality, but for LESS+
 - LESS+ can be compiled either to LESS (to use in the client-side LESS compiler, or another LESS compiler), or automatically into CSS (utilizing lessc)


##Notes
 - I realize that the curly brackets at the end of blocks should be on their own lines. However, they are added to the end of the last line in the block to insure that line numbers are not changed between the source and the original. If you want the output to be more readable then you can pass it through a LESS formatter.
 - LESS+ is just an abbreviation for LESSplus


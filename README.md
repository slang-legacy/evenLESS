LESSplus
========

LESSplus is a compiler which takes indentation-based LESS and outputs regular LESS. For example, this LESS+ code: 

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

line-to-line conversion (so all lines match up between the source and original)
indentation-based syntax works with existing LESS syntax highlighting

*Note: I realize that the curly brackets at the end of blocks should be on their own lines. However they are added to the end of the last line in the block to insure that line numbers are not changed between the source and the original. If you want the output to be more readable then you can pass it through a LESS formatter*


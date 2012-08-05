LESSplus
========

LESSplus is a compiler which takes indentation-based LESS and outputs regular LESS.

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

line-to-line conversion (so all lines match up between the source and original)
indentation-based syntax works with existing LESS syntax highlighting


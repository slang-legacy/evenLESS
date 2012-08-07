#this file can be removed if you don't need to test the evenLESS compiler (nothing relies on it)

import evenless

compiled = evenless.compile(
"""
@import "lib.css"

.border-radius (@radius: 5px) //a parametric mixin
	border-radius: @radius
	-moz-border-radius: @radius
	color: @radius

//a comment on its own line
	//an indented comment

#header
	.border-radius(4px)

	#header // nested!
		.border-radius(4px)

	strayrule: #000;

/*a multi-
line
comment*/

.button
	.border-radius

.realcss#really {// real CSS/LESS!
	arealrule: #000;
	arealrule: #000;

	#really_indented rule {
		arealrule: #000;
		.border-radius(4px); //real LESS!!!
		arealrule: #000 //didn't really need that ";" anyway
	}

	a-real-stray-rule: #000;
}

//back to evenLESS
#header
	.border-radius(4px)

	#header // nested!
		.border-radius(4px)

		header // really nested !@#$%^&*()!!!111!!!
			.border-radius(4px)

			#header // nested!
				.border-radius(4px)

	#header // a little less nested
		.border-radius(4px)

"""
)

print compiled

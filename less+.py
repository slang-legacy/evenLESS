import re


def count_lines(text):
	return len(re.findall(r'\n', text))


def statement(scanner, token):
	"""token for rules, selectors and even mixins. the characters which must be added are determined by indentation"""
	return "statement", token


def indent(scanner, token): return "indent", token


def comment(scanner, token):
	"""token for a comment, this also captures any whitespace in front of the comment and newlines in the comment, so the indentation of the comment, and linebreaks are preserved without creating / parsing indent tokens. Any  are also captured because """
	return "comment", token


def newline(scanner, token): return ("newline",)


def parse(inputLESS):
	"""convert indentation based LESS into regular LESS"""
	scanner = re.Scanner([
		(r"[\t]*//.*", comment),
		(r"[\t]*\/\*(.|\n)*(?!\/\*)(.|\n)*\*\/", comment),  # css style
		(r"\t", indent),
		(r"\n", newline),
		(r"[^\n/]*", statement),
		(r"[\s+]", None),
	])

	tokens, remainder = scanner.scan(inputLESS)

	#check if there is any code that didn't get tokenized
	if remainder != "":
		print 'ERROR: invalid syntax on line ' + str(count_lines(inputLESS) - count_lines(remainder))

	#parse all the data in to an array with one entry per line of code
	lines = []

	i = 0
	while i in range(len(tokens)):
		indents = 0

		if tokens[i][0] == 'indent':
			#count number of indents starting line
			for e in range(i, len(tokens)):
				if tokens[e][0] != 'indent':
					break  # stop counting

			indents = e - i  # so e = total indents (number of indents it passed over)
			i = e  # move index up to where the last loop ended

		if tokens[i][0] == 'statement':
			text = tokens[i][1]

			#process optional comment
			if tokens[i + 1][0] == 'comment':
				i += 1
				comment_text = tokens[i][1]
			else:
				comment_text = ''

			lines.append((indents, text, comment_text))

			if tokens[i + 1][0] != 'newline': break  # statements need a newline after them, except at the end of the code

			i += 1  # pass the newline
		elif tokens[i][0] == 'newline' or tokens[i][0] == 'comment':
			lines.append(tokens[i])  # directly add blank line or comment
		else:
			return "error unexpected token"

		i += 1  # continue the loop

	i = 0
	output = ''

	while i in range(len(lines)):
		if lines[i][0] == 'newline':
			output += "\n"
		elif lines[i][0] == 'comment':
			output += lines[i][1]
		else:  # statement

			output += "\t" * lines[i][0] + lines[i][1].strip()  # print indentation and text

			#look ahead to the next statement to find indentation
			next_indentation = 0  # if there isn't another line then assume 0 indentation to close all brackets at the end of the file
			for e in range(i + 1, len(lines)):
				if lines[e][0] != 'newline' and lines[e][0] != 'comment':
					next_indentation = lines[e][0]
					break

			if lines[i][0] + 1 == next_indentation:  # must be beginning of a block if next line has one more indent
				output += '{'  # remove the ":" and whitespace around the text first
			elif lines[i][0] >= next_indentation:  # must be a rule
				output += ';'
			else:
				return 'ERROR: unexpected indent'

			output += lines[i][2]  # output comment if there is one

			# deal with closing blocks
			if next_indentation < lines[i][0]:
				output += '}' * (lines[i][0] - next_indentation)

			output += '\n'

		i += 1

	return output

print parse("""
@import "lib.css"

.border-radius (@radius: 5px) //a mixin
	border-radius: @radius // a cool comment
	-moz-border-radius: @radius
	color: @radius

//a comment on its own line
		//an indented comment on its own line

		/*an indented comment on its own line*/

/*a multi-
	line
comment with some
indentation*/

		/*a multi-
			line
		comment with some
		indentation*/

#header
	.border-radius(4px)

	#header
		.border-radius(4px)

.button
	.border-radius
""")

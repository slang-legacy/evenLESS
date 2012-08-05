import re
import subprocess
import os

"""
	compile indentation based LESS (LESS+) into CSS
	this module relies on the lessc binary (which comes with the less node package) for compiling LESS into CSS, but the compile_LESSplus method can still be used to compile LESS+ into regular LESS without lessc
"""

TMP_DIR = os.path.dirname(__file__) + '/tmp/'  # holds temporary files, should be empty, directory must already exist


def compile(LESSplus):
	"""
		compile LESS+ directly into CSS and return the CSS as a string
		this is the reccomended way of using the LESS+ compiler, but it relies on lessc
	"""
	return compile_LESS(compile_LESSplus(LESSplus))


def _statement(scanner, token):
	"""token for rules, selectors and even mixins. the characters which must be added are determined by indentation"""
	return "statement", token


def _indent(scanner, token): return "indent", token


def _comment(scanner, token):
	"""token for a comment, this also captures any whitespace in front of the comment and newlines in the comment, so the indentation of the comment, and linebreaks are preserved without creating / parsing indent tokens. Any  are also captured because """
	return "comment", token


def _newline(scanner, token): return ("newline",)


def compile_LESSplus(LESSplus):
	"""convert indentation based LESS (LESS+) into regular LESS"""
	scanner = re.Scanner([
		(r"[\t]*//.*", _comment),
		(r"[\t]*\/\*(.|\n)*(?!\/\*)(.|\n)*\*\/", _comment),  # css style
		(r"\t", _indent),
		(r"\n", _newline),
		(r"[^\n/]*", _statement),
		(r"[\s+]", None),
	])

	tokens, remainder = scanner.scan(LESSplus)

	#check if there is any code that didn't get tokenized
	if remainder != "":
		print 'ERROR: invalid syntax on line ' + str(LESSplus.count('\n') - remainder.count('\n'))  # get line num by subtracting total remaining lines from input lines

	#parse all the data in to another array to combine indents with statments
	lines = []
	indents = 0
	for token in tokens:
		if token[0] == 'indent':
			indents += 1
		elif token[0] == 'statement':
			lines.append((indents, token[1]))
			indents = 0
		elif token[0] == 'newline' or token[0] == 'comment':
			lines.append(token)  # directly add blank lines or comments (they need no processing)
		else:
			return 'error: unexpected token'

	del tokens  # not needed anymore

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

			# deal with closing blocks
			if next_indentation < lines[i][0]:
				output += '}' * (lines[i][0] - next_indentation)

		i += 1

	return output


def compile_LESS(less_code):
	"""
		compile LESS code into CSS using the lessc binary (which must be installed for this to work)
		return a string containing the compiled CSS
	"""
	temp_file = TMP_DIR + '/style.less'
	open(temp_file, 'w').write(less_code)
	css = subprocess.check_output(['lessc', '--yui-compress', temp_file])
	os.remove(temp_file)
	return css

# Rocky Raccoon
## A static website generator using Python

Python3 is a tool that can be used to generate static web pages, given markdown-like files as input

Disclaimer: Rocky Raccoon is not by any means a serious project and was created solely for educational purposes.
It is not fit to use on real projects and its code is very messy and redundant.
A better version of Rocky Raccoon is being created and should be published here as soon as I get a good grip of RegEx and invent a cool name.

## Usage

Clone this repo.
Create or edit templates in the input/templates folder.
The template can be any piece of HTML, and should have \<!--TITLE--> and \<!--CONTENT--> where the title and content of the article should be respectively.

Create a file with of .qmd filetype with the following structure:

```
EXTENDS [name of the temaplate without '.html']
TITLE [title of the current page]
TAGS [all of the page tags separated by spaces]

# Heading 1
## Heading 2
### Heading 3

@ Comment

=
Paragraph
This will be on the same line as the line above
=

IMAGE image.source.com
```

Then, just cd to 'src/' and run the 'raccoon.py' file, the output will be in the 'output/' folder.

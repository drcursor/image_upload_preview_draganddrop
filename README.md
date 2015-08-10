# image_upload_preview_draganddrop
Example of an HTML Image element with preview that accepts drag and drop

## Objective
I spent several hours googling around and trying different solutions from stackoverflow until I was able to figure out a very hacked way to get what I wanted working:

- A simple HTML Image Element
 - With image preview,
 - That would accept drag and drop,
 - That would filter files based on file extension,
 - That I could change based on an AJAX call
- And I wanted to do this without having to add 999 external JS files (ended up adding JQuery out of lazyness to write some of the JS...)

## Hack
Why is this a hack? Becase the drag and drop is actualy using a text input element to pass on the file on the POST data (at first I thought it wouldn't work because of the character limits of the HTML text element..but it actually worked on all major browsers).

## How to use
First, please take into account that this is just an example, and that its probably full of small imperfections (although it works :) ).

I've included the sample logic for a Django form but it should be easy enough to adapt it to PHP or whatever you need (please make a pull request if you have any other example on how to use it)

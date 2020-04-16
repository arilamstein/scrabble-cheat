# scrabble-cheat
Fun little project to help me beat my Mom at Words with Friends.

My New Year's Resolution was to learn Python. After taking a bunch of online courses, I finally found a fun
little side project that Python would be a good fit for.

My Mom - a retired high school English teacher no less - has recently taken to Words with Friends as a way
to pass the time during the COVID-19 Lockdowns. I personally hate the game, have no aptitude for it, and got 
tired of losing. 

So I did what any software engineer would do - I wrote a program to generate all possible words from a given
set of tiles. The dictionary comes from [here](https://github.com/dwyl/english-words/). It returns all possible words as 
well as their score. The main function is `get_all_possible_words`. It takes a set of tiles arranged as a string:

````
get_all_possible_words('stac') 
[('acts', 7),
 ('cast', 7),
 ('cats', 7),
 ('scat', 7),
 ('act', 6),
 ('cat', 6),
 ('cst', 6),
 ('cts', 6),
 ('sac', 6),
 ('sct', 6),
 ('ac', 5),
 ('ca', 5),
 ('cs', 5),
 ...
````

There is an optional second parameter, `requirements`, that allows you to specify the length of the word, as well as 
any letters that must appear in a specific position. `*` is a wildcard, so `***s` will match any 4 letter word that ends in "s":

````
get_all_possible_words('stac', '***s')
[('acts', 7), ('cats', 7)]
````



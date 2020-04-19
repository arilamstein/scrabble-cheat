# scrabble-cheat
Fun little project to help me beat my Mom at Words with Friends.

My New Year's Resolution was to learn Python. After taking a bunch of online courses, I finally found a fun
little side project that Python would be a good fit for.

My Mom - a retired high school English teacher no less - has recently taken to Words with Friends as a way
to pass the time during the COVID-19 Lockdowns. I personally hate the game, have no aptitude for it, and got 
tired of losing. 

So I did what any software engineer would do - I wrote a program to generate all possible words from a given
set of tiles. The dictionary comes from [here](https://github.com/dwyl/english-words/). It returns all possible words as 
well as their score. The main function is `get_all_words`. It takes a set of tiles arranged as a string:

````
get_all_words('ilzsiwl')
[('zills', 16),
 ('swiz', 16),
 ('zill', 15),
 ('wiz', 15),
 ('liz', 13),
 ('isz', 12),
 ('zs', 11),
 ('wills', 10),
 ('swill', 10),
 ('willi', 10),
 ...
````

`get_all_words` takes several optional parameters: `required_letters`, `max_length`, `starts_with` and `ends_with`. As an example, here is how we would limit the above search to return words that only end in `s`.
````
get_all_words('stac', ends_with="s")
[('zills', 16),
 ('zs', 11),
 ('swills', 11),
 ('wills', 10),
 ('sills', 7),
 ('wiss', 7),
 ('iwis', 7),
 ('ills', 6),
 ('wis', 6),
 ('isls', 5),
 ...
````

The biggest limitation of this script is that the dictionary it uses is not the same as the dictionary that Words with Friends uses. In particular, this dictionary appears to be much larger, so it will often recommend words that WWF does not consider valid. 

The project was mainly an exercise as I teach myself Python, and to provide some humor during the COVID-19 lockdowns. As a side benefit, it occasionally provides some help while playing Words with Friends. 


## Video Poker - C Language Version

A text-based video poker game

### SYNOPSIS

`videopoker` [`-b`] [`-b1`] [`-g` _game_] [`-is` _#chips_] [`-k` _5-char-string_] [`-mh`] [`-q`] [`-u`<D>] [`-v`]

### DESCRIPTION

`videopoker` is a text-based video poker game. It has an efficient user interface that takes a little time to learn, but allows fast play and requires only one hand to operate.

### DISCLAIMER

By default, `videopoker` is intended to closely match the behavior of **9/6 Jacks or Better** video poker machines in casinos, and an option allows selection of other games and pay tables. However, the author is not an expert on gaming, and no guarantee whatsoever is made that `videopoker`'s behavior is an exact match to that of any other video poker. Please take that into careful consideration before trying out a real video poker machine.

### HOW TO PLAY

Start the game and rest the fingers of your right hand on the keyboard as when touch typing.
Your thumb will be on the **space** bar, and your index finger through little finger
will be on the keys **j**, **k**, **l**, and semicolon (**;**). 

A five-card hand will be displayed. To hold cards, type the keys corresponding to the cards:

	SPACE   Leftmost card  
	j       Second card from left
	k       Middle card  
	l       Second card from right  
	;       Rightmost card  

The keys may be typed in any order, and a key can be entered more than once to toggle the held/discarded state of the card. The backspace key may be used to undo mistakes.

Then type the Enter key to deal. Discarded cards are redealt, and the final hand is shown, along with how it is recognized as either a winning or losing hand, and the new score.

The game will continue until you either quit or run out of chips.

To quit, type either **q** or **e**, then the **Enter** key.

**Changing the Bet**

To increase your bet from the default, type **b**, followed by a digit from **1** to **5**, along with the keys to hold cards. For example,

**lb4;**

will hold the rightmost two cards, and increase the bet to 4x. By itself,

**b3**

will increase the bet to 3x, but not hold any cards.

The increase takes effect starting with the next hand and stays in effect until changed using the same method. The only exception is when the number of chips is less than the bet, in which case the bet is automatically reduced to make it equal to the number of chips remaining, where it will stay until you change it.

**The Pay Table**

The pay table for the default game `9/6 Jacks or Better` is the following:

    Royal Flush    800
    Straight Flush  50
    Four of a Kind  25
    Full House       9
    Flush            6
    Straight         4
    Three of a Kind  3
    Two Pair         2
    Pair             1

The `-g` option may be used to play versions of the game with different pay tables.

### OPTIONS

`-b`

("Bold") Use boldface text output to display the cards. (When using the -u1 and -u2 options only.)

`-b1`

("Bet 1") Use a minimum bet of one chip, rather than the default ten. Typically used along with the `-is` option.

`-g` _name_

("Game") Play a different variant of video poker. The default is 9/6 Jacks or Better, but you can change it to another by specifying one of the strings in the left column of the following list:

	aa        All American
	tens      Tens or Better  
	jb95      9/5 Jacks or Better  
	jb86      8/6 Jacks or Better  
	jb85      8/5 Jacks or Better  
	jb75      7/5 Jacks or Better  
	jb65      6/5 Jacks or Better  

The above list is in order of payout. `All American` and `Tens or Better` have more favorable payout than the default. `All American` pays 8 for full houses, flushes, and straights. `Tens or Better` pays only 6 for a full house and 5 for a flush, but requires only 10s or better for a pair to win a payout.

The remaining games are low-pay versions of Jacks or Better. The numbers in the names are the respective payouts for full houses and flushes.

`-is` _integer_

("Initial Score") Start the game with _integer_ chips, rather than the default 1000. _integer_ may be in the range of 1 to 100,000.

`-k` "_string_"

("Keys") Replace the standard " jkl;" input keys with the ones in _string_, which must be 5 characters long and not contain a **q** or **w** character.

`-mh`

("Mark Held") Print **+** characters under the cards that are held. This option is helpful for new players, and also when testing the string supplied with the `-k` option.

`-q`

("Quiet") Don't print the banner at the start of the game, nor the final message.

`-u`<D>

("Unicode") Control Unicode output. <D> is a digit from 0 to 3.

    -u0   As with -u1, except all text is displayed in the default
          color. (For monochrome terminals, or any terminals that
          do not support ANSI escape codes.)
    -u1   No Unicode. Suits are displayed with the characters C,
          D, H, and S. Diamonds and hearts are displayed in red,
          clubs and spades are displayed in the default text color.
    -u2   (default) Display suits using Unicode playing card
          suit symbols.
    -u3   (Experimental) Display entire cards as Unicode characters.

In order for the `-u1` or `-u2` options to work, videopoker needs to use a font that contains the necessary Unicode playing card characters. On Linux, the **monospace** and **DejaVu** fonts may be used.

For `-u2` to work, the system needs to be able to properly display Unicode playing card characters.

Unicode playing card faces appear no larger than other text characters. When using the `-u2` option, increase the font size as necessary (i.e., 24 pixels or larger).

`-v`

("Version") Print the version number and exit.

### BUGS

When played with the (experimental) `-u3` option, cards may not be equally spaced apart. This may be due to improper handling of ANSI escape codes (used to change text colors) and/or improper handling of Unicode playing card characters by various virtual terminals.

### VERSION

This manual page is for version 1.0 of the program.

### AUTHOR

Jay Ts  
(http://jayts.com)

### COPYRIGHT

Copyright 2016 Jay Ts

Released under the GNU Public License, version 3.0 (GPLv3)
(http://www.gnu.org/licenses/gpl.html)

# more strings and text

# defining x as "theyre are %d types of people, which calls a number (the %d)
x = "there are %d types of people." % 10
# defining binary as "binary"
binary = "binary"
# defining doNot as "don't"
doNot = "don't"
# defining y as "those who know %s and those who know %s", the %s will call something to be placed there
y = "those who know %s and those who know %s" % (binary, doNot)

# this is ?
print(x)
# this is
print(y)

print("I said: %r.:" % x)
print("i also said: '%s'." % y)

hilarious = True
jokeEvaluation = "isn't that joke so funny!? %r"

print(jokeEvaluation % hilarious)

w = "this is the left side of..."
e = "a string with a right side."
print(w+e)

# more printing fun
print("mary had a little lamb.")
print("it's fleece was white as %s." % 'snow')
print("and everywhere that mary went.")
print("." * 10)
end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

print(end1 + end2 + end3 + end4 + end5 + end6,)
print(end7 + end8 + end9 + end10 + end11 + end12)

# But wait! There's more:
formatter = "%r %r %r %r"
print(formatter % (1, 2, 3, 4))
print(formatter % ("one", "two", "three", "four"))
print(formatter % (True, False, False, True))
print(formatter % (formatter, formatter, formatter, formatter))

# why do I use %r instead of %s in the above example?

# which should I use on a regular basis?

# why does %r sometimes give me single quotes around things?

days = "monday tuesday wednesday thursday friday saturday sunday"
months = "january\nfebruary\nmarch\napril\nmay\njune\njuly\naugust"

print("here are the days: ", days)
print("here are the months: ", months)

print("""
there's something going on here.
with the three double-quotes.
we'll be able to type as much as we like.
even 4 lines if we want, or 5, or 6.
""")

# examine closely the differences between the %r formatter and %s formatter
print("here are the months: %r" % months)
print("here are the months: %s" % months)

# escape sequences redux
tabbyCat = "\tI'm tabbed in."
persianCat = "I'm split\non a line."
backslashCat = "I'm \\ a \\ cat."
topCat = """
# creates a list of things
I'll do a list:
\t* litter box chilling
\t* eating ALL the snacks
\t* sleeping\n\t* scratches
"""
# this calls the definitons we made earlier
print(tabbyCat)
print(persianCat)
print(backslashCat)
print(topCat)

# Escape Seq            What it does?
# \\
# \'
# \"
# \a
# \b
# \f
# \n
# \N{name}
# \r
# \t
# \uxxxx
# \Uxxxxxxxx
# \v
# \ooo
# \xhh

# What does the following code do:
#   while True:
#       for i in ["/", "-", "|", "\\", "|"]:
#           print("%s\r" % i, end='')

#  Can you use ''' instead of """ ?

question 1 = input("how is your day going? ")
question 2 = input("")

print("so, you are feeling %r and %r is  ." % (age, height))

# jessie remember to ask 4 more questions dummy
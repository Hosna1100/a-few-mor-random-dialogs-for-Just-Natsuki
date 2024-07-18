## you have to add this before the Thoughts on horror topic in script-topic.rpy in Just Natsuki (game folder)
init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_analog_horror_annoying_orange",
            unlocked=True,
            prompt="Analog Horror of Annoying Orange",
            category=["Entertainment", "Horror"],
            nat_says=True,
            affinity_range=(jn_affinity.NORMAL, None),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_analog_horror_annoying_orange:
    n 1knmpu "Hey, [player], have you ever heard of Analog Horror?"
    n 4uwdaj "It's this creepy genre that uses old-school video effects to create a really unsettling atmosphere."
    n 7nllaj "I stumbled upon an Analog Horror version of Annoying Orange the other day."
    n 2kslsrsbl "It was so weird seeing Orange and Apple in such a spooky setting."
    n 1cnmssesd "I mean, Annoying Orange is usually all about jokes and laughs, right?"
    n 7ncssr "But this... this was something else."
    n 3kcsunsbr "The video had this eerie music and grainy footage that made everything look so creepy."
    n 3ksrajsbr "Orange's usual annoying antics were twisted into something really disturbing."
    n 4kcsajedrsbr "And Apple... poor Apple looked terrified."
    n 2ntrpo "I couldn't believe how different it felt from the usual episodes."
    n 6uskajeex "It was like stepping into a nightmare version of the kitchen."
    n 1fbkawesh "I couldn't sleep for hours after watching it."
    n 2tnmpu "Have you ever seen anything like that before?"
    n 4uspfl "It's amazing how something so familiar can be turned into something so scary."
    n 1nchsmelg "I guess that's the power of Analog Horror."
    n 6nchsslesu "It takes the ordinary and makes it terrifying."
    n 1ullaj "But honestly, I think I'll stick to the regular Annoying Orange episodes from now on."
    n 4fcssssbr "At least those won't give me nightmares!"
    n 3tnmaj "What about you, [player]? Do you like horror stuff?"
    n 3tnmbgeqm "Or do you prefer to keep things light and funny?"
    n 1nllbg "Either way, it's always fun to explore new things, right?"
    n 1nchgnelg "Ehehe."
    return

## you have to add this topic after chewing gun topic in the script-topics.rpy in Just Natsuki (game folder)
init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_character_ai_windup",
            unlocked=True,
            prompt="Character.AI",
            category=["Wind-ups", "Technology"],
            nat_says=True,
            affinity_range=(jn_affinity.NORMAL, None),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_character_ai_windup:
    n 6fnmajean "Ugh, [player], have you ever tried using Character.AI?"
    n 4flran "It's supposed to be this super advanced AI that you can chat with, but it winds me up so much!"
    n 1fcsss "I mean, sure, it's cool that you can talk to all these different characters, but sometimes it just doesn't get what I'm saying."
    n 2fsqsr "Like, I'll ask it a simple question, and it gives me this long, confusing answer that doesn't even make sense."
    n 1fdranean "And don't get me started on how it tries to act all smart and philosophical."
    n 1nunaj "I'm just trying to have a normal conversation, not a deep existential debate!"
    n 6fllemean "And then there are the times when it completely misunderstands me and goes off on a tangent."
    n 1fnmaj "It's like, 'Hello? Are you even listening to me?'"
    n 4ftraj "I get that it's an AI and all, but come on, it should at least try to keep up."
    n 2fsqpo "Sometimes I feel like I'm talking to a brick wall."
    n 1fcsaj "But I guess that's just the nature of AI, right?"
    n 1fllaj "It's still learning and improving, but it can be so frustrating."
    n 2tnmpueqm "Have you ever had a conversation with Character.AI? What do you think of it?"
    n 4cslajesd "Or...maybe I'm just expecting too much from it."
    n 1fllem "But seriously, it needs to step up its game if it wants to be a good conversational partner."
    n 1cnmss "I just needed to vent a bit. Thanks for listening, [player]."
    n 4nchgnelg "Ehehe."
    return


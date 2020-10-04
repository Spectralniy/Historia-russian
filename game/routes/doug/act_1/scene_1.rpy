label start:

    $ stopAllAudioTracks()


    window show
    scene bg black
    with dissolve


    scene shakeyDougRoomGame

    play music "sounds/doug/act_1/bgm_vague_anxieties.ogg" fadein 1.0

    with Dissolve(0.2)

    dad "Doug, you’d better not be on that game again!"



    $ renpy.sound.set_volume (0.5, 0, channel="sound")
    play sound "sounds/doug/act_1/doug_glass_rattle.ogg"

    "Dad’s voice booms through the house. I could swear that I heard the glasses rattle in the kitchen."

    "I bet he’s been drinking again."

    $ renpy.sound.set_volume (1, 2.0, channel="sound")
    doug "No, I’m studying."

    scene zoomedDougRoomWiki
    with Dissolve(0.2)

    "It’s not entirely a lie. At least I’m not playing a game. I hurriedly open up a Wikipedia page before the door swings open.\n"

    play sound "sounds/doug/act_1/doug_door_open.ogg"

    show doug_dad angry close
    with Dissolve(0.2)

    dad "Then show me…"

    show doug_dad sneer close
    with Dissolve(0.2)

    doug "See?"

    "Dad’s face remains in a sneer. I can tell that he’s not buying it."

    show doug_dad angry close
    with Dissolve(0.2)

    dad "Do you think I was born yesterday? Don’t make me check your history…"

    show doug_dad sneer close
    with Dissolve(0.2)

    doug "You’re saying you don’t trust me?"

    show doug_dad angry close
    with Dissolve(0.2)

    dad "How could I? I’ve known you since you were born."

    "I can feel my blood boiling. I’ve got too much going on to put up with Dad’s shit tonight."

    show doug_dad sneer close
    with Dissolve(0.2)

    doug "You’ve really got no clue, do you?"

    show doug_dad angry close
    with Dissolve(0.2)

    dad "I have more of a clue than you could ever imagine. Now show me your history. If you’ve been studying it should be obvious."

    scene bumpDougRoomOff
    play sound "sounds/doug/act_1/doug_unplug_pc.ogg"
    show doug_dad sneer close
    with None

    "Dad reaches over me and tries to open the browser history. I pull the power cord before he can reach the keyboard, and the screen goes dark.\n"

    doug "Whoops."

    show doug_dad angry close
    with Dissolve(0.2)

    dad "You little prick. Get out of here!"

    show doug_dad sneer close
    with Dissolve(0.2)

    doug "Don’t worry, I don’t want to hang around you when you’re in one of your moods."

    show doug_dad angry close
    with Dissolve(0.2)

    dad "What’s that supposed to mean?"

    "I ignore him, grab my backpack and push past him, {nw}"

    play sound "sounds/doug/act_1/doug_bump_desk.ogg" noloop

    extend "bumping the storage shelf on my way to the door."

    scene zoomedDougRoomNoPack
    show doug_dad sneer close
    with Dissolve(0.2)

    "I knew it wasn’t a huge room when I moved in, but it was better than sharing with my sister."

    "I thought I would get some privacy by sleeping in the old store room, but my dad knows no boundaries."

    "It’s a pain."

    show doug_dad angry close
    with Dissolve(0.2)

    dad "Where do you think you’re going?"

    show doug_dad sneer close
    with Dissolve(0.2)

    doug "None of your business!"

    stop music fadeout 2.0

    show doug_dad angry close
    with Dissolve(0.2)

    dad "You’re damned right it’s my business! Get back here!"



    scene bg doug livingroom with dissolve
    show doug mum headphones

    play music "sounds/doug/act_1/doug_mum_headphone.ogg" fadein 1.0


    show doug mum headphones

    "I walk out the back door to the house, waving a farewell to my mother, who is trying to drown out our fight with her headphones."

    "I feel sorry for her, but then again, it’s her husband."

    mom "Don’t be too late."

    stop music fadeout 1.0

    scene bg street dark with dissolve

    play sound "sounds/doug/act_1/doug_door_close.ogg"

    "The door closes before I get the chance to reply."



    play ad_bg_4 "sounds/doug/act_1/doug_nighttime_traffic.ogg" fadein 2.0

    "This is the third time this month that dad has come home and started ranting before even saying hello."

    "I have no idea what his deal is, but it pisses me off. No point in staying in the house and suffering."

    play sound "sounds/doug/act_1/doug_phone_ring.ogg"

    $ _history = False

    "I pull my phone out from my bag and make a call."

    show max wide smile round overlay
    with Dissolve(0.2)

    stop sound

    friendMax "Yo, Doug, what’s up?"

    "Max’s cheerful tone pisses me off. Ever since he was a kid he had his life together."

    "We’ve been friends since we both moved here years ago. At the time there weren’t many families in Penrith, so you were friends with whomever was around."

    "Back then, I didn’t notice the difference in our families, but now it was painfully obvious."

    "He never said anything about it, but I could tell. His dad drove a BMW, always a new model."

    "My dad has had the same Subaru for as long as I can remember."

    "I have to sleep in a store room. Max practically has a whole floor of his house to himself."

    $ _history = True

    $ showHiddenText('', "I have to sleep in a store room.{fast}{nw}")

    $ _history = False

    "His dad was some kind of mining consultant. I guess that explained it."

    doug "I need to blow off some steam. Can I come over?"

    $ _history = True

    $ showHiddenText(doug, "I need to stop talking to myself. People will start to think the wrong thing.{fast}{nw}")

    $ _history = False

    show max smug smile round overlay
    with Dissolve(0.2)

    friendMax "Sure thing, I’ve got nothing on. I’ll download a movie. Grab some Coke on the way."

    doug "OK. See you soon."

    $ _history = True

    $ showHiddenText(doug, "I should at least pretend to sing to myself.{fast}{nw}")

    $ _history = False

    "I walk to Max’s house, stopping at a convenience store on the way. Coke alone won’t be enough. I grab a bag of chips as well."

    $ _history = True

    $ showHiddenText('', "I walk restlessly through the streets in an attempt to burn off some of my anger.{fast}{nw}")

    stop ad_bg_4 fadeout 1.0
    stop music fadeout 1.0
    scene bg max corridor dark light on
    with Dissolve(0.2)

    play music "sounds/doug/act_1/bgm_lazy_afternoon.ogg" fadein 1.0

    show max smile
    with Dissolve(0.2)

    $ _history = False

    friendMax "Dude, what took you so long? Never mind, I got Hot Rod. It’s hilarious. You seen it?"

    $ _history = True

    $ showHiddenText('', "I think about the rage that burns inside my father, especially if he's drunk.{fast}{nw}")

    "I shake my head."

    $ _history = False

    friendMax "You’ll love it. Come on, let’s get this party started."

    scene bg max room dark lights on with dissolve
    show max smile

    "That’s one thing about Max. No bullshit. He knows what I want to do and just gets on with it. No dumb questions, no trying to make things better."

    $ _history = True

    $ showHiddenText('', "I try to think of a way to calm myself down, but there's nothing for me at home.{fast}{nw}")

    "Just Coke and a movie."

    $ _history = False

    "He knows me too well."

    $ _history = True

    $ showHiddenText('', "But maybe that is good enough.{fast}{nw}")

    show max smug smile

    $ _history = False

    friendMax "It’s not like you to sneak out. You’re usually too straight laced."

    doug "Yeah I know. Life has been pretty crap recently."

    $ _history = True

    $ showHiddenText(doug, "I guess that life can be pretty crap.{fast}{nw}")

    $ showHiddenText('', "I don't want to talk to anyone about my dad's drinking, or Mum's ignorace of that fact.{fast}{nw}")

    $ _history = False

    "I don’t want to tell him about Dad’s drinking or Mum’s ignorance of that fact."

    $ _history = True

    "I just want to chill out."

    show max smile

    $ _history = False

    friendMax "Things have a way of working themselves out. You’ll get over it. Only a couple of months and then exams are over."

    doug "I guess."

    $ _history = True

    $ showHiddenText(doug, "I guess I'll just head home and watch Hot Rod.{fast}{nw}")

    $ _history = False

    friendMax "Just think! When summer’s over you can be in university, far away from your parents."

    $ _history = True

    $ showHiddenText('', "I only have to make it through this summer, then I'm away from my parents.{fast}{nw}")

    $ _history = False
    show max smug smile

    friendMax "…and Natalia.{w} Don’t worry, I’ll look after her for you…"

    $ _history = True

    $ showHiddenText('',"I guess my only regret is that I'll be away from my sister. {fast}{nw}")

    $ _history = False

    doug "You touch my sister and I’ll kill you myself…"

    $ _history = True

    $ showHiddenText('', " If anything were to happen to her I'd never forgive myself.{fast}{nw}")

    show max wide smile

    $ _history = False

    "Max punches me playfully."

    friendMax "I’d like to see you try."

    doug "Aren’t you going to go to some fancy university as well?"

    show max serious looking away

    friendMax "Probably. Thinking about taking a gap year though. Dad keeps bugging me about it."

    friendMax "But why on earth are we talking about school? Are we watching this movie or not?"

    $ _history = True

    $ showHiddenText('', "I climb back into my window, trying not to make a sound.{fast}{nw}")

    $ _history = False

    show max smile

    friendMax "We’re here to get our laughs on."

    $ _history = True

    $ showHiddenText('', "time to get my laughs on.{fast}{nw}")

    doug "Sounds like a plan."

    show max smug smile

    $ _history = False

    friendMax "Besides, if I start thinking about how hot your sister is I won’t be able to sleep."

    doug "Shut up you wanker!"

    show max wide smile

    friendMax "Fine, fine. I can see you want her for yourself."

    "I want to make a comeback, but I realise that I’ve lost this fight."

    "I know Max would never really try and make a move on Natalia. He’s only doing it to get at me."

    "But, then again, that’s probably his point. He’s expertly taken my mind off my troubles at home."

    doug "Just put the damned movie on."



    friendMax "You’re too easy to stir up. It’s all that honour crap you’ve got in your head."

    friendMax "But don’t worry - Uncle Max has got the pill to chill your ills. Trust me - this is hilarious."

    doug "You keep saying that but I don’t see anything on your TV."

    friendMax "Alright, don’t get your knickers in a twist. Here you go."

    scene bg max room dark tv on with dissolve

    $ _history = True

    "The movie is hilarious. Within minutes I’ve forgotten about my petulant father and his drunken rampages."

    "In the back of my mind I can see his point. It’s my last year of high school. If I screw up now it can ruin the rest of my life."

    "But that’s my mistake to make, not his."

    "Mum seems to get it. She keeps telling me to keep my head on straight and remember what’s important."

    "I know that they are both right. I don’t want to fight with them, but it’s a stressful time."

    "I try to be good. I don’t drink or party like some of my friends, even though there’s not much else to do out here."

    "A lot of people seem to fall into that trap. They get bored, so they start drinking."

    "And because they spend all their money on booze, they can’t afford to get out of here."

    "It’s a vicious cycle."

    $ _history = False

    "Max gets it though. He’s a bit of a study freak, but he knows how to wind down as well. That’s why I like him."

    $ _history = True

    $ showHiddenText('',"ƞĀŁ gets it though. sHe’s a bit of a study freak, but she knows how to wind down as well. That’s why I like her.{fast}{nw}")

    "I laugh my backside off through the movie, losing myself in the childish humor. But, like all good things, it comes to an end."

    hide max
    show bg max room dark lights on with dissolve
    show max wide smile
    with dissolve
    $ _history = False

    doug "You were right, that’s exactly what I needed. I haven’t laughed so hard in ages."


    friendMax "I know, right? It’s so stupid that it becomes genius. You gunna stay over?"

    $ _history = True

    "I look at my watch."

    $ showHiddenText('', "I should turn in. It's hella late.{fast}{nw}")

    show max smile

    $ _history = False

    doug "Nah, I should get home. Things should have calmed down over there. Mum will be worried."

    friendMax "No probs. You’re always welcome here you know."

    doug "Thanks man."

    "I want to take him up on the offer, but I know that I have to patch things up with Dad. I don't like leaving things to fester."

    "Better deal with them before they get out of hand."

    "I sigh and pick myself up out of Max’s beanbag."

    doug "See you at school tomorrow?"

    friendMax "Sure. Let's come here when you're done and we can look at that maths assignment you’ve got. It’s due on Friday, you know."

    doug "Ugh, don’t remind me."

    show max wide smile

    stop music fadeout 7.0

    friendMax "You’ll be fine. Anyway, night."

    $ _history = True

    doug "Night."

    $ _history = False


    jump dougActOneSceneTwo
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

label dougActOneSceneFour:

    $ stopAllAudioTracks()


    window show
    scene bg black
    with dissolve


    scene bg street daylight
    scene bg max house changed
    with dissolve

    play music "sounds/doug/act_1/doug_bowl_ambience.ogg"

    "Max’s house stands as it always has; the two-story town house in a nice area."

    "The front garden with its perfectly maintained lawn, the immaculate white paint, the faux marble entranceway."

    "I had leaned to deal with the difference in our lifestyles, but I think part of me secretly hated him for that."

    "I take a step towards the front door, but something stops me."

    "Even though I was here less than 12 hours ago, something is different."

    "The car in the driveway is an old but well maintained Toyota. I could have sworn his dad had a BMW."

    "Something's amiss with the curtains as well. Weren’t they beige, not brown?"

    "I’m still shook up. There is something wrong with this reality."

    "Or maybe… maybe this is all just some kind of trip?"

    "I bet Max will be inside, laughing his arse off and dying to reveal what he slipped me last night."

    "Drugs are easy enough to get at my school, and Max has the money - and gall - to pull a stunt like that."

    "He's told me countless times before that I'm too much of a straight arrow and need to lighten up."

    "‘One of these days I’ll break you out of that boy-scout shell. It’s my personal mission’ is what he used to say."

    "Maybe he decided to get a little heavier-handed in his methods."

    "If that’s what happened, I’m going to wring his neck."

    "Then again, after the last 24 hours, I think I would prefer a bad acid trip to warping through realities."

    "…or seeing that giant snake dream again."

    play sound "sounds/doug/act_1/doug_doorbell.ogg"

    "I walk across the soft grass and press the doorbell. It feels delightfully solid. I can faintly hear it ring inside."

    "The noise is somehow calming. The drug theory is making more and more sense."

    "I'm not going crazy after all."

    "Unknown" "Coming!"

    "It’s a voice I’ve not heard before. An old lady. Maybe he has a visitor?"

    "The door opens {nw}"

    play sound "sounds/doug/act_1/doug_door_open.ogg"

    extend " and I can see an old Asian woman in front of me."

    show bg max corridor changed
    with dissolve

    "Lady" "Can I help you?"

    doug "Um, yeah. Is Max in?"

    "I peer in behind the woman. Everything looks different from what I remember."

    "The stairway looks the same, but the furniture has all been changed."

    "Lady" "Max? I think you have the wrong house."

    doug "No, this is the right house. Max Dunbar has lived here for years."

    "Lady" "Well, now I know that you are wrong. This has been my home since it was built 13 years ago."

    "The nausea hits me again and I falter backwards."

    "She shakes her head before closing the door."

    show bg max house changed
    with dissolve

    play music "sounds/doug/act_1/bgm_best_friends.ogg"

    "I stumble away from the house. As I cross onto the footpath, I feel like I'm pushing through the air."

    "Like I'm walking through a wall of mud."

    "My memory clears, and I can see the ghostly snake devouring Max clearing in my mind's eye."

    "I take a deep breath of air and squeeze my eyes shut, forcing my memories to the fore."

    show mixedMemories with dissolve



    "My mind is at odds with itself; part of it is telling me Max was a dream."

    "That he never existed. The more I try to recall our childhood together, the harder it gets to remember him."

    "It’s like chasing a rainbow - no matter how fast you run towards it, it's always out of reach."

    show maxGhostSmug with dissolve

    $ renpy.sound.set_volume(0.6, 0, channel="sound")
    play sound "sounds/doug/act_1/doug_reversed.ogg" noloop

    "Doubt creeps into my consciousness."

    hide maxGhostSmug
    show maxGhostSmugBloody

    with dissolve

    $ renpy.sound.set_volume(1,5, channel="sound")
    "Maybe I’m crazy. Maybe I was the one that fed myself drugs, and Max is an illusion."

    hide maxGhostSmugBloody
    hide mixedMemories
    scene bg max house changed
    with vpunch

    stop music fadeout 10.0

    "No, that can’t be right. He’s real. I’m real. None of this world is real."

    "But I need to pull myself together. People are going to think that I’m crazy."

    "Running screaming from school will have that effect on your reputation."

    "I need to get my world under control, but it's spinning too fast - or maybe that's just my head."

    "Nothing makes sense and I feel exhausted. As much as I want to avoid a run-in with Mum right now, I decide the best option is to sneak home."

    "If I can rest for a little bit then maybe I can clear my head and sort out this mess in my mind."

    scene bg street daylight
    with dissolve

    "The walk home feels longer than it should be, and I could swear that I can smell traces of ozone."

    "A cold breeze blows down Max’s street, and I feel the chill against my skin."

    "The wind blows the smell from my nose before I can verify it."

    "By the time I get home I have almost convinced myself that this is reality, and that Max was the dream."

    stop music fadeout 7

    scene bg_doug_livingroom_daylight
    with dissolve

    "I quietly open the back door to the house. Dad should be at work by now, but it doesn't hurt to be careful."

    "Mum is likely asleep after her night shift. She doesn't usually get up until well after we finish school."

    natalia "I was wondering when you’d come back here."

    play music "sounds/doug/act_1/bgm_nat_theme_1_main.ogg" fadein 3.0

    show natalia upset closer
    with Dissolve(0.2)

    "Natalia is waiting for me at the kitchen table, negating the need for stealth."

    doug "How did you know I’d be here?"

    natalia "You ran screaming from school in some kind of drug fever. I knew you’d have to come back here eventually."

    "I sheepishly try to avoid her stare. She’s right, I went a little overboard this morning."

    doug "Sorry. I must have slept poorly or something."

    show natalia upset suspicious closer
    with Dissolve(0.2)

    natalia "That didn’t look like sleep to me. Are you using?"

    "I recoil physically at her accusation. But, from her point of view, it’s a reasonable conclusion."

    doug "No! I swear. I’m just a little messed up right now."

    doug "I think that I had some weird dream last night; that I saw some kind of attack."

    doug "But I'm ok now."

    show natalia sad closer
    with Dissolve(0.2)

    natalia "You’d better not be taking anything. I have to put up with enough crap from Dad and those junkies in school."

    natalia "You’re supposed to be the diamond in the rough here."

    "I tussle my little sister’s hair."

    show natalia sad smile
    with dissolve

    doug "You don’t need to worry about me. I’ve got too much going for me to fuck it up now."

    "I’m not totally convinced by that, but I do know that I can’t afford to lose focus now."

    "I can count the rest of my high school life in weeks; and I know just how behind I am on my studies."

    "If I want to end up at a half-decent university and get out of this backwater, I need to hit the books."

    "I fill my lungs and try to push the remnants of this dream from my head."

    "I need to forget fantasies of snakes and monsters. Focusing on some hard facts from a textbook should help with that."

    natalia "You’d better not. Oh, I brought your bag back. Told your roll call teacher that you had a fever."

    doug "Thanks."

    show natalia sad closer
    with dissolve

    natalia "You’re welcome. I’m going back to school now. Get your head together, ok?"

    doug "S-sure. Oh, Nat?"

    show natalia question closer
    with Dissolve(0.2)

    natalia "Hmmm?"

    doug "Don’t tell Mum, ok? She’ll flip out and send me for a bunch of tests or something…"

    show natalia upset pouting closer
    with Dissolve(0.2)

    natalia "You got it. But pull a stunt like this again and I’ll make you piss in a cup myself…"


    hide natalia
    with dissolve

    "Natalia picks up her school bag and heads out the door."

    "Talking to another person helps to calm my mind, and suddenly I feel tired."

    "Running around like a madman all morning has taken its toll."

    "But I need to study to clear my head. It’s not often that I’ll get a chance to have the house to myself."

    $ _history = False

    "I grab a glass of milk from the fridge, {nw}"

    play sound "sounds/doug/act_1/doug_fridge_close.ogg"

    $ _history = True

    "I grab a glass of milk from the fridge, {fast}slamming it shut before opening my school books on the kitchen table."

    "It’s much easier to study here than in my room with the piles of old cardboard boxes."

    "The small windows in that room simply don't provide enough ventilation. Too long in there and I'll give myself a headache."

    scene bg_doug_livingroom_sunset
    with dissolve

    "I become engrossed in my history book, and before I know it the white light streaming in through the windows has taken on an orange hue."

    stop music fadeout 2.0

    "I’d better shift back to my pitiful room before anyone gets home."


    jump dougActTwoSceneOne
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

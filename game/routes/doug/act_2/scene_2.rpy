label dougActTwoSceneTwo:

    $ stopAllAudioTracks()


    window show
    scene bg black
    with dissolve


    scene bg street dark

    $ resetTracksAudio(["ad_bg_1", "ad_bg_2", "ad_bg_3", "ad_bg_4"])

    play ad_fg_1 "sounds/doug/act_1/doug_ride_bike.ogg" loop
    $ renpy.music.set_volume(0.4,0,channel="music")
    play music "sounds/doug/act_1/bgm_serpent_ambient_swirl.ogg"

    "I pump my legs harder against the wind in my face. The blood surging through my body helps to clear my head."

    "Forget about wild dreams of serpents or stomach cramps."

    $ _history = False

    "Forget about Max and of epic fights in the night."

    $ _history = True

    "Just push, push, and push some more."



    "All these things work themselves out in the end. Just push through it and you'll work it out."

    "That's how I've dealt with everything else so far. Deal with what you have to, and filter out the rest."

    "But, then again, I've not dealt with something like this before."

    "Stop thinking! Push!"

    "I chastise myself for letting my mind wander, and I charge my legs for another sprint."

    "The school whizzes by on my left as I head towards the river."

    scene bg street2 night
    with dissolve

    "At this hour there are hardly any people in sight. I'm not sure what Mum was worried about; there aren't even any cars out."

    "I see someone walking a dog, but apart from that, nothing."

    "I turn right and continue parallel to the river, out towards the industrial areas."

    "The lighting is a little lower out here, but then again, there are fewer people."

    "And I need to go fast. As the road levels out I pedal with increased fervour."

    "My stomach cramps slightly. Maybe I'm pushing too hard."

    $ renpy.music.set_volume(1, 5, channel="music")

    play music "sounds/doug/act_1/bgm_ambient_2.ogg" fadein 10

    "I grit my teeth and continue forward, but the throbbing in my stomach grows with every rotation of the wheels until it develops into a full cramp."
    play ad_bg_1 "sounds/doug/act_1/doug_bike_skid.ogg" noloop


    stop ad_fg_1 fadeout 2.0

    "I slam on the brakes and the bike skids to a stop."

    "Ozone fills my nostrils."

    doug "What the hell…?"

    "I speak before I can stop myself."

    "No sooner have the words left my lips than the tightening in my stomach turns into a full knot,{nw}"

    play ad_bg_3 "sounds/doug/act_1/doug_bike_crash.ogg" noloop

    extend " and I let my bike fall to the ground."

    "There, across the road, I can see it."

    "The flickering rainbow of colours emanating from the windows of a nearby house."

    "Colours that I saw less than a day before - the light emitted from the body of the snake."

    play sound "sounds/doug/act_1/doug_dry_heave.ogg"

    "Vomit churns in my throat but I swallow it back down. I need to confront this beast now."

    "I need to know which of my memories is 'real'."
    $ renpy.sound.set_volume (0.6, 0, channel ="ad_bg_3")
    play ad_bg_3 "sounds/doug/act_1/doug_distorted_water.ogg" fadein 9.0

    play sound "sounds/doug/act_1/doug_door_bang_3.ogg"

    scene bg door

    "I rush to the front door and start to pound on it furiously, but there is no answer."

    doug "Let me in!"

    play sound "sounds/doug/act_1/doug_door_bang_3.ogg"

    "I must look like a madman, pounding on the door in this quiet street."

    "But the air here feels thick, like in the classroom this morning; like I'm stuck in some kind of bubble."

    "I try to look at the houses around me, but they shimmer in the distance as if far away on a hot day."

    play sound "<from 0.4>sounds/doug/act_1/doug_kick_door.ogg"

    play ad_bg_4 "sounds/doug/act_1/doug_serpent_low_left.ogg" loop fadein 2.0
    play music "sounds/doug/act_1/bgm_reality_bubble_glitch_3.ogg" loop fadeout 0.5 fadein 0.5
    "Madness possesses me and I kick{nw}"

    show bg door open
    with vpunch
    extend " in the door."

    "It gives way easily, as if it weren't completely solid; somehow it's not completely real."

    play sound "sounds/doug/act_1/doug_splish_splash.ogg" fadein 2.0
    $ renpy.sound.set_volume (0.6, 0, channel ="ad_bg_2")
    play ad_bg_1 "sounds/doug/act_1/doug_serpent_eating.ogg" noloop
    play ad_bg_4 "sounds/doug/act_1/doug_serpent_snarl.ogg" noloop

    "Inside the house, I can hear a sickening chewing and see the strobing flashes across the hallway."

    "I charge into the house, hoping that I can save whomever is in there, "


    $ renpy.music.set_volume (1, 3, channel ="music")

    play sound "sounds/doug/act_1/doug_serpent_short_scream.ogg" noloop
    window show
    show bg door open serpent
    with dissolve
    stop ad_bg_1
    extend "but before I can cross the threshold, the serpent appears at the end of the hall."

    play music "sounds/doug/act_1/bgm_reality_bubble_glitch_1.ogg" fadein 2 fadeout 2

    unknown "Get down!"

    "From behind me, I hear a girl's voice over the cacophony of the approaching serpent."

    "My legs don't wait for my brain; they curl up beneath me and before I can think I'm crouching on the floor."

    "A glass bottle sails over my head and shatters{nw}"
    show bg door open serpent bottle

    play sound "sounds/doug/act_1/doug_glass_breaks.ogg"

    extend " on the floor, spraying liquid everywhere."

    play sound "sounds/doug/act_1/doug_distorted_roar.ogg"
    queue sound "sounds/doug/act_1/serpent_angry_10.ogg"

    "The serpent retreats briefly before charging directly at us, exposing its infinite maw and the rows of teeth that line it."

    stop ad_bg_4 fadeout 0.2
    $ renpy.sound.set_volume (1, 0, channel ="ad_bg_2")

    play sound "sounds/doug/act_1/doug_serpent_roar.ogg" noloop

    show bg door open serpent scream

    "It lets out a scream like a wave crashing over my head, and I clasp my hands over my ears to block out the noise."

    unknown "Oh shit… Get out of there!"

    scene cg michelle bottle

    "By the doorway, I can see a small figure in silhouette beckoning me towards her, a glass bottle in her hand."

    "Instincts kick in and I dive through the door into the darkness of the residential street."

    "I feel the serpent behind me, but the silhouette hurls the bottle{nw}"

    play ad_bg_4 "sounds/doug/act_1/doug_glass_breaks.ogg" noloop
    play sound "sounds/doug/act_1/doug_serpent_scream.ogg"
    extend " over my head and it shatters above the serpent."

    "Momentum carries my roll across the lawn. As I tumble, I see the snake's body arch up and burrow into the floor."

    $ renpy.music.set_volume(0.6, 3, channel="ad_fg_1")
    stop sound fadeout 0.2
    stop ad_bg_1 fadeout 1
    stop ad_bg_2 fadeout 1
    stop ad_bg_3 fadeout 1
    stop ad_bg_4 fadeout 1
    play ad_fg_1 "sounds/doug/act_1/doug_nighttime_traffic.ogg" fadeout 1 fadein 1
    stop music fadeout 3

    "Like a switch, the sound of draining water is gone."

    "The noises of a suburban street return."

    "As does the panting of a girl out of breath."

    show bg door no-rush

    "I turn to see the house, but the light is now gone. The front door stands intact as if nothing ever happened."

    "I pick myself up from the ground, brushing blades of grass off my clothes."

    "I approach the front door, my hand running over the solid wood that I had shattered mere moments ago."

    "Like Max, someone died here. Eaten by a giant snake."

    "A lump starts to form in my throat, but then I feel a hand on my shoulder."

    unknown "So… Is this our new routine?"
    $ renpy.music.set_volume(0.7,0,channel="music")
    play music "sounds/doug/act_1/bgm_michelle_soft.ogg" fadein 3

    show bg street2 night
    with dissolve

    show michelle jacket side mischievous
    with Dissolve(0.2)

    $ _history = False

    doug "Who… who are you? And you saw it too?"

    $ _history = True



    $ showHiddenText (doug, "Hey, you're that girl from last night, right?{fast}{nw}")

    "The tension in my gut starts to subside, and I realize that if two of us saw the same thing then maybe I'm not going crazy."

    "Well, at least not in the 'Did I really just see a snake eat my friend?' crazy."

    unknown "Of course. But it reacted, right? To the turpentine?"

    doug "You mean that bottle? It seemed pretty pissed off…"

    $ _history = False

    show michelle jacket side grin
    with Dissolve(0.2)

    "The girl seems genuinely happy in an odd sort of way. She clenches her fist in a victorious pumping motion."

    "She seems familiar but I can't place her."

    $ _history = True

    $ showHiddenText ('',"Michelle seems genuinely happy in an odd sort of way. She clenches her fist in a victorious pumping motion.{fast}{nw}")

    doug "So you know what's going on here?"

    show michelle jacket side blank
    with Dissolve(0.2)

    $ _history = False

    "The girl stops her celebration for a second to look at me. She's wearing my school's uniform."

    $ _history = True

    $ showHiddenText ('',"Michelle stops her celebration for a second to look at me. She's wearing my school's uniform.{fast}{nw}")

    $ _history = False

    doug "Wait, you go to my school, right?"

    show michelle jacket front speaking
    with Dissolve(0.2)

    "The girl rolls her eyes."

    unknown "Yes, genius, I do. It's me, Michelle."

    show michelle jacket front
    with Dissolve(0.2)

    "I draw a blank. I might have seen this person in school, but she's somehow never registered in my brain."

    "She seems short and dirty, her uniform muddied and probably torn. It's hard to tell in the moonlight."

    doug "Er, sure. I'm Doug…"

    michelle "..."

    "She keeps staring at me..."

    "Did I say something wrong?"

    show michelle jacket front speaking
    with Dissolve(0.2)

    michelle "Are you serious? Do you honestly not know who I am?"

    show michelle jacket front surprised
    with Dissolve(0.2)

    michelle "Oh."

    $ _history = True

    michelle "You don't remember anything from last night."

    "It sounds less like a question and more like a realization."

    "Why would she know anything about last night?"

    show michelle jacket profile bitter
    with Dissolve(0.2)

    "Before I can open my mouth she waves her hand with a bitter smile."

    michelle "Haven't you heard of me? Everyone else has. I'm in your sister's class too, you know."

    doug "Oh, really...? No, wait! About last night... I remember some things. It's like I have two memories from last night."

    show michelle jacket profile lookaway


    $ _history = False
    doug "One where I stayed at home and fought with my dad, and another where that snake thing ate my friend. Where you--{nw}"

    $ _history = True

    $ showHiddenText (doug, "One where I stayed at home and fought with my dad, and èeÓĢğģĜűūƏ  ŧŤŦ Őōő GƏŤ Më oűt of hër geŦ mè őuŧ ōF HæRe--")

    michelle "Rainbow Serpent."

    doug "Excuse me?"

    michelle "It's called a Rainbow Serpent."

    michelle "..."

    "Why is she so upset right now? She seemed so friendly just a moment ago, now she won't even look me in the eye."

    "I don't get what her deal is."

    michelle "You really know nothing about all this, do you?"

    doug "'fraid not."

    "If she can help me understand what the hell is going on, I think I can stomach her attitude."

    michelle "Well, I can tell you two things. One, you're not crazy, and neither am I. And two, it's not going to come back to this house."

    show michelle jacket profile bitter
    with Dissolve(0.2)

    michelle "And actually: three, you owe me a hot drink. Hm, two by now if I'm keeping score."

    doug "What for?"

    show michelle jacket profile upset
    with Dissolve(0.2)

    michelle "For saving your arse.{w} Twice."

    "The last word is icy cold."

    doug "What?"

    show michelle jacket profile lookaway
    with Dissolve(0.2)

    michelle "Nevermind..."

    $ _history = False

    "She sighs deeply, clearly disappointed in me. I only wish I could know why..."

    "She saved me now, kind of. Did she do the same yesterday?"

    "But no matter how much I strain my brain to remember nothing comes up, her face didn't awaken any memories either."

    "If the memories about the monster are true, how did I get back home last night...?"

    $ _history = True

    $ showHiddenText ('',"Of course - she must have been the one that dragged me home last night...{fast}{nw}")

    michelle "There's a diner near here. Buy me a coffee and I'll call it even."

    doug "S-sure."

    "I collect my bike and push it as I walk alongside Michelle."

    show bg street dark blur
    show michelle jacket side lookaway closeup at right
    with Dissolve(0.2)

    doug "Rainbow Serpent, you say?"

    michelle "Yes, Rainbow Serpent. You've heard of it, right? Or do you sleep through history class?"

    doug "I thought it was some kind of Aboriginal legend?"

    michelle "Bingo."

    doug "But didn't it create the rivers and the land and then die or something?"

    show michelle jacket side upset closeup at right
    with Dissolve(0.2)

    michelle "Did that look dead to you?"

    doug "I guess not."

    show michelle jacket side lookaway closeup at right
    with Dissolve(0.2)

    stop music fadeout 5.0

    "Michelle's stand-offish nature rubs against me, so I decide to keep my mouth shut."

    "Before long the yellow glow of the fast food restaurant fills the road ahead, and we shuffle into the warm eatery."
    scene bg black
    with fade
    stop ad_fg_1 fadeout 2.0
    $ resetTracksAudio(["ad_bg_1", "ad_bg_2", "ad_bg_3", "ad_bg_4", "music", "ad_fg_1"])


    jump dougActTwoSceneThree
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

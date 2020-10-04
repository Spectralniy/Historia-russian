label dougActFourSceneTwo:

    $ stopAllAudioTracks()


    window show
    scene bg black
    with dissolve


    scene bg doug bedroom wiki on

    "I sit in my room, staring blankly at my text books."

    "Polynomials simply don't seem real to me anymore."

    "A mythological creature is suddenly taking up more of my head space than the real world in front of me."

    "Any other day and I'd assume that I was high or something."

    "But this is real. {w}Too real."

    "Weeum's reading has brought clarity to my memories, and I can clearly see the wash of the serpent's colours blitzing across my mind."

    "And those teeth… infinite rows of teeth to drag its victims down into the gulf of its belly."

    "It terrifies me. Part of me wishes that it ate me as well on that fateful night so that I wouldn't have to think about it."

    $ _history = False
    doug "Pull yourself together."
    $ _history = True

    $ showHiddenText (friendMax, "Pull yourself together.{fast}{nw}")

    "I guess, in a way, I'm a 'chosen one' now."

    "There's no backing away from that. This snake could devour everyone in this city and no-one would be the wiser."

    "I can't let that happen."

    "The thing is clearly alive. It has some form of purpose."

    "If we can't kill it, we can probably limit the damage."

    "Maybe chase it out of town?"

    play sound "sounds/doug/act_1/doug_computer_clicking.ogg" fadein 1.0 loop

    "I need to learn more about it."

    "There's nothing helpful on the net. The Dreamtime stories are just that… stories. Legends."

    "Centuries of mistranslations and interpretations have left them as nothing but fables."

    "Tall tales of creatures crawling across the land, carving rivers into existence and turning themselves into islands when they die."

    "And the Rainbow Serpent is one of the most widely spread legends of them all."

    "I try looking for Weeums 'Dirawong' but there is even less there."

    "A Goanna that fought the serpent and got bitten."

    "Hardly helpful. That worm barely even has a head to speak of. Only those red eyes and limitless teeth."

    stop sound

    show bg doug bedroom
    with dissolve

    play sound "sounds/doug/act_1/doug_unplug_pc.ogg" noloop

    "I shut down the computer in disgust."

    "I'm not going to be finding any answers on Wikipedia."

    "If we want to defeat this beast, we're going to need to do it ourselves."

    "Michelle has been chasing this thing for years. Maybe she has more up her sleeve."

    "But, then again, she seems a little unstable. A little untrustworthy."

    "Sometimes I get the sense that she's got some kind of ulterior motive for hanging around me."

    "That killing the serpent is secondary to some other agenda."

    "Never mind. I have my mission. I need to stop the serpent for good. Do whatever it takes to make sure that it doesn't erase everyone in this town from history."

    "…or the world. What if this beast was the beginning of the end of humanity? Could it eat its way through to the last human?"

    "I shudder at the thought of a lifeless world, spinning through the universe without a trace of humans ever existing."

    "Not even ruins to show that we were once here."

    play ad_bg_1 "sounds/doug/act_1/doug_phone_vibrate_4.ogg" noloop

    "My phone vibrates, startling me a little. It's time."

    play sound "sounds/doug/act_1/doug_door_lock.ogg" noloop

    "9:45. I don't want Michelle knocking on my door, so I lock the door to my bedroom and creep out the window."

    scene bg street dark
    with dissolve

    play music "sounds/doug/act_1/doug_nighttime_traffic.ogg"

    "The sun has set, and I can feel the spring air already cool around me."

    "Not quite cold enough to warrant a jacket, but enough to be slightly uncomfortable."

    "I sit under my window sill, watching the street for an approaching girl."

    "My mind starts to wander again; but this time, it's about school."

    "I never really skipped out on school before. I thought the world would fall down around me, but I guess they don't care."

    "Our learning is our own responsibility. That's what they say at least."

    "Teachers seem happy to put effort into the kids that want to learn. They save their energy on those that don't."

    "I check my phone. Michelle's late. I didn't expect that of her."

    "It's not until 10:10 that I see a shadow shuffling around the corner of my vision."

    "In the dark of night, I finally see Michelle, a large bundle slung over her shoulder."

    show michelle jacket front
    with dissolve

    "She looks like she's struggling. I don't want her causing a scene near my house, so I rush towards her."

    doug "What have you got there?"

    show michelle jacket front speaking
    with dissolve

    michelle "Nothing. Supplies. It doesn't matter."

    "I smell turpentine and kerosene on her."

    michelle "Can we get going?"

    doug "I was thinking that we needed to cover more ground, so I took these."

    "I proudly hold up my dad's car keys."

    show michelle jacket surprised
    with dissolve

    doug "If we want to be able to catch this beast, we need to move fast. What do you think?"

    "Michelle looks ecstatic."

    michelle "You… you can drive?"

    doug "Kind of, I guess."

    doug "But does that matter? What's more important, following the rules or catching this fucker?"

    show michelle jacket side grin
    with dissolve

    "Michelle purses her lips and nods in approval."

    michelle "Good. This is good. Let's do it."

    hide michelle with dissolve

    $ renpy.music.set_volume(0.5,2.0,channel="music")

    show bg car inside with dissolve

    play sound "sounds/doug/act_1/doug_drop_bag.ogg" noloop

    "I quietly enter the car as Michelle loads her bulky supplies into the boot. I hear sloshing and clanking, but I don't risk asking her about it again."

    "So long as the car doesn't stink when I put it back tonight."

    "I have only had a couple of practice drives with mum, but I think I had the hang of it."

    "And the roads are mostly empty at this time of night."

    "So long as we don't get pulled over we should be ok."

    "Michelle, finshed fiddling at the back of the car, takes her seat and closes the door."

    play sound "<from 9>sounds/doug/act_1/doug_car_door_close.ogg" noloop

    show michelle jacket side lookaway closeup flipped at left
    with dissolve

    doug "I was thinking that we could go to the top of that hill near the river and keep an eye out."

    doug "Then if we see anything we can speed there. Sound good?"

    "Michelle is still excited."

    show michelle jacket side lookaway smile closeup flipped
    with dissolve

    michelle "Sure! Beats walking."

    "I wonder if this little bit of larceny will let her keep her tattered uniform from getting any worse."

    "I'm not sure why I care about that, but for some reason I do."

    "I think Natalia is overreacting. Michelle has been through a lot in her life. Of course she seems withdrawn and weird."

    "Anyone who's suffered that kind of trauma at such a young age is bound to have some kind of mental issue."

    "But if we at least succeed in subduing the serpent, maybe she'll be able to get some kind of closure."

    "Be able to break free of the shadow that has been cast over her life."

    "Just as it has mine."

    "In the end, I really do feel connected to her in a way."

    doug "Right then, let's go."

    play sound "sounds/doug/act_1/doug_car_start_slow.mp3"

    "I fearfully turn the key and shudder as the ignition starts the engine."

    "I really hope that dad doesn't notice. He would be furious."

    "Nothing ventured, nothing gained, right?"

    "I ease on the accelerator and the car lurches out of the driveway and onto the road."
    with vpunch

    show michelle jacket side mocking closeup flipped
    with dissolve

    michelle "You sure you know how to drive this thing?"

    doug "Yeah… yeah. I'll be fine."

    show michelle jacket side lookaway smile closeup flipped
    with dissolve

    "I nurse the car along the empty streets towards a small hill overlooking the houses lined up along the river."

    "When I was young there was a big flood every other year, but then the government strengthened the dam upstream."

    "Since then there haven't been any major floods. They had to release some water from time to time, but it seemed to be under control."

    "As the danger subsided, people started building closer and closer to the river."

    play sound "<from 10>sounds/doug/act_1/doug_car_drive_stop.mp3" fadeout 0.5 fadein 0.5

    "New developments popped up to support the town's growing population. Rows and rows of identical kit homes."

    "A few of my friends from school lived in them. The houses always smelt new. Like new car smell: house edition."

    "I wonder if you can buy it in shops."


    scene bg lookout night with fade

    show michelle jacket front surprised closer
    with dissolve

    michelle "Oh, you really can see most places from up here."

    "Michelle peers through the windshield as I park the car on the side of the street and shut down the engine."

    michelle "How long do you think it would take us to get to those houses if we saw it?"

    doug "I dunno. Maybe a couple of minutes? I've never driven from here to there before."

    michelle "Hmmm…"

    "Michelle seems to sigh a little."

    doug "Well, how did you patrol in the past?"

    show michelle jacket front speaking closer
    with dissolve

    michelle "I had a route. I'd leave home and then walk around the town."

    michelle "And if I saw anything I'd chase it down."

    doug "Did that work?"

    show michelle jacket profile bitter closer
    with dissolve

    michelle "I guess… not. Then again, I found you, didn't I?"

    doug "I suppose you did."

    show michelle jacket profile lookaway closer
    with dissolve

    "Does she mean the last time we saw the serpent? Somehow, I feel like that's not the case."

    "Maybe because I can't figure out the meaning behind that sad note in her voice."

    "I shake my head slightly. It's not that important."

    doug "We need to get more systematic. If we want to work out the serpent's motive we need to know where it is attacking, and why."

    doug "If we don't know who it is attacking that will be harder."

    show michelle jacket profile upset closer
    with dissolve

    michelle "You're right. But how do we do that?"

    doug "Not sure. Maybe we need to start marking the attacked houses on a map? See if they line up?"

    "Michelle reaches into her pocket and pulls out her phone."

    show michelle jacket front surprised closer
    with dissolve

    michelle "You mean like this?"

    "She shows me a map app with three pins on it."

    michelle "I thought about that, but I can't see anything, can you?"

    "She's right. I was hoping they would line up or something, but with only three points it's a little hard to work anything out."

    doug "I guess we need to wait until we get a few more points."

    "As much as I hate the thought, perhaps another attack would help us unravel the mystery a little further."

    michelle "Any other ideas?"

    "Michelle seems genuinely interested in hearing my thoughts."

    doug "None for now, sorry."

    doug "I tried looking up the stuff that Weeum was saying, but it's all pretty vague."

    doug "Each tribe seemed to have its own version of the Rainbow Serpent story."

    doug "But none of them seemed… real."

    doug "You know when you hear a legend that was at least partially true, you can kind of tell?"

    doug "Like stuff around solar eclipses or floods or comets."

    doug "But the Rainbow Serpent almost always seems like some kind of pure fantasy, like the Greek gods."

    show michelle jacket profile bitter closer
    with dissolve

    michelle "I think I know what you mean."

    doug "So I really have no idea why this beast is here now, for real."

    michelle "Maybe it's always been here?"

    doug "Huh? But then we would have heard of it, right?"

    "Michelle rolls her eyes."

    michelle "The serpent deletes you from history. Totally. So if it ate everyone in this town…"

    doug "…then no-one would ever know."

    show michelle jacket profile lookaway closer
    with dissolve

    "Realisation hits me like a freight train."

    "Maybe this town is just the most recent in a never-ending loop of towns that were settled, devoured, and forgotten."

    "And no-one would ever be the wiser."

    "This mythical beast could have been here all along."

    doug "But then why would it allow the town to get this big?"

    michelle "I dunno. Maybe it needs to eat a lot?"

    doug "You said you've been patrolling for what, 5 years? And it never attacked in that time?"

    doug "And now twice in one week?"

    "My mind spins as I try to find the pattern that I know is hidden out there somewhere."



    show michelle jacket profile bitter closer
    with dissolve

    michelle "Well, it's not like I could have covered the whole town every night."

    michelle "I might have missed it."

    show michelle jacket profile upset closer
    with dissolve

    michelle "Besides, I don't see you doing anything much."

    "She looks genuinely upset, as if I've insulted her. I reach across the car and put a hand on her shoulder."

    doug "I didn't mean it like that. Only that if it was waiting for enough people to feed on, why did it only attack once and then wait 5 years?"

    show michelle jacket profile lookaway closer
    with dissolve

    "Michelle's mood lightens only a little, but at least she calms down."

    michelle "Maybe you're right."

    "Her gaze lingers on me for a moment before returning to scanning the town before us."

    "I decide to leave the harder questions about Rainbow Serpents for the moment, and join her survey of the scenery."

    "We sit in silence for some time before Michelle's quiet voice startles me slightly."

    michelle "I think I remember him, you know?"

    "I look at her expectantly, frowning. She shots me a nervous glance but quickly turns back to the windshield."

    "She couldn't have meant…"

    $ _history = False
    michelle "Max."

    $ _history = True

    $ showHiddenText(michelle, "ƞĀŦ")

    $ showHiddenText(friendMax, "Woah... where is this coming from?{fast}{nw}")

    "I suddenly feel so happy. As if he came back to life with those words."

    "The serpent has failed, he has not been erased. Someone else remembered him as well."

    doug "But… How come? He knew Nat but I don't think he hung out with anyone else from her class."

    show michelle jacket mocking closer
    with dissolve

    "Michelle lets out a short laugh."

    michelle "He hit on your sister, didn't he!"

    "My mouth opens and closes without a word but I can't help but smile."

    "Michelle chuckles again and continues talking. She must have noticed that I want to know more. That talking about Max puts me in this weird mood."

    "Fresh grief mixed with relief."

    michelle "If you only knew how many boys come over just to say hello to her. It's hillarious!"

    michelle "Anyhow… I didn't talk with Max much. We met in the library, he noticed that I was… well, I was writing something. Don't laugh, okay?"

    $ showHiddenText(friendMax, "Dude, she's lying.{fast}{nw}")

    show michelle jacket profile bitter closer
    with dissolve

    michelle "He pestered me about it and I let him read it…"

    michelle "At first he was being a dick but when he realized that I was getting seriously upset he changed his tone."

    michelle "He gave me some advice, told me which parts he liked. I guess he was trying to be nice to a weirdo sitting alone."

    $ showHiddenText(friendMax, "She's making this up!{fast}{nw}")

    "Michelle shrugs, finishing her story."

    doug "Ha!"

    show michelle jacket front smile closer
    with dissolve

    "I can't manage anything else through my tightening throat. "

    "He gave her some writing advice? Seems I had even more in common with Michelle than I thought."

    "The silly fan-fictions we wrote together… Were they still in that box behind my wardrobe? Or did they disappear with him?"

    show michelle jacket pleading closer
    with dissolve

    "Michelle awkwardly pats my back and I realize that I'm on the verge of tears, just sitting there, a painful smile plastered on my face."

    michelle "Sorry, maybe I shouldn't have brought him up."

    doug "No! No… It's just a weird feeling. But not a bad one."

    doug "I guess I'm glad that someone else remembers him too."

    $ showHiddenText(friendMax, "Don't let her play you!{fast}{nw}")

    show michelle jacket front determined closer
    with dissolve

    michelle "We'll avenge him, don't you worry."

    "Her battle mode is back on and she pats me for the last time, stronger."

    "I nod, returning the wicked smile. She certainly deserves it."

    "And I'm sure he wouldn't want anyone to get hurt either. I couldn't save him, but I could still prevent another disaster from happening."

    "Just as I feel my motivation growing Michelle lets out a yawn."

    doug "Heh, looks like we're out of luck tonight."

    show michelle jacket profile bitter closer
    with dissolve

    michelle "It's warm in the car, it makes me sleepy. But yeah… maybe you're right."

    play sound "sounds/doug/act_1/doug_car_start_fast.mp3"

    hide michelle with dissolve

    show bg car inside with dissolve

    "I fire up the car again, the engine loud in the still of night."

    "An uneventful patrol. But at least that means no-one had to die tonight."

    doug "Tomorrow maybe we should bring a laptop so we can look up anything that's changed in the last few years."

    show michelle jacket side lookaway closeup flipped at left
    with dissolve

    michelle "Sounds good."

    doug "Do you want me to drop you off at your place?"

    show michelle jacket side surprised flipped closeup
    with dissolve

    michelle "N-nah. That's ok. Your place is fine. I'll walk from there."

    doug "Ok. Suit yourself."

    michelle "But can you look after my stuff?"

    "I'd almost forgotten about the bulky bag in the back of the car."

    doug "Sure. I'll put it in the shed."

    show michelle jacket side lookaway smile closeup flipped
    with dissolve

    michelle "Great."

    "I pull the car gently into the parking space in front of our house. Hopefully no-one will notice that I couldn't line it up too well."

    stop sound fadeout 3.0

    show michelle jacket side closeup flipped with dissolve

    michelle "Same time tomorrow?"

    doug "Sure."

    show michelle jacket side lookaway smile2 closeup flipped with dissolve

    "Michelle flashes me a smile,{nw}"

    extend " then jogs off into the darkness of the street, leaving me to hide her 'equipment'."

    hide michelle
    with dissolve

    "I take a peek inside the sack, but all I can see is a collection of pipes and bottles."

    "I'm sure it makes sense to her."

    "I stash the sack in our garden shed, then slip back in through my bedroom window before tumbling into bed."

    $ renpy.music.set_volume(1, 3.0, channel="music")
    stop music fadeout 1.5


    jump dougActFourSceneThree
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

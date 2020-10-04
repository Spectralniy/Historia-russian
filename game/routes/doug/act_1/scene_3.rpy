label dougActOneSceneThree:

    $ stopAllAudioTracks()


    window show
    scene bg black
    with dissolve


    window show
    scene bg_doug_room_sunlight
    with dissolve

    "The morning sun breaks through my window, rousing me before my alarm."


    $ renpy.sound.set_volume (0.7, 0, channel="ad_bg_1")
    play ad_bg_1 "sounds/doug/act_1/bird_song_cheerful.ogg"
    play music "sounds/doug/act_1/bgm_birdsong.ogg"

    "I check my phone, noting that it's only 15 minutes before my alarm was due to sound anyway."

    "To be robbed of those precious last moments of sleep irritates me for some reason, but I know that I'm not going to be able to reclaim them."

    "It doesn't help that I can't put my finger on when I got to sleep last night. I remember tossing and turning in bed, complaining about not sleeping."

    "But that's it. I guess my temper flared too high and messed with my sleeping patterns."

    "I know that I must have gone to sleep at some point, but part of me doesn't believe it."

    "I'm just as tired as I was when I crawled into bed."

    "Such is the life of a high school boy, I guess."

    "After trying to force my eyes shut for five minutes, I realise the futility of it all and drag my sorry arse out of bed."

    "The house is silent. I must have been the first up. Mum is likely still passed out. She's been working long shifts recently."

    "Dad…"

    "His car is in the driveway, so he's here, but I honestly couldn't care right now."

    "He had no right to act the way he did last night."

    "Alcohol is no excuse to lose your mind in that kind of way."

    "In any case, I can't hear him around. Maybe he's still hung over and sleeping it off."

    "I pull on a uniform and head to the kitchen to fix myself some breakfast."

    scene bg doug kitchen sunset
    show cg nat cornflakes phone
    with dissolve

    stop music fadeout 5.0

    play music_2 "sounds/doug/act_1/bgm_nat_theme_1_main.ogg" fadein 2.0
    play ad_fg_1 "sounds/doug/act_1/bgm_nat_theme_1_guitar1.ogg"
    play ad_fg_2 "sounds/doug/act_1/bgm_nat_theme_1_guitar2.ogg"

    $ renpy.music.set_volume (0, 0, channel="ad_fg_1")
    $ renpy.music.set_volume (1, 2.0, channel="ad_fg_2")
    $ renpy.sound.set_volume (0.55, 2.0, channel="ad_bg_1")

    "To my surprise, Natalia is already quietly eating a bowl of cereal."

    show cg nat cornflakes question hair
    with dissolve

    natalia "Oh, morning, Doug. Did I wake you?"

    doug "Nah, you can blame the sun for that."

    show cg nat cornflakes smile2 hair
    with dissolve

    "I can see a flicker of relief rush across her."

    natalia "Oh, good. I just didn't want to disturb anyone after…"

    show cg nat cornflakes troubled hair
    with dissolve

    natalia " you know…"
    "I guess everyone is walking on eggshells this morning."

    doug "It's ok. So you thought you'd get out of here early?"

    show cg nat cornflakes unamused
    with dissolve

    natalia "Yeah, you could say that."

    natalia "Although I would think that you're the one that would want to sneak out."

    natalia "It's barely seven. Dad won't be up until half past - if you leave now you'll miss him…"

    "The thought had crossed my mind. It might be a lot easier to avoid Dad today."

    doug "I'll think about it."

    show cg nat cornflakes phone
    with dissolve

    play sound "sounds/doug/act_1/doug_pour_cereal.ogg"
    queue sound "sounds/doug/act_1/doug_eat_cereal.ogg" loop

    "I pour myself a bowl of cereal and sit opposite my sister."

    "I glance at my own uniform; clean but crumpled."

    "It's a far cry from the neat perfection of Natalia's."

    "I guess we have different priorities. No-one cares what a guy's clothes look like."

    "But girls seem to pay attention to different things."


    $ renpy.sound.set_volume (0.2, 0, channel ="ad_bg_2")
    play ad_bg_2 "sounds/doug/act_1/doug_serpent_low_left.ogg" noloop


    "We eat in silence, careful not to rouse the monster that ruined last night."

    show cg nat cornflakes advising
    with dissolve

    natalia "Look, it's not my place to tell you how to live your life, and Dad was clearly in the wrong…"

    doug "But…?"

    natalia "But you don't need to provoke him."

    natalia "Especially when he's drunk."

    "I feel a knot in my chest. She's probably right, but pride won't let me admit that."

    "She always was Dad's favourite; she doesn't know how hard he is on me."

    "I swallow hard to keep my stomach in check before answering."

    stop sound fadeout 2.0

    doug "I didn't provoke him! He just never listens to me."

    doug "I was only trying to explain myself."

    show cg nat cornflakes phone
    with dissolve

    natalia "That's exactly the point."

    natalia "You always have to 'win' - even when it's impossible."

    natalia "Do you think that he's going to listen to you when he's like that?"

    natalia "You're better off keeping your mouth shut. Then maybe we can be a family again."

    $ renpy.music.set_volume (0, 15.0, channel="music_2")
    $ renpy.music.set_volume (0, 15.0, channel="ad_fg_1")
    $ renpy.music.set_volume (0, 15.0, channel="ad_fg_2")
    play ad_bg_2 "sounds/doug/act_1/bgm_reality_bubble.ogg" fadein 10.0
    "I open my mouth to reply, but I pause for a second."

    "Replays of last night run through my mind as I process what she said."

    "Dad came home and accused me of wasting time on the computer."

    "I turned off the computer before he could check it."





    $ _history = False

    "He lost his mind and started trying to take the computer apart."

    $ _history = True
    $ showHiddenText('', "Hè lost his mind and starŧed tryinĢ to Ťake the computeŖ apart.{fast}{nw}")
    $ _history = False

    "I told him that I had an assignment due tomorrow."

    $ _history = True
    $ showHiddenText('', "I tōőd him that I hΔd an æssiğnment due ŦomoŖrow.{fast}{nw}")
    $ _history = False
    $ showHiddenText('', "Voices gōt louder.{fast}{nw}")
    $ _history = True
    $ showHiddenText('', "voiçes ğōt Łouder.{fast}{nw}")
    $ _history = False

    "Natalia tried to intervene, but upon seeing the maelstrom retreated into her room."

    $ _history = True
    $ showHiddenText('', "MaxΔŁia tried to intervene, but üÞøħ seeing the mælstrom, retreated into his room.{fast}{nw}")
    $ _history = False

    "Mum refused to be drawn into the conflict; her long shift had ended and she needed to wind down."

    $ _history = True
    $ showHiddenText('', "MΔX refused to be drawn into the conflict; his long shift had ended and she needed to wind down.{fast}{nw}")
    $ _history = False

    "So it was Dad and I yelling insults at each other until he stepped out of my room."

    $ _histoty = True
    $ showHiddenText('', "sÓ it was Dad and I, yƏlling insults at æch other until .I. crept őuŧ of my rŐōőm.{fast}{nw}")
    $ _history = False

    "I spotted my chance and barricaded my door."

    "Mum was finally moved to act when he went for an axe to break into my room."

    "But, by that point, I'd already slipped out through the window."

    "She laid into him before heading off to get some sleep."

    "If this weren't a regular occurrence, I'm sure that our neighbours would have called the police at that point."

    "I imagine that they're getting used to these escalating exchanges."

    $ _history = True

    "It's the same pattern every night."

    show cg nat cornflakes smile3 hair
    with dissolve

    "But I'm glad that I can count on my sister. She's practically my best friend."

    "I don't know what I'd do if she weren't around."

    doug "But what else am I supposed to do? Roll over and let him ruin my life?"

    show cg nat cornflakes sad
    with dissolve

    doug "I'm seventeen. Nearly eighteen. By this time next year I'll be in university."

    doug "But he treats me like I'm some five-year-old that needs to be told how to do everything."

    doug "Just because he's bigger than me doesn't make him right."

    doug "It's infuriating."

    "My hands start to tremble as the memories from last night tumble around my mind."

    show cg nat cornflakes smile4
    with dissolve

    natalia "But you do act like a child sometimes."

    natalia "What did you end up doing last night after he quieted down?"

    natalia "Did you study?"

    "She knows me too well. I try to avoid her piercing gaze but it's impossible."

    $ renpy.sound.set_volume (0, 4.0, channel="ad_bg_2")
    $ renpy.music.set_volume (1.0, 4.0, channel="music_2")
    $ renpy.music.set_volume (1.0, 4.0, channel="ad_fg_2")

    "Her voice is a calming influence on me, helping me see through the fog that lingers in my mind."

    "For some time now she's been able to tell exactly when I was lying."

    doug "Nah, I watched 'Hot Rod' in my room then tried to force myself to sleep."

    natalia "Maybe you do need someone to look out for you."

    show cg nat cornflakes smile3 hair
    with dissolve

    "I've always been close to my sister. Something about her just makes me want to look after her."

    "Like she's an innocent version of myself that I need to protect from the big, bad world."

    "But, recently, I've felt as if the tables have turned, and she's started looking out for me more than I have her."

    "She's certainly more level-headed than I am."

    "And she's able to make friends easily - something that has always vexed me."

    "I've never really had any friends, at least none that I would rely upon."

    "Maybe that is why she's a little more stable than myself; she always seems to have someone to talk to."

    show cg nat cornflakes phone
    with dissolve

    "Yet, I feel something tugging on the back of my mind; a dream half dreamed."

    "I shake off the feeling and shovel the remaining cereal into my mouth."

    doug "But I do have someone looking out for me. That's your job, right?"

    show cg nat cornflakes shocked
    with dissolve

    natalia "What are you saying? You're supposed to be the big brother here…"

    doug "Relax, I'm pulling your leg. I'll be fine. Only a couple more months and then I'm out of here."

    doug "You can come visit me if you'd like…"

    show cg nat cornflakes smile4
    with dissolve

    natalia "What, to a uni dorm? No thanks. I've seen your room. I can't imagine what it would be like if Mum didn't force you to clean up."

    doug "Don't tell me you're afraid of some dirty clothes?"

    natalia "If that was all I had to worry about finding in your room then I'd be ok with it."

    "I want to reply but I realise that I've backed myself into a corner."

    "I either incriminate myself or disgust my sister."

    "Or, more than likely, both."

    show cg nat cornflakes smile
    with dissolve

    "But the joshing has changed my mood a little. After being berated all night it's good to chat freely with a friend."

    $ renpy.sound.set_volume (1, 15.0, channel="ad_bg_2")
    $ renpy.sound.set_volume (0.2, 2.0, channel="ad_bg_1")

    stop music_2 fadeout 2.0
    stop ad_fg_1 fadeout 2.0
    stop ad_fg_2 fadeout 2.0

    show cg nat cornflakes shocked
    with dissolve

    play sound "sounds/doug/act_1/doug_cough_1.ogg"

    $ _history = False

    natalia "Are you all right?"

    $ _history = True
    $ showHiddenText(natalia, "Oh my god! Doug!{fast}{nw}")
    $ _history = False

    doug "Huh?"

    natalia "Oh, nothing. It looked like you were coughing… or something…?"

    $ _history = True
    $ showHiddenText('', "I look up from the pool of vomit on the table, my eyes apologising to my sister.{fast}{nw}")
    $ _history = False

    "My body is convulsing, and I don't realise it."

    "Like I'm trying to heave up some unknown poison from my gut."

    $ _history = True
    $ showHiddenText('', "However, it feels good to have this poison released from my gut.{fast}{nw}")

    show cg nat cornflakes worried
    with dissolve

    doug "Just some gas I guess…"

    "I didn't even register my body moving."

    natalia "Do you want me to get Mum to look at you? I can wake her…"

    doug "Nah, she'll panic like she always does."

    doug "I'll go for a walk and it will be all right."

    show cg nat cornflakes question
    with dissolve

    $ renpy.sound.set_volume (0.6, 0, channel="ad_bg_3")
    play ad_bg_3 "sounds/doug/act_1/doug_serpent_low_right.ogg" noloop

    natalia "Good idea. Best to leave before the dragon awakes…"



    show cg nat cornflakes smile
    with dissolve

    stop ad_bg_2 fadeout 5.0

    "I wave back at my sister as I walk out the door."

    $ renpy.sound.set_volume (0.7, 2.0, channel="ad_bg_1")
    $ renpy.sound.set_volume (1, 2.0, channel="ad_bg_3")
    scene bg street daylight
    with dissolve

    "I know that she's trying to make light of the situation, but it's not a great place for any of us right now."

    "Dad can't seem to leave work at work, so he's already stressed by the time he walks in the door."

    "Even when he's not drunk it's like sitting on a keg of gunpowder."

    "Mum has given up helping. She sees enough death and destruction at work; she tries to drown out our fights where she can."

    "So Nat and I have banded together to protect one another."

    "At least, I'd like to believe that."

    "I know that I have a share of the blame when it comes to the fights at home."

    "I can't stop myself. I know that I should shut up and let him blow off steam, but I can't."

    "Fighting back seems to be part of my nature."

    "I simply can't let him believe he's right when he's clearly in the wrong."

    "But it's not fair on Nat. Maybe I should pay more attention to her."

    "I stare at my feet as I shuffle along the road as if on autopilot."

    "I've walked to school a thousand times. My body knows where it is going."



    "Instead, I put my mind to deciphering last night's events."

    "What could I have said differently?"

    "What can I tell myself to prevent my reacting?"

    "A mental fuse that I can blow before flying off the handle?"

    "…"

    "It's pointless. No matter how many times I look through last night's events, I can't see myself reacting any differently."

    "I'm a sucker for a fight."

    "I guess people don't change."

    $ renpy.sound.set_volume (0.4, 3, channel="ad_bg_1")

    "If you put the same person in the same situation a hundred times, you'll get the same result a hundred times over."

    "It's far too early to show up at school, but I could go to a cafe somewhere and crack a textbook there I guess."

    $ renpy.sound.set_volume (0.65, 0, channel="ad_bg_3")

    play ad_bg_3 "sounds/doug/act_1/doug_heartbeat_58_bpm.ogg"

    "Something prompts me to look up, and I realise I am lost."

    scene bg max house changed
    with dissolve




    "I'm standing in front of an unfamiliar house; a two-story townhouse that seems to be an exact copy of the other houses on its street."

    "I know I've never seen it before, but I can't ignore the tingle of deja-vu coursing down my spine."

    "I'm drawn to this house somehow… but I don't know why."

    "I look down to my hand and see it shaking - just like it was at breakfast."

    "Looking at the house makes me feel like I want to vomit, so I turn my back to it and head towards school."

    "I barely make it ten steps before I feel an eruption in my gut charging for my mouth."

    play sound "sounds/doug/act_1/doug_vomit_2.ogg"

    "I have no chance to stop it, and I aim the stream of black bile into a nearby gutter."

    "The mass of vomit seems to crawl along the concrete like some kind of animal, seeking shelter in a nearby drain."

    "I turn back towards the house I've just left."



    "It appears hazy in my vision; out of focus."

    "Like when you try to take a photo without enough light."

    $ renpy.sound.set_volume (0.3 , 0, channel="ad_bg_2")

    play ad_bg_2 "sounds/doug/act_1/doug_serpent_low_right.ogg" noloop

    "Blurred."

    $ _history = False

    doug "Max…"

    $ _history = True

    "Max? Why have I heard that name before?"

    $ renpy.sound.set_volume (1 , 2, channel="ad_bg_2")
    $ showHiddenText(friendMax, "How could you forget me?{fast}")




    "And, more importantly, why am I saying it?"

    $ showHiddenText(friendMax, "We were best friends, man!{fast}")

    "I need a drink of water."

    "The spring heat is starting to get to me. I'm overtired and dehydrated."

    "I close my eyes and take some deep breaths, charging my lungs with oxygen, before pushing on back towards school."

    scene bg street daylight
    with dissolve



    "The unexpected detour has cost me some time, and as I approach the school I start to see other students meander in the same direction."

    "I pay them no mind. Regardless of opening hours, I need a coffee and a water to soothe my dried throat."

    stop ad_bg_1 fadeout 1.0

    $ renpy.sound.set_volume (1, 0, channel="ad_bg_1")

    scene bg cafeday
    with dissolve

    play ad_bg_3 "sounds/doug/act_1/doug_restaurant_quiet.ogg"

    "A latte and a cold bottle of water. I've blown most of the money I'm carrying for lunch, but I'll cross that bridge when I come to it."

    "I take alternating sips of the hot drink and cold water. I'm not sure why, but it helps to wash away the taste of the vomit."

    $ _history = False

    doug "Max… who is Max?"

    $ _history = True

    "I'm perplexed by this figment of a memory."

    "It's little more than a name, but there is some connection there."

    "I close my eyes and try to sort out my thoughts."




    "As the liquids mix in my stomach I can start to feel something deep within me."

    "Some kind of imbalance in the universe."

    "Like I'm missing some piece of me."

    "I try to breathe in deeply, but it feels as if I can't fill my lungs."

    "I over-extend myself, trying to get air into each branch of my chest, but it's no use."

    "I'm not exhausted yet I feel short of breath."

    "Like I'm drowning in thick air."

    "A memory is desperately clinging to the back of my mind. I try to shake it off, but I can't."

    "Eyes closed, I reach for my coffee…"

    play sound "sounds/doug/act_1/doug_spill_coffee.ogg"

    doug "Shit…"

    "Reflexes kick in and I shake the hot liquid off my hand."

    "I open my eyes to see the spilled coffee spread out like a brown wave across the table, drenching everything in its path."

    doug "Crap!"

    "A levee of napkins is quickly created to contain the disaster. Somehow I have emerged unscathed besides some slightly soiled hands."



    "I sweep up as much of the coffee as I can into a mountain of soaked tissue before heading to the bathroom to wash my hands."

    stop ad_bg_3 fadeout 2.0

    scene bg bathroom
    with dissolve

    "The stink in the bathroom is already sickening. Didn't they clean this last night?"

    "Or have the years of grease from the fast-food atmosphere simply made this place uninhabitable?"

    play ad_bg_2 "sounds/doug/act_1/doug_tap_running.ogg"

    "Never mind. I turn on the faucet and place my hands in the water."
    $ renpy.sound.set_volume (0.7, 0, channel ="ad_bg_2")

    play sound "sounds/doug/act_1/doug_zap.ogg"
    show bg bathroom
    with Pixellate(0.5,4)

    "Electricity arcs between my hands as they make contact with the stream,{nw}"
    play ad_bg_3 "sounds/doug/act_1/doug_michelle_car_bump.ogg" noloop
    extend " causing me to trip over myself."

    doug "What the…?"

    "Again I feel the urge to vomit;{nw} "

    play sound "sounds/doug/act_1/doug_vomit_1.ogg"

    extend "I barely drag myself to the filthy toilet before I lose control and discharge the coffee mix into the bowl."

    play sound "sounds/doug/act_1/doug_zap.ogg"
    show bg bathroom
    with Pixellate(0.5,4)

    "I feel a tear in my reality."

    "An unfamiliar face calls to me."
    $ _history = False
    show maxGhostSerious

    friendMax "Doug! {w=0.3}{nw}"

    hide maxGhostSerious

    doug "Max?"

    $ _history = True
    "The figment loses itself in the swirl of the toilet, beyond the reach of my senses."

    "My stomach pinches again, and the memories of sitting at home last night shudder and fade, like a bad recording on a security camera."

    doug "The fuck was that…"

    "So much for keeping myself clean. Grey-brown stains are smeared across the knees of my school pants, and flecks of black vomit litter my shirt."

    "But there is no time to change."

    "I need to get to school. Clear my head. Get over whatever fever-dream I'm having."

    "Part of me wants to go home and crawl into bed, but I'll never hear the end of it if I do."

    "The water is still pouring from the faucet into the sink. I want to splash my face but the shock from the first time scares me."

    stop ad_bg_2 fadeout 3.0

    "I shut off the tap and carefully leave the bathroom."

    "Guiltily I eye off the disaster zone of the coffee flood before bolting out the door of the cafe and into the school yard."

    "Someone will clean it up, I'm sure."

    "I mean, that's their job, right?"


    stop ad_bg_1 fadeout 3.0

    $ renpy.sound.set_volume (0.5, 0, channel ="ad_bg_1")
    $ renpy.sound.set_volume (1, 0, channel ="ad_bg_2")

    "Maybe it will be practice for them before they attempt to clean the bathroom."

    scene bg school playground
    with dissolve

    play ad_bg_1 "sounds/doug/act_1/doug_school_playground.ogg" fadein 1.0

    "The familiarity of the playground settles my mind and stomach."

    "Groups are huddled in their 'spots'. Sporty kids are kicking a ball around on the oval, the nerds are playing a game of chess under the shade of a tree…"

    "My friends are sitting around, joking and already eating their lunch."

    doug "Sup…"

    "The group nods roughly at me, paying no heed to my appearance before returning to their conversations about girls and cars."

    "Both things that none of them have any real experience with, but that doesn't prevent them posing as experts in their fields."

    "I must have eaten something funky last night. That is the only explanation."

    "Maybe this is some kind of drug trip?"

    "Did one of these guys slip me something without me noticing?"

    play sound "sounds/doug/act_1/school_bell.ogg"

    "Before I can ask, the bell rings and we shuffle towards roll call."


    $ renpy.sound.set_volume (0.2, 0, channel ="ad_bg_1")
    scene bg school classroom
    with dissolve

    "The schoolyard banter continues, drawing disgusted stares from some of the girls in the class, but we don't seem to mind."

    "However, as the teacher strides in we all settle down."

    stop ad_bg_1 fadeout 2.0

    teacher "All right, quiet up. Roll call time."

    $ renpy.sound.set_volume (0.2, 0, channel ="ad_bg_2")
    play ad_bg_1 "sounds/doug/act_1/doug_serpent_low_left.ogg" noloop

    teacher "Daisy?"

    teacher "Darrel?"

    teacher "Doug?"

    teacher "Edgar?"

    teacher "Edith?"

    teacher "Graham?"

    show classWavetx
    with Dissolve(3.0)
    play music "sounds/doug/act_1/doug_reality_bubble.ogg" fadein 5.0

    $ renpy.music.set_volume (0, 0, channel="ad_fg_1")
    $ renpy.music.set_volume (0, 0, channel="ad_fg_2")
    $ renpy.music.set_volume (0, 0, channel="ad_fg_3")

    play ad_fg_1 "sounds/doug/act_1/bgm_reality_bubble_glitch_1.ogg"
    play ad_fg_2 "sounds/doug/act_1/bgm_reality_bubble_glitch_2.ogg"
    play ad_fg_3 "sounds/doug/act_1/bgm_reality_bubble_glitch_3.ogg"

    $ renpy.music.set_volume (0, 0, channel="music")
    $ renpy.music.set_volume (1, 1, channel="music")
    $ renpy.music.set_volume (1, 0, channel="ad_fg_1")
    $ renpy.music.set_volume (0, 3, channel="ad_fg_1")

    $ showHiddenText(teacher, "Rebecca?")
    $ _history = False
    $ scrambledPhrase(teacher, "Max?", "Rebecca?", 'MaxŖßëĈca', 3)
    $ _history = True

    doug "Huh?"

    teacher "Quiet please Doug, you've had your turn."

    doug "No, what did you say?"
    $ showHiddenText(teacher, "Rebecca?")
    $ _history = False
    $ scrambledPhrase(teacher, "Max", "Rebecca?", 'MaxŖßëĈca', 3)
    $ _history = True

    $ renpy.music.set_volume (0, 0, channel="music")
    $ renpy.music.set_volume (1, 2, channel="music")
    $ renpy.music.set_volume (0.75, 0, channel="ad_fg_2")
    $ renpy.music.set_volume (0, 3, channel="ad_fg_2")

    "The walls of the classroom flex in towards me, and again I feel as if I can't breathe."

    "I'm underwater, unable to fill my lungs."

    play ad_bg_2 "sounds/doug/act_1/doug_panting_loop.ogg" fadein 2.0 noloop

    "I need to escape."

    $ _history = False

    teacher "{alpha=0.5}Max?{/alpha} Are {nw}"

    $ scrambleWordInPhrase(teacher, "__DougMax__? Are you ok?")
    $ _history = True

    teacher "{alpha=0}Mæx? ΔrƏ űū ŐŐŐŐŐōőōőōő?{/alpha}{fast}{nw}"

    $ _history = False

    $ renpy.music.set_volume (0, 0, channel="music")
    $ renpy.music.set_volume (1, 2, channel="music")
    $ renpy.music.set_volume (0.75, 0, channel="ad_fg_3")
    $ renpy.music.set_volume (0, 3, channel="ad_fg_3")

    teacher "Doug? Are you ok?{fast}"



















    $ renpy.music.set_volume (0, 0, channel="music")
    $ renpy.music.set_volume (1, 2, channel="music")
    $ renpy.music.set_volume (0.75, 0, channel="ad_fg_1")
    $ renpy.music.set_volume (0, 3, channel="ad_fg_1")

    hide classWavetx
    show classWave

    $ showRapidPhrases(doug, [
        "Yeah{nw}",
        "{alpha=0.5}ĢeŦ {/alpha}{fast}{nw}",
        "Yeah I'm{fast}{nw}",
        "{alpha=0.5}Ĝëŧ Mæ oUt{/alpha}{fast}{nw}",
        "Yeah I'm fine.{fast}{nw}",
        "{alpha=0.5}geŦ mè őuŧ ōF HæRe{/alpha}{fast}{p=0.05}{nw}",
    ])

    $ _history = True

    friendMax "Ĝëŧ mƏ OuT ōF HeRë!{fast}{nw}"

    $ _history = False

    doug "Yeah I'm fine."

    $ _history = True

    "I can see the classroom's spinning fan pull the air along with it, slowly dissolving the ceiling and pulling it into an off-white swirl above me."

    teacher "{alpha=0.3}Max{/alpha} - Can you help Doug get to the nurse's office?{nw}"

    $ _history = False
    $ scrambleWordInPhrase(teacher, "__EdgarMax__ - Can you help Doug get to the nurse's office?")
    $ _history = True

    $ renpy.music.set_volume (0, 0, channel="music")
    $ renpy.music.set_volume (1, 2, channel="music")
    $ renpy.music.set_volume (0.75, 0, channel="ad_fg_3")
    $ renpy.music.set_volume (0, 3, channel="ad_fg_3")

    teacher "Edgar - Can you help Doug get to the nurse's office?{fast}"

    "Windows melt in the hot, hot sun that is beating down on me from above."

    "Its light dancing as it refracts through the liquid ceiling."

    doug "It's fine… I've gotta… I've gotta get Max…"

    $ _history = False

    teacher "Who is Max? {alpha=0.2}Max{/alpha} - please, help him lie down.{nw}"
    $ scrambleWordInPhrase(teacher, "Who is Max? __EdgarMax__ - please, help him lie down.")
    $ _history = True

    $ renpy.music.set_volume (0, 0, channel="music")
    $ renpy.music.set_volume (1, 2, channel="music")
    $ renpy.music.set_volume (0.75, 0, channel="ad_fg_1")
    $ renpy.music.set_volume (0, 3, channel="ad_fg_1")

    teacher "Who is Max? Edgar - please, help him lie down.{fast}"

    "A vague figure approaches me and places a hand on my shoulder."

    "Fire burns my insides and I recoil from his touch."

    doug "Don't touch me!"

    play sound "sounds/doug/act_1/doug_bump_desk.ogg"
    stop ad_bg_2 fadeout 3.0

    "I leap back, tripping over my desk."

    doug "I need to find Max… Now…"

    teacher "Edith - please go get the nurse. Now!"

    "I feel a presence slip past me, but it's hard to see through the thick air."

    "It reminds me of something buried deep in my mind - a repressed memory."

    "Fangs and rushing water tear at the edges of my mind, forever out of reach."

    "But at the end of my conscience I can sense its malevolent presence."

    "I need to get out of this space - this reality that is falling down around me."

    "The door's shape beckons to me, and I swim through the fluid space towards it."

    "Beyond it I can see the school's hallway, shimmering as if I were looking through a soapy bubble."

    doug "I'm not going to let you eat me!"

    "My voice echoes around the classroom, shifting in pitch as it bounces off the walls of this bubble."

    "With much effort I reach the door and tear myself through its membrane and into the clear air beyond."

    play music "sounds/doug/act_1/bgm_ambient_2.ogg" fadeout 1.0

    hide classWave
    scene bg school corridor
    with dissolve

    "My memory returns."

    "Behind me, reality snaps back into place and I see two dozen scared faces staring at me."

    "But there is no time to explain this to them."

    "How would they understand anyway?"

    "There is a monster on the loose, and there is a chance that Max is still out there, somewhere."

    "I can feel his presence calling to me."

    "The school's nurse rounds the corner of the hallway, a concerned look on his face."

    "My feet start to move automatically, carrying me away from the nurse and deeper into the school."

    play ad_bg_3 "sounds/doug/act_1/footsteps_1_walking.ogg"

    nurse "Doug, it's ok. I'm here to help you!"

    "His footsteps speed up as he tries to keep pace, but I know that I'm younger and faster."

    play ad_bg_4 "sounds/doug/act_1/footsteps_1_running.ogg"

    "I break into a sprint, running down the hallway."

    "I misjudge my speed and{nw}"

    play sound "sounds/doug/act_1/doug_michelle_car_bump.ogg" noloop

    extend " crash into a classroom door as I round a corner."

    scene bg school corridor flip
    with dissolve

    stop ad_bg_3 fadeout 0.2

    stop ad_bg_4 fadeout 0.2

    "The class beyond stares at me through the windows, and a worried face jumps out at me."

    show natalia shocked
    with dissolve

    "It's Nat, horrified to see the commotion that her brother is causing."

    "She jumps up and runs to the door before I can gather myself and run off."

    show natalia scared shouting
    with dissolve

    natalia "Doug! Are you ok? What's going on?!"

    doug "It's Max! He's gone! Some monster has him. I need to try and save him!"

    show natalia concerned reaching
    with dissolve

    natalia "Doug, what are you talking about? I think you need to lie down…"

    play sound "sounds/doug/act_1/doug_slap.ogg"
    show natalia concerned
    with dissolve

    "I slap away my sister's reassuring hand. If I don't get out of here soon, I'll be trapped here forever."

    "Escape is my only option, even if that means pissing Nat off."

    doug "Sorry, but this has to be done."


    show natalia worried
    with dissolve


    doug "The whole town is in danger…!"

    "Behind me the nurse has finally caught up."

    doug "Love you, sis!"

    play ad_bg_4 "sounds/doug/act_1/footsteps_1_running.ogg"

    "My legs pump as I run through Natalia's classroom and leap from an open window and out in to the playground."

    scene bg school playground
    with dissolve

    "The nurse peers his head out the ground floor window. It's not too far from the ground, but too high for him to jump."

    "I turn my back on the school building and sprint through the grassy playground and onto the street beyond."

    stop ad_bg_4 fadeout 4.0

    "Intersecting memories overlap in my mind, but I can now clearly see Max's house in my mind."

    "My body must have been taking me there this morning to check on him."

    "If only I weren't so stupid to realise that was what was going on."

    "It feels like I've been drugged and my memories replaced."

    "But it's more powerful than that."

    "Like Max was some creation of my mind that I forgot about."

    "A childhood memory that was forgotten, only to come rushing back with total clarity due to some random stimulus."

    "Like remembering a summer trip if you smell a certain scent, or a joke you were told over ice cream."

    "I can't be sure that it's real, but the only way for me to know for sure is to confront Max - or the monster - and find out."


    $ resetTracksAudio([
        "ad_fg_1", "ad_fg_2", "ad_fg_3", "ad_fg_4", "ad_fg_5", "ad_fg_6", "ad_fg_7", "ad_fg_8",
        "music",
        "ad_bg_1", "ad_bg_2","ad_bg_3","ad_bg_4", "ad_bg_5", "ad_bg_6", "ad_bg_7"
    ])

    jump dougActOneSceneFour
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

label dougActFourSceneFour:

    $ stopAllAudioTracks()


    window show



    scene bg lookout night
    with dissolve

    $ renpy.sound.set_volume(0.4, 0, channel="music")

    play music "sounds/doug/act_1/bgm_michelle_soft.ogg"

    show michelle jacket side lookaway closeup at right
    with dissolve

    "Sitting in the silence of the darkened car is uncomfortable, but somehow I feel that talking to Michelle would be even more so."

    "Natalia's impassioned pleas ring heavy in my ears."

    "Perhaps she's right, and Michelle is a dangerous person. But until the serpent is dead, she's my only ally."

    "After this is done, one way or the other, we'll part ways."

    "I'll go back to my studies, graduate, and find some nice university on the other side of the country."

    "Maybe get a night shift job to have some spending money."

    "Party away the memories of supernatural beings."

    $ _history = False

    "Sounds nice. {w}If it were true."

    "Deep inside me, I can see a future where I do nothing but fight this snake until I die."

    "Every night, charging into battle with an immortal enemy."

    "Until finally it gets the upper hand on me and I disappear from history."

    "It's a depressing thought. I sigh in frustration."

    show michelle jacket side upset closeup
    with dissolve

    $ _history = True

    michelle "You're not yawning, are you?"

    doug "What? No. Just thinking."

    michelle "About what?"

    doug "Nothing. {w}The future I guess."

    "Michelle's eyes narrow."

    $ _history = False

    michelle "There is no future whilst that thing is around."

    $ _history = True

    $ showHiddenText(michelle, "There is no past whilst that thing is around.{fast}{nw}")

    "In a way, she's right. The serpent is like a boulder sitting on the train track of my life."

    "Before we met, I was cruising along a pretty well-defined path."

    "Now, until it is cleared from the tracks, I'm going nowhere."

    doug "True that."

    show michelle jacket side lookaway closeup
    with dissolve

    "Silence descends upon us again, and our gazes stare out across this small patch of the town."

    "I can see the lights in the houses extinguish one by one as people tuck themselves into bed."

    "The subtle blue glow of TV sets in darkened rooms."

    "I think about the lives being lived in there. The kids in my class that are probably still awake, studying."

    "The elderly, already fast asleep."

    "How many couples are out there, before me, losing themselves in each other's bodies?"

    "And yet here we are, a couple of kids, watching over a town that doesn't even know it needs protecting."

    "Why couldn't this have happened to anyone else?"

    stop music fadeout 3.0

    play ad_fg_2 "sounds/doug/act_1/doug_reality_bubble.ogg" fadein 2.5 loop

    show michelle jacket side surprise closeup
    with dissolve

    michelle "There…!"

    $ renpy.sound.set_volume(1, 0.5, channel="music")

    "Michelle's shrill voice tears through the air."

    michelle "See it?!"

    "I squint through the windshield trying to follow her outstretched finger."

    doug "I… don't really… where?"

    michelle "Who cares if you can see it? Let's go!"

    play ad_bg_1 "sounds/doug/act_1/doug_car_start_drive_fast.ogg" noloop

    hide michelle with dissolve
    show bg car inside with dissolve

    "Michelle's orders run directly to my brain, and before I know it I'm turning over the ignition and driving mindlessly."

    doug "Where to?"

    show michelle jacket side surprised flipped closeup at left
    with dissolve

    michelle "Down by the river, near the parkway."

    michelle "Move it!"

    "I aim the car towards the town and head down the hill. Out of the corner of my eye, I think I catch what Michelle sees."

    "A spear of multi-coloured light bursting from the windows of a house."

    "Flashbacks of Max's house replay through my mind, but I force them from my consciousness."

    doug "I see it!"

    play sound "sounds/doug/act_1/doug_car_seatbelt_undone.ogg"

    "Michelle unclips her seatbelt and clambers into the back seat."

    hide michelle with moveoutleft



    doug "What are you doing?"

    michelle "Preparations! You drive, let me deal with this."

    "I see her slender frame reach over the back seat of the car in my rear-view mirror, but I can't see what she is doing."

    "All I can hear is her grunting and swearing under her breath, and the thick smell of kerosene."

    "It would appear she's graduated from turpentine."

    "Thankfully, the night-time streets are empty, allowing me to speed through the town towards the parkway."

    "Bile builds in my stomach and I taste ozone over the petrochemical smells Michelle is producing in the back of the car."

    "We're on the right track."

    play sound "<to 1.2>sounds/doug/act_1/doug_car_skid_only.ogg"
    queue sound "sounds/doug/act_1/doug_michelle_car_bump.ogg" noloop

    "I push through the sensation and take the turn into the parkway a little too fast."

    michelle "Watch it, idiot!"

    "Michelle curses as her body slams against the side of the car."

    doug "Sorry. I wanted to get there as fast as possible. Are you ready?"

    michelle "You bet I am."

    "The rising sensation in my gut reaches a crescendo as I see the house appear before me."

    "It's a three-story house, and the serpent's Technicolour aura is pouring from every window."

    michelle "Leave this to me!"
    stop ad_bg_1 fadeout 5

    play sound "sounds/doug/act_1/doug_car_door_open_fast.ogg"

    "Michelle tears open the car's rear door before I can even stop the vehicle."

    "She's carrying some contraption made of pipes and tubing, around which is a faint glow…"

    "You can't be serious…"

    play sound "sounds/doug/act_1/doug_car_handbrake_on.ogg"

    play ad_bg_2 "sounds/doug/act_1/doug_serpent_purring.ogg" loop

    "I rip up the car's handbrake and charge out after Michelle, but I'm too far behind her to stop."

    play ad_fg_2 "sounds/doug/act_1/bgm_serpent_pt2_master.ogg" fadeout 1.0 fadein 1.0 loop

    play ad_bg_1 "sounds/doug/act_1/doug_serpent_snarl_2.ogg" noloop

    scene bg black with dissolve

    "She has already entered the house. I feel myself enter the serpent's bubble, and time seems to freeze."



    "I plunge into the gut-wrenching blackness of the house. Whatever Michelle is carrying casts flickering orange shadows around the entranceway."

    scene cg michelle flamethrower with dissolve
    show flameThrowerNone with Dissolve (3)

    michelle "Come on out, motherfucker…"
    play sound "sounds/doug/act_1/doug_serpent_surprised.ogg"

    "Instantly, the hallway is filled with strobing, colourful light, and the serpent's head punches through the wall."

    hide flameThrowerNone
    show flameThrower with Dissolve(0.2)

    play sound "sounds/doug/act_1/doug_flamethrower_short.ogg"

    play ad_bg_1 "sounds/doug/act_1/doug_serpent_snarl.ogg" noloop

    "Michelle throws a lever on her contraption and a plume of fire and smoke erupts from her makeshift flame thrower."

    play sound "sounds/doug/act_1/doug_serpent_scream.ogg"

    "The bright orange light challenges the serpent's own glow for dominance in the small space."

    play ad_bg_4 "sounds/doug/act_1/doug_house_fire.ogg" fadein 7.0 loop
    play ad_bg_1 "sounds/doug/act_1/doug_serpent_roar.ogg" noloop

    "An ungodly sound tears through the house as the flames lick over the serpent's body, and it recoils through the wall from whence it came."

    play ad_bg_3 "sounds/doug/act_1/doug_smoke_alarm_weird.ogg"

    $ renpy.sound.set_volume(0.3, delay=0, channel='ad_bg_3')

    "Smoke alarms instantly add to the noise with their shrill cry."

    "Puddles of fuel, still flaming, line the hallway."

    stop sound fadeout 0.5
    stop ad_bg_2 fadeout 0.5

    "I can feel the effect of the serpent starting to slip away, like a bubble collapsing in on itself."

    play sound "sounds/doug/act_1/doug_flamethrower_long.ogg"

    michelle "Die!"

    show cg michelle flamethrower with Dissolve(0.4)
    hide flameThrower with Dissolve(0.4)
    show flameThrowerNone with Dissolve (0.5)

    "Michelle opens up her flamethrower again, drenching the hallway in flames and fuel."

    "But I know the serpent has already left, and history is re-writing itself as we speak."

    play ad_fg_2 "sounds/doug/act_1/bgm_fire_cello.ogg" fadeout 5.0

    doug "We need to go!"

    hide flameThrower with dissolve
    show flameThrowerNone

    michelle "Never! I'm going to kill this fucker tonight!"

    queue sound "sounds/doug/act_1/doug_flamethrower_three.ogg"
    queue sound "sounds/doug/act_1/doug_flamethrower_short.ogg"

    "The smell of ozone disappears and my stomach begins to settle, but still the flames begin to grow."

    play ad_bg_3 "sounds/doug/act_1/doug_smoke_alarm_normal.ogg" fadein 0.5

    "There is a subtle pitch in the tone of the fire alarms as the bubble finally collapses, leaving us alone in reality."

    doug "Michelle! It's gone!"

    doug "You're burning down the new house!"

    "I can't get through to her. I rush forward and feel the intense heat from the fire against my bare face."

    "The smell is awful; kerosene mixed with the nauseating smell of burnt hair and carpet. I gag at the combination of odours."

    "As I reach Michelle, the plume of flame seems to waver, shrink, and stop."

    "I grab her by the waist and pick up the girl, flamethrower and all, and drag her from the inferno."

    hide flameThrowerNone
    scene bg burning house with dissolve
    show michelle flamethrower shocked

    "The makeshift contraption is leaking fuel; we need to get out of here before we're both burned alive."

    "Michelle kicks and screams against me, and I can begin to hear noises from the outside world."

    "The reality bubble has collapsed… and the house is still on fire."

    "Bleating fire alarms are still screaming."

    "We have gone from demon hunters to arsonists. We need to leave."

    "I double down on my strength and drag Michelle from the house."
    scene bg street dark blur

    show michelle flamethrower furious
    with Dissolve (0.5)

    doug "I'm leaving, now! If we get caught we're both going to jail."

    doug "You coming or not?"

    "Michelle, her eyes narrow and furious, snarls at me."

    michelle "Why did you stop me?!"

    doug "It was gone! You're burning down a house now!"

    doug "What if there were still people in there?"

    michelle "Fuck them! Nothing matters but killing that snake."

    michelle "They can burn for all I care."

    doug "Nat was right…"

    show michelle flamethrower shocked talking
    with dissolve

    "I curse myself for speaking, but the words slip out of my mouth."

    michelle "{i}What did you say…?{/i}"

    "Michelle's stare freezes my heart in place. Veins bulge on her forehead and her mouth pulls back at the corners, revealing her teeth ever so slightly."

    show michelle flamethrower shocked
    with dissolve

    doug "Nothing. We {i}need{/i} to get out of here…"



    show michelle flamethrower shocked talking
    with dissolve

    michelle "We {i}need{/i} to kill that thing!"

    michelle "I thought I could trust you!"

    show michelle flamethrower shocked
    with dissolve

    doug "And I thought you would be a rational person!"

    doug "Someone is going to notice this fire soon, and we need to be gone before they do."

    doug "I'm leaving, are you coming?"

    "As much as I am terrified of Michelle's animalistic expression, what we have done here is a crime."

    "In the real world."

    stop ad_bg_3 fadeout 5.0

    "There is no history-erasing here that will shield us from the consequences of burning down a house."

    "Michelle stares at me, her breathing fast and shallow. I see her nostrils flaring and chest rising in time."

    show michelle flamethrower furious
    with dissolve

    michelle "What would Max say to all this, huh?! You no longer want to avenge him?"

    $ showHiddenText(friendMax, "Not like this...{fast}{nw}")

    "I grit my teeth as she mentions Max's name. Of course I do. He was my best friend. But I doubt he'd want me to burn somebody's house in the process."

    doug "The serpent is gone!"

    doug "Just get out of here. We should talk about this tomorrow."

    show michelle flamethrower shocked
    with dissolve

    "I leave the furious girl on the lawn of the glowing house."

    "Black smoke is starting to billow out of the windows. It will only be a moment before someone looks outside and sees it."


    stop ad_bg_4 fadeout 10.0

    stop music fadeout 5

    "If they get my number plate, then I'm a dead man."

    play sound "sounds/doug/act_1/doug_car_start_drive_fast.ogg"

    hide michelle with dissolve
    show bg car inside with dissolve

    "The key slides into the ignition and the engine cranks itself into life."

    "Michelle's terrible stare never once leaves me as I pull away."

    "She needs to get out of there. If anyone sees her with that makeshift flamethrower, she'll have no excuse."

    "I only hope that she is sane enough to run from the scene of the crime."

    "Stopping the serpent is priority number one."

    "But that is impossible from within a jail cell."

    "And if the only way to stop it from killing people is to sacrifice innocent people, then what is the point?"

    "But my voice won't reach Michelle now. She's well beyond reason. When she calms down we can think about discussing it again."

    "As I drive away, I can see the yellow-orange glow of the burning house start to stain the sky in my rear-view mirror."

    "Part of me secretly hopes that Michelle didn't make it away in time, that she gets caught and somehow doesn't implicate me in the process."

    "Fighting the serpent alone doesn't really appeal to me, but if Michelle acts like this forever, it will be impossible."

    stop sound fadeout 3
    $ renpy.sound.set_volume(1, delay=0, channel='ad_bg_3')
    stop ad_fg_2 fadeout 2

    jump dougActFiveSceneOne
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

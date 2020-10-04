label dougActFiveSceneFive:

    $ stopAllAudioTracks()


    window show
    scene bg black
    with dissolve


    scene bg lookout night with dissolve
    show michelle jacket side lookaway closeup at right with dissolve



    play music "sounds/doug/act_1/bgm_lazy_afternoon_corrupt_no_drums.ogg"

    "The town below me has never looked so uninviting."

    "Michelle is sitting silently on the car's hood, her 'equipment' weighing heavy in the car's boot."

    "Every now and again a tear starts to roll from my eye. I pretend that I have allergies so as not to tip off Michelle."

    "The last thing I want is her sympathy…"

    "…or pity."

    "That's of course under an assumption that she's even capable of such feelings, which I doubt."

    "It became painfully clear that Michelle's completely stuck. She won't move on unless the Serpent is dead."

    "That suits me just fine right now. There's nothing else I want or need."

    "We're going to find this monster and stop it. Somehow, we'll stop it."

    show michelle jacket side surprise closeup with dissolve

    michelle "There!"


    "Michelle's shrill voice pierces the blanket of silence."

    play sound "sounds/doug/act_1/doug_car_start_drive_fast.ogg"

    "I follow her outstretched finger and see the Serpent's aura streaming out of a nearby house."

    hide michelle
    show bg car inside river street
    with dissolve

    "My only reply is to fire up the engine and speed towards the light as Michelle leaps into the passenger's seat."

    show michelle jacket side lookaway smile closeup flipped at left with moveinleft

    "I've thrown caution to the wind."

    "If we get pulled over, then the flamethrower in the boot is enough to implicate us both."

    "If we crash then I'm going to sit here until I burn."

    "That would be a fitting end to all of this."

    show maxGhostSerious with dissolve

    $ _history = False

    friendMax "Don't be so hard on yourself."

    "I ignore the phantom. I don't need Michelle getting involved in this."

    friendMax "After all - this is a monster that deletes people from history."

    friendMax "What kind of chance do you stand against something like that?"

    friendMax "One wrong move and - gulp! - everything you've ever done is unwound."

    friendMax "You're gone, forever. {w} Like you never existed."

    $ _history = True

    $ showHiddenText(friendMax, " Like you never existed.{fast}")

    play ad_bg_3 "sounds/doug/act_1/doug_car_skid_only.ogg" noloop

    show michelle jacket side surprised flipped closeup with hpunch
    "I swing the car to the side, and Michelle leans against her seatbelt."

    $ _history = False

    hide maxGhostSerious
    show maxGhostSmugBloody

    "Max, however, stays put, his head between the driver and passenger's seat, smug as ever."

    friendMax "I get it. I was only trying to help."

    hide maxGhostSmugBloody with Dissolve(2.0)

    "The phantom disappears, and once again there are only two of us in the car."

    $ _history = True

    "We round the last corner in the small residential street and are greeted by the flashing cornucopia of colours from the house in front of us."

    play ad_bg_2 "sounds/doug/act_1/doug_car_handbrake_on.ogg" noloop
    stop sound fadeout 0.5

    play ad_bg_3 "sounds/doug/act_1/doug_car_seatbelt_undone.ogg" noloop

    doug "Let's get this son of a bitch."

    stop music fadeout 2.0
    $ renpy.music.play("sounds/doug/act_1/bgm_serpent_flamehouse_pt1_master.ogg", channel='ad_fg_1', loop=True, fadeout=None, synchro_start = True, fadein = 1.5, tight=None, if_changed=False)
    $ renpy.music.play("sounds/doug/act_1/bgm_serpent_flamehouse_pt2_master.ogg", channel='ad_fg_2', loop=True, fadeout=None, synchro_start = True, fadein = 0.5, tight=None, if_changed=False)
    $ renpy.music.set_volume (1, 0, channel="ad_fg_1")
    $ renpy.music.set_volume (0, 0, channel="ad_fg_2")


    show michelle jacket side mocking closeup flipped

    michelle "You've got it - partner."

    play ad_bg_2 "sounds/doug/act_1/doug_car_door_open_fast.ogg" noloop

    hide michelle with moveoutleft

    "She leaps from the car and straps on her flamethrower, leaving a large satchel behind."

    play ad_bg_3 "sounds/doug/act_1/doug_car_slam_door.ogg"

    michelle "Take that with you!"

    doug "What's this?"

    michelle "Just bring it!"

    "Reluctantly I lift the sack from the car. I'm surprised she was even able to carry it."

    "It is incredibly heavy and smells of fuel."

    "No. There is no way I'm going to carry this to the house."

    play ad_bg_1 "sounds/doug/act_1/doug_drop_bomb.ogg" noloop

    "I leave the package on the kerb and chase after Michelle, who is already inside the serpent's bubble."

    play audio "sounds/doug/act_1/doug_flamethrower_short.ogg"
    play ad_bg_2 "sounds/doug/act_1/doug_hot_contact_boiling.ogg" noloop
    scene cg michelle flamethrower
    show flameThrower with Dissolve(3.0)
    play sound "sounds/doug/act_1/doug_serpent_2_snarl.ogg"
    queue sound "sounds/doug/act_1/doug_serpent_purring.ogg" loop

    "The orange blasts from her flamethrower partially drown out the softer blues and greens from the Serpent."

    "I rush inside to find Michelle even more unhinged than before."

    michelle "Did you bring the bomb?"

    doug "Bomb?"

    play ad_bg_3 "sounds/doug/act_1/doug_flamethrower_2_blasts.ogg" noloop

    michelle "The bomb! From the car!"

    doug "Are you insane? Haven't you done enough damage?"

    doug "You killed two people already with your stupid flamethrower!"

    michelle "Are you kidding me? I didn't think you were this weak."

    play ad_bg_3 "sounds/doug/act_1/doug_flamethrower_long.ogg" noloop
    play ad_bg_4 "sounds/doug/act_1/doug_hot_contact_boiling.ogg" noloop
    play ad_bg_1 "sounds/doug/act_1/doug_serpent_scream.ogg" noloop

    michelle "We won't get anywhere if you let your conscience stop you every single time!"

    michelle "You either give it your all and act or nothing changes! There's no room for hesitation, Doug!"

    "Her words make sense but I still can't take a risk that big. There's no point in killing that monster if we need to destroy the city while doing it."

    "But to Michelle this doesn't matter. For her, only the monster exists. Everyone else is simply an NPC in her grand crusade."

    "I just shake my head."

    michelle "That's why I saved you from the Serpent that first time! I saw a fighter! I thought that with you, we stood a chance!"

    play ad_bg_3 "sounds/doug/act_1/doug_flamethrower_three.ogg" noloop
    play ad_bg_1 "sounds/doug/act_1/doug_distorted_beat.ogg" loop

    "Michelle lets out some blasts from her weapon and the Serpent retreats through a wall, leaving me alone with her."

    michelle "I should have realized that time would dampen that passion."

    "No. What is she saying?"

    "It was Nat who nursed me after Max died. I remember that. I remember her worried face above my head."

    "My throat tightens again when I realize I can no longer ask her about it."

    "But, on the other hand, I don't even feel the need to."

    "I'm certain that Michelle is lying. She's trying to win me over with lies."

    doug "That's a lie. It was Nat who saved me that night. I remembered that, you won't fool me."

    scene bg burning house with dissolve

    play ad_bg_4 "sounds/doug/act_1/doug_house_fire.ogg" loop fadein 10

    show michelle flamethrower huh with dissolve

    "It came out like a hiss and Michelle opens her mouth, shocked."

    stop sound fadeout 2
    stop music fadeout 4

    play ad_bg_2 "sounds/doug/act_1/doug_heartbeat_90_bpm.ogg" loop



    show michelle flamethrower furious with dissolve

    michelle "Say WHAT?!"

    doug "You only wanted to use me, didn't you. You're incapable of feeling anything except the hate for that stupid monster. That's all you are."

    show michelle flamethrower shocked with dissolve

    doug "What else did you lie about? That story about your uncle and aunt, the lonesome patrols every night since then, was that a lie as well?"

    show michelle flamethrower shocked talking with dissolve

    michelle "I've never lied to you, dumbass!!!"

    $ _history = False

    doug "And the fact that you knew Max? That he helped you with your writing?"

    $ _history = True

    $ showHiddenText(doug,"And the fact that you knew Nat? That she helped you with your writing?{fast}{nw}")

    show michelle flamethrower huh
    with dissolve

    "Frenzied just a moment ago, Michelle freezes at those words."

    "So it was true. She did lie to me. Told me what I wanted to hear to pull me closer and then use me."

    $ _history = False

    doug "His hair. What color was it?"

    $ _history = True

    $ showHiddenText(doug, "Her birthday - when was it?{fast}{nw}")

    show michelle flamethrower furious with dissolve

    michelle "Are you nuts? I don't have time for a quiz!"

    $ _history = False

    doug "Is it so hard? It's just one word. You remember him, don't you? Spit it out!"

    show michelle flamethrower huh with dissolve

    $ _history = True

    $ showHiddenText(doug, "Is it so hard? It's one day. You remember her, don't you? Spit it out!{fast}{nw}")

    "I already know the truth."

    $ _history = False

    "She has no idea who Max even was."

    $ _history = True

    $ showHiddenText('',"She has no idea who Nat even was.{fast}{nw}")

    "Her nervousness now is obvious and painful to watch."

    "And as much as I hate to admit it, realizing that my only ally has became a traitor is excruciating."

    $ _history = False

    show michelle flamethrower furious with dissolve

    michelle "Fine! Black! It was black!"

    $ _history = True

    $ showHiddenText(michelle, "Fine! November! It was November{fast}{nw}")

    stop ad_bg_2 fadeout 3
    play ad_bg_3 "sounds/doug/act_1/doug_heartbeat_90_bpm.ogg" loop fadein 3

    "I chuckle, but mostly out of pity for myself."

    "How did I let her deceive me so? Did I need someone to talk to that desperately?"

    "Maybe I really am weak."

    $ _history = False

    doug "It wasn't black. Nat was right. You're a liar and a psychopath."

    $ _history = True

    $ showHiddenText(doug, "It wasn't November. She was right. You're a liar and a psychopath.{fast}{nw}")

    show michelle flamethrower scared with dissolve

    $ _history = False

    doug "I felt bad for you for your tragic past, I felt connected because you remembered my friend."

    $ _history = True

    $ showHiddenText(doug, "I felt bad for you for your tragic past, I felt connected because you remembered my sister.{fast}{nw}")

    doug "But those were just illusions you created to use me."

    "I really should have listened to Nat. I'm such an idiot…"

    $ _history = False

    show michelle flamethrower pleading
    with dissolve

    michelle "F-fine! I lied about Max, but I just wanted you to feel better! There's nothing wrong with my intentions!"

    $ _history = True

    $ showHiddenText(michelle, "F-fine! I lied about Max, but I just wanted you to feel better! There's nothing wrong with my intentions!{fast}{nw}")

    show michelle flamethrower scared
    with dissolve

    michelle "I never--"

    doug "You killed innocent people in their sleep, Michelle! You're no different than that moster!"

    show michelle flamethrower furious with dissolve

    michelle "Did she tell you that? She put those ideas into your head, didn't she!"

    michelle "Ha! Good riddance then!"

    doug "What did you say?"

    michelle "You heard me! Natalia! She was constantly getting between us!"

    michelle "Bad influence my arse… We have ONE job. Anything else is a distraction."

    "My body reacts before my mind can catch up, and I've grabbed Michelle's thin arms, shaking her."

    show bg burning house blur

    show michelle flamethrower front angry closeup with hpunch

    doug "What have you done to her!?"

    "But she doesn't flinch; she only stares at me with glowering eyes."

    show michelle flamethrower front angry talking closeup with dissolve

    michelle "I didn't know you were so attracted to your own sister."

    michelle "This is a war. Everyone loses someone. {w}Get over it."

    michelle "The only thing she did was divert you from our goal! Maybe now that she's gone, you'll finally realize what's important!"

    michelle "Open your eyes, Doug!"

    show michelle flamethrower front angry closeup with dissolve
    $ renpy.music.set_volume (0, 2, channel="ad_fg_1")
    $ renpy.music.set_volume (1, 2, channel="ad_fg_2")

    play sound "sounds/doug/act_1/doug_serpent_purring.ogg" fadein 15

    "Open my eyes? Nat being a distraction?"

    doug "Give me a break… You're just crazy."

    doug "She saved me, time and time again. Without her I--"

    hide michelle with hpunch

    "Michelle frees herself from my weakened grip. I don't know what to think anymore."

    "But before I can react, the Serpent's head bursts through a wall, charging at the girl."

    play audio "sounds/doug/act_1/doug_flamethrower_long.ogg"

    scene cg michelle flamethrower serpent

    "She reacts immediately and turns to intercept the monster."

    "A gout of flame erupts from her weapon and the serpent dodges upwards, burrowing into the ceiling."

    play sound "sounds/doug/act_1/doug_serpent_hit_by_flamethrower.ogg"

    play ad_bg_1 "sounds/doug/act_1/doug_steam_loop.ogg"


    "Its liquid body courses like a gleaming pipe between wall and ceiling, with Michelle coating it in flames as it passes."

    "The sound of boiling water sizzles in the enclosed space, but the serpent seems to take no damage."

    "Steam fills the room, reflecting the fire's fierce glow."

    scene bg burning house with dissolve
    stop ad_bg_1 fadeout 1

    "The Serpent disappears down the hall, and Michelle chases after it."

    "Turbulent emotions strain at my head."

    "Was the accident at the dam really an accident…? Would Michelle--"

    "Of course she would."

    "She didn't even bat an eyelid when she found out she killed those people in their house."

    "And who am I kidding… She practically admitted doing it herself!"

    "I can't let this go on."

    $ _history = False

    friendMax "You seem like you need a friend about now."

    $ _history = True

    $ showHiddenText(friendMax, "Oh, give me a home on the range…{fast}{nw}")

    $ _history = False

    show maxGhost
    with dissolve

    "Max's phantom appears amongst the flames."

    doug "I don't have time for your shit, Max."

    $ _history = True

    $ showHiddenText(doug, "I've started singing to myself in the confusion.{fast}{nw}")

    $ _history = False

    hide maxGhost
    show maxGhostBummedBloody

    friendMax "She's not going to surrender, you know."

    doug "Go away."

    $ _history = True

    $ showHiddenText(doug, "I need her to go away.{fast}{nw}")

    $ _history = False

    hide maxGhostBummedBloody
    show maxGhostSmugBloody
    with dissolve

    friendMax "I'm just saying… what do you really want to do?"

    $ _history = True

    $ showHiddenText(doug, "What do I really want to do? {fast}{nw}")

    $ _history = False

    doug "I want to kill her. To wrap my hands around her throat and squeeze the life from her."

    $ _history = True

    $ showHiddenText(doug, "I'm going to choke the life out of her pathetic body.{fast}{nw}")

    $ _history = False

    friendMax "Then why don't you? No-one would notice."

    $ _history = True

    $ showHiddenText(doug, "No-one would notice if she were gone.{fast}{nw}")

    $ _history = False

    hide maxGhostSmugBloody
    show maxGhostSeriousBloody
    with dissolve

    friendMax "If you left her here, she would burn with the house. You'd be off the hook for the arson, and she'd be dead."

    $ _history = True

    $ showHiddenText(doug, "She would burn here. A serial arsonist that made a mistake. {fast}{nw}")

    $ showHiddenText(doug, "I'd be off the hook for everything.{fast}{nw}")

    doug "What difference would it make?"

    $ showHiddenText(doug, "I back down internally.{fast}{nw}")

    $ _history = False
    hide maxGhostSeriousBloody
    show maxGhostSmugBloody
    with dissolve

    friendMax "You can't do it, can you?"

    friendMax "You can't bring yourself to kill someone, no matter how much you hate them."

    "I want to fight with Max, and prove him wrong, but he's right."

    $ _history = True

    "After so much death, I don't think I want to see another body."

    play ad_bg_3 "sounds/doug/act_1/doug_heartbeat_120_bpm.ogg" loop

    "Let alone one born of my own hands."

    $ _history = False

    friendMax "I knew it. But, you know, there might be another way…"

    $ _history = True

    $ showHiddenText('', "But what if there was another way…?")

    play audio "sounds/doug/act_1/doug_flamethrower_three.ogg" noloop

    $ _history = False

    hide maxGhostSmugBloody
    with Dissolve(1.5)

    "Max's visage flickers and dissolves into the flames, which begin to rage in their intensity."

    $ _history = True

    show michelle flamethrower fire with moveinright

    "Michelle charges back into the hall, her weapon belching orange flames."

    play audio "sounds/doug/act_1/doug_flamethrower_short.ogg" noloop

    show michelle flamethrower fire speaking
    with dissolve

    michelle "Make yourself useful and bring me that bomb!"

    doug "Fuck you!"

    play audio "sounds/doug/act_1/doug_serpent_low_right.ogg" noloop

    michelle "I was wrong to trust you. I should never have trusted anyone."

    show serpent top left
    with Dissolve(2)

    play ad_bg_1 "sounds/doug/act_1/doug_serpent_low_left.ogg" noloop

    "A shimmering head slowly appears behind the raging girl."

    "She dodges the attack {nw}"

    show michelle flamethrower fire at right
    with move

    play audio "sounds/doug/act_1/doug_flamethrower_long.ogg" noloop

    extend "and returns fire with her flamethrower."

    "The serpent's red eyes begin to glow, and rows of teeth quiver in anticipation."

    "My mind races."

    "If the serpent devours Michelle, then she'll be removed from history."

    "Poof. Gone. Forever."

    "Present, future… and past."

    "Everything that she's ever done will be re-written."

    "I'd never have met her."

    "We'd have never started chasing this monster."

    "No flamethrowers, no innocent victims…"

    "…no 'accident' at the dam."

    $ _history = False

    show maxGhostSmugBloody
    with dissolve
    friendMax "It's ok. Save Natalia."

    friendMax "I'll be fine like this. Revenge never solves anything anyway."

    $ _history = True

    $ showHiddenText(doug, "This will solve everything.{fast}{nw}")

    hide maxGhostSmugBloody
    with dissolve

    "My mind is made up, and my body begins to act."

    "I rush forward, tackling Michelle towards the serpent."

    show michelle flamethrower shocked talking fire

    "As I connect, I can see her eyes widen in shock."

    play sound "sounds/doug/act_1/doug_serpent_short_roar.ogg" noloop
    queue sound "sounds/doug/act_1/doug_serpent_purring.ogg" noloop
    queue sound "sounds/doug/act_1/doug_serpent_low_left.ogg" noloop
    queue sound "sounds/doug/act_1/doug_serpent_purring.ogg" noloop
    queue sound "sounds/doug/act_1/doug_serpent_low_right.ogg" noloop
    queue sound "sounds/doug/act_1/doug_serpent_purring.ogg" loop

    scene cg michelle serpent
    with hpunch

    "The Serpent reacts instantly, curling itself around Michelle's slender body, trapping her in a coil of pulsating phantom energy."

    "Its head cranes up and over her, swaying gently as it positions itself for the strike."

    "Michelle tries to struggle but can't extricate herself from the serpentine embrace."

    michelle "What are you doing?!"

    doug "You killed my sister!"

    doug "You murdered those people in that house!"

    doug "I'd rather die myself than help you destroy even more!"

    show cg michelle serpent angry

    michelle "You fool! This snake will kill us all!"

    doug "Maybe, but at least I'll be rid of you."

    michelle "Fuck you! Fuck you all! When I get out of this I'm going to raze this city to the ground!"

    show cg michelle serpent looking

    "I notice a change in the pitch of the Serpent's gurgling, and it draws down until it is eye to eye with Michelle."

    "Its red eyes meet with Michelle's furiously bloodshot eyes, and for a moment it's like they are communicating."

    "Michelle's fury reaches a peak, and she manages to free an arm from the serpent's body, slapping {nw}"

    play audio "sounds/doug/act_1/doug_slap.ogg" noloop
    play sound "sounds/doug/act_1/doug_serpent_short_scream.ogg" fadeout 0.2 noloop

    show cg michelle serpent slapping

    "Michelle's fury reaches a peak, and she manages to free an arm from the serpent's body, slapping {fast}forward and connecting with one of its eyes."

    "The snake recoils and launches itself into the ceiling, releasing Michelle from its grasp."

    play music "sounds/doug/act_1/bgm_reality_bubble_glitch_2.ogg" fadein 1.0
    stop ad_fg_1 fadeout 1.0
    stop ad_fg_2 fadeout 1.0
    stop ad_bg_3 fadeout 10
    scene bg burning house
    show michelle flamethrower shocked talking

    "I can already feel the reality bubble starting to collapse around me."

    stop sound fadeout 5
    stop ad_bg_4 fadeout 2
    show bg corridor
    with ImageDissolve("images/bg/bg burning house.png", 1.0)

    "Inexplicably, Michelle is still alive."

    "Alive, and furious."

    show michelle flamethrower shocked

    stop ad_bg_4 fadeout 2

    play audio "sounds/doug/act_1/doug_flamethower_dodgy.ogg" noloop

    "She reaches for her flamethrower and toggles the trigger, but the device only lets out a faint hiss."

    "It was destroyed by the serpent's crushing grip."

    scene cg michelle fury with hpunch

    "Michelle throws the useless device to the ground and screams."

    play sound "sounds/doug/act_1/doug_drop_bag.ogg" noloop

    michelle "You… you traitor!"

    michelle "You'll pay for this! You'll all pay!"

    "Michelle storms past me,{nw}"

    play sound "sounds/doug/act_1/doug_michelle_car_bump.ogg" noloop

    extend " shoving me against the wall as she does."

    stop ad_bg_4 fadeout 2
    show bg corridor
    with ImageDissolve("images/bg/bg burning house.png", 2.0)

    "I want to stop her, but I can't."

    "My knees are weak and my throat tight."

    "My entire energy reserve has been sapped from me."

    "Instead of chasing her I fall to my knees. Tears that I've been suppressing since Max's demise flow freely from my eyes."

    "Here, on some stranger's floor, I find myself unable to move, sobbing like a baby."

    "I've lost."

    "We've lost."

    "We never had a chance to defeat this monster, and now it's taken everything from me."

    "I just want to lie here until it comes to consume me and remove me from this wretched life."

    "Come on you fucker!"

    "What are you waiting for!"

    "I know you want me gone, so come and finish me off!"

    "But I know that I'm not that lucky."

    "If it didn't want Michelle, then it won't want me either."

    "We're both cursed. Somehow, we're not part of the Serpent's grand plans."

    stop music fadeout 3.0
    scene bg car inside with dissolve

    "After who knows how long, I manage to crawl outside the house and back to my father's car."

    "Michelle's remaining equipment is gone, but the car remains."

    "Defeat washes over me. I sit in the driver's seat, afraid to turn the key."

    "I don't know how I can face my parents, let alone myself."

    "Maybe I'd really be better off dead."

    window hide
    with dissolve
    scene bg black
    with Dissolve(2)

    $ renpy.pause(delay=3, hard=True)


    jump dougActSixSceneOne
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

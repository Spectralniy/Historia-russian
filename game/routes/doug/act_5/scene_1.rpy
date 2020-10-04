label dougActFiveSceneOne:

    $ stopAllAudioTracks()


    window show
    scene bg black
    with dissolve


    scene bg_doug_room_sunlight

    play ad_bg_1 "sounds/doug/act_1/bird_song_cheerful.ogg"
    play music "sounds/doug/act_1/bgm_birdsong.ogg"

    window show

    "Somehow I manage to drag myself out of bed."

    "I'm not used to this small amount of sleep."

    "Combined with the stress and exertion of chasing the serpent, it's starting to make me feel groggy every morning."

    "I guess you could call it a ghost-hunting hangover?"

    "Whatever. It doesn't matter. All I need to do it make it to school. I can probably find a place to nap if I look hard enough."

    "If the school is ok with truancy then they should be fine with someone catching some zzz's."

    scene bg doug kitchen sunrise
    with dissolve

    play sound "sounds/doug/act_1/doug_make_coffee.ogg"

    "I brew a pot of coffee, the dribbling sound of the dripping liquid into the glass pot is loud in the morning."

    "It doesn't take long for there to be enough for me, so I hurriedly pour a cup."

    "I throw in an ice cube or two to take off the edge, then take a deep draught."

    "Luke-warm caffeine strokes my oesophagus and starts my body ticking."

    "I hope Michelle got away last night. There were sirens blaring all through the night. It must have been a hell of a fire."

    "Anyway, what's done is done. We can't take that back."

    "So long as no-one saw us leaving the area then we should be fine."

    natalia "Good morning, sleepy head. I didn't expect you to be here before me."

    "Nat helps herself to some cereal and some orange juice from the fridge."

    play sound "sounds/doug/act_1/doug_fridge_close.ogg"
    play ad_bg_1 "sounds/doug/act_1/doug_pour_cereal.ogg"
    queue ad_bg_1 "sounds/doug/act_1/doug_eat_cereal.ogg" loop

    show cg nat cornflakes smile2 hair
    with dissolve

    doug "Should I pour you a cup?"

    natalia "I'm fine with juice thanks."

    "She's yet to develop the unhealthy addiction to coffee that seems to fuel the rest of the family."

    "Between Mum's shift-work, Dad's late nights and my studies, the rest of us find it hard to make it through the day without some kind of help."

    "But Natalia is still a kid. She doesn't know what it means to need coffee to even hold a conversation."

    "I'm jealous of that. It won't be long though and she'll be just like us."

    "The half-dream from last night comes back to me and I suddenly feel grateful for her presence."

    "Nat is my anchor in reality. Always there to catch me when I'm falling."

    "I'm still not sure about the memories about Max's death but maybe, before the reality overwrote itself and removed him from history, she helped me yet again."

    "A feeling of gratitude and guilt washes over me and I try to smile despite my fatigue."

    doug "Yeah, well, you know. Study and all that. Early bird gets the worm."

    "Lying to her is painful."

    show cg nat cornflakes sad
    with dissolve

    "I can see her scrutinising me. I know she wants to say something, but she lets it slip away from her."

    show cg nat cornflakes smile3 hair
    with dissolve

    natalia "You're right. At least, that's what I'm going to start telling myself."

    play sound "sounds/doug/act_1/doug_phone_vibrate_1.ogg"
    queue sound "sounds/doug/act_1/doug_phone_lock.ogg"

    show cg nat cornflakes phone
    with dissolve

    "Natalia sits across from me and whips out her phone, scrolling through it with her left hand as she shovels the cereal with her right."

    "She slurps the milk a little. I'm sure Mum would complain, but she hasn't joined us for breakfast in weeks."

    "Most mornings it's just Nat and I, sitting in silence. {w}Like strangers on a train."

    "The thought of that alone stirs me into action."

    doug "Do you want to go to school together?"

    "I want to find some way to tell her that maybe she is right about Michelle."

    "Maybe she knows some way to control her, or at least some kinds of ways that I can get her to listen to me."

    show cg nat cornflakes unamused
    with dissolve

    natalia "Love to. Can't though. Have an excursion today."

    doug "Excursion? Where to?"

    natalia "The dam. It's for Geography. Water supplies and the like."

    show cg nat cornflakes phone
    with dissolve

    "Natalia is clearly distracted by her phone; her usual prose has been clipped into short sentences."

    doug "Oh. Right. Have fun."

    "I'll have to find some other time to talk."

    "Chances are I won't see Michelle until tonight anyway. It can wait."

    stop ad_bg_1 fadeout 1.0

    show cg nat cornflakes shocked
    with dissolve

    play sound "sounds/doug/act_1/doug_drop_fork.ogg"

    natalia "Oh my god…"

    "I start at Natalia's sudden exclamation."

    doug "What is it?"

    natalia "It looks like there was a fire downtown last night…"

    "It didn't take long for that news to break."

    natalia "…and the people inside died…"

    play music "sounds/doug/act_1/bgm_reality_bubble_glitch_3.ogg"

    play ad_bg_1 "sounds/doug/act_1/doug_heartbeat_90_bpm.ogg" loop

    "I swallow hard to prevent my panicked heart bursting from my chest."

    doug "Died…?"

    natalia "Here, look."

    scene cg phone news

    "Natalia passes me her phone. An article from the local newspaper flashes across the screen."

    "The remains of two people… {w}…a full investigation…"

    "Chills run from head to toe, and I can't stop myself from shaking."

    natalia "Are you all right? Did you know them?"

    doug "N-no…"

    "The words somehow creep out by themselves. My brain is frozen, trying to process what happened."

    "I scroll down slightly to find a photo of the house, surrounded by fire trucks discharging their hoses into the flaming building."

    "There is no mistake; that is the house that Michelle and I were in last night."

    "We're murderers."

    "Murderers."

    "This wasn't how it was supposed to happen."

    "I wanted to kill that beast so that no-one else would need to lose anyone."

    "And yet, we've ended up becoming killers ourselves."

    $ _history = False
    "I lose the fight with{nw}"

    play sound "sounds/doug/act_1/doug_vomit_2.ogg"

    $ _history = True
    "I lose the fight with{fast} my stomach and vomit starts to race towards my head."

    scene bg doug kitchen sunrise
    with dissolve

    "I barely make it to the sink before the black coffee I drank a moment ago is spiralling down the drain."

    show natalia shocked closer
    with dissolve

    natalia "Are you ok?"

    "Natalia jumps up and grabs my shoulders, patting my back instinctively to help calm my stomach."

    doug "Yeah… fine…"

    natalia "You don't look fine."

    doug "It's ok. Coffee didn't sit well with me is all."

    "I try to hide my dry retching from her as I sit back down."

    show natalia worried hand down closer
    with dissolve

    natalia "Maybe you should skip school? Get some rest?"

    "Part of me agrees with her. I want to run as far as I can from this town and everyone in it."

    "Especially that maniac, Michelle."

    "She should have listened to me."

    "I told her that the reality bubble was collapsing around us, but she wouldn't stop…"

    "She just wouldn't stop…"

    "And now two people are dead, and we're going to be under suspicion."

    "I don't want to go to jail for life…"

    "I was supposed to live a comfortable life."

    "Study hard, get into some kind of university."

    "Get a job. Find a wife. Have some kids."

    "A normal, boring life."

    "But because of that lizard and the maniac, I'm going to rot in jail."

    "A wasted life."

    "I want to cry, but I can't let Natalia see me like that."

    "It's not fair to her."

    "I take a deep breath to settle my stomach, then look her in the eyes."

    doug "It's ok. I'm fine. I drank too much coffee on an empty stomach, is all."

    show natalia concerned hand down closer
    with dissolve

    natalia "Well, look after yourself."

    natalia "I can't look after you today. Gotta run; we have to be there half an hour beforehand."

    doug "Sure, sure."

    "Natalia throws the unfinished cereal to the sink and chugs her orange juice."

    show natalia sad smile2 closer
    with dissolve

    natalia "Well, see you after school!"

    hide natalia
    with moveoutright

    "She's bought my story, hook, line and sinker."

    "I guess she's happy about the excursion. Not even a sick brother could get her down."

    "On the other hand, I need to be at school. If I start to act suspicious then maybe the police will be on to me quicker."

    "The article didn't mention that they were treating it as arson yet, so maybe there is a chance that they won't work it out that it was us."

    "Or maybe I should simply go to the cops directly and report Michelle."

    "Two birds with one stone…"

    "No.{w} The serpent has caused enough damage. {w}We need to stop it."

    "We'll work out how to contain it or how to kill it."

    "Then, once that is done I'll hand Michelle over to the police like the killer she is."

    "Maybe they can get her the help she needs."

    "Maybe not."

    "Either way, she won't be my problem any more."

    "We just need to kill that monster and be done with it."
    stop ad_bg_1 fadeout 10
    stop music fadeout 3


    jump dougActFiveSceneTwo
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

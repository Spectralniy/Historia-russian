label dougActFourSceneOne:

    $ stopAllAudioTracks()


    window show
    scene bg black
    with dissolve


    scene bg doug kitchen sunset

    "I manage to get home before Mum or Dad. I'm hoping that the school didn't notify them of my recent truancy."

    "I've not skipped out from school before, so I'm not even sure if they'd notice."

    "But I know there are kids that do it all the time. If they did make some kind of notification then they couldn't get away with it all the time…"

    "Right?"
    play sound "sounds/doug/act_1/doug_drop_bag.ogg"

    "I throw my bag on the dining room floor and open the fridge. Weeum's cave was a long walk from home."

    play sound "sounds/doug/act_1/doug_fridge_close_with_rattle.ogg"

    "I pull a bottle of orange juice from the fridge and slam it shut."

    natalia "And where were you…?"

    $ renpy.music.set_volume(0.7,0,channel="music")
    $ renpy.music.set_volume(0,0,channel="ad_fg_1")
    play music "sounds/doug/act_1/bgm_nat_kinda_concerned.ogg"
    play ad_fg_1 "sounds/doug/act_1/bgm_nat_very_concerned.ogg"

    show natalia upset closer at left
    with dissolve

    doug "Shit, Nat, you scared me. What do you mean?"

    natalia "Don't try and hide it from me. I know you skipped school."

    "Her eyes cut shreds off me. I've never been able to lie to my sister."

    "At least not with any efficacy."

    doug "Yeah… I needed some time to think."

    natalia "About this 'Max' nonsense?"

    $ showHiddenText(friendMax, "Damn Nat! That's cold...{fast}{nw}")

    "I wince at the mention of Max's name. I know that it doesn't matter how many times I explain it, she'll never understand."

    doug "Yeah, kinda. I think maybe I'm just overdoing the study… maybe…?"

    "Natalia doesn't look convinced. Sure, I've been pulling long hours in the past trying to study, but she also knows me."

    "I'm not going to stay up too late…"

    natalia "Fine. Have it your way."

    "Somehow I've dodged a bullet."

    natalia "But…"

    $ showHiddenText (friendMax, "Uh-oh.{fast}{nw}")

    "Or maybe not."

    show natalia upset front closer at left
    with dissolve

    natalia "Did you leave with Michelle? Michelle Symon. From my class?"

    "I try not to choke on my juice."

    doug "W-why would you think that?"

    natalia "She was in class up until lunch, but then the two of you were nowhere to be seen."

    natalia "Same with yesterday. She disappeared after you left."

    show natalia lookaway closer at left
    with dissolve

    natalia "Are you two… you know…"

    natalia "Like, dating or something?"

    play sound "sounds/doug/act_1/doug_spit_take.ogg"

    "This time I really do choke on the orange juice, the tart liquid clogging my sinuses."

    doug "What?! No! It's not like that."

    show natalia upset front closer at left
    with dissolve

    natalia "So you are leaving with her…"

    $ showHiddenText(friendMax, "She's got you there...{fast}{nw}")

    "Damn, she's good."

    doug "Well, yes. But it's not what you think."

    show natalia upset closer at left
    with dissolve

    natalia "Two teenagers leaving school at lunchtime. You have a hard case to defend there."

    doug "I know how it looks, and you're right, I've been leaving school with Michelle."

    doug "But we're not together. Nothing like that."

    doug "She's trying to help me…"

    "My brain races to complete this sentence."

    doug "…sort out what's going on in my head."

    show natalia scared closer at left
    with dissolve

    natalia "Doug! Don't you start smoking weed… it's hard enough living in this shitty town without you starting to smoke like the rest of them."

    natalia "I knew she was a bad influence."

    show natalia shocked closer at left
    with dissolve

    doug "No! That's not it. Michelle doesn't smoke either."

    natalia "Then why is she so weird all the time?"

    doug "That's a little harder to explain."

    doug "But she understands what I'm going through. She believes me."

    show natalia worried hand down closer at left
    with dissolve

    natalia "I want to believe you Doug, but you're acting crazy now. You know that, right?"

    natalia "You need real help, not advice from the class weirdo."

    doug "Real help can't help me now…"

    $ showHiddenText (friendMax, "Dude, you're blowing it.{fast}{nw}")

    show natalia scared closer at left
    with dissolve

    natalia "Bullshit!"

    natalia "She's dangerous, you know. A bad influence."

    natalia "If you want a girlfriend, ask me to help! Anyone but her!"

    $ showHiddenText(friendMax, "Tell her the truth...{fast}{nw}")

    doug "What have you got against her?"

    show natalia worried hand down closer at left
    with dissolve

    "This is a side of Natalia that I haven't seen before. She's usually positive about everyone."

    "I've never seen her get this worked up about anyone before."

    "And even though I have my own doubts about Michelle, those empty insults irk me."

    show natalia lookaway closer at left
    with dissolve

    natalia "I… I don't have anything against her."

    natalia "But she… I tried to get close to her, but I couldn't."

    show natalia upset pouting closer at left
    with dissolve

    natalia "She pushes everyone away from her. She has nothing in common with anyone."

    natalia "That's not you, Doug!"

    show natalia concerned hand down closer at left
    with dissolve

    "Part of me wants to fight back, but when I see how concerned my little sister is, I can't help but concede."

    doug "Maybe you're right, but maybe she's just a little misunderstood."

    doug "In any case, we're not dating. It's more like… hanging out, I guess."

    show natalia sad closer at left
    with dissolve

    "Natalia's expression softens slightly, but I can still see the concern in her eyes."

    natalia "I think that you shouldn't do that. Nothing good can come of it."

    natalia "I wish that she wasn't like that, but she is."

    natalia "And you've been so weird recently… I don't want you turning into her."

    play sound "sounds/doug/act_1/doug_stiflied_laugh_male.ogg"

    "I stifle a laugh. I didn't know that Natalia had a side like this."

    "Then again, I guess it's my fault. I can't explain anything to her. Maybe I could try…"

    $ renpy.music.set_volume(0,4,channel="music")
    $ renpy.music.set_volume(0.5,4,channel="ad_fg_1")

    $ showHiddenText ("dead Max", "Do it man! She's smarter than you!{fast}{nw}")

    "A shudder winds its way down my spine."

    "What if explaining it to her makes her a target? I couldn't live with myself if I made Natalia a target of the serpent."

    "What if Michelle's actions don't kill the serpent, but piss it off? What if it comes for revenge?"

    "I feel that too-familiar bile rising in my stomach. It feels like it is eating away my soul at the thought of losing my family."

    "I need to make sure she doesn't get dragged into this."

    doug "Don't worry. I'll protect you."

    show natalia question closer at left
    with dissolve

    natalia "Huh?"

    show natalia worried hand down closer at left
    with dissolve

    natalia "Doug, you really need some help. Do you want me to help you talk to mum and dad?"

    doug "Nah… nah that's not it. I… I think I just need some rest."

    natalia "You're really beginning to worry me. Can you at least promise me that you won't… you know… 'do' her?"

    doug "What?! No! Of course not."

    show natalia sad smile at left
    with dissolve

    natalia "Well, that's at least something. And no drugs…"

    doug "None. I swear."

    show natalia playful pout closer at left
    with dissolve

    natalia "If I find out you're lying to me…"

    "Natalia holds up a fist in a challenge, but I can see that she doesn't mean it."

    "The concern hasn't left her eyes."

    doug "Look, give me a week. If I can't work anything out in a week, you can tell mum and dad everything."

    doug "The skipping school, Michelle… I'll even do a drug test."

    doug "But I need you to at least give me a week."

    natalia "O-ok. One week. That's it!"

    "I pull her into a quick hug, rustling her hair in the act."

    doug "I knew I could count on you."

    show natalia upset pouting closer at left
    with dissolve

    natalia "You're a clown."

    "Natalia pulls herself away from me and leaves the kitchen for her room."

    hide natalia
    with moveoutleft

    "The bile starts to subside."

    "I've bought myself a week. It's not much time, but we need to start moving fast to understand the serpent."

    "If anything happens to Natalia, then I'm going to jump into that snake's mouth and destroy it from the inside myself…"


    stop music fadeout 3.0
    $ renpy.music.set_volume(1,3,channel="music")

    jump dougActFourSceneTwo
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

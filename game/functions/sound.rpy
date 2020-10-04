init python:
    def stopAllAudioTracks():
        tracks = [
            "music",
            "voice",
            "sound",
            "ad_bg_1",
            "ad_bg_2",
            "ad_bg_3",
            "ad_bg_4",
            "ad_bg_5",
            "ad_bg_6",
            "ad_bg_7",
            "ad_fg_1",
            "ad_fg_2",
            "ad_fg_3",
            "ad_fg_4",
            "ad_fg_5",
            "ad_fg_6",
            "ad_fg_7",
            "ad_fg_8",
            "music_2"
        ]
        
        for track in tracks:
            renpy.music.stop(track, 3)
        
        return

    def resetTrackAudio(track):
        renpy.music.set_volume(1, 1, channel=track) 
        
        return

    def resetTracksAudio(tracks):
        for track in tracks:
            resetTrackAudio(track)
        
        return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

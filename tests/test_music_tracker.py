import pytest
from lib.music_tracker import *

def test_adds_track_to_list():
    song = MusicTracker()
    song.add_song("Unholy")
    result = song.see_listened_tracks()
    assert result == "Listened tracks: Unholy"

'''
Successfully reutrns a formatted list of songs
'''
def test_return_formatted_list():
    song = MusicTracker()
    song.add_song("Unholy")
    song.add_song("Tired BOY")
    song.add_song("FLOAT")
    result = song.see_listened_tracks()
    assert result == "Listened tracks: Float; Tired Boy; Unholy"

'''
Try to add empty string
Returns error message
'''
def test_errors_if_add_empty_string():
    song = MusicTracker()
    with pytest.raises(Exception) as e:
        song.add_song("")
    assert str(e.value) == "Cannot add an empty string to the list."

'''
Try to add same song twice
Returns error message
'''
def test_errors_for_adding_same_song_twice():
    song = MusicTracker()
    song.add_song("Unholy")
    with pytest.raises(Exception) as e:
        song.add_song("UNHOLY")
    assert str(e.value) == "Cannot add the same song twice."

'''
If list of songs is empty,
Returns error message when see_listened_tracks is called
'''
def test_errors_for_seeing_empty_list():
    song = MusicTracker()
    with pytest.raises(Exception) as e:
        song.see_listened_tracks()
    assert str(e.value) == "No songs to show."


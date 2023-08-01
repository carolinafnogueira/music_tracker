# {{PROBLEM}} Class Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

_Put or write the user story here. Add any clarifying notes you might have._

As a user
So that I can keep track of my music listening
I want to (1)add tracks I've listened to and (2)see a list of them.

## 2. Design the Class Interface

_Include the initializer, public properties, and public methods with all parameters, return values, and side-effects._

```python
# EXAMPLE

class MusicTracker:
    # Keeps record of listened tracks

    def __init__(self):
        # Parameters: none
        # Side effects:
        #   Saves a list with listened tracks
        pass # No code here yet

    def add_song(self, song):
        # Parameters:
        #   song: string representing a single song title
        # Returns:
        #   Nothing
        # Side-effects
        #   Saves song name to a list defined in the constructor method
        pass # No code here yet

    def see_listened_tracks(self):
        # Parameters: none
        # Returns:
        #   A formatted string with all the elements of the list created
        # Side-effects:
        #   Throws an exception if list is empty
        pass # No code here yet
```

## 3. Create Examples as Tests

_Make a list of examples of how the class will behave in different situations._

``` python
'''
Successfully adds new track to list
'''
song = MusicTracker()
song.add_song("Unholy")
see_listened_tracks() => ["Unholy"]

'''
Successfully reutrns a formatted list of songs
'''
song = MusicTracker()
song.add_song("Unholy")
song.add_song("Tired BOY")
song.add_song("FLOAT")
see_listened_tracks() => "Listened tracks: Float; Tired Boy; Unholy"

'''
Try to add empty string
Returns error message
'''
song = MusicTracker()
song.add_song("") => "Cannot add an empty string to the list."

'''
Try to add same song twice
Returns error message
'''
song = MusicTracker()
song.add_song("Unholy")
song.add_song("UNHOLY") => "Cannot add the same song twice."     # Also tests for case sensitivity

'''
If list of songs is empty,
Returns error message when see_listened_tracks is called
'''
song = MusicTracker()
see_listened_tracks() => "No songs to show."




```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._


<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

**How was this resource?**  
[😫](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=resources%2Fsingle_class_recipe_template.md&prefill_Sentiment=😫) [😕](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=resources%2Fsingle_class_recipe_template.md&prefill_Sentiment=😕) [😐](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=resources%2Fsingle_class_recipe_template.md&prefill_Sentiment=😐) [🙂](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=resources%2Fsingle_class_recipe_template.md&prefill_Sentiment=🙂) [😀](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=resources%2Fsingle_class_recipe_template.md&prefill_Sentiment=😀)  
Click an emoji to tell us.

<!-- END GENERATED SECTION DO NOT EDIT -->
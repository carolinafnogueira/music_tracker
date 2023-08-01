class MusicTracker:
    # Keeps record of listened tracks

    def __init__(self):
        self.listened_tracks = []

    def add_song(self, song):
        song = song.strip().title()
        if song == "":
            raise Exception("Cannot add an empty string to the list.")
        elif song in self.listened_tracks:
            raise Exception("Cannot add the same song twice.")
        self.listened_tracks.append(song)

    def see_listened_tracks(self):
        if self.listened_tracks == []:
            raise Exception("No songs to show.")
        formatted_list = "Listened tracks: " + "; ".join(sorted(self.listened_tracks))
        return formatted_list

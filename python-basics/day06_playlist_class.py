class Track:
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist

class Playlist:
    def __init__(self, name):
        self.name = name
        self.tracks = []

    def add_track(self, track):
        self.tracks.append(track)
        return f"'{track.title}' added to {self.name}."

my_gym_mix = Playlist("Gym Jams")
song = Track("Eye of the Tiger", "Survivor")
print(my_gym_mix.add_track(song))
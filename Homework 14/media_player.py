class Player:
    def __init__(self, name, video_link, duration):
        self.name = name
        self.video_link = video_link
        self.duration = duration
        self.playing = False
        self.current_time = 0
        self.quality = 'HD'

    def play(self, video_address):
        if video_address == self.video_link:
            self.playing = True
            print(f"Playing {self.name} - {self.video_link}")
            return True
        else:
            print("Video address not found.")
            return False

    def pause(self):
        if self.playing:
            self.playing = False
            print(f"Paused {self.name}")
        else:
            print("Player is not playing.")

    def save_last_time(self, current_time):
        self.current_time = current_time
        print(f"Saved current time: {self.current_time}")

    def change_quality(self, quality):
        self.quality = quality
        print(f"Changed quality to {self.quality}")

if __name__ == "__main__":
    netflix_player = Player(name="Netflix Player", video_link="https://www.netflix.com/the_equalizer", duration="2:30:00")
    address = "https://www.netflix.com/the_equalizer"
    netflix_player.play(address)
    netflix_player.pause()
    netflix_player.save_last_time("1:14:33")
    netflix_player.change_quality("2K")

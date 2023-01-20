from pygame import mixer
mixer.init()
channel_number = 1


class Sound():
    def __init__(self, path, volume):
        global channel_number
        self.path = path
        self.volume = volume
        self.channel = mixer.Channel(channel_number)
        channel_number += 1
        mixer.set_num_channels(channel_number)

    def play(self):
        self.channel.set_volume(self.volume)
        self.channel.play(mixer.Sound(self.path))

    def pause(self):
        self.channel.pause()

    def resume(self):
        self.channel.unpause()

    def stop(self):
        self.channel.stop()

from workers.video import VideoGen
from workers.tts import TTS
from workers.music import Music


class Orchestrator:

    def __init__(self):
        self.video = VideoGen()
        self.tts = TTS()
        self.music = Music()

    def run_scene(self, scene, idx):

        video_path = f"outputs/video_{idx}.mp4"
        audio_path = f"outputs/audio_{idx}.wav"
        music_path = f"outputs/music_{idx}.wav"

        v = self.video.generate(scene["visual"], video_path)
        a = self.tts.generate(scene["voice"], audio_path)
        m = self.music.generate(scene["music"], music_path)

        return {
            "video": v,
            "audio": a,
            "music": m
        }

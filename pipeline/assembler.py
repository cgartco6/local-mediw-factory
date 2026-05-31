from moviepy.editor import VideoFileClip, AudioFileClip, CompositeAudioClip


class Assembler:

    def build(self, scene_outputs, output="outputs/final.mp4"):

        clips = []

        for s in scene_outputs:

            video = VideoFileClip(s["video"])
            audio = AudioFileClip(s["audio"])

            final = video.set_audio(audio)
            clips.append(final)

        final_video = clips[0]
        final_video.write_videofile(output)

        return output

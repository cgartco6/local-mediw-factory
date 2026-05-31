from moviepy.editor import ColorClip


class VideoGen:

    def generate(self, text, output_path):

        clip = ColorClip(size=(1280, 720), color=(20, 20, 20), duration=5)
        clip.write_videofile(output_path, fps=24)

        return output_path

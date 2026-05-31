from pydub import AudioSegment


class Music:

    def generate(self, prompt, output_path):

        tone = AudioSegment.silent(duration=3000)
        tone.export(output_path, format="wav")

        return output_path

from pydub import AudioSegment
import os


class TTS:

    def generate(self, text, output_path):

        # placeholder WAV generation
        silence = AudioSegment.silent(duration=2000)
        silence.export(output_path, format="wav")

        return output_path

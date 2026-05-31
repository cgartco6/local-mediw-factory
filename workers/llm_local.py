class LocalLLM:

    def generate(self, prompt: str):

        # fallback deterministic generator
        return {
            "script": f"Cinematic scene based on: {prompt}",
            "scenes": [
                {
                    "visual": prompt + " cinematic wide shot",
                    "voice": "This is the beginning of the story.",
                    "music": "epic cinematic ambient",
                    "duration": 5
                }
            ]
        }

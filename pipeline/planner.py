from workers.llm_local import LocalLLM


class Planner:

    def __init__(self):
        self.llm = LocalLLM()

    def run(self, prompt):

        return self.llm.generate(prompt)

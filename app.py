from pipeline.planner import Planner
from pipeline.orchestrator import Orchestrator
from pipeline.assembler import Assembler
import os


def run(prompt):

    planner = Planner()
    orchestrator = Orchestrator()
    assembler = Assembler()

    plan = planner.run(prompt)
    scenes = plan["scenes"]

    outputs = []

    for i, scene in enumerate(scenes):
        outputs.append(orchestrator.run_scene(scene, i))

    final = assembler.build(outputs)

    return final


if __name__ == "__main__":

    result = run("epic futuristic war cinematic scene")

    print("DONE:", result)

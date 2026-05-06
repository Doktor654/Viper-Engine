import sys
import os

MAIN_TEMPLATE = """from engine import *
from GameScene import GameScene

Game(scenes={"game": GameScene},start_scene="game", screen_size=(1280, 720), fps=60).run()
"""

SCENE_TEMPLATE = """from engine import *

class GameScene(Scene):
    def __init__(self, input, scene_manager):
        super().__init__(input, scene_manager)
        
"""

def main():
    args = sys.argv[1:]

    if not args or args[0] != "new" or len(args) < 2:
        print("USAGE: viper new <ProjectName>")
        return

    name = args[1]

    if os.path.exists(name):
        print(f"Map '{name}' already exists!")
        return

    os.makedirs(f"{name}/assets")

    with open(f"{name}/main.py", "w") as f:
        f.write(MAIN_TEMPLATE)

    with open(f"{name}/GameScene.py", "w") as f:
        f.write(SCENE_TEMPLATE)

    print(f"✅ Project '{name}' Created! Run: cd {name} && python main.py")
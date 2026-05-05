# Viper Engine 🐍
A lightweight Python game engine with a node-based scene system. Built on pygame-ce.

## Installation
```bash
pip install viper-pygame-engine
```

## Getting Started
Create a new project with a single command:
```bash
viper new MyGame
cd MyGame
python main.py
```

This creates a ready-to-use project structure with `main.py` and `GameScene.py` — just open and start building.

## Nodes
| Node | Description |
|------|-------------|
| `Node` | Base for everything |
| `TransformNode` | Adds world position |
| `SpriteNode` | Renders sprites/textures |
| `PlayerNode` | Movable node with input |
| `CollisionBody` | Collision rectangle with signal |
| `CameraNode` | Smoothly follows a target node |
| `UINode` | UI base, unaffected by camera |
| `LabelNode` | Renders text |
| `ButtonNode` | Clickable button with signal |
| `TimerNode` | Countdown timer with delta |
| `ScrollingBackground` | Scrolling background |
| `AudioPlayer` | Plays audio |

## Example Projects
- **[Flappy Bird](https://github.com/Doktor654/FlappyBird-viper-engine)**

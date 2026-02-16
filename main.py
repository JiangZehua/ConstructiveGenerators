from generators.binary.wfc_generator import WFCGenerator
from generators.binary.bsp_generator import BSPGenerator
from generators.binary.ca_generator import CAGenerator
from generators.binary.digger_generator import DiggerGenerator
from generators.binary.random_generator import RandomGenerator
from generators.binary.connect_generator import ConnectGenerator
from generators.binary.maze_generator import MazeGenerator
import pcg_benchmark
import matplotlib.pyplot as plt

if __name__ == "__main__":
    env = pcg_benchmark.make("binary-large-v0")

    generator = RandomGenerator(0.6)
    level = generator.generate(env.content_space.sample())
    plt.imshow(env.render(level))
    plt.show()
    generator = MazeGenerator()
    level = generator.generate(level)
    plt.imshow(env.render(level))
    plt.show()

    generator = CAGenerator()
    level = generator.generate(env.content_space.sample())
    plt.imshow(env.render(level))
    plt.show()
    generator = ConnectGenerator()
    level = generator.generate(level)
    plt.imshow(env.render(level))
    plt.show()
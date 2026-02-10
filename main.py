from generators.binary.wfc_generator import WFCGenerator
from generators.binary.bsp_generator import BSPGenerator
from generators.binary.ca_generator import CAGenerator
from generators.binary.digger_generator import DiggerGenerator
from generators.binary.random_generator import RandomGenerator
from generators.binary.connect_generator import ConnectGenerator
import pcg_benchmark
import matplotlib.pyplot as plt

if __name__ == "__main__":
    env = pcg_benchmark.make("binary-large-v0")

    generator = CAGenerator()
    level = generator.generate(env.content_space.sample())
    plt.imshow(env.render(level))
    plt.show()
    generator = ConnectGenerator()
    level = generator.generate(level)
    plt.imshow(env.render(level))
    plt.show()
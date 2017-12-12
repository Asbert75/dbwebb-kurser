#!/usr/bin/env python3
"""
Holds the adventure game main function.
"""
import options, game


def main():
    """
    Main function, this is what runs the game.
    """
    options.parseOptions()

    game.loadFiles()

    game.intro()
    game.run()


if __name__ == "__main__":
    main()

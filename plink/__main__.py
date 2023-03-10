import argparse
import analyser
from options import Options

def initialise(arguments):
    return Options(whitelist=arguments.whitelist, recursion_depth=arguments.depth, blacklist=arguments.blacklist, start_url=arguments.start_url)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("start_url", type=str, help="URL to analyse")
    parser.add_argument("--whitelist", help="Domains to analyse (default is the start_url domain). Ignored if blacklist is specified", nargs="*")
    parser.add_argument("--blacklist", help="Domains to blacklist", nargs="*")
    parser.add_argument("--depth", type=int, help="Number of analysis cycles")
    args = parser.parse_args()
    options = initialise(args)
    analyser.analyse(options)

if __name__ == '__main__':
    main()
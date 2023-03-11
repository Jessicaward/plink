import argparse
from analyser import Analyser
from options import Options

def initialise(arguments):
    return Options(whitelist=arguments.whitelist, depth=arguments.depth, blacklist=arguments.blacklist, start_url=arguments.start_url, verbose=arguments.verbose)

def main():
    #Retrieve, validate and parse arguments from CLI
    parser = argparse.ArgumentParser()
    parser.add_argument("start_url", type=str, help="URL to analyse")
    parser.add_argument("--whitelist", "-w", help="Domains to analyse (default is the start_url domain). Ignored if blacklist is specified", nargs="*")
    parser.add_argument("--blacklist", "-b", help="Domains to blacklist", nargs="*")
    parser.add_argument("--depth", "-d", type=int, help="Number of analysis cycles", const=3, default=3, nargs="?")
    parser.add_argument("--verbose", "-v", action="store_true", help="Give more output")
    args = parser.parse_args()

    #Both whitelist and blacklist cannot be specified
    if args.whitelist is not None and args.blacklist is not None:
        parser.error("Either provide a whitelist, or a blacklist, you cannot specify both")

    options = initialise(args)
    a = Analyser(options)
    a.analyse()

if __name__ == '__main__':
    main()
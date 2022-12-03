import argparse
import os


def get_parser():
    parser = argparse.ArgumentParser(
        description="change extension of files in a working directory"
    )
    parser.add_argument(
        "work_dir",
        metavar="WORK_DIR",
        type=str,
        nargs=1,
        help="the directory where to change extension",
    )
    parser.add_argument(
        "old_ext", metavar="OLD_EXT", type=str, nargs=1, help="old extension"
    )
    parser.add_argument(
        "new_ext", metavar="NEW_EXT", type=str, nargs=1, help="new extension"
    )
    parser.add_argument(
        "ant_arg", metavar="ANT_ARG", type=str, nargs=1, help="another extension"
    )
    return parser


def main():
    """
    This will be called if the script is directly invoked.
    """
    # adding command line argument
    parser = get_parser()
    args = vars(parser.parse_args())
    print(type(args))
    print(args)


if __name__ == "__main__":
    main()

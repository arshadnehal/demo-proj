import sys
from lib import Utils


if __name__ == "__main__":

    valid_env = Utils.check_environment_var(sys.argv)
    print(valid_env)

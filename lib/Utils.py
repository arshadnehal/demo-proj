

def check_environment_var(sys.argv):

    valid_env = ['local','test','prod']

    env_ext = sys.argv[1] if len(sys.argv) == 2 else input('Please specify your environment: ').lower()

    if env_ext in valid_env:
        return env_ext
    else:
        print('Invalid environment exiting...')
        sys.exit(-1)

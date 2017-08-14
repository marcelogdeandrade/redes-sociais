import os
import twitter

from twitter.error import TwitterError


ROOT_NODE = 'marceloga1995'

DATA_FOLDER = 'myTwitter'

FILE_NAME = '../twitter-keys.txt'

CONSUMER_KEY = None
CONSUMER_SECRET = None
ACCESS_TOKEN_KEY = None
ACCESS_TOKEN_KEY_SECRET = None

def getCredentials():
    global CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN_KEY, ACCESS_TOKEN_KEY_SECRET
    with open(FILE_NAME) as f:
        lines = f.readlines()
        CONSUMER_KEY = lines[0].split()[1]
        CONSUMER_SECRET = lines[1].split()[1]
        ACCESS_TOKEN_KEY = lines[2].split()[1]
        ACCESS_TOKEN_KEY_SECRET = lines[3].split()[1]

def build_path(node):
    return os.path.join(DATA_FOLDER, node + '.txt')


def main():
    api = twitter.Api(
        consumer_key=CONSUMER_KEY,
        consumer_secret=CONSUMER_SECRET,
        access_token_key=ACCESS_TOKEN_KEY,
        access_token_secret=ACCESS_TOKEN_KEY_SECRET,
        sleep_on_rate_limit=True,
    )

    root_path = build_path(ROOT_NODE)

    with open(root_path, 'w', encoding='utf-8') as root_file:
        root_data = api.GetFriends(screen_name=ROOT_NODE)

        for root_subdata in root_data:
            node = root_subdata.screen_name

            print(node)

            try:
                data = api.GetFriends(screen_name=node)
            except TwitterError:
                continue

            root_file.write(node + '\n')

            path = build_path(node)

            with open(path, 'w', encoding='utf-8') as file:
                for subdata in data:
                    file.write(subdata.screen_name + '\n')


if __name__ == '__main__':
    getCredentials()
    main()

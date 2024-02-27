from requests import RequestException
from orange.utils import clear, setup
from orange.dashboard import dash


def main():
    clear()
    # try:
    if setup():
        dash()
    # except KeyboardInterrupt:
    #     print("👋 Goodbye")
    # except RequestException:
    #     print("❌ I can't reach the modem")
    # except:
    #     print("❌ an error occurred")
    
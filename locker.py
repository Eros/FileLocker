from filelock import Timeout, FileLock
from colorama import Fore
import argparse


def main():
    print(Fore.GREEN + 'GIT LOCKER\n' + Fore.LIGHTGREEN_EX + 'Run -h to get started' + Fore.RESET)

    parser = argparse.ArgumentParser('Commands for git-locker')
    parser.add_argument('-l', help='locks a file')
    parser.add_argument('-t', help='Time limit for the file to be locked')
    parser.add_argument('-pg', help='Prevent git from committing the file [F|T]')
    args = parser.parse_args()

    if not args.l or not args.t:
        print(Fore.RED + '[X] Invalid usage!')
        print(Fore.RED + '[+] ' + parser.usage + Fore.RESET)
    else:
        file_path = args.l
        lock_path = file_path + '.lock'
        timeout = args.t
        lock = FileLock(lock_file=lock_path)
        print(
            Fore.GREEN + '[+]' + Fore.LIGHTCYAN_EX + ' locked file ' + Fore.MAGENTA + lock_path + Fore.LIGHTCYAN_EX
            + ' for ' + Fore.MAGENTA + str(timeout))
        try:
            with lock.acquire(timeout=timeout):
                if not lock.is_locked and timeout == 0:
                    print(Fore.BLUE + '[*] Releasing lock!')
                    lock.release()
        except Timeout:
            print(Fore.RED + '[X] Another instance is currently holding a lock!')


if __name__ == '__main__':
    main()

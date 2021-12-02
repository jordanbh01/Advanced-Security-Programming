from queue import Queue
from socket import *
import threading

target = '127.0.0.1'
queue = Queue()


def portscan(port):
    try:
        sock = socket(AF_INET, SOCK_STREAM)
        sock.connect((target, port))
        return True
    except:
        return False


def get_ports(mode):
    if mode == 1:
        for port in range(1, 1024):
            queue.put(port)


def thread_worker():
    while not queue.empty():
        port = queue.get()
        if portscan(port):
            print("Port {} is open ".format(port))


def run_scanner(threads, mode):
    get_ports(mode)

    thread_list = []

    for t in range(threads):
        thread = threading.Thread(target=thread_worker)
        thread_list.append(thread)

    for thread in thread_list:
        thread.start()

    for thread in thread_list:
        thread.join()


def run():
    run_scanner(100, 1)


if __name__ == '__main__':
    run()

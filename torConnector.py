import requests
from stem import Signal
from stem.control import Controller
import stem.process

from stem.util import term


def print_bootstrap_lines(line):
  if "Bootstrapped " in line:
    print(term.format(line, term.Color.BLUE))

def launch_tor(port, controlPort, exitNodes):
    print(term.format("Starting Tor:\n", term.Attr.BOLD))
    try:
        tor_process = stem.process.launch_tor_with_config(
            config={
                'SocksPort': str(port),
                'ControlPort': str(controlPort),
                'HashedControlPassword': '16:05834BCEDD478D1060F1D7E2CE98E9C13075E8D3061D702F63BCD674DE', #password
                'ExitNodes' : exitNodes
            },
            init_msg_handler=print_bootstrap_lines,
        )

    except:
        print("Exception was raised!\n"
              "Killing tor instance...")
        tor_process.kill()  #cleanup messy tor connection
    return tor_process

def renew_connection(tor_control_port):
    with Controller.from_port(port = tor_control_port) as controller:
        controller.authenticate(password="password")
        controller.signal(Signal.NEWNYM)

def get_tor_session(tor_port):
    session = requests.session()
    session.proxies = {'http':  'socks5://127.0.0.1:'+str(tor_port),
                       'https': 'socks5://127.0.0.1:'+str(tor_port)}
    return session
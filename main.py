import torConnector as tc

tor_port = 9070
tor_control_port = 9073

exitNodes = {'619349D82424C601CAEB94161A4CF778993DAEE7', '7DD29A65C370B86B5BE706EA3B1417745714C8AF',
             '71CFDEB4D9E00CCC3E31EC4E8A29E109BBC1FB36', 'B84F248233FEA90CAD439F292556A3139F6E1B82'}


def main():
    tor_instance = tc.launch_tor(tor_port, tor_control_port, exitNodes)
    session = tc.get_tor_session(tor_port)
    try:
        print(session.get("http://httpbin.org/ip").text)
    except:
        print("Killed Tor in Exception")
        tor_instance.kill()
    tor_instance.kill()

    print(tc.term.format("\nKilled Tor!\n", tc.term.Attr.BOLD))

    tor_instance = tc.launch_tor(tor_port, tor_control_port, exitNodes)

    session = tc.get_tor_session(tor_port)
    try:
        print(session.get("http://httpbin.org/ip").text)
    except:
        print("Killed Tor in Exception")
        tor_instance.kill()
    tor_instance.kill()


if __name__ == '__main__':
    main()


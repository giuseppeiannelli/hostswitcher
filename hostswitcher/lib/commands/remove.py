import hostswitcher.lib

class remove_command(object):

    def __init__(self, args):
        self.path_hosts = hostswitcher.lib.hosts_path()
        print('run %s command' % __name__)
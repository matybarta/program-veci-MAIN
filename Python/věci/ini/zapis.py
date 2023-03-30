import configparser

config = configparser.ConfigParser()

config.add_section('FTP')

config['FTP']['host'] = '93.91.250.153'
config['FTP']['port'] = '27227'
config['FTP']['user'] = 'bramborak'
config['FTP']['password'] = "Bag3t!cka874"

with open('FTP_server.ini', 'w') as configfile:
    config.write(configfile)
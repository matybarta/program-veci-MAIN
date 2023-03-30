import configparser

config = configparser.ConfigParser()
config.read('FTP_server.ini')

print(config)
print(config.sections())

host = config['FTP']['host']
port = config['FTP']['port']
user = config['FTP']['user']
password = config['FTP']["password"]
print('FTP configuration:')

print(f'Host: {host}')
print(f'Port: {port}')
print(f'User: {user}')
print(f'Password: {password}')

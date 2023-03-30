import configparser

config = configparser.ConfigParser()
config.read('db.ini')

print(config)

sections = config.sections()
print(f'Sections: {sections}')

sections.append('sqlite')

for section in sections:

    if config.has_section(section):
      print(f'Config file has section {section}')
    else:
      print(f'Config file does not have section {section}')
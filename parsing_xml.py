import xml.parsers.expat


def start_element(name, attrs):
    print('Start element:', name, attrs)


def end_element(name):
    print('End element:', name)


def character_data(data):
    print('Character data: %s' % data)


parser = xml.parsers.expat.ParserCreate()
parser.StartElementHandler = start_element
parser.EndElementHandler = end_element
parser.CharacterDataHandler = character_data
parsed_file = parser.ParseFile(open("C:/Users/User/PycharmProjects/pytest/My_own_tests/test_data/response.xml", 'rb'))

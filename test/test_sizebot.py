import unittest

from configparser import ConfigParser

ID_SERVER1 = "Server1"
ID_SERVER2 = "Server2"


class MyTestCase(unittest.TestCase):
    size = [
        "1 mm",
        "1 cm",
        "1 inch",
        "3 inch",
        "6 inch",
        "1 foot",
        "3 foot",
        "6 foot",
        "12 foot",
        "50 foot",
        "100 foot",
        "200 foot",
        "400 foot",
        "500 foot",
        "600 foot",
        "800 foot",
        "1000 foot",
        "2000 foot",
        "3000 foot",
        "5000 foot"
    ]

    def test_sort(self):
        config = ConfigParser()
        config.add_section(ID_SERVER1)
        config[ID_SERVER1]['000002'] = self.size[2]
        config[ID_SERVER1]['000001'] = self.size[10]
        config[ID_SERVER1]['000003'] = self.size[7]

        this_list = {}
        for user in config.options(ID_SERVER1):
            this_list[user] = config[ID_SERVER1][user]
        self.assertEqual(len(this_list), 3)
        print(this_list)

        sorted_list = sorted(this_list, key=lambda x: self.size.index(this_list[x]), reverse=True)
        print(sorted_list)
        self.assertEqual(sorted_list[0], '000001')
        self.assertEqual(sorted_list[1], '000003')
        self.assertEqual(sorted_list[2], '000002')


if __name__ == '__main__':
    unittest.main()

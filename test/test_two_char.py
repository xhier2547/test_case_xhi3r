from two_char.two_char_utils import get_char
import unittest

class Two_Charaters(unittest.TestCase):
    def test_give_beabeefeab_is_5(self):
        string = 'beabeefeab'
        max_len = get_char(string)
        self.assertEqual(max_len, 5)

    def test_give_qwsdfg_is_2(self):
        string = 'qwsdfg'
        max_len = get_char(string)
        self.assertEqual(max_len, 2)

    def test_give_hxcbjz_is_2(self):
        string = 'hxcbjz'
        max_len = get_char(string)
        self.assertEqual(max_len, 2)

    def test_give_wwerghikolololollcvb_is_2(self):
        string = 'wwerghikolololollcvb'
        max_len = get_char(string)
        self.assertEqual(max_len, 2)

    def test_give___is_0(self):
        string = ''
        max_len = get_char(string)
        self.assertEqual(max_len, 0)

    def test_give_asdasadsadsadsdadads_is_0(self):
        string = 'asdasadsadsadsdadads'
        max_len = get_char(string)
        self.assertEqual(max_len, 0)

    def test_give_dtrfvygbuyhnijmk_is_3(self):
        string = 'dtrfvygbuyhnijmk'
        max_len = get_char(string)
        self.assertEqual(max_len, 3)

    def test_give_tlymrvjcylhqifsqtyyzfaugtibkkghfhyzxqbsizkjguqlqwwetyofqihtpkmpdlgthfybfhhmjerjdkybwppwrdapirukcshkpngayrdruanjtziknnwxmsjpnuswllymhkmztsrcwwzmlbcoakswwffveobbvzinkhnmvwqhpfednhsuzmffaebi_is_0(self):
        string = 'tlymrvjcylhqifsqtyyzfaugtibkkghfhyzxqbsizkjguqlqwwetyofqihtpkmpdlgthfybfhhmjerjdkybwppwrdapirukcshkpngayrdruanjtziknnwxmsjpnuswllymhkmztsrcwwzmlbcoakswwffveobbvzinkhnmvwqhpfednhsuzmffaebi'
        max_len = get_char(string)
        self.assertEqual(max_len, 0)

    def test_give_wsxcftghjuiooliuytredcvghjuikolkiuytrdvghjhgfdertyhfwsxcvghwqsdcvfghjkrfghj_(self):
        string = 'wsxcftghjuiooliuytredcvghjuikolkiuytrdvghjhgfdertyhfwsxcvghwqsdcvfghjkrfghj'
        max_len = get_char(string)
        self.assertEqual(max_len, 9)
from caesar.caesar import caesar_Cipher
import unittest

class Caesar_Cipher(unittest.TestCase):
    def test_give_Hello_World_and_4_is_Lipps_Asvph(self):
        string = 'Hello_World'
        number = 4
        encrypted = caesar_Cipher(string, number)
        self.assertEqual(encrypted, 'Lipps_Asvph')

    def test_give_159357lcfd_and_98_is_159357fwzx(self):
        string = '159357lcfd'
        number = 98
        encrypted = caesar_Cipher(string, number)
        self.assertEqual(encrypted, '159357fwzx')

    def test_give_6DWV95HzxTCHP85dvv3NY2crzt1aO8j6g2zSDvFUiJj6XWDlZvNNr_and_87_is_6MFE95QigCLQY85mee3WH2laic1jX8s6p2iBMeODrSs6GFMuIeWWa(self):
        string = '6DWV95HzxTCHP85dvv3NY2crzt1aO8j6g2zSDvFUiJj6XWDlZvNNr'
        number = 87
        encrypted = caesar_Cipher(string, number)
        self.assertEqual(encrypted, '6MFE95QigCLQY85mee3WH2laic1jX8s6p2iBMeODrSs6GFMuIeWWa')

    def test_give_Shirakamiiii_and_5000_is_Lipps_Apqzisiuqqqq(self):
        string = 'Shirakamiiii'
        number = 5000
        encrypted = caesar_Cipher(string, number)
        self.assertEqual(encrypted, 'Apqzisiuqqqq')

    def test_give_ArtifiCi8L_and_37_is_LcetqtNt8W(self):
        string = 'ArtifiCi8L'
        number = 37
        encrypted = caesar_Cipher(string, number)
        self.assertEqual(encrypted, 'LcetqtNt8W')

    def test_give_ertyhnmkuytdrrt12_and_45_is_xkmragfdnrmwkkm12(self):
        string = 'ertyhnmkuytdrrt12'
        number = 45
        encrypted = caesar_Cipher(string, number)
        self.assertEqual(encrypted, 'xkmragfdnrmwkkm12')

    def test_give_D3q5_and_0_is_D3q5(self):
        string = 'D3q5'
        number = 0
        encrypted = caesar_Cipher(string, number)
        self.assertEqual(encrypted, 'D3q5')

    def test_give_Ciphering_and_26_is_Ciphering(self):
        string = 'Ciphering'
        number = 26
        encrypted = caesar_Cipher(string, number)
        self.assertEqual(encrypted, 'Ciphering')
import unittest
import Bank


class TestBankTransaction(unittest.TestCase):
    def setUp(self):
        # create an instance bank
        self.bank = Bank()
    def test_if_savings_account_is_created(self):
        self.assertEqual(self.bank.create_account("denis juma", "savings", 1000), 
                         "A savings account is sucessfuly created for DENIS JUMA")

    def test_if_current_account_is_created(self):
        self.assertEqual(self.bank.create_account("denis juma", "current", 1000), 
                         "A current account is sucessfuly created for DENIS JUMA")

    def test_if_account_is_created_with_missing(self):
        self.assertEqual(self.bank.create_account("denis juma", " ", 1000), 
                         "Account not created please provide missing details")
        self.assertEqual(self.bank.create_account("christine nagadya", "current"), 
                         "Account not created please provide missing details")
        self.assertEqual(self.bank.create_account(" ", "savings", 1000), 
                         "Account not created please provide missing details")

    def test_if_account_type_is_valid(self):
        self.assertEqual(self.bank.create_account("denis juma", "checking", 1000), 
                         "checking is an invalid account type")

    def test_if_current_account_opening_ammount_is_valid(self):
        self.assertEqual(self.bank.create_account("denis juma", "current", 999), 
                         "Initial deposit should be 1000 or more")
        self.assertEqual(self.bank.create_account("sharon owino", "current", 0), 
                         "Initial deposit should be 1000 or more")
        self.assertEqual(self.bank.create_account("victor wamocha", "current", -1000), 
                         "Initial deposit should be 1000 or more")

    def test_if_one_can_make_deposits(self):
        self.bank.create_account("denis juma", "current", 1000)
        self.assertEqual(self.bank.deposit("denis juma", 4000), 
                         " 4000 has been deposited to DENIS JUMA's current account account balnce is 5000")
        self.assertEqual(self.bank.deposit("denis juma", 6000), 
                         " 6000 has been deposited to DENIS JUMA's current account account balnce is 11000")

    def test_if_one_can_make_deposits_on_a_non_existant_account(self):
        self.assertEqual(self.bank.deposit("Bob colimore", 4000), 
                         "BOB COLIMORE account does not exist")
    
    def test_if_you_can_deposit_less_than_zero_or_zero_ammount(self):
        self.bank.create_account("denis juma", "current", 1000)
        self.assertEqual(self.bank.deposit("sharon owino", 0), 
                         "deposit should be more than zero")
        self.assertEqual(self.bank.deposit("victor wamocha",-1000), 
                         "deposit should be more than zero")

    def test_if_one_can_make_widrawals(self):
        self.bank.create_account("denis juma", "current", 20000)
        self.assertEqual(self.bank.withdraw("denis juma", 4000), 
                         " 4000 has been withdrawn from DENIS JUMA's current account account balnce is 16000")
        self.assertEqual(self.bank.withdraw("denis juma", 6000), 
                         " 6000 has been witdrawn from DENIS JUMA's current account account balnce is 10000")

    def test_if_one_can_make_withdrawals_on_a_non_existant_account(self):
        self.assertEqual(self.bank.withdraw("Bob colimore", 4000), 
                         "BOB COLIMORE's account does not exist")
    
    def test_if_you_can_withdraw_less_than_zero_or_zero_ammount(self):
        self.bank.create_account("denis juma", "current", 2000)
        self.assertEqual(self.bank.withdraw("sharon owino", 0), 
                         "withdrawal should be more than zero")
        self.assertEqual(self.bank.withdraw("victor wamocha",-1000), 
                         "withdrawal should be more than zero")


    def test_if_you_can_withdraw_more_than_the_deposited_ammount_in_current_account(self):
        self.bank.create_account("david musila", "savings", 1000)
        self.assertEqual(self.bank.withdraw("David Musila", 5000), 
                         "Ammount in your account is insufficient")














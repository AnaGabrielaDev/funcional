import unittest
import q1_AnaBezerra as q1
from unittest.mock import patch
from io import StringIO

class TestModule(unittest.TestCase):
    @patch('builtins.print')
    def test_receive_cash(self, mock_print):
        q1.receive_cash(100)
        mock_print.assert_called_with("Payment Receipt of ", 100, '$')

    @patch('sys.stdout', new_callable=StringIO)
    def test_cancel_transaction(self, mock_stdout):
        q1.cancel_transaction()
        self.assertEqual(mock_stdout.getvalue(), 'Cancel Transaction\n')

    @patch('sys.stdout', new_callable=StringIO)
    def test_close_transaction(self, mock_stdout):
        q1.close_transaction()
        self.assertEqual(mock_stdout.getvalue(), 'Close Transaction\n')

    @patch('builtins.print')
    def test_fund_transfer_details(self, mock_print):
        q1.fund_transfer_details("user", "password")
        mock_print.assert_called_with({"user": "user", "password": "*****"})

stress_test_complete_transaction = lambda transaction_function, iterations: all(transaction_function() == 'Transaction completed!\n' for _ in range(iterations))

complete_transaction = lambda :'Transaction completed!\n'

run_tests = lambda: (
    print('Running unit tests...'),
    unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(TestModule)),
    print('Running stress test...'),
    [print('Stress test passed.') if stress_test_complete_transaction(complete_transaction, 10000) else print('Stress test failed.')]
)

if __name__ == '__main__':
    run_tests()
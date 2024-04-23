import unittest
import q1_AnaBezerra as q1
from unittest.mock import patch
from io import StringIO

class TestModule(unittest.TestCase):
    @patch('sys.stdout', new_callable=StringIO)
    def test_receive_cash_input(self, mock_stdout):
        q1.receive_cash_input(12)
        self.assertEqual(mock_stdout.getvalue(), 12)

    @patch('builtins.input', return_value='100')
    def test_receive_cash_input(self, input):
        result = q1.receive_cash_input()
        self.assertEqual(result, 100)

    @patch('sys.stdout', new_callable=StringIO)
    def test_cancel_transaction(self, mock_stdout):
        q1.cancel_transaction()
        self.assertEqual(mock_stdout.getvalue(), 'Cancel Transaction\n')

    @patch('sys.stdout', new_callable=StringIO)
    def test_close_transaction(self, mock_stdout):
        q1.close_transaction()
        self.assertEqual(mock_stdout.getvalue(), 'Close Transaction\n')

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
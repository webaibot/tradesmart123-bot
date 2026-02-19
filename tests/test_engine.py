import unittest
from bot.engine import TradingBot
from bot.models import SessionState

class TestTradingBot(unittest.TestCase):
    def setUp(self):
        self.bot = TradingBot()
        self.session_id = 'test_session'

    def test_process_message_initial(self):
        response = self.bot.process_message(self.session_id, 'portfolio')
        self.assertIn('Tracking portfolio', response)

    def test_process_message_risk(self):
        response = self.bot.process_message(self.session_id, 'risk')
        self.assertIn('Risk calculation', response)

    def test_session_management(self):
        self.bot.process_message(self.session_id, 'message 1')
        self.bot.process_message(self.session_id, 'message 2')
        self.assertEqual(self.bot.sessions[self.session_id].message_count, 2)

if __name__ == '__main__':
    unittest.main()
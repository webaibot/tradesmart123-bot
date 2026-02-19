from .models import SessionState, TradingIndicator
from .knowledge import trading_patterns, indicators_data
from .responses import generate_response
import random

class TradingBot:
    def __init__(self):
        self.sessions = {}

    def process_message(self, session_id: str, message: str) -> str:
        if session_id not in self.sessions:
            self.sessions[session_id] = SessionState()
        session = self.sessions[session_id]

        if 'portfolio' in message.lower():
            return self.track_portfolio(session)
        elif 'risk' in message.lower():
            return self.calculate_risk(session, message)
        else:
            return self.analyze_message(session, message)

    def track_portfolio(self, session: SessionState) -> str:
        return 'Tracking portfolio for user...'

    def calculate_risk(self, session: SessionState, message: str) -> str:
        return 'Risk calculation based on current market conditions.'

    def analyze_message(self, session: SessionState, message: str) -> str:
        analysis = []
        for indicator in indicators_data:
            if indicator in message.lower():
                analysis.append(f'{indicator}: {indicators_data[indicator]}')
        return generate_response(analysis)

    def get_statistics(self) -> dict:
        return {
            'total_sessions': len(self.sessions),
            'messages_processed': sum(session.message_count for session in self.sessions.values())
        }
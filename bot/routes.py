from flask import Blueprint, request, jsonify, render_template
from .engine import TradingBot

bp = Blueprint('bot', __name__)
bot = TradingBot()

@bp.route('/', methods=['GET'])
def index():
    return render_template('index.html', bot_name='TradeSmart Bot')

@bp.route('/api/chat', methods=['POST'])
def chat():
    data = request.json
    session_id = data.get('session_id')
    message = data.get('message')
    response = bot.process_message(session_id, message)
    return jsonify({'response': response})

@bp.route('/api/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'healthy'})

@bp.route('/api/stats', methods=['GET'])
def stats():
    return jsonify(bot.get_statistics())

def register_routes(app):
    app.register_blueprint(bp)
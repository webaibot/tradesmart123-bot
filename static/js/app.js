document.addEventListener('DOMContentLoaded', function() {
    const chatForm = document.getElementById('chat-form');
    const chatInput = document.getElementById('chat-input');
    const chatContainer = document.querySelector('.chat-container');

    chatForm.onsubmit = async function(e) {
        e.preventDefault();
        const message = chatInput.value;
        if (!message) return;

        appendMessage('You', message);
        chatInput.value = '';

        const response = await fetch('/api/chat', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ session_id: getSessionId(), message })
        });

        const data = await response.json();
        appendMessage('TradeSmart Bot', data.response);
    };

    function appendMessage(sender, message) {
        const messageBubble = document.createElement('div');
        messageBubble.className = 'bubble';
        messageBubble.textContent = `${sender}: ${message}`;
        chatContainer.appendChild(messageBubble);
        chatContainer.scrollTop = chatContainer.scrollHeight;
    }

    function getSessionId() {
        let sessionId = sessionStorage.getItem('sessionId');
        if (!sessionId) {
            sessionId = 'session_' + Math.random().toString(36).substr(2, 9);
            sessionStorage.setItem('sessionId', sessionId);
        }
        return sessionId;
    }
});
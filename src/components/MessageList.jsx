import MessageBubble from './MessageBubble'

function MessageList({ messages, isSending }) {
    return (
        <section className="message-list" aria-live="polite" aria-label="Conversation">
        {messages.map((message) => (
            <MessageBubble key={message.id} message={message} />
        ))}
        {isSending && (
            <div className="message-row">
            <div className="message-bubble message-bubble-pending">
                <span className="message-label">Assistant</span>
                <p>Thinking...</p>
            </div>
            </div>
        )}
        </section>
    )
}

export default MessageList

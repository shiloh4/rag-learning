function MessageBubble({ message }) {
    const isUser = message.role === 'user'

    return (
        <article className={`message-row ${isUser ? 'message-row-user' : ''}`}>
        <div className={`message-bubble ${isUser ? 'message-bubble-user' : ''}`}>
            <span className="message-label">{isUser ? 'You' : 'Assistant'}</span>
            <p>{message.content}</p>
        </div>
        </article>
    )
}

export default MessageBubble

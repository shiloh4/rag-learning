function ChatComposer({ draft, error, isSending, onChange, onSubmit }) {
    function handleKeyDown(event) {
        if (event.key === 'Enter' && !event.shiftKey) {
        event.preventDefault()
        onSubmit(event)
        }
    }

    return (
        <div className="composer-wrap">
        <form className="chat-composer" onSubmit={onSubmit}>
            <label className="sr-only" htmlFor="chat-message">
            Message
            </label>
            <textarea
            id="chat-message"
            value={draft}
            onChange={(event) => onChange(event.target.value)}
            onKeyDown={handleKeyDown}
            placeholder="Ask a question..."
            rows="1"
            disabled={isSending}
            />
            <button type="submit" disabled={!draft.trim() || isSending}>
            {isSending ? 'Sending' : 'Send'}
            </button>
        </form>
        {error && <p className="composer-error" role="alert">{error}</p>}
        <p className="composer-hint">Press Enter to send. Use Shift + Enter for a new line.</p>
        </div>
    )
}

export default ChatComposer

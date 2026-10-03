function ChatHeader({ onReset }) {
    return (
        <header className="chat-header">
        <div>
            <p className="eyebrow">RAG learning workspace</p>
            <h1>Ask the library</h1>
            <p className="header-description">A focused space for exploring your knowledge base.</p>
        </div>
        <button className="reset-button" type="button" onClick={onReset}>
            New chat
        </button>
        </header>
    )
}

export default ChatHeader

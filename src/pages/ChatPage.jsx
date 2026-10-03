import { useState } from 'react'
import ChatComposer from '../components/ChatComposer'
import ChatHeader from '../components/ChatHeader'
import MessageList from '../components/MessageList'
import { sendMessage } from '../services/chatService'

const initialMessages = [
    {
        id: 'welcome',
        role: 'assistant',
        content:
        'Hi, I am your learning assistant. Ask me about retrieval, embeddings, or anything in this project.',
    },
]

function ChatPage() {
    const [messages, setMessages] = useState(initialMessages)
    const [draft, setDraft] = useState('')
    const [isSending, setIsSending] = useState(false)
    const [error, setError] = useState('')

    async function handleSubmit(event) {
        event?.preventDefault()
        const content = draft.trim()

        if (!content || isSending) {
        return
        }

        const userMessage = {
        id: crypto.randomUUID(),
        role: 'user',
        content,
        }

        setMessages((currentMessages) => [...currentMessages, userMessage])
        setDraft('')
        setError('')
        setIsSending(true)

        try {
        const reply = await sendMessage({
            message: content,
                history: [...messages, userMessage],
        })

        setMessages((currentMessages) => [
            ...currentMessages,
            {
            id: crypto.randomUUID(),
            role: 'assistant',
            content: reply,
            },
        ])
        } catch (requestError) {
        setError(requestError.message)
        } finally {
        setIsSending(false)
        }
    }

    function handleReset() {
        setMessages(initialMessages)
        setDraft('')
        setError('')
    }

    return (
        <main className="chat-shell">
        <ChatHeader onReset={handleReset} />
        <MessageList messages={messages} isSending={isSending} />
        <ChatComposer
            draft={draft}
            error={error}
            isSending={isSending}
            onChange={setDraft}
            onSubmit={handleSubmit}
        />
        </main>
    )
}

export default ChatPage

const apiBaseUrl = import.meta.env.VITE_API_BASE_URL

export async function sendMessage({ message, history }) {
  if (!apiBaseUrl) {
    throw new Error('The chat API is not configured. Add VITE_API_BASE_URL to your frontend environment.')
  }

  const response = await fetch(`${apiBaseUrl}/chat`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ message, history }),
  })

  if (!response.ok) {
    throw new Error('The assistant could not respond. Please try again.')
  }

  const data = await response.json()

  if (!data.reply || typeof data.reply !== 'string') {
    throw new Error('The chat API returned an unexpected response.')
  }

  return data.reply
}

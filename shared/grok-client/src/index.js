/**
 * grok-client — xAI Grok API wrapper for x-platform-toolkit
 * Part of the grok-install family · Apache 2.0
 */

const API_BASE = 'https://api.x.ai/v1';

class GrokClient {
  constructor({ apiKey, model = 'grok-2-latest' } = {}) {
    this.apiKey = apiKey || process.env.XAI_API_KEY;
    this.model = model;
    if (!this.apiKey) {
      throw new Error('XAI_API_KEY required. Set env var or pass apiKey option.');
    }
  }

  async chat(messages, { temperature = 0.7, maxTokens = 1024 } = {}) {
    const res = await fetch(`${API_BASE}/chat/completions`, {
      method: 'POST',
      headers: {
        'Authorization': `Bearer ${this.apiKey}`,
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        model: this.model,
        messages,
        temperature,
        max_tokens: maxTokens
      })
    });

    if (!res.ok) {
      const body = await res.text();
      throw new Error(`Grok API ${res.status}: ${body}`);
    }

    const data = await res.json();
    return data.choices[0].message.content;
  }

  async complete(prompt, options = {}) {
    return this.chat([{ role: 'user', content: prompt }], options);
  }
}

module.exports = GrokClient;

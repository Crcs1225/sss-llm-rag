<template>
  <div class="home-bg">
    <!-- Not Started State -->
    <div v-if="!hasStarted" class="welcome-container">
      <h1 class="welcome-title">Welcome to SSS AI Assistant</h1>
      <p class="welcome-description">
        AI powered chat assistant for SSS queries. Get instant answers about
        benefits, contributions, and more.
      </p>
      <div class="welcome-input-wrapper">
        <input
          v-model="input"
          @keyup.enter="sendPrompt"
          placeholder="Ask something about SSS..."
          class="welcome-input"
        />
        <button @click="sendPrompt" class="welcome-send">Send</button>
      </div>
    </div>

    <!-- Started State -->
    <template v-else>
      <!-- Header -->
      <div class="chat-header">
        <h2 class="chat-title">SSS AI Assistant</h2>
      </div>

      <!-- Scrollable Chat History -->
      <div class="chat-history" ref="chatHistory">
        <div
          v-for="(msg, index) in messages"
          :key="index"
          :class="['chat-bubble', msg.role]"
        >
          <span>{{ msg.text }}</span>

          <!-- Show sources if available -->
          <div
            v-if="msg.sources && msg.sources.length > 0"
            class="message-sources"
          >
            <div class="sources-label">Sources:</div>
            <div
              v-for="(source, idx) in msg.sources"
              :key="idx"
              class="source-item"
            >
              {{ source }}
            </div>
          </div>

          <!-- Show response metadata -->
          <div v-if="msg.response_time" class="message-meta">
            <span class="meta-item">Model: {{ msg.model_used }}</span>
            <span class="meta-item">Time: {{ msg.response_time }}s</span>
          </div>
        </div>
      </div>

      <!-- Fixed Input Footer -->
      <div class="chat-input-wrapper">
        <div class="chat-input-container">
          <input
            v-model="input"
            @keyup.enter="sendPrompt"
            placeholder="Ask something about SSS..."
            class="chat-input"
          />
          <button @click="sendPrompt" class="chat-send">Send</button>
        </div>
      </div>
    </template>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "HomeView",
  props: {
    messages: {
      type: Array,
      default: () => [],
    },
    hasStarted: {
      type: Boolean,
      default: false,
    },
  },
  data() {
    return {
      input: "",
      // Get API URL from environment variable
      apiBaseUrl: process.env.VUE_APP_API_URL || "http://127.0.0.1:8000",
    };
  },
  methods: {
    async sendPrompt() {
      const prompt = this.input.trim();
      if (!prompt) return;

      if (!this.hasStarted) {
        this.$emit("update-started", true);
      }

      const newMessages = [...this.messages, { role: "user", text: prompt }];
      this.$emit("update-messages", newMessages);
      this.input = "";

      // Scroll to bottom after adding message
      this.$nextTick(() => {
        this.scrollToBottom();
      });

      // Add typing indicator
      const typingMessages = [
        ...newMessages,
        { role: "bot", text: "Typing..." },
      ];
      this.$emit("update-messages", typingMessages);

      try {
        // Get saved settings
        const selectedModel =
          localStorage.getItem("selectedModel") || "mistral";
        const maxTokens = parseInt(localStorage.getItem("maxTokens")) || 256;
        const temperature =
          parseFloat(localStorage.getItem("temperature")) || 0.7;

        const res = await axios.post(`${this.apiBaseUrl}/chat`, {
          query: prompt,
          model: selectedModel,
          temperature: temperature,
          max_tokens: maxTokens,
          use_rag: true,
        });

        // Remove typing indicator and add response
        const finalMessages = [
          ...newMessages,
          {
            role: "bot",
            text: res.data.answer,
            sources: res.data.sources || [],
            model_used: res.data.model_used,
            response_time: res.data.response_time,
          },
        ];
        this.$emit("update-messages", finalMessages);

        // Scroll to bottom after bot response
        this.$nextTick(() => {
          this.scrollToBottom();
        });
      } catch (err) {
        console.error("Chat error:", err);
        // More detailed error message
        let errorMessage = "❌ Something went wrong. ";
        if (err.response) {
          // Server responded with error
          errorMessage += err.response.data?.detail || err.response.statusText;
        } else if (err.request) {
          // No response from server
          errorMessage +=
            "Cannot connect to the server. Please check if the API is running.";
        } else {
          // Other error
          errorMessage += err.message;
        }
        const errorMessages = [
          ...newMessages,
          {
            role: "bot",
            text: errorMessage,
          },
        ];
        this.$emit("update-messages", errorMessages);
      }
    },
    scrollToBottom() {
      if (this.$refs.chatHistory) {
        this.$refs.chatHistory.scrollTop = this.$refs.chatHistory.scrollHeight;
      }
    },
  },
  watch: {
    messages() {
      // Scroll to bottom when messages change
      this.$nextTick(() => {
        this.scrollToBottom();
      });
    },
  },
};
</script>

<style scoped>
.home-bg {
  height: 100vh;
  background: linear-gradient(135deg, #e0e7ff 0%, #f8fafc 100%);
  display: flex;
  flex-direction: column;
  position: relative;
  overflow: hidden;
}

/* Welcome State Styles */
.welcome-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 100%;
  padding: 2rem;
  text-align: center;
}

.welcome-title {
  font-size: 3rem;
  font-weight: 700;
  margin-bottom: 1.5rem;
  background: linear-gradient(135deg, #6366f1 0%, #818cf8 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.welcome-description {
  font-size: 1.25rem;
  color: #64748b;
  max-width: 600px;
  margin-bottom: 3rem;
  line-height: 1.6;
}

.welcome-input-wrapper {
  display: flex;
  gap: 0.75rem;
  width: 100%;
  max-width: 600px;
  background: rgba(255, 255, 255, 0.9);
  padding: 1.5rem;
  border-radius: 2rem;
  box-shadow: 0 8px 32px rgba(99, 102, 241, 0.1);
  backdrop-filter: blur(10px);
}

.welcome-input {
  flex: 1;
  padding: 1rem 1.5rem;
  border-radius: 1.5rem;
  border: 2px solid #e5e7eb;
  background: #fff;
  font-size: 1.125rem;
  transition: all 0.2s;
}

.welcome-input:focus {
  border-color: #6366f1;
  outline: none;
  box-shadow: 0 0 0 3px rgba(99, 102, 241, 0.1);
}

.welcome-send {
  padding: 1rem 2.5rem;
  border-radius: 1.5rem;
  border: none;
  background: linear-gradient(135deg, #6366f1 0%, #818cf8 100%);
  color: white;
  font-weight: 600;
  font-size: 1.125rem;
  cursor: pointer;
  transition: all 0.2s;
  white-space: nowrap;
}

.welcome-send:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(99, 102, 241, 0.3);
}

/* Chat State Styles */
.chat-header {
  padding: 1.5rem 2rem;
  text-align: center;
}

.chat-title {
  font-size: 1.75rem;
  font-weight: 700;
  margin: 0;
  background: linear-gradient(135deg, #6366f1 0%, #818cf8 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

/* Scrollable Chat History */
.chat-history {
  flex: 1;
  overflow-y: auto;
  padding: 1rem 1.5rem 8rem 1.5rem;
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
  max-width: 800px;
  width: 100%;
  margin: 0 auto;
  scrollbar-width: thin;
  scrollbar-color: #cbd5e1 transparent;
}

.chat-history::-webkit-scrollbar {
  width: 6px;
}

.chat-history::-webkit-scrollbar-track {
  background: transparent;
}

.chat-history::-webkit-scrollbar-thumb {
  background: #cbd5e1;
  border-radius: 3px;
}

/* Chat Bubbles */
.chat-bubble {
  padding: 0.875rem 1.25rem;
  border-radius: 1.25rem;
  max-width: 70%;
  word-wrap: break-word;
  font-size: 1rem;
  line-height: 1.5;
  animation: fadeIn 0.3s ease;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
}

.chat-bubble.user {
  align-self: flex-end;
  background: linear-gradient(135deg, #6366f1 0%, #818cf8 100%);
  color: white;
  border-bottom-right-radius: 0.25rem;
}

.chat-bubble.bot {
  align-self: flex-start;
  background: #fff;
  color: #1e293b;
  border-bottom-left-radius: 0.25rem;
}

/* Fixed Input Container */
.chat-input-wrapper {
  position: fixed;
  bottom: 0;
  left: 0;
  right: 0;
  padding: 1.5rem;
  z-index: 100;
}

.chat-input-container {
  max-width: 800px;
  width: 100%;
  margin: 0 auto;
  display: flex;
  gap: 0.75rem;
  background: rgba(255, 255, 255, 0.95);
  padding: 1.25rem;
  border-radius: 2rem;
  box-shadow: 0 4px 24px rgba(0, 0, 0, 0.08);
  backdrop-filter: blur(10px);
  border: 1px solid rgba(99, 102, 241, 0.1);
}

.chat-input {
  flex: 1;
  padding: 1rem 1.5rem;
  border-radius: 1.5rem;
  border: 2px solid #e5e7eb;
  background: #fff;
  font-size: 1rem;
  transition: all 0.2s;
}

.chat-input:focus {
  border-color: #6366f1;
  outline: none;
  box-shadow: 0 0 0 3px rgba(99, 102, 241, 0.1);
}

.chat-send {
  padding: 1rem 2rem;
  border-radius: 1.5rem;
  border: none;
  background: linear-gradient(135deg, #6366f1 0%, #818cf8 100%);
  color: white;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s;
  white-space: nowrap;
}

.chat-send:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(99, 102, 241, 0.3);
}
/* Message sources */
.message-sources {
  margin-top: 0.5rem;
  padding-top: 0.5rem;
  border-top: 1px solid rgba(255, 255, 255, 0.2);
  font-size: 0.875rem;
  opacity: 0.8;
}

.chat-bubble.bot .message-sources {
  border-top-color: rgba(0, 0, 0, 0.1);
}

.sources-label {
  font-weight: 600;
  margin-bottom: 0.25rem;
}

.source-item {
  font-size: 0.75rem;
  margin-left: 0.5rem;
  opacity: 0.7;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

/* Message metadata */
.message-meta {
  margin-top: 0.5rem;
  padding-top: 0.5rem;
  border-top: 1px solid rgba(255, 255, 255, 0.2);
  font-size: 0.75rem;
  opacity: 0.6;
  display: flex;
  gap: 1rem;
}

.chat-bubble.bot .message-meta {
  border-top-color: rgba(0, 0, 0, 0.1);
}

.meta-item {
  display: inline-block;
}

/* Animations */
@keyframes fadeIn {
  from {
    opacity: 0;
    transform: translateY(10px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

/* Responsive */
@media (max-width: 768px) {
  .welcome-title {
    font-size: 2rem;
  }

  .welcome-description {
    font-size: 1rem;
  }

  .welcome-input-wrapper {
    flex-direction: column;
    padding: 1.25rem;
  }

  .welcome-input,
  .welcome-send {
    width: 100%;
  }

  .chat-title {
    font-size: 1.5rem;
  }

  .chat-history {
    padding: 0.5rem 1rem 7rem 1rem;
  }

  .chat-bubble {
    max-width: 85%;
    font-size: 0.9375rem;
  }

  .chat-input-wrapper {
    padding: 1rem;
  }

  .chat-input-container {
    padding: 1rem;
  }

  .chat-input {
    padding: 0.875rem 1rem;
    font-size: 0.9375rem;
  }

  .chat-send {
    padding: 0.875rem 1.5rem;
    font-size: 0.9375rem;
  }
}

/* Account for sidebar on desktop */
@media (min-width: 769px) {
  .chat-input-wrapper {
    left: 80px; /* Sidebar width */
  }
}
</style>

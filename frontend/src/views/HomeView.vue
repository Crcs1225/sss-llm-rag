<template>
  <div class="home-container">
    <!-- Initial View (Search Style) -->
    <div v-if="!hasStarted" class="search-bar-container">
      <input
        v-model="input"
        @keyup.enter="sendPrompt"
        placeholder="Ask something about SSS..."
        class="search-bar"
      />
      <button @click="sendPrompt">Send</button>
    </div>

    <!-- Chat View -->
    <transition name="fade">
      <div v-if="hasStarted" class="chat-container">
        <div class="chat-history">
          <div
            v-for="(msg, index) in messages"
            :key="index"
            :class="['chat-bubble', msg.role]"
          >
            <span>{{ msg.text }}</span>
          </div>
        </div>

        <div class="chat-input">
          <input
            v-model="input"
            @keyup.enter="sendPrompt"
            placeholder="Type your message..."
          />
          <button @click="sendPrompt">Send</button>
        </div>
      </div>
    </transition>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "HomeView",
  data() {
    return {
      input: "",
      messages: [],
      hasStarted: false,
    };
  },
  methods: {
    async sendPrompt() {
      const prompt = this.input.trim();
      if (!prompt) return;

      this.hasStarted = true;
      this.messages.push({ role: "user", text: prompt });
      this.input = "";

      // Simulate loading (replace with your FastAPI call)
      this.messages.push({ role: "bot", text: "Typing..." });

      try {
        const res = await axios.post("http://localhost:8000/ask", {
          query: prompt,
        });
        this.messages.pop(); // Remove "Typing..."
        this.messages.push({ role: "bot", text: res.data.answer });
      } catch (err) {
        this.messages.pop();
        this.messages.push({ role: "bot", text: "❌ Something went wrong." });
      }
    },
  },
};
</script>

<style scoped>
.home-container {
  max-width: 800px;
  margin: auto;
  padding: 2rem;
}

.search-bar-container {
  display: flex;
  justify-content: center;
  gap: 0.5rem;
}

.search-bar {
  width: 70%;
  padding: 0.75rem;
  font-size: 1rem;
}

.chat-container {
  display: flex;
  flex-direction: column;
  height: 80vh;
}

.chat-history {
  flex-grow: 1;
  overflow-y: auto;
  margin-bottom: 1rem;
}

.chat-bubble {
  padding: 0.75rem 1rem;
  margin: 0.5rem 0;
  border-radius: 1rem;
  max-width: 70%;
  word-wrap: break-word;
}

.chat-bubble.user {
  align-self: flex-end;
  background-color: #007bff;
  color: white;
}

.chat-bubble.bot {
  align-self: flex-start;
  background-color: #f1f1f1;
  color: #333;
}

.chat-input {
  display: flex;
  gap: 0.5rem;
}

.chat-input input {
  flex-grow: 1;
  padding: 0.75rem;
}

.chat-input button {
  padding: 0.75rem 1rem;
}

.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.4s ease;
}
.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}
</style>

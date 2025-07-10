<!-- src/views/SettingsView.vue -->
<template>
  <div class="settings-view">
    <div class="settings-header">
      <h1>Settings</h1>
      <p class="settings-subtitle">Configure your free LLM model preferences</p>
    </div>

    <div class="settings-content">
      <!-- Model Selection Section -->
      <section class="settings-section">
        <h2 class="section-title">Free LLM Model Selection</h2>
        <p class="section-description">
          Choose from available open-source and free language models
        </p>

        <div class="model-grid">
          <div
            v-for="model in availableModels"
            :key="model.id"
            :class="['model-card', { active: selectedModel === model.id }]"
            @click="selectModel(model.id)"
          >
            <div class="model-header">
              <div class="model-icon">
                <svg viewBox="0 0 24 24" fill="currentColor">
                  <path
                    d="M12 2L2 7v10c0 5.55 3.84 10.74 9 12 5.16-1.26 9-6.45 9-12V7l-10-5z"
                  />
                </svg>
              </div>
              <div class="model-info">
                <h3 class="model-name">{{ model.name }}</h3>
                <span class="model-type">{{ model.type }}</span>
              </div>
            </div>

            <p class="model-description">{{ model.description }}</p>

            <div class="model-specs">
              <div class="spec">
                <span class="spec-label">Size:</span>
                <span class="spec-value">{{ model.size }}</span>
              </div>
              <div class="spec">
                <span class="spec-label">RAM:</span>
                <span class="spec-value">{{ model.ram }}</span>
              </div>
            </div>

            <div class="model-features">
              <div
                class="feature"
                v-for="feature in model.features"
                :key="feature"
              >
                <svg
                  class="feature-icon"
                  viewBox="0 0 20 20"
                  fill="currentColor"
                >
                  <path
                    fill-rule="evenodd"
                    d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z"
                    clip-rule="evenodd"
                  />
                </svg>
                <span>{{ feature }}</span>
              </div>
            </div>

            <div class="model-footer">
              <span class="free-badge">
                <svg class="badge-icon" viewBox="0 0 20 20" fill="currentColor">
                  <path
                    fill-rule="evenodd"
                    d="M5 2a2 2 0 00-2 2v14l3.5-2 3.5 2 3.5-2 3.5 2V4a2 2 0 00-2-2H5zm4.707 3.707a1 1 0 00-1.414-1.414l-3 3a1 1 0 000 1.414l3 3a1 1 0 001.414-1.414L8.414 9H10a3 3 0 013 3v1a1 1 0 102 0v-1a5 5 0 00-5-5H8.414l1.293-1.293z"
                    clip-rule="evenodd"
                  />
                </svg>
                Free
              </span>
              <button
                v-if="selectedModel === model.id"
                class="selected-badge"
                disabled
              >
                Active
              </button>
            </div>
          </div>
        </div>
      </section>

      <!-- API Configuration -->
      <section class="settings-section">
        <h2 class="section-title">API Configuration</h2>

        <div class="api-config">
          <div class="config-item">
            <label>API Endpoint</label>
            <input
              v-model="apiConfig.endpoint"
              placeholder="http://localhost:8000"
              @change="updateConfig"
            />
          </div>

          <div class="config-item">
            <label>Max Tokens</label>
            <input
              type="number"
              v-model="apiConfig.maxTokens"
              min="50"
              max="4096"
              @change="updateConfig"
            />
          </div>

          <div class="config-item">
            <label>Temperature</label>
            <div class="slider-container">
              <input
                type="range"
                min="0"
                max="1"
                step="0.1"
                v-model="apiConfig.temperature"
                @change="updateConfig"
              />
              <span class="slider-value">{{ apiConfig.temperature }}</span>
            </div>
          </div>
        </div>
      </section>
      <!-- Add this after the API Configuration section -->
      <section class="settings-section" v-if="systemInfo">
        <h2 class="section-title">System Status</h2>
        <div class="system-status">
          <div class="status-grid">
            <div class="status-item">
              <span class="status-label">LLM Status:</span>
              <span
                :class="[
                  'status-value',
                  systemInfo.llm_loaded ? 'success' : 'error',
                ]"
              >
                {{ systemInfo.llm_loaded ? "✓ Loaded" : "✗ Not Loaded" }}
              </span>
            </div>
            <div class="status-item">
              <span class="status-label">ChromaDB:</span>
              <span
                :class="[
                  'status-value',
                  systemInfo.chromadb_loaded ? 'success' : 'error',
                ]"
              >
                {{ systemInfo.chromadb_loaded ? "✓ Loaded" : "✗ Not Loaded" }}
              </span>
            </div>
            <div class="status-item">
              <span class="status-label">Embedder:</span>
              <span
                :class="[
                  'status-value',
                  systemInfo.embedder_loaded ? 'success' : 'error',
                ]"
              >
                {{ systemInfo.embedder_loaded ? "✓ Loaded" : "✗ Not Loaded" }}
              </span>
            </div>
          </div>
        </div>
      </section>

      <!-- Test Connection -->
      <section class="settings-section">
        <h2 class="section-title">Test Configuration</h2>
        <div class="test-section">
          <button
            @click="testConnection"
            class="test-button"
            :disabled="testing"
          >
            <svg
              v-if="!testing"
              class="button-icon"
              viewBox="0 0 20 20"
              fill="currentColor"
            >
              <path
                fill-rule="evenodd"
                d="M10 18a8 8 0 100-16 8 8 0 000 16zM9.555 7.168A1 1 0 008 8v4a1 1 0 001.555.832l3-2a1 1 0 000-1.664l-3-2z"
                clip-rule="evenodd"
              />
            </svg>
            <svg
              v-else
              class="button-icon spinning"
              viewBox="0 0 20 20"
              fill="currentColor"
            >
              <path
                fill-rule="evenodd"
                d="M4 2a1 1 0 011 1v2.101a7.002 7.002 0 0111.601 2.566 1 1 0 11-1.885.666A5.002 5.002 0 005.999 7H9a1 1 0 010 2H4a1 1 0 01-1-1V3a1 1 0 011-1zm.008 9.057a1 1 0 011.276.61A5.002 5.002 0 0014.001 13H11a1 1 0 110-2h5a1 1 0 011 1v5a1 1 0 11-2 0v-2.101a7.002 7.002 0 01-11.601-2.566 1 1 0 01.61-1.276z"
                clip-rule="evenodd"
              />
            </svg>
            {{ testing ? "Testing..." : "Test Connection" }}
          </button>

          <div v-if="testResult" class="test-result" :class="testResult.status">
            <svg class="result-icon" viewBox="0 0 20 20" fill="currentColor">
              <path
                v-if="testResult.status === 'success'"
                fill-rule="evenodd"
                d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z"
                clip-rule="evenodd"
              />
              <path
                v-else
                fill-rule="evenodd"
                d="M10 18a8 8 0 100-16 8 8 0 000 16zM8.707 7.293a1 1 0 00-1.414 1.414L8.586 10l-1.293 1.293a1 1 0 101.414 1.414L10 11.414l1.293 1.293a1 1 0 001.414-1.414L11.414 10l1.293-1.293a1 1 0 00-1.414-1.414L10 8.586 8.707 7.293z"
                clip-rule="evenodd"
              />
            </svg>
            <span>{{ testResult.message }}</span>
          </div>
        </div>
      </section>

      <!-- Save Button -->
      <div class="action-buttons">
        <button @click="saveSettings" class="save-button">Save Settings</button>
        <button @click="resetSettings" class="reset-button">
          Reset to Default
        </button>
      </div>

      <!-- Save Status -->
      <div v-if="saveStatus" class="save-status" :class="saveStatus">
        <svg class="status-icon" viewBox="0 0 20 20" fill="currentColor">
          <path
            v-if="saveStatus === 'success'"
            fill-rule="evenodd"
            d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z"
            clip-rule="evenodd"
          />
          <path
            v-else
            fill-rule="evenodd"
            d="M10 18a8 8 0 100-16 8 8 0 000 16zM8.707 7.293a1 1 0 00-1.414 1.414L8.586 10l-1.293 1.293a1 1 0 101.414 1.414L10 11.414l1.293 1.293a1 1 0 001.414-1.414L11.414 10l1.293-1.293a1 1 0 00-1.414-1.414L10 8.586 8.707 7.293z"
            clip-rule="evenodd"
          />
        </svg>
        <span>{{
          saveStatus === "success"
            ? "Settings saved successfully!"
            : "Failed to save settings"
        }}</span>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
const MODEL_METADATA = {
  deepseek: {
    name: "DeepSeek R1",
    size: "~7B params",
    ram: "API-based",
    description:
      "Advanced reasoning model from DeepSeek with strong analytical capabilities and complex problem-solving abilities.",
    features: [
      "Excellent reasoning",
      "Complex analysis",
      "Multi-step thinking",
      "High accuracy",
    ],
  },
  llama: {
    name: "Llama 3.1 8B Instruct",
    size: "8B params",
    ram: "API-based",
    description:
      "Meta's latest Llama model optimized for instruction following and conversational tasks.",
    features: [
      "Fast responses",
      "Great for chat",
      "Multilingual support",
      "Reliable outputs",
    ],
  },
  mistral: {
    name: "Mistral 7B Instruct",
    size: "7B params",
    ram: "API-based",
    description:
      "Efficient and powerful open model from Mistral AI, optimized for instruction-following tasks.",
    features: [
      "Balanced performance",
      "Good reasoning",
      "Efficient processing",
      "Versatile capabilities",
    ],
  },
};
export default {
  name: "SettingsView",
  data() {
    return {
      selectedModel: localStorage.getItem("selectedModel") || "tinyllama",
      saveStatus: null,
      testing: false,
      testResult: null,
      systemInfo: null,
      apiBaseUrl: process.env.VUE_APP_API_URL || "http://127.0.0.1:8000",
      apiConfig: {
        maxTokens: parseInt(localStorage.getItem("maxTokens")) || 256,
        temperature: parseFloat(localStorage.getItem("temperature")) || 0.7,
      },
      availableModels: [],
      currentModelInfo: null,
    };
  },
  // ADD THIS - This is what's missing!
  async mounted() {
    console.log("Settings component mounted");
    console.log("Using API URL:", this.apiBaseUrl);
    // Load available models from API
    await this.loadModels();
    // Get system health
    await this.checkHealth();
  },
  methods: {
    async loadModels() {
      console.log("Loading models from:", this.apiBaseUrl);
      try {
        const response = await axios.get(`${this.apiBaseUrl}/models`);
        console.log("Models response:", response.data);

        // Update available models from API
        this.availableModels = response.data.available_models.map((model) => {
          const meta = MODEL_METADATA[model.id] || {};
          return {
            id: model.id,
            name: meta.name || model.id,
            type: "Cloud API",
            size: meta.size || "Unknown",
            ram: meta.ram || "API-based",
            provider: model.provider || "Unknown",
            description:
              meta.description || `${model.model} via ${model.provider}`,
            features: meta.features || [],
            status: model.status || "available",
          };
        });

        // Don't override the selected model from localStorage!
        const storedModel = localStorage.getItem("selectedModel");
        if (!storedModel && response.data.current_model) {
          this.selectedModel = response.data.current_model;
        }
        console.log("Selected model after load:", this.selectedModel);
      } catch (error) {
        console.error("Failed to load models:", error);
        // Fallback models if API fails
        this.availableModels = [
          {
            id: "mistral",
            name: "Mistral 7B Instruct",
            type: "Cloud API",
            size: "7B params",
            ram: "API-based",
            provider: "novita",
            description:
              "Efficient and powerful open model from Mistral AI, optimized for instruction-following tasks.",
            features: [
              "Balanced performance",
              "Good reasoning",
              "Efficient processing",
            ],
            status: "available",
          },
          {
            id: "deepseek",
            name: "DeepSeek R1",
            type: "Cloud API",
            size: "~7B params",
            ram: "API-based",
            provider: "fireworks",
            description:
              "Advanced reasoning model with strong analytical capabilities.",
            features: [
              "Excellent reasoning",
              "Complex analysis",
              "High accuracy",
            ],
            status: "available",
          },
          {
            id: "llama",
            name: "Llama 3.1 8B Instruct",
            type: "Cloud API",
            size: "8B params",
            ram: "API-based",
            provider: "fireworks",
            description:
              "Meta's latest Llama model optimized for instruction following.",
            features: [
              "Fast responses",
              "Great for chat",
              "Multilingual support",
            ],
            status: "available",
          },
        ];
      }
    },

    selectModel(modelId) {
      console.log("Selecting model:", modelId);
      this.selectedModel = modelId;
      this.saveStatus = null;
      this.$forceUpdate();
    },

    async checkHealth() {
      try {
        const response = await axios.get(`${this.apiBaseUrl}/health`);
        this.systemInfo = response.data;
      } catch (error) {
        console.error("Health check failed:", error);
      }
    },

    async testConnection() {
      this.testing = true;
      this.testResult = null;

      try {
        // Test health endpoint
        const healthResponse = await axios.get(`${this.apiBaseUrl}/health`);

        // Test chat endpoint with a simple query
        const chatResponse = await axios.post(`${this.apiBaseUrl}/chat`, {
          query: "Test connection",
          model: this.selectedModel,
          temperature: this.apiConfig.temperature,
          max_tokens: 50,
          use_rag: false,
        });

        this.testResult = {
          status: "success",
          message: "Connection successful! API is ready.",
          details: {
            health: healthResponse.data,
            model_test: chatResponse.data.model_used,
            response_time: chatResponse.data.response_time,
          },
        };
      } catch (error) {
        this.testResult = {
          status: "error",
          message: "Connection failed. Please check your settings.",
          details: error.message,
        };
      } finally {
        this.testing = false;
      }
    },

    async saveSettings() {
      try {
        // Save only user preferences to localStorage (not the API URL)
        localStorage.setItem("selectedModel", this.selectedModel);
        localStorage.setItem("maxTokens", this.apiConfig.maxTokens.toString());
        localStorage.setItem(
          "temperature",
          this.apiConfig.temperature.toString()
        );

        console.log("Saved settings:", {
          selectedModel: this.selectedModel,
          maxTokens: this.apiConfig.maxTokens,
          temperature: this.apiConfig.temperature,
        });

        // Try to switch the backend model
        try {
          await axios.post(
            `${this.apiBaseUrl}/switch-model/${this.selectedModel}`
          );
          console.log("Backend switched to:", this.selectedModel);
        } catch (error) {
          console.error("Failed to switch backend model:", error);
          // Continue anyway - the frontend will send the model with each request
        }

        this.saveStatus = "success";
      } catch (error) {
        this.saveStatus = "error";
        console.error("Save settings error:", error);
      }

      setTimeout(() => {
        this.saveStatus = null;
      }, 3000);
    },

    resetSettings() {
      this.selectedModel = "mistral";
      this.apiConfig = {
        maxTokens: 256,
        temperature: 0.7,
      };
      this.testResult = null;
    },

    updateConfig() {
      this.saveStatus = null;
      this.testResult = null;
    },

    async testSearch() {
      // Test RAG search functionality
      try {
        const response = await axios.post(`${this.apiBaseUrl}/search`, {
          query: "SSS benefits",
          top_k: 3,
        });

        console.log("Search test results:", response.data);
        return response.data;
      } catch (error) {
        console.error("Search test failed:", error);
        return null;
      }
    },
  },

  computed: {
    isHuggingFaceDeployment() {
      // Check if running on Hugging Face Spaces
      return (
        this.apiBaseUrl.includes("huggingface.co") ||
        this.apiBaseUrl.includes("hf.space")
      );
    },

    modelConstraints() {
      // Different constraints for different models
      const constraints = {
        tinyllama: {
          maxTokens: { min: 50, max: 512 },
          temperature: { min: 0.1, max: 1.0 },
        },
        phi2: {
          maxTokens: { min: 50, max: 1024 },
          temperature: { min: 0.1, max: 1.0 },
        },
        mistral: {
          maxTokens: { min: 50, max: 2048 },
          temperature: { min: 0.1, max: 1.0 },
        },
        deepseek: {
          maxTokens: { min: 50, max: 2048 },
          temperature: { min: 0.1, max: 1.0 },
        },
        llama: {
          maxTokens: { min: 50, max: 2048 },
          temperature: { min: 0.1, max: 1.0 },
        },
      };

      return (
        constraints[this.selectedModel] || {
          maxTokens: { min: 50, max: 512 },
          temperature: { min: 0.1, max: 1.0 },
        }
      );
    },

    // Add computed property to show API endpoint in UI (read-only)
    displayApiEndpoint() {
      return this.apiBaseUrl;
    },
  },
};
</script>
<style scoped>
.settings-view {
  min-height: 100vh;
  background: #f8fafc;
  padding: 2rem;
}

.settings-header {
  margin-bottom: 3rem;
}

.settings-header h1 {
  font-size: 2.5rem;
  color: #1e293b;
  margin-bottom: 0.5rem;
}

.settings-subtitle {
  color: #64748b;
  font-size: 1.125rem;
}

.settings-content {
  max-width: 1200px;
  margin: 0 auto;
}

.settings-section {
  background: white;
  border-radius: 1rem;
  padding: 2rem;
  margin-bottom: 2rem;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
}

.section-title {
  font-size: 1.5rem;
  color: #1e293b;
  margin-bottom: 0.5rem;
}

.section-description {
  color: #64748b;
  margin-bottom: 2rem;
}

/* Model Grid */
.model-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(350px, 1fr));
  gap: 1.5rem;
}

.model-card {
  background: #f8fafc;
  border: 2px solid #e2e8f0;
  border-radius: 0.75rem;
  padding: 1.5rem;
  cursor: pointer;
  transition: all 0.2s ease;
}

.model-card:hover {
  border-color: #cbd5e1;
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
}

.model-card.active {
  border-color: #6366f1;
  background: #eef2ff;
}

.model-header {
  display: flex;
  align-items: center;
  gap: 1rem;
  margin-bottom: 1rem;
}

.model-icon {
  width: 48px;
  height: 48px;
  background: #6366f1;
  border-radius: 0.75rem;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
}

.model-icon svg {
  width: 24px;
  height: 24px;
}

.model-info {
  flex: 1;
}

.model-name {
  font-size: 1.25rem;
  font-weight: 600;
  color: #1e293b;
  margin: 0;
}

.model-type {
  color: #64748b;
  font-size: 0.875rem;
}

.model-description {
  color: #475569;
  font-size: 0.875rem;
  line-height: 1.5;
  margin-bottom: 1rem;
}

.model-specs {
  display: flex;
  gap: 1.5rem;
  margin-bottom: 1rem;
}

.spec {
  display: flex;
  gap: 0.5rem;
  font-size: 0.875rem;
}

.spec-label {
  color: #64748b;
}

.spec-value {
  color: #1e293b;
  font-weight: 500;
}

.model-features {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
  margin-bottom: 1rem;
}

.feature {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  font-size: 0.875rem;
  color: #475569;
}

.feature-icon {
  width: 16px;
  height: 16px;
  color: #10b981;
}

.model-footer {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-top: 1rem;
}

.free-badge {
  display: flex;
  align-items: center;
  gap: 0.375rem;
  padding: 0.25rem 0.75rem;
  background: #10b981;
  color: white;
  border-radius: 0.375rem;
  font-size: 0.75rem;
  font-weight: 500;
}

.badge-icon {
  width: 14px;
  height: 14px;
}

.selected-badge {
  padding: 0.375rem 1rem;
  background: #6366f1;
  color: white;
  border: none;
  border-radius: 0.375rem;
  font-size: 0.875rem;
  font-weight: 500;
  cursor: default;
}

/* API Configuration */
.api-config {
  display: grid;
  gap: 1.5rem;
}

.config-item {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.config-item label {
  font-weight: 500;
  color: #1e293b;
  font-size: 0.875rem;
}

.config-item input {
  padding: 0.75rem 1rem;
  border: 2px solid #e2e8f0;
  border-radius: 0.5rem;
  font-size: 1rem;
  transition: border-color 0.2s;
}

.config-item input:focus {
  outline: none;
  border-color: #6366f1;
}

.slider-container {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.slider-container input[type="range"] {
  flex: 1;
  height: 6px;
  background: #e2e8f0;
  border-radius: 3px;
  outline: none;
  -webkit-appearance: none;
  appearance: none;
}

.slider-container input[type="range"]::-webkit-slider-thumb {
  -webkit-appearance: none;
  width: 20px;
  height: 20px;
  background: #6366f1;
  border-radius: 50%;
  cursor: pointer;
}

.slider-container input[type="range"]::-moz-range-thumb {
  width: 20px;
  height: 20px;
  background: #6366f1;
  border-radius: 50%;
  cursor: pointer;
  border: none;
}

.slider-value {
  min-width: 40px;
  text-align: center;
  font-weight: 500;
  color: #1e293b;
}

/* Test Section */
.test-section {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.test-button {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 0.5rem;
  padding: 0.75rem 1.5rem;
  background: #6366f1;
  color: white;
  border: none;
  border-radius: 0.5rem;
  font-size: 1rem;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.2s;
}

.test-button:hover:not(:disabled) {
  background: #4f46e5;
  transform: translateY(-1px);
}

.test-button:disabled {
  opacity: 0.7;
  cursor: not-allowed;
}

.button-icon {
  width: 20px;
  height: 20px;
}

.spinning {
  animation: spin 1s linear infinite;
}

@keyframes spin {
  from {
    transform: rotate(0deg);
  }
  to {
    transform: rotate(360deg);
  }
}

.test-result {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  padding: 1rem;
  border-radius: 0.5rem;
  font-size: 0.875rem;
}

.test-result.success {
  background: #d1fae5;
  color: #065f46;
}

.test-result.error {
  background: #fee2e2;
  color: #991b1b;
}

.result-icon {
  width: 20px;
  height: 20px;
}

/* Action Buttons */
.action-buttons {
  display: flex;
  gap: 1rem;
  margin-top: 2rem;
}

.save-button {
  flex: 1;
  padding: 1rem 2rem;
  background: #6366f1;
  color: white;
  border: none;
  border-radius: 0.5rem;
  font-size: 1rem;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.2s;
}

.save-button:hover {
  background: #4f46e5;
  transform: translateY(-1px);
}

.reset-button {
  padding: 1rem 2rem;
  background: transparent;
  color: #6366f1;
  border: 2px solid #6366f1;
  border-radius: 0.5rem;
  font-size: 1rem;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.2s;
}

.reset-button:hover {
  background: #eef2ff;
}

/* Save Status */
.save-status {
  position: fixed;
  bottom: 2rem;
  right: 2rem;
  display: flex;
  align-items: center;
  gap: 0.75rem;
  padding: 1rem 1.5rem;
  border-radius: 0.5rem;
  font-weight: 500;
  animation: slideIn 0.3s ease;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
}

.save-status.success {
  background: #10b981;
  color: white;
}

.save-status.error {
  background: #ef4444;
  color: white;
}

.status-icon {
  width: 24px;
  height: 24px;
}
/* System Status Styles */
.system-status {
  background: #f8fafc;
  padding: 1.5rem;
  border-radius: 0.75rem;
}

.status-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 1rem;
}

.status-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0.75rem;
  background: white;
  border-radius: 0.5rem;
  border: 1px solid #e2e8f0;
}

.status-label {
  font-weight: 500;
  color: #64748b;
}

.status-value {
  font-weight: 600;
}

.status-value.success {
  color: #10b981;
}

.status-value.error {
  color: #ef4444;
}

@keyframes slideIn {
  from {
    transform: translateX(100%);
    opacity: 0;
  }
  to {
    transform: translateX(0);
    opacity: 1;
  }
}

/* Responsive Design */
@media (max-width: 768px) {
  .settings-view {
    padding: 1rem;
  }

  .model-grid {
    grid-template-columns: 1fr;
  }

  .model-specs {
    flex-direction: column;
    gap: 0.5rem;
  }

  .action-buttons {
    flex-direction: column;
  }

  .save-status {
    bottom: 1rem;
    right: 1rem;
    left: 1rem;
  }
}
</style>

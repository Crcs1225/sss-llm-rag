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
            <label>Model Path (for local models)</label>
            <input
              v-model="apiConfig.modelPath"
              placeholder="/path/to/model"
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

export default {
  name: "SettingsView",
  data() {
    return {
      selectedModel: localStorage.getItem("selectedModel") || "llama2-7b",
      saveStatus: null,
      testing: false,
      testResult: null,
      apiConfig: {
        endpoint:
          localStorage.getItem("apiEndpoint") || "http://localhost:8000",
        modelPath: localStorage.getItem("modelPath") || "",
        maxTokens: parseInt(localStorage.getItem("maxTokens")) || 512,
        temperature: parseFloat(localStorage.getItem("temperature")) || 0.7,
      },
      availableModels: [
        {
          id: "llama2-7b",
          name: "Llama 2 7B",
          type: "Local/API",
          size: "7B parameters",
          ram: "8GB",
          description:
            "Meta's open-source model. Great for general tasks and conversations.",
          features: ["Open source", "Good performance", "Active community"],
        },
        {
          id: "mistral-7b",
          name: "Mistral 7B",
          type: "Local/API",
          size: "7B parameters",
          ram: "6GB",
          description:
            "Efficient and powerful open model with excellent performance.",
          features: [
            "Fast inference",
            "Low resource usage",
            "Strong performance",
          ],
        },
        {
          id: "falcon-7b",
          name: "Falcon 7B",
          type: "Local/API",
          size: "7B parameters",
          ram: "8GB",
          description:
            "Open-source model from TII, trained on diverse datasets.",
          features: ["Multilingual", "Commercial use", "Good accuracy"],
        },
        {
          id: "vicuna-13b",
          name: "Vicuna 13B",
          type: "Local/API",
          size: "13B parameters",
          ram: "16GB",
          description:
            "Fine-tuned LLaMA model with improved conversational abilities.",
          features: ["Better reasoning", "Detailed responses", "ChatGPT-like"],
        },
        {
          id: "gpt4all",
          name: "GPT4All",
          type: "Local",
          size: "3-7B parameters",
          ram: "4-8GB",
          description:
            "Ecosystem of open-source models optimized for consumer hardware.",
          features: ["CPU friendly", "Easy setup", "Multiple models"],
        },
        {
          id: "alpaca-7b",
          name: "Alpaca 7B",
          type: "Local/API",
          size: "7B parameters",
          ram: "8GB",
          description: "Stanford's instruction-following model based on LLaMA.",
          features: ["Instruction tuned", "Research friendly", "Good baseline"],
        },
      ],
    };
  },
  methods: {
    selectModel(modelId) {
      this.selectedModel = modelId;
      this.saveStatus = null;
    },

    async testConnection() {
      this.testing = true;
      this.testResult = null;

      try {
        const response = await axios.post(`${this.apiConfig.endpoint}/test`, {
          model: this.selectedModel,
          config: this.apiConfig,
        });

        this.testResult = {
          status: "success",
          message:
            response.data.message ||
            "Connection successful! Model is ready to use.",
          details: response.data.details || null,
        };
      } catch (error) {
        this.testResult = {
          status: "error",
          message:
            error.response?.data?.message ||
            "Connection failed. Please check your settings.",
          details: error.response?.data?.details || error.message,
        };
      } finally {
        this.testing = false;
      }
    },

    async saveSettings() {
      try {
        // Save to localStorage
        localStorage.setItem("selectedModel", this.selectedModel);
        localStorage.setItem("apiEndpoint", this.apiConfig.endpoint);
        localStorage.setItem("modelPath", this.apiConfig.modelPath);
        localStorage.setItem("maxTokens", this.apiConfig.maxTokens);
        localStorage.setItem("temperature", this.apiConfig.temperature);

        // Send to backend
        await axios.post(`${this.apiConfig.endpoint}/settings`, {
          model: this.selectedModel,
          config: this.apiConfig,
        });

        this.saveStatus = "success";
      } catch (error) {
        this.saveStatus = "error";
      }

      setTimeout(() => {
        this.saveStatus = null;
      }, 3000);
    },

    resetSettings() {
      this.selectedModel = "llama2-7b";
      this.apiConfig = {
        endpoint: "http://localhost:8000",
        modelPath: "",
        maxTokens: 512,
        temperature: 0.7,
      };
      this.testResult = null;
    },

    updateConfig() {
      this.saveStatus = null;
      this.testResult = null;
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

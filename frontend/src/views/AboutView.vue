<template>
  <div class="about-view">
    <div class="about-header">
      <h1 class="about-title">About SSS AI Assistant</h1>
      <p class="about-subtitle">
        Understanding the technology behind your intelligent SSS companion
      </p>
    </div>

    <div class="about-content">
      <!-- Summary Section -->
      <section class="about-section">
        <div class="section-icon">
          <svg viewBox="0 0 24 24" fill="currentColor">
            <path
              d="M12 2L2 7v10c0 5.55 3.84 10.74 9 12 5.16-1.26 9-6.45 9-12V7l-10-5z"
            />
          </svg>
        </div>
        <h2 class="section-title">What is SSS AI Assistant?</h2>
        <div class="section-content">
          <p>
            The SSS AI Assistant is an advanced conversational AI system
            designed to help users navigate and understand the Social Security
            System (SSS) in the Philippines. Built using cutting-edge
            technologies, it combines:
          </p>
          <div class="tech-cards">
            <div class="tech-card">
              <h3>RAG Technology</h3>
              <p>
                Retrieval-Augmented Generation ensures accurate, context-aware
                responses by combining AI with a comprehensive SSS knowledge
                base.
              </p>
            </div>
            <div class="tech-card">
              <h3>LLM Powered</h3>
              <p>
                Large Language Models provide natural language understanding and
                generation, making interactions feel human-like and intuitive.
              </p>
            </div>
            <div class="tech-card">
              <h3>Intelligent Assistant</h3>
              <p>
                Smart query processing and response generation tailored
                specifically for SSS-related inquiries and assistance.
              </p>
            </div>
          </div>
        </div>
      </section>

      <!-- Dataset Section -->
      <section class="about-section">
        <div class="section-icon">
          <svg viewBox="0 0 24 24" fill="currentColor">
            <path
              d="M14,2H6A2,2 0 0,0 4,4V20A2,2 0 0,0 6,22H18A2,2 0 0,0 20,20V8L14,2M18,20H6V4H13V9H18V20M10,19L12,15H9V10H15V15L13,19H10Z"
            />
          </svg>
        </div>
        <h2 class="section-title">Dataset Sources</h2>
        <div class="section-content">
          <p>
            Our AI assistant is trained on comprehensive SSS data from official
            sources:
          </p>
          <div class="code-block">
            <div class="code-header">
              <span>dataset_sources.json</span>
              <button @click="copyDatasetCode" class="copy-btn">
                <svg viewBox="0 0 24 24" fill="currentColor">
                  <path
                    d="M16 1H4c-1.1 0-2 .9-2 2v14h2V3h12V1zm3 4H8c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h11c1.1 0 2-.9 2-2V7c0-1.1-.9-2-2-2zm0 16H8V7h11v14z"
                  />
                </svg>
              </button>
            </div>
            <pre><code>{
  "datasets": [
    {
      "name": "SSS Main Portal",
      "urls": [
        "https://www.sss.gov.ph/",
        "https://www.sss.gov.ph/the-sss-mandate/",
        "https://www.sss.gov.ph/ss-commission/",
        "https://www.sss.gov.ph/management-directory/"
      ],
      "type": "primary_source",
      "description": "Core SSS information and organizational structure"
    },
    {
      "name": "Citizens Charter & Annual Reports",
      "urls": [
        "https://www.sss.gov.ph/wp-content/uploads/2025/06/SSS-Citizens-Charter-2025-1st-Edition.pdf",
        "https://www.sss.gov.ph/wp-content/uploads/2024/07/6a-2023-sss-citizens-charter-1st-edition.pdf",
        "https://www.sss.gov.ph/wp-content/uploads/2025/01/SSS-2023-Annual-Report-full.pdf",
        "https://www.sss.gov.ph/wp-content/uploads/2024/10/2022-SSS-Annual-Report-Final.pdf",
        "https://www.sss.gov.ph/wp-content/uploads/2023/02/SSS-Annual-Report_FINAL_2021.pdf"
      ],
      "type": "official_documents",
      "format": "PDF",
      "years": "2015-2025"
    },
    {
      "name": "Contribution Guidelines",
      "urls": [
        "https://www.sss.gov.ph/sss-contribution-table/",
        "https://www.sss.gov.ph/pay-contribution/",
        "https://www.sss.gov.ph/mysss-pension-booster/",
        "https://www.sss.gov.ph/wp-content/uploads/2024/12/Cir-2024-006-Employers-scaled.jpg",
        "https://www.sss.gov.ph/wp-content/uploads/2024/12/Cir-2024-007-HR-Kasambahay-scaled.jpg",
        "https://www.sss.gov.ph/wp-content/uploads/2024/12/Cir-2024-008-Self-Employed-scaled.jpg"
      ],
      "type": "contribution_data",
      "format": "HTML/Images",
      "last_updated": "2024"
    },
    {
      "name": "Membership Categories",
      "urls": [
        "https://www.sss.gov.ph/become-an-sss-member/",
        "https://www.sss.gov.ph/employees/",
        "https://www.sss.gov.ph/employer-er/",
        "https://www.sss.gov.ph/self-employed/",
        "https://www.sss.gov.ph/voluntary-member/",
        "https://www.sss.gov.ph/ofw-member/",
        "https://www.sss.gov.ph/kasambahay/",
        "https://www.sss.gov.ph/household-employer/",
        "https://www.sss.gov.ph/non-working-spouse/"
      ],
      "type": "membership_guides",
      "coverage": "All member types"
    },
    {
      "name": "Benefits Programs",
      "urls": [
        "https://www.sss.gov.ph/sickness-benefit/",
        "https://www.sss.gov.ph/maternity-benefit/",
        "https://www.sss.gov.ph/disability-benefit/",
        "https://www.sss.gov.ph/retirement-benefit/",
        "https://www.sss.gov.ph/death-benefit/",
        "https://www.sss.gov.ph/funeral-benefit/",
        "https://www.sss.gov.ph/unemployment-benefit/",
        "https://www.sss.gov.ph/employees-compensation-program/"
      ],
      "type": "benefits_information",
      "categories": "8 benefit types"
    },
    {
      "name": "Loan Services",
      "urls": [
        "https://www.sss.gov.ph/salary-loan/",
        "https://www.sss.gov.ph/calamity-loan/",
        "https://www.sss.gov.ph/pension-loan-first-time-applicants/",
        "https://www.sss.gov.ph/sss-conso-loan-program/",
        "https://www.sss.gov.ph/pay-loans/",
        "https://www.sss.gov.ph/option-to-sell/"
      ],
      "type": "loan_programs",
      "services": "6 loan types"
    },
    {
      "name": "Legal & Regulatory",
      "urls": [
        "https://www.sss.gov.ph/social-security-laws/",
        "https://www.sss.gov.ph/sss-circulars/",
        "https://www.sss.gov.ph/ssc-rules-of-procedure/",
        "https://www.sss.gov.ph/bilateral-agreements/",
        "https://www.sss.gov.ph/transparency-seal/"
      ],
      "type": "legal_framework",
      "content": "Laws, circulars, procedures"
    },
    {
      "name": "External Guides",
      "urls": [
        "https://filipiknow.net/how-to-pay-sss-contribution/",
        "https://filipiknow.net/sss-online-registration/",
        "https://businessdiary.com.ph/32998/sss-online-registration-benefits-loans/"
      ],
      "type": "third_party_guides",
      "source": "Educational platforms"
    },
    {
      "name": "Contact & Support",
      "urls": [
        "https://www.sss.gov.ph/contact-us/",
        "https://www.sss.gov.ph/news-and-updates/",
        "https://www.sss.gov.ph/employment-opportunities/"
      ],
      "type": "support_resources",
      "services": "Contact info, news, careers"
    }
  ],
  "total_sources": 63,
  "last_updated": "2025",
  "coverage": "Complete SSS ecosystem"
}</code></pre>
          </div>
        </div>
      </section>

      <!-- Methods/Workflow Section -->
      <section class="about-section">
        <div class="section-icon">
          <svg viewBox="0 0 24 24" fill="currentColor">
            <path
              d="M12,2A10,10 0 0,0 2,12A10,10 0 0,0 12,22A10,10 0 0,0 22,12A10,10 0 0,0 12,2M12,4A8,8 0 0,1 20,12A8,8 0 0,1 12,20A8,8 0 0,1 4,12A8,8 0 0,1 12,4M12,6A6,6 0 0,0 6,12A6,6 0 0,0 12,18A6,6 0 0,0 18,12A6,6 0 0,0 12,6M12,8A4,4 0 0,1 16,12A4,4 0 0,1 12,16A4,4 0 0,1 8,12A4,4 0 0,1 12,8Z"
            />
          </svg>
        </div>
        <h2 class="section-title">Methods & Workflow</h2>
        <div class="section-content">
          <p>
            Our AI assistant follows a sophisticated workflow to provide
            accurate responses:
          </p>
          <div class="workflow-diagram">
            <div class="workflow-step">
              <div class="step-number">1</div>
              <h4>Query Processing</h4>
              <p>
                User input is analyzed and preprocessed using NLP techniques
              </p>
            </div>
            <div class="workflow-arrow">→</div>
            <div class="workflow-step">
              <div class="step-number">2</div>
              <h4>Context Retrieval</h4>
              <p>
                Relevant SSS information is retrieved from the vector database
              </p>
            </div>
            <div class="workflow-arrow">→</div>
            <div class="workflow-step">
              <div class="step-number">3</div>
              <h4>Response Generation</h4>
              <p>LLM generates contextual response based on retrieved data</p>
            </div>
          </div>

          <h3 class="subsection-title">Technical Implementation</h3>
          <div class="tech-list">
            <div class="tech-item">
              <strong>Vector Database:</strong> ChromaDB for efficient
              similarity search
            </div>
            <div class="tech-item">
              <strong>Embeddings:</strong> Sentence transformers for text
              vectorization
            </div>
            <div class="tech-item">
              <strong>LLM Integration:</strong> Support for multiple open-source
              models
            </div>
            <div class="tech-item">
              <strong>API Framework:</strong> FastAPI for high-performance
              backend
            </div>
          </div>
        </div>
      </section>

      <!-- GitHub Repository Section -->
      <section class="about-section">
        <div class="section-icon">
          <svg viewBox="0 0 24 24" fill="currentColor">
            <path
              d="M12 2A10 10 0 0 0 2 12c0 4.42 2.87 8.17 6.84 9.5.5.08.66-.23.66-.5v-1.69c-2.77.6-3.36-1.34-3.36-1.34-.46-1.16-1.11-1.47-1.11-1.47-.91-.62.07-.6.07-.6 1 .07 1.53 1.03 1.53 1.03.87 1.52 2.34 1.07 2.91.83.09-.65.35-1.09.63-1.34-2.22-.25-4.55-1.11-4.55-4.92 0-1.11.38-2 1.03-2.71-.1-.25-.45-1.29.1-2.64 0 0 .84-.27 2.75 1.02.79-.22 1.65-.33 2.5-.33.85 0 1.71.11 2.5.33 1.91-1.29 2.75-1.02 2.75-1.02.55 1.35.2 2.39.1 2.64.65.71 1.03 1.6 1.03 2.71 0 3.82-2.34 4.66-4.57 4.91.36.31.69.92.69 1.85V21c0 .27.16.59.67.5C19.14 20.16 22 16.42 22 12A10 10 0 0 0 12 2Z"
            />
          </svg>
        </div>
        <h2 class="section-title">GitHub Repository</h2>
        <div class="section-content">
          <div class="github-card">
            <div class="repo-header">
              <h3>sss-ai-assistant</h3>
              <span class="repo-visibility">Public</span>
            </div>
            <p class="repo-description">
              An intelligent AI assistant for Philippine Social Security System
              (SSS) queries using RAG and LLM technologies
            </p>
            <div class="repo-stats">
              <div class="stat">
                <svg viewBox="0 0 16 16" fill="currentColor">
                  <path
                    d="M8 .25a.75.75 0 01.673.418l1.882 3.815 4.21.612a.75.75 0 01.416 1.279l-3.046 2.97.719 4.192a.75.75 0 01-1.088.791L8 12.347l-3.766 1.98a.75.75 0 01-1.088-.79l.72-4.194L.818 6.374a.75.75 0 01.416-1.28l4.21-.611L7.327.668A.75.75 0 018 .25z"
                  />
                </svg>
                <span>Stars</span>
              </div>
              <div class="stat">
                <svg viewBox="0 0 16 16" fill="currentColor">
                  <path
                    d="M5 3.25a.75.75 0 11-1.5 0 .75.75 0 011.5 0zm0 2.122a2.25 2.25 0 10-1.5 0v.878A2.25 2.25 0 005.75 8.5h1.5v2.128a2.251 2.251 0 101.5 0V8.5h1.5a2.25 2.25 0 002.25-2.25v-.878a2.25 2.25 0 10-1.5 0v.878a.75.75 0 01-.75.75h-4.5A.75.75 0 015 6.25v-.878zm3.75 7.378a.75.75 0 11-1.5 0 .75.75 0 011.5 0zm3-8.75a.75.75 0 100-1.5.75.75 0 000 1.5z"
                  />
                </svg>
                <span>Forks</span>
              </div>
              <div class="stat">
                <svg viewBox="0 0 16 16" fill="currentColor">
                  <path
                    d="M1.5 8a6.5 6.5 0 1113 0 6.5 6.5 0 01-13 0zM8 0a8 8 0 100 16A8 8 0 008 0zM6.379 5.227A.25.25 0 006 5.442v5.117a.25.25 0 00.379.214l4.264-2.559a.25.25 0 000-.428L6.379 5.227z"
                  />
                </svg>
                <span>MIT License</span>
              </div>
            </div>
            <div class="repo-tech-stack">
              <span class="tech-tag">Vue.js</span>
              <span class="tech-tag">FastAPI</span>
              <span class="tech-tag">Python</span>
              <span class="tech-tag">ChromaDB</span>
              <span class="tech-tag">LangChain</span>
            </div>
            <div class="repo-actions">
              <a
                href="https://github.com/yourusername/sss-ai-assistant"
                target="_blank"
                class="github-link"
              >
                View Repository
                <svg viewBox="0 0 16 16" fill="currentColor">
                  <path
                    d="M4.22 11.78a.75.75 0 010-1.06L9.44 5.5H5.75a.75.75 0 010-1.5h5.5a.75.75 0 01.75.75v5.5a.75.75 0 01-1.5 0V6.56l-5.22 5.22a.75.75 0 01-1.06 0z"
                  />
                </svg>
              </a>
              <button @click="copyCloneCommand" class="clone-btn">
                Clone Repository
              </button>
            </div>
          </div>
        </div>
      </section>

      <!-- Reference Documentation Section -->
      <section class="about-section">
        <div class="section-icon">
          <svg viewBox="0 0 24 24" fill="currentColor">
            <path
              d="M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zm-5 14H7v-2h7v2zm3-4H7v-2h10v2zm0-4H7V7h10v2z"
            />
          </svg>
        </div>
        <h2 class="section-title">Reference Documentation</h2>
        <div class="section-content">
          <p>
            Learn more about the technologies and concepts used in this project:
          </p>
          <div class="reference-grid">
            <a
              href="https://www.geeksforgeeks.org/blogs/how-to-build-rag-pipelines-for-llm-projects/"
              target="_blank"
              class="reference-card"
            >
              <div class="ref-icon geeks">G</div>
              <div class="ref-content">
                <h4>RAG Architecture</h4>
                <p>Understanding Retrieval-Augmented Generation</p>
                <span class="ref-source">GeeksforGeeks</span>
              </div>
            </a>

            <a
              href="https://developers.google.com/machine-learning/resources/intro-llms"
              target="_blank"
              class="reference-card"
            >
              <div class="ref-icon geeks">G</div>
              <div class="ref-content">
                <h4>Large Language Models</h4>
                <p>Introduction to LLMs and their applications</p>
                <span class="ref-source">GeeksforGeeks</span>
              </div>
            </a>

            <a
              href="https://learn.microsoft.com/en-us/data-engineering/playbook/solutions/vector-database/"
              target="_blank"
              class="reference-card"
            >
              <div class="ref-icon geeks">M</div>
              <div class="ref-content">
                <h4>Vector Databases</h4>
                <p>How vector databases enable semantic search</p>
                <span class="ref-source">GeeksforGeeks</span>
              </div>
            </a>

            <a
              href="https://www.deeplearning.ai/resources/natural-language-processing/"
              target="_blank"
              class="reference-card"
            >
              <div class="ref-icon geeks">D</div>
              <div class="ref-content">
                <h4>NLP Fundamentals</h4>
                <p>Natural Language Processing basics and techniques</p>
                <span class="ref-source">GeeksforGeeks</span>
              </div>
            </a>

            <a
              href="https://fastapi.tiangolo.com/"
              target="_blank"
              class="reference-card"
            >
              <div class="ref-icon geeks">F</div>
              <div class="ref-content">
                <h4>FastAPI Framework</h4>
                <p>Building high-performance APIs with Python</p>
                <span class="ref-source">GeeksforGeeks</span>
              </div>
            </a>

            <a
              href="https://vuejs.org/guide/introduction"
              target="_blank"
              class="reference-card"
            >
              <div class="ref-icon geeks">V</div>
              <div class="ref-content">
                <h4>Vue.js Guide</h4>
                <p>Progressive JavaScript framework for UIs</p>
                <span class="ref-source">GeeksforGeeks</span>
              </div>
            </a>
          </div>
        </div>
      </section>
    </div>

    <!-- Copy notification toast -->
    <transition name="toast">
      <div v-if="showToast" class="toast">
        {{ toastMessage }}
      </div>
    </transition>
  </div>
</template>

<script>
export default {
  name: "AboutView",
  data() {
    return {
      showToast: false,
      toastMessage: "",
    };
  },
  methods: {
    copyDatasetCode() {
      const code = `{
  "datasets": [
    {
      "name": "SSS Official Documentation",
      "url": "https://www.sss.gov.ph/",
      "type": "primary_source",
      "last_updated": "2024"
    },
    {
      "name": "SSS Benefits & Services",
      "url": "https://www.sss.gov.ph/sss/appmanager/pages.jsp",
      "type": "structured_data",
      "format": "HTML/PDF"
    },
    {
      "name": "SSS Forms Repository",
      "url": "https://www.sss.gov.ph/sss/DownloadContent",
      "type": "document_collection",
      "count": "50+ forms"
    },
    {
      "name": "SSS FAQ Database",
      "source": "Curated from official SSS resources",
      "type": "question_answer_pairs",
      "entries": "1000+"
    }
  ]
}`;
      navigator.clipboard.writeText(code);
      this.showNotification("Dataset code copied to clipboard!");
    },

    copyCloneCommand() {
      const command =
        "git clone https://github.com/yourusername/sss-ai-assistant.git";
      navigator.clipboard.writeText(command);
      this.showNotification("Clone command copied to clipboard!");
    },

    showNotification(message) {
      this.toastMessage = message;
      this.showToast = true;
      setTimeout(() => {
        this.showToast = false;
      }, 3000);
    },
  },
};
</script>

<style scoped>
.about-view {
  min-height: 100vh;
  background: #f8fafc;
  padding: 2rem;
}

.about-header {
  text-align: center;
  margin-bottom: 4rem;
  padding: 2rem 0;
}

.about-title {
  font-size: 3rem;
  font-weight: 700;
  color: #1e293b;
  margin-bottom: 1rem;
  background: linear-gradient(135deg, #6366f1 0%, #818cf8 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.about-subtitle {
  font-size: 1.25rem;
  color: #64748b;
  max-width: 600px;
  margin: 0 auto;
}

.about-content {
  max-width: 1200px;
  margin: 0 auto;
}

/* Section Styles */
.about-section {
  background: white;
  border-radius: 1rem;
  padding: 3rem;
  margin-bottom: 2rem;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
  position: relative;
  overflow: hidden;
}

.section-icon {
  position: absolute;
  top: 2rem;
  right: 2rem;
  width: 60px;
  height: 60px;
  background: linear-gradient(135deg, #6366f1 0%, #818cf8 100%);
  border-radius: 1rem;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
}

.section-icon svg {
  width: 30px;
  height: 30px;
}

.section-title {
  font-size: 2rem;
  color: #1e293b;
  margin-bottom: 1.5rem;
  padding-right: 100px;
}

.section-content {
  color: #475569;
  line-height: 1.8;
}

.section-content p {
  margin-bottom: 1.5rem;
}

/* Tech Cards */
.tech-cards {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 1.5rem;
  margin-top: 2rem;
}

.tech-card {
  background: #f1f5f9;
  padding: 1.5rem;
  border-radius: 0.75rem;
  border: 1px solid #e2e8f0;
}

.tech-card h3 {
  color: #6366f1;
  margin-bottom: 0.75rem;
  font-size: 1.125rem;
}

.tech-card p {
  color: #64748b;
  font-size: 0.875rem;
  line-height: 1.6;
  margin: 0;
}

/* Code Block */
.code-block {
  background: #1e293b;
  border-radius: 0.75rem;
  overflow: hidden;
  margin-top: 1.5rem;
}

.code-header {
  background: #334155;
  padding: 0.75rem 1.5rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
  color: #e2e8f0;
  font-size: 0.875rem;
}

.copy-btn {
  background: transparent;
  border: 1px solid #475569;
  color: #94a3b8;
  padding: 0.375rem 0.75rem;
  border-radius: 0.375rem;
  cursor: pointer;
  display: flex;
  align-items: center;
  gap: 0.5rem;
  transition: all 0.2s;
}

.copy-btn:hover {
  background: #475569;
  color: white;
}

.copy-btn svg {
  width: 16px;
  height: 16px;
}

.code-block pre {
  margin: 0;
  padding: 1.5rem;
  overflow-x: auto;
}

.code-block code {
  color: #e2e8f0;
  font-family: "Consolas", "Monaco", monospace;
  font-size: 0.875rem;
  line-height: 1.6;
}

/* Workflow Diagram */
.workflow-diagram {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin: 2rem 0;
  padding: 2rem 0;
  overflow-x: auto;
}

.workflow-step {
  flex: 1;
  min-width: 200px;
  text-align: center;
  padding: 1.5rem;
  background: #f8fafc;
  border-radius: 0.75rem;
  border: 2px solid #e2e8f0;
  position: relative;
}

.step-number {
  width: 40px;
  height: 40px;
  background: #6366f1;
  color: white;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: bold;
  margin: 0 auto 1rem;
}

.workflow-step h4 {
  color: #1e293b;
  margin-bottom: 0.5rem;
}

.workflow-step p {
  color: #64748b;
  font-size: 0.875rem;
  margin: 0;
}

.workflow-arrow {
  color: #cbd5e1;
  font-size: 2rem;
  margin: 0 1rem;
}

/* Tech List */
.subsection-title {
  font-size: 1.25rem;
  color: #1e293b;
  margin: 2rem 0 1rem;
}

.tech-list {
  background: #f8fafc;
  padding: 1.5rem;
  border-radius: 0.75rem;
}

.tech-item {
  padding: 0.75rem 0;
  border-bottom: 1px solid #e2e8f0;
  color: #475569;
}

.tech-item:last-child {
  border-bottom: none;
}

.tech-item strong {
  color: #1e293b;
}

/* GitHub Card */
.github-card {
  background: #f8fafc;
  border: 1px solid #e2e8f0;
  border-radius: 0.75rem;
  padding: 2rem;
}

.repo-header {
  display: flex;
  align-items: center;
  gap: 1rem;
  margin-bottom: 1rem;
}

.repo-header h3 {
  color: #1e293b;
  font-size: 1.5rem;
  margin: 0;
}

.repo-visibility {
  background: #e2e8f0;
  color: #64748b;
  padding: 0.25rem 0.75rem;
  border-radius: 1rem;
  font-size: 0.75rem;
}

.repo-description {
  color: #64748b;
  margin-bottom: 1.5rem;
}

.repo-stats {
  display: flex;
  gap: 2rem;
  margin-bottom: 1.5rem;
}

.stat {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  color: #64748b;
  font-size: 0.875rem;
}

.stat svg {
  width: 16px;
  height: 16px;
}

.repo-tech-stack {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
  margin-bottom: 1.5rem;
}

.tech-tag {
  background: #e0e7ff;
  color: #6366f1;
  padding: 0.25rem 0.75rem;
  border-radius: 0.375rem;
  font-size: 0.75rem;
  font-weight: 500;
}

.repo-actions {
  display: flex;
  gap: 1rem;
}

.github-link {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.75rem 1.5rem;
  background: #1e293b;
  color: white;
  text-decoration: none;
  border-radius: 0.5rem;
  font-weight: 500;
  transition: all 0.2s;
}

.github-link:hover {
  background: #334155;
  transform: translateY(-2px);
}

.github-link svg {
  width: 16px;
  height: 16px;
}

.clone-btn {
  padding: 0.75rem 1.5rem;
  background: transparent;
  color: #6366f1;
  border: 2px solid #6366f1;
  border-radius: 0.5rem;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.2s;
}

.clone-btn:hover {
  background: #6366f1;
  color: white;
}

/* Reference Grid */
.reference-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 1.5rem;
  margin-top: 1.5rem;
}

.reference-card {
  display: flex;
  gap: 1rem;
  padding: 1.5rem;
  background: #f8fafc;
  border: 1px solid #e2e8f0;
  border-radius: 0.75rem;
  text-decoration: none;
  transition: all 0.2s;
}

.reference-card:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
  border-color: #cbd5e1;
}

.ref-icon {
  width: 48px;
  height: 48px;
  border-radius: 0.5rem;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: bold;
  font-size: 1.5rem;
  flex-shrink: 0;
}

.ref-icon.geeks {
  background: #2f8d46;
  color: white;
}

.ref-content {
  flex: 1;
}

.ref-content h4 {
  color: #1e293b;
  margin: 0 0 0.25rem;
  font-size: 1.125rem;
}

.ref-content p {
  color: #64748b;
  font-size: 0.875rem;
  margin: 0 0 0.5rem;
  line-height: 1.4;
}

.ref-source {
  color: #94a3b8;
  font-size: 0.75rem;
  font-weight: 500;
}

/* Toast Notification */
.toast {
  position: fixed;
  bottom: 2rem;
  right: 2rem;
  background: #1e293b;
  color: white;
  padding: 1rem 1.5rem;
  border-radius: 0.5rem;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
  z-index: 1000;
}

.toast-enter-active,
.toast-leave-active {
  transition: all 0.3s ease;
}

.toast-enter-from {
  transform: translateY(100%);
  opacity: 0;
}

.toast-leave-to {
  transform: translateY(100%);
  opacity: 0;
}

/* Responsive Design */
@media (max-width: 1024px) {
  .tech-cards {
    grid-template-columns: 1fr;
  }

  .workflow-diagram {
    flex-direction: column;
    align-items: stretch;
  }

  .workflow-arrow {
    transform: rotate(90deg);
    margin: 1rem 0;
  }

  .workflow-step {
    margin-bottom: 1rem;
  }
}

@media (max-width: 768px) {
  .about-view {
    padding: 1rem;
  }

  .about-title {
    font-size: 2rem;
  }

  .about-subtitle {
    font-size: 1rem;
  }

  .about-section {
    padding: 2rem 1.5rem;
  }

  .section-icon {
    width: 48px;
    height: 48px;
    top: 1.5rem;
    right: 1.5rem;
  }

  .section-icon svg {
    width: 24px;
    height: 24px;
  }

  .section-title {
    font-size: 1.5rem;
    padding-right: 60px;
  }

  .repo-stats {
    flex-direction: column;
    gap: 0.75rem;
  }

  .repo-actions {
    flex-direction: column;
  }

  .reference-grid {
    grid-template-columns: 1fr;
  }

  .toast {
    bottom: 1rem;
    right: 1rem;
    left: 1rem;
  }

  .code-block pre {
    padding: 1rem;
    font-size: 0.75rem;
  }
}

/* Animation for section appearance */
.about-section {
  animation: fadeInUp 0.6s ease;
}

.about-section:nth-child(1) {
  animation-delay: 0.1s;
}

.about-section:nth-child(2) {
  animation-delay: 0.2s;
}

.about-section:nth-child(3) {
  animation-delay: 0.3s;
}

.about-section:nth-child(4) {
  animation-delay: 0.4s;
}

.about-section:nth-child(5) {
  animation-delay: 0.5s;
}

@keyframes fadeInUp {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

/* Hover effects for interactive elements */
.tech-card {
  transition: all 0.3s ease;
}

.tech-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 8px 24px rgba(99, 102, 241, 0.1);
  border-color: #6366f1;
}

.workflow-step {
  transition: all 0.3s ease;
}

.workflow-step:hover {
  transform: translateY(-4px);
  box-shadow: 0 8px 24px rgba(99, 102, 241, 0.1);
  border-color: #6366f1;
}

.workflow-step:hover .step-number {
  transform: scale(1.1);
}

/* Print styles */
@media print {
  .about-view {
    background: white;
  }

  .about-section {
    break-inside: avoid;
    box-shadow: none;
    border: 1px solid #e2e8f0;
  }

  .copy-btn,
  .clone-btn,
  .toast {
    display: none;
  }
}
</style>

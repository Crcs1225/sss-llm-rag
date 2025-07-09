<template>
  <div>
    <!-- Mobile Toggle Button -->
    <button
      class="mobile-toggle"
      @click="toggleSidebar"
      :class="{ 'sidebar-open': isSidebarOpen }"
    >
      <span></span>
      <span></span>
      <span></span>
    </button>

    <!-- Overlay for mobile -->
    <div
      v-if="isSidebarOpen && isMobile"
      class="overlay"
      @click="closeSidebar"
    ></div>

    <!-- Sidebar -->
    <aside
      class="side-nav"
      :class="{
        open: isSidebarOpen,
        mobile: isMobile,
      }"
    >
      <!-- Logo/Brand -->
      <div class="nav-brand">
        <svg class="brand-icon" viewBox="0 0 24 24" fill="currentColor">
          <!-- First S -->
          <path
            d="M5 6c0-1.1 0.9-2 2-2s2 0.9 2 2c0 0.7-0.4 1.3-0.9 1.6L6.5 8.5C5.6 9 5 9.9 5 11c0 1.1 0.9 2 2 2"
            stroke="currentColor"
            stroke-width="1.5"
            fill="none"
            stroke-linecap="round"
          />
          <!-- Second S -->
          <path
            d="M10 6c0-1.1 0.9-2 2-2s2 0.9 2 2c0 0.7-0.4 1.3-0.9 1.6l-1.6 0.9C10.6 9 10 9.9 10 11c0 1.1 0.9 2 2 2"
            stroke="currentColor"
            stroke-width="1.5"
            fill="none"
            stroke-linecap="round"
          />
          <!-- Third S -->
          <path
            d="M15 6c0-1.1 0.9-2 2-2s2 0.9 2 2c0 0.7-0.4 1.3-0.9 1.6l-1.6 0.9C15.6 9 15 9.9 15 11c0 1.1 0.9 2 2 2"
            stroke="currentColor"
            stroke-width="1.5"
            fill="none"
            stroke-linecap="round"
          />
          <!-- Bottom connecting line -->
          <path
            d="M4 15h16c0 2.5-2 4.5-4.5 4.5h-7C6 19.5 4 17.5 4 15z"
            fill="currentColor"
            opacity="0.2"
          />
        </svg>
        <span class="brand-text">SSS.ai</span>
      </div>

      <!-- Navigation Links -->
      <nav class="nav-links">
        <router-link to="/" exact @click="handleLinkClick">
          <svg class="nav-icon" viewBox="0 0 24 24" fill="currentColor">
            <path d="M10 20v-6h4v6h5v-8h3L12 3 2 12h3v8z" />
          </svg>
          <span class="nav-text">Home</span>
        </router-link>

        <router-link to="/about" @click="handleLinkClick">
          <svg class="nav-icon" viewBox="0 0 24 24" fill="currentColor">
            <path
              d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm1 15h-2v-6h2v6zm0-8h-2V7h2v2z"
            />
          </svg>
          <span class="nav-text">About</span>
        </router-link>
      </nav>

      <!-- Bottom section (optional) -->
      <div class="nav-footer">
        <router-link to="/settings" @click="handleLinkClick">
          <svg class="nav-icon" viewBox="0 0 24 24" fill="currentColor">
            <path
              d="M19.14 12.94c.04-.3.06-.61.06-.94 0-.32-.02-.64-.07-.94l2.03-1.58c.18-.14.23-.41.12-.61l-1.92-3.32c-.12-.22-.37-.29-.59-.22l-2.39.96c-.5-.38-1.03-.7-1.62-.94l-.36-2.54c-.04-.24-.24-.41-.48-.41h-3.84c-.24 0-.43.17-.47.41l-.36 2.54c-.59.24-1.13.57-1.62.94l-2.39-.96c-.22-.08-.47 0-.59.22L2.74 8.87c-.12.21-.08.47.12.61l2.03 1.58c-.05.3-.09.63-.09.94s.02.64.07.94l-2.03 1.58c-.18.14-.23.41-.12.61l1.92 3.32c.12.22.37.29.59.22l2.39-.96c.5.38 1.03.7 1.62.94l.36 2.54c.05.24.24.41.48.41h3.84c.24 0 .44-.17.47-.41l.36-2.54c.59-.24 1.13-.56 1.62-.94l2.39.96c.22.08.47 0 .59-.22l1.92-3.32c.12-.22.07-.47-.12-.61l-2.01-1.58zM12 15.6c-1.98 0-3.6-1.62-3.6-3.6s1.62-3.6 3.6-3.6 3.6 1.62 3.6 3.6-1.62 3.6-3.6 3.6z"
            />
          </svg>
          <span class="nav-text">Settings</span>
        </router-link>
      </div>
    </aside>
  </div>
</template>

<script>
export default {
  name: "SideNav",
  data() {
    return {
      isSidebarOpen: false,
      isMobile: false,
    };
  },
  mounted() {
    this.checkMobile();
    window.addEventListener("resize", this.checkMobile);
  },
  beforeUnmount() {
    window.removeEventListener("resize", this.checkMobile);
  },
  methods: {
    checkMobile() {
      this.isMobile = window.innerWidth <= 768;
      if (!this.isMobile) {
        this.isSidebarOpen = false;
      }
    },
    toggleSidebar() {
      this.isSidebarOpen = !this.isSidebarOpen;
    },
    closeSidebar() {
      this.isSidebarOpen = false;
    },
    handleLinkClick() {
      if (this.isMobile) {
        this.closeSidebar();
      }
    },
  },
  watch: {
    isSidebarOpen(val) {
      this.$emit("sidebar-toggle", val);
    },
  },
};
</script>

<style scoped>
/* Mobile Toggle Button */
.mobile-toggle {
  display: none;
  position: fixed;
  top: 1rem;
  left: 1rem;
  z-index: 1001;
  background: #fff;
  border: none;
  padding: 0.5rem;
  border-radius: 0.5rem;
  cursor: pointer;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  width: 40px;
  height: 40px;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  gap: 4px;
}

.mobile-toggle span {
  display: block;
  width: 24px;
  height: 3px;
  background: #1e293b;
  border-radius: 2px;
  transition: all 0.3s ease;
}

.mobile-toggle.sidebar-open span:nth-child(1) {
  transform: rotate(45deg) translate(5px, 5px);
}

.mobile-toggle.sidebar-open span:nth-child(2) {
  opacity: 0;
}

.mobile-toggle.sidebar-open span:nth-child(3) {
  transform: rotate(-45deg) translate(7px, -6px);
}

/* Overlay */
.overlay {
  display: none;
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.5);
  z-index: 999;
}

/* Sidebar */
.side-nav {
  position: fixed;
  top: 0;
  left: 0;
  width: 80px;
  height: 100vh;
  background: #fff;
  box-shadow: 2px 0 8px rgba(0, 0, 0, 0.06);
  display: flex;
  flex-direction: column;
  padding: 1rem 0;
  z-index: 1000;
  transition: all 0.3s ease;
  overflow: hidden;
}

/* Brand Section */
.nav-brand {
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 1rem;
  margin-bottom: 2rem;
  position: relative;
}

.brand-icon {
  width: 32px;
  height: 32px;
  color: #6366f1;
  flex-shrink: 0;
}

.brand-text {
  display: none;
  font-weight: bold;
  font-size: 1.25rem;
  color: #1e293b;
  margin-left: 0.75rem;
}

/* Navigation Links */
.nav-links {
  flex: 1;
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
  padding: 0 0.75rem;
}

.nav-links a,
.nav-footer a,  /* Add this */
.nav-link {
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 0.75rem;
  border-radius: 0.75rem;
  text-decoration: none;
  color: #64748b;
  background: transparent;
  border: none;
  cursor: pointer;
  transition: all 0.2s ease;
  position: relative;
  overflow: hidden;
}

.nav-icon {
  width: 24px;
  height: 24px;
  flex-shrink: 0;
}

.nav-text {
  display: none;
  margin-left: 1rem;
  font-weight: 500;
  white-space: nowrap;
}

.nav-links a:hover,
.nav-footer a:hover,  /* Add this */
.nav-link:hover {
  background: #f1f5f9;
  color: #6366f1;
}

.nav-links a.router-link-exact-active,
.nav-footer a.router-link-exact-active {
  /* Add this */
  background: #6366f1;
  color: #fff;
}

/* Footer */
.nav-footer {
  padding: 0 0.75rem;
  margin-top: auto;
}

/* Hover state for desktop - expand on hover */
@media (min-width: 769px) {
  .side-nav:hover {
    width: 240px;
  }

  .side-nav:hover .brand-text,
  .side-nav:hover .nav-text {
    display: block;
  }

  .side-nav:hover .nav-links a,
  .side-nav:hover .nav-footer a,  /* Add this */
  .side-nav:hover .nav-link {
    justify-content: flex-start;
  }
}

/* Mobile styles */
@media (max-width: 768px) {
  .mobile-toggle {
    display: flex;
  }

  .overlay {
    display: block;
  }

  .side-nav {
    width: 280px;
    transform: translateX(-100%);
  }

  .side-nav.mobile {
    box-shadow: 2px 0 16px rgba(0, 0, 0, 0.1);
  }

  .side-nav.open {
    transform: translateX(0);
  }

  .brand-text,
  .nav-text {
    display: block !important;
  }

  .nav-links a,
  .nav-footer a,
  .nav-link {
    justify-content: flex-start !important;
  }
}
</style>

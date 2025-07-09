<template>
  <div id="app">
    <SideNav @sidebar-toggle="handleSidebarToggle" />
    <main class="main-content" :class="{ 'sidebar-mobile-open': sidebarOpen }">
      <router-view
        :messages="messages"
        :has-started="hasStarted"
        @update-messages="updateMessages"
        @update-started="updateStarted"
      />
    </main>
  </div>
</template>

<script>
import SideNav from "./components/SideNav.vue";
export default {
  components: { SideNav },
  data() {
    return {
      sidebarOpen: false,
      messages: [],
      hasStarted: false,
    };
  },
  methods: {
    handleSidebarToggle(isOpen) {
      this.sidebarOpen = isOpen;
    },
    updateMessages(newMessages) {
      this.messages = newMessages;
    },
    updateStarted(started) {
      this.hasStarted = started;
    },
  },
};
</script>

<style>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}
html,
body {
  height: 100%;
  width: 100%;
  overflow-x: hidden;
}
body {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen,
    Ubuntu, Cantarell, sans-serif;
}
#app {
  display: flex;
  min-height: 100vh;
  width: 100%;
  position: relative;
}
.main-content {
  flex: 1;
  margin-left: 80px; /* Use margin-left instead of padding-left */
  min-height: 100vh;
  width: calc(100% - 80px); /* Explicitly set width */
  overflow-x: hidden;
  position: relative;
  transition: margin-left 0.3s ease;
}
/* When hovering sidebar on desktop */
@media (min-width: 769px) {
  .side-nav:hover ~ .main-content {
    margin-left: 240px;
    width: calc(100% - 240px);
  }
}
/* Mobile styles */
@media (max-width: 768px) {
  .main-content {
    margin-left: 0;
    width: 100%;
    padding-top: 60px; /* Space for mobile toggle button */
  }

  .main-content.sidebar-mobile-open {
    transform: translateX(280px);
  }
}
</style>

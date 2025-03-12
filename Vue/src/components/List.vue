<template>
  <div class="list-container">
    <h1>Team Members ({{ totalMembers }})</h1>
    
    <!-- Router Link to Add New Member -->
    <router-link to="/add" class="add-member-link">+</router-link>

    <!-- Search Bar -->
    <input
      v-model="searchQuery"
      placeholder="Search by name or email"
      class="search-bar"
    />
    
    <!-- Display Filtered Members -->
    <ul>
      <li v-for="member in members" :key="member.id" @click="editMember(member.id)" class="member-item">
        <div class="member-info">
          <h2>
            <span class="name">{{ member.first_name }} {{ member.last_name }}</span>
            <span class="email">{{ member.email }}</span>
            <span class="phone">{{ member.phone }}</span>
          </h2>
          <span v-if="member.role === 'admin'" class="admin-tag">Admin</span>
        </div>
      </li>
    </ul>

    <!-- Pagination Controls -->
    <div class="pagination-controls">
      <button @click="prevPage" :disabled="currentPage === 1">Previous</button>
      <span>Page {{ currentPage }} of {{ totalPages }}</span>
      <button @click="nextPage" :disabled="currentPage === totalPages">Next</button>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
// Native JavaScript debounce function
function debounce(func, wait) {
  let timeout;
  return function (...args) {
    clearTimeout(timeout);
    timeout = setTimeout(() => func.apply(this, args), wait);
  };
} 

export default {
  data() {
    return {
      searchQuery: '', // Holds the search query
      members: [], // Holds the current page of team members
      currentPage: 1, // Current page number
      totalPages: 1, // Total number of pages
      totalMembers: 0, // Total number of team members
    };
  },
  watch: {
    // Watch for changes in the search query and fetch data from the backend
    searchQuery: debounce(function(newQuery) {
      this.currentPage = 1; // Reset to the first page when searching
      this.fetchTeamMembers(newQuery);
    }, 300), // Wait 300ms after the user stops typing
    // Watch for changes in the current page and fetch data
    currentPage() {
      this.fetchTeamMembers(this.searchQuery);
    },
  },
  async mounted() {
    // Fetch team members when the component is mounted
    await this.fetchTeamMembers();
  },
  methods: {
    // Method to fetch team members from the backend
    async fetchTeamMembers(query = '') {
      try {
        const response = await axios.get('http://localhost:8000/api/team-members/', {
          params: {
            search: query, // Send the search query to the backend
            page: this.currentPage, // Send the current page to the backend
          },
        });
        this.members = response.data.results; // Update the members list
        this.totalPages = Math.ceil(response.data.count / 10); // Calculate total pages
        this.totalMembers = response.data.count; // Update total number of members
      } catch (error) {
        console.error('Error fetching team members:', error);
      }
    },
    // Method to go to the previous page
    prevPage() {
      if (this.currentPage > 1) {
        this.currentPage--;
      }
    },
    // Method to go to the next page
    nextPage() {
      if (this.currentPage < this.totalPages) {
        this.currentPage++;
      }
    },
    // Method to edit member, routes to the edit page
    editMember(id) {
      this.$router.push(`/edit/${id}`);
    },
  },
};
</script>

<style scoped>
.list-container {
  padding: 20px;
  max-width: 900px;
  margin: 0 auto;
  background-color: #f9f9f9;
  border-radius: 10px;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
}

h1 {
  text-align: center;
  color: #333;
}

.add-member-link {
  display: inline-block;
  padding: 10px 20px;
  background-color: #42b883;
  color: white;
  border-radius: 50%;
  font-size: 24px;
  text-align: center;
  margin-bottom: 20px;
  text-decoration: none;
}

.add-member-link:hover {
  background-color: #34a074;
}

ul {
  list-style-type: none;
  padding: 0;
}

.member-item {
  background-color: #fff;
  margin: 10px 0;
  padding: 15px;
  border-radius: 5px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  cursor: pointer;
}

.member-item:hover {
  background-color: #e9f7f5;
}

.member-info {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.admin-tag {
  color: #e74c3c;
  font-weight: bold;
}

.search-bar {
  width: 100%;
  padding: 0.8rem;
  margin-bottom: 1rem;
  border: 1px solid #ccc;
  border-radius: 4px;
  font-size: 1rem;
}

.search-bar:focus {
  outline: none;
  border-color: #4CAF50;
  box-shadow: 0 0 5px rgba(76, 175, 80, 0.5);
}

.pagination-controls {
  display: flex;
  justify-content: center;
  align-items: center;
  margin-top: 20px;
}

.pagination-controls button {
  padding: 0.5rem 1rem;
  margin: 0 0.5rem;
  border: 1px solid #ccc;
  border-radius: 4px;
  background-color: #fff;
  cursor: pointer;
}

.pagination-controls button:disabled {
  background-color: #f0f0f0;
  cursor: not-allowed;
}

.pagination-controls button:hover:not(:disabled) {
  background-color: #42b883;
  color: white;
  border-color: #42b883;
}

.member-info {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 10px;
  background-color: #fafafa;
  border-radius: 5px;
  transition: background-color 0.3s ease;
}

.member-info:hover {
  background-color: #f0f0f0;
}

.member-info h2 {
  margin: 0;
  font-size: 1.1rem;
  color: #333;
  display: flex;
  flex-direction: column;
  gap: 5px;
}

.member-info h2 span {
  font-size: 0.9rem;
  color: #666;
}

.member-info h2 .name {
  font-weight: bold;
  color: #42b883;
}

.member-info h2 .email {
  color: #007bff;
}

.member-info h2 .phone {
  color: #28a745;
}

.admin-tag {
  background-color: #e74c3c;
  color: white;
  padding: 5px 10px;
  border-radius: 15px;
  font-size: 0.8rem;
  font-weight: bold;
  text-transform: uppercase;
}
</style>

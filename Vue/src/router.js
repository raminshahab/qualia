import { createRouter, createWebHistory } from 'vue-router';
import TeamMemberList from './components/List.vue';
import AddTeamMember from './components/Add.vue';
import EditTeamMember from './components/Edit.vue';

const routes = [
    { path: '/', component: TeamMemberList },
    { path: '/add', component: AddTeamMember },
    { path: '/edit/:id', component: EditTeamMember },
  ];
  
  const router = createRouter({
    history: createWebHistory(),
    routes,
  });

  export default router;
  
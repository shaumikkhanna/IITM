import { createWebHistory, createRouter } from "vue-router";
import Login from "./components/Login.vue";
import Home from "./components/Home.vue";
import CreateBlog from "./components/CreateBlog.vue";
import EditBlog from "./components/EditBlog.vue";
import Blogpost from "./components/Blogpost.vue";
import Signup from "./components/Signup.vue";
import User from "./components/User.vue";

const routes = [
  {
    name: "home page",
    path: "/",
    component: Home,
  },
  {
    name: "login page",
    path: "/login",
    component: Login,
  },
  {
    name: "Signup page",
    path: "/signup",
    component: Signup,
  },
  {
    name: "Create Blog page",
    path: "/create",
    component: CreateBlog,
  },
  {
    name: "Show Blog",
    path: "/blog/:id",
    component: Blogpost,
  },
  {
    name: "Edit Blog",
    path: "/editblog/:id",
    component: EditBlog,
  },
  {
    name: "User Profile",
    path: "/user/:username",
    component: User,
  },
  {
    name: "User Blogs",
    path: "/userfeed/:id",
    component: User,
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;

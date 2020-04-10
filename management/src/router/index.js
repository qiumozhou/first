import Vue from 'vue'
import Router from 'vue-router'



Vue.use(Router)

const commonRoutes = [
  // {
  //   path: "/",
  //   name: "index",
  //   meta: { title: "主页" },
  //   component: () => import("../components/index.vue"),
  //   children: [
  //     {
  //       path: "/user",
  //       name: "user",
  //       meta: { title: "用户管理" },
  //       component: () => import("../components/user.vue")
  //     }

  //   ]
  // },
  {
    path: "/login",
    name: "login",
    meta: { title: "登录" },
    component: () => import("../components/login.vue")
  }, {
    path: "/register",
    name: "register",
    meta: { title: "注册" },
    component: () => import("../components/register.vue")
  }, {
    path: "/404",
    name: "404",
    meta: { title: "404" },
    component: () => import("../components/404.vue")

  }

]

export const asyncRoutes = [
  {
    path: "/index",
    name: "index",
    meta: { title: "主页" },
    component: () => import("../components/index.vue"),
    children: [
      {
        path: "/user",
        name: "user",
        meta: { title: "用户管理" },
        component: () => import("../components/user.vue")
      }

    ]
  }
]

const creatRouter = () => new Router({
  routes: commonRoutes,
})


const router = creatRouter()

export function resetRouter() {
  const newRouter = creatRouter()
  router.matcher = newRouter.matcher
}

export default router


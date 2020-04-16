import Vue from 'vue'
import Router from 'vue-router'



Vue.use(Router)

export const commonRoutes = [
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
    path: "/forbidden",
    name: "forbidden",
    meta: { title: "forbidden" },
    component: () => import("../components/forbidden.vue")

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
      },
      {
        path: "/permission",
        name: "permission",
        meta: { title: "权限管理" },
        component: () => import("../components/permission.vue")
      },
      {
        path: "/device",
        name: "device",
        meta: { title: "设备管理" },
        component: () => import("../components/device.vue")
      },

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


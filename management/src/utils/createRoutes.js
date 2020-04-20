import { asyncRoutes } from "@/router"
import store from "../store"

// 将菜单信息转成对应的路由信息 动态添加
export default function createRoutes(data) {
    const result = []
    const children = []
    result.push({
        path: '/index',
        name: "index",
        meta: { "title": "主页" },
        component: () => import('../components/index.vue'),
        children,
    })

    data[0].children.forEach(item => {
        generateRoutes(children, item)
    })

    // 最后添加404页面 否则会在登陆成功后跳到404页面
    result.push(
        { path: '*', redirect: '/forbidden' }
    )
    store.commit("setMenu", children)
    return result
}

function generateRoutes(children, item) {
    let pageList = ['user', "device", "permission", "home"]
    if (pageList.indexOf(item.name) != -1) {
        children.push(item)

    }
}
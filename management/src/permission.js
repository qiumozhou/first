// import { LoadingBar } from "view-design"
import router from "./router"
import { asyncRoutes, commonRoutes } from "./router"
import createRoutes from "@/utils/createRoutes"
import { getDocumentTitle, resetTokenAndClearUser } from "./utils"



// 判断是否是共有页面
function isCommon(data) {
    var flag = false
    commonRoutes.forEach((item, index) => {
        if (item.path == data) {
            flag = true
        }
    })
    return flag
}
//  是否有菜单数据
let hasMenus = false
router.beforeEach(async (to, from, next) => {
    document.title = getDocumentTitle(to.meta.title)
    // LoadingBar.start()
    localStorage.setItem("token", "111")
    if (localStorage.getItem("token")) {
        if (isCommon(to.path)) {
            next()
        } else if (hasMenus) {
            next()
        } else {
            try {
                // 这里可以用 await 配合请求后台数据来生成路由
                // const data = await axios.get('xxx')
                // const routes = createRoutes(data)
                const routes = createRoutes(asyncRoutes)
                // 动态添加路由
                router.addRoutes(routes)
                hasMenus = true
                next("/index")

            } catch (error) {
                resetTokenAndClearUser()
                next("/login?redirect=${to.path}")
            }
        }
    } else {
        hasMenus = false
        if (to.path === "/login") {
            next()
        } else {
            next("/login?redirect=${to.path}")
        }
    }
})



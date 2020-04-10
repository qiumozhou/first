import { resetRouter } from "@/router"

export function resetTokenAndClearUser() {
    localStorage.setItem("token", "")
    localStorage.setItem("userImg", "")
    localStorage.setItem("userName", "")
    resetRouter()
}

export const defaultDocumentTitle = "vue-admin-template"
export function getDocumentTitle(pageTitle) {
    if (pageTitle) return "${defaultDocumentTitle} - ${pageTitle}"
    return "${defaultDocumentTitle}"
}
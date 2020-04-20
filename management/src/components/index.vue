<template>
  <div style="height:984px">
    <el-container style="height: 100%; border: 1px solid #eee">
      <el-aside>
        <el-row class="tac">
          <el-col style="width:302px;text-align:center">
            <h3>后台管理系统</h3>
            <el-menu
              class="el-menu-vertical-demo"
              background-color="#545c64"
              text-color="#fff"
              active-text-color="#ffd04b"
              :default-active="$route.path"
            >
              <el-menu-item v-for="(item,index) in pageList" :index="item.path" :key="index">
                <router-link :to="item.path">
                  <i class="iconfont" :class="item.meta.icon">{{ item.meta.title }}</i>
                </router-link>
              </el-menu-item>
            </el-menu>
          </el-col>
        </el-row>
      </el-aside>
      <el-container>
        <el-header>
          <div class="log">
          <!-- 用户头像 -->
          <div class="user-avator">
            <img src="../assets/img.png" />
          </div>
          <el-dropdown class="user-name" trigger="click" @command="handleCommand">
            <span class="el-dropdown-link">
              {{username}}
            </span>
            <el-dropdown-menu slot="dropdown">
              <el-dropdown-item divided command="loginout">退出登录</el-dropdown-item>
            </el-dropdown-menu>
          </el-dropdown>
          </div>
        </el-header>
        <el-main>
          <router-view />
        </el-main>

        <!-- <el-footer style="height:200px">Footer</el-footer> -->
      </el-container>
    </el-container>
  </div>
</template>

<script>
import device from "./device";
import user from "./device";
import store from "../store";
export default {
  name: "index",
  components: { device, user },
  data() {
    return {
      pageList: "",
      username:"admin"
    };
  },
  methods: {
    // 用户名下拉菜单选择事件
        handleCommand(command) {
            if (command == 'loginout') {
                localStorage.removeItem('ms_username');
                this.$router.push('/login');
            }
        },
  },
  mounted() {
    this.pageList = store.state.menuList;
  }
};
</script>

<style scoped>
.el-header {
  background-color: #b3c0d1;
  color: #333;
  line-height: 60px;
  position: relative;
}

.el-aside {
  overflow: hidden;
  color: #333;
  background-color: rgb(84, 92, 100);
}
a {
  position: relative;
  display: block;
  width: 100%;
  height: 100%;
  text-decoration: none;
  text-align: center;
  font-size: 20px;
}
.el-icon-setting {
  position: absolute;
  top: 18px;
  left: 60px;
}
.el-header,
.el-footer {
  background-color: #b3c0d1;
  color: #333;
  text-align: center;
  line-height: 60px;
}
.el-main {
  background-color: #e9eef3;
  color: #333;
  text-align: center;
  line-height: 160px;
}
i {
  vertical-align: middle;
  display: table-cell;
  padding-left: 80px;
}
.user-avator {
  margin: 10px auto;
  float: left;
}
.user-avator img {
  display: block;
  width: 40px;
  height: 40px;
  border-radius: 50%;
}
.el-dropdown{
text-align: center
}
.el-dropdown-link {
    color: #fff;
    cursor: pointer;
}
.el-dropdown-menu__item {
    text-align: center;
}
.log{
  position: absolute;
  right: 40px;
}
.el-icon-caret-bottom
{
  width: 30px
}
</style>

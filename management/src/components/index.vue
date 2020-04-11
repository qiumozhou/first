<template>
  <div style="height:984px">
    <el-container style="height: 100%; border: 1px solid #eee">
      <el-aside>
        <el-row class="tac">
          <el-col style="width:302px">
            <h5>自定义颜色</h5>
            <el-menu
              class="el-menu-vertical-demo"
              background-color="#545c64"
              text-color="#fff"
              active-text-color="#ffd04b"
              :default-active="$route.path"
            >
              <el-menu-item v-for="(item,index) in pageList" :index="item.path" :key="index">
                <router-link :to="item.path">
                  <i class="el-icon-setting"></i>
                  {{ item.meta.title }}
                </router-link>
              </el-menu-item>
            </el-menu>
          </el-col>
        </el-row>
      </el-aside>
      <el-container>
        <el-header>Header</el-header>
        <el-main>
          <router-view />
        </el-main>

        <el-footer>Footer</el-footer>
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
      pageList: ""
    };
  },
  methods: {},
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
</style>

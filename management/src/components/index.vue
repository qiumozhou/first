<template>
  <div>
    <el-container style="height: 100%; border: 1px solid #eee">
      <el-aside>
        <el-row class="tac">
          <el-col style="width:302px">
            <h5>自定义颜色</h5>
            <el-menu
              default-active="2"
              class="el-menu-vertical-demo"
              @open="handleOpen"
              @close="handleClose"
              background-color="#545c64"
              text-color="#fff"
              active-text-color="#ffd04b"
            >
              <el-menu-item index="1">
                <i class="el-icon-s-custom"></i>
                <span slot="title">账户管理</span>
              </el-menu-item>
              <el-menu-item index="2">
                <i class="el-icon-setting"></i>
                <span slot="title">车型库</span>
              </el-menu-item>
              <el-menu-item index="3">
                <i class="el-icon-menu"></i>
                <span slot="title">板件库</span>
              </el-menu-item>
              <el-menu-item index="4">
                <i class="el-icon-document"></i>
                <span slot="title">油漆库</span>
              </el-menu-item>
              <el-menu-item index="5">
                <i class="el-icon-setting"></i>
                <span slot="title">工艺库</span>
              </el-menu-item>
            </el-menu>
          </el-col>
        </el-row>
      </el-aside>

      <el-container>
        <el-header style="text-align: right; font-size: 12px">
          <el-dropdown>
            <i class="el-icon-setting" style="margin-right: 15px"></i>
            <el-dropdown-menu slot="dropdown">
              <el-dropdown-item>查看</el-dropdown-item>
              <el-dropdown-item>新增</el-dropdown-item>
              <el-dropdown-item>删除</el-dropdown-item>
            </el-dropdown-menu>
          </el-dropdown>
          <span>王小虎</span>
        </el-header>

        <el-main>
          <el-table :data="tableData">
            <el-table-column prop="date" label="日期" width="140"></el-table-column>
            <el-table-column prop="name" label="姓名" width="120"></el-table-column>
            <el-table-column prop="address" label="地址"></el-table-column>
          </el-table>
        </el-main>
      </el-container>
    </el-container>
  </div>
</template>

<script>
export default {
  name: "index",
  data() {
    const item = {
      date: "2016-05-02",
      name: "王小虎",
      address: "上海市普陀区金沙江路 1518 弄"
    };
    return {
      tableData: Array(20).fill(item)
    };
  },
  methods: {
    handleOpen(key, keyPath) {
      console.log(key, keyPath);
    },
    handleClose(key, keyPath) {
      console.log(key, keyPath);
    }
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
</style>

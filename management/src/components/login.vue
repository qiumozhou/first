<template>
  <div class="container">
    <div class="login">
      <el-form
        :model="ruleForm"
        status-icon
        ref="ruleForm"
        label-width="130px"
        class="demo-ruleForm"
      >
        <el-form-item label="帐号">
          <el-input type="text" v-model="ruleForm.pass" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="密码">
          <el-input type="password" v-model="ruleForm.checkPass" autocomplete="off"></el-input>
        </el-form-item>

        <el-form-item class="tijiao">
          <el-button type="primary" @click="submitForm('ruleForm')">登录</el-button>
        </el-form-item>
      </el-form>
    </div>
  </div>
</template>
<script>
export default {
  name: "login",
  data() {
    return {
      ruleForm: {
        pass: "",
        checkPass: "",
        age: ""
      },
    };
  },
  methods: {
  }
};
</script>

<style scoped>
.tijiao {
  margin: 0 auto;
}
.el-form-item {
  width: 300px;
  margin-top: 40px;
}

.el-input {
  width: 200px;
  /* margin: 0 auto; */
}
.login {
  position: absolute;
  left: 50%;
  top: 50%;
  margin-left: -225px;
  margin-top: -150px;
  width: 450px;
  height: 300px;
  background-color: rgba(0, 0, 0, 0.5);
}
.container {
  width: 100%;
  height: 100%;
  background-image: url(../assets/login.jpg);
  background-repeat: no-repeat;
  background-size: cover;
}
</style>
<template>
  <div class="register-wrapper">
    <div class="card">
      <div class="card2">
        <form class="form">
          <p id="heading">注册</p>
          <div class="field">
            <input
              v-model="username"
              type="text"
              class="input-field"
              placeholder="用户名"
              autocomplete="off"
            />
          </div>
          <div class="field">
            <input
              v-model="email"
              type="email"
              class="input-field"
              placeholder="邮箱"
              autocomplete="off"
            />
          </div>
          <div class="field">
            <input
              v-model="password"
              type="password"
              class="input-field"
              placeholder="密码"
            />
          </div>
          <div class="field">
            <input
              v-model="confirmPassword"
              type="password"
              class="input-field"
              placeholder="确认密码"
            />
          </div>
          <div class="btn">
            <button type="button" class="button1" @click.prevent="register">
              &nbsp;&nbsp;&nbsp;&nbsp;注册&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
            </button>
          </div>
          <div class="login-link">
            <span>已有账号？</span>
            <a @click="goLogin">点击登录~</a>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      username: "",
      email: "",
      password: "",
      confirmPassword: "",
    };
  },
  methods: {
    goLogin() {
      this.$router.push("/login");
    },
    register() {
      // 注册逻辑
    },
  },
};
</script>

<style scoped>
.register-wrapper {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
  width: 100%;
  background-color: #0a0a0a;
}

.card {
  background-image: linear-gradient(163deg, #00ff75 0%, #3700ff 100%);
  border-radius: 22px;
  transition: all 0.3s;
  padding: 2px;
  width: 380px;
}

.card2 {
  border-radius: 0;
  transition: all 0.2s;
}

.card2:hover {
  transform: scale(0.98);
  border-radius: 20px;
}

.card:hover {
  box-shadow: 0px 0px 30px 1px rgba(0, 255, 117, 0.3);
}

#heading {
  text-align: center;
  margin: 2em;
  color: rgb(255, 255, 255);
  font-size: 1.5em;
}

.field {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 0.5em;
  border-radius: 25px;
  padding: 0.6em;
  border: none;
  outline: none;
  color: white;
  background-color: #171717;
  box-shadow: inset 2px 5px 10px rgb(5, 5, 5);
}

.input-field {
  background: none;
  border: none;
  outline: none;
  width: 100%;
  color: #d3d3d3;
  padding: 0.5em;
}

.form {
  display: flex;
  flex-direction: column;
  gap: 10px;
  padding-left: 2em;
  padding-right: 2em;
  padding-bottom: 0.4em;
  background-color: #171717;
  border-radius: 25px;
  transition: 0.4s ease-in-out;
}

.form .btn {
  display: flex;
  justify-content: center;
  flex-direction: row;
  margin-top: 0.5em;  /* 从2.5em调整为1.5em */
  margin-bottom: 1em;
}

.button1 {
  padding: 0.5em;
  padding-left: 1.1em;
  padding-right: 1.1em;
  border-radius: 5px;
  margin-right: 0.5em;
  margin-bottom: 10px;
  border: none;
  outline: none;
  transition: 0.4s ease-in-out;
  background-color: #252525;
  color: white;
}

.button1:hover {
  background-color: black;
  color: white;
}

.login-link {
  text-align: center;
  margin-top: 1em;
  color: #d3d3d3;
}

.login-link a {
  color: #00ff75;
  cursor: pointer;
  text-decoration: none;
}

.login-link a:hover {
  text-decoration: underline;
}
</style>
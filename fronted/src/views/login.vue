<template>
  <div class="login-wrapper">
    <!-- 修改系统名称位置 -->
    <h1 class="system-title">若听个人音乐管理系统</h1>
    <div class="card">
      <div class="card2">
        <form class="form">
          <p id="heading">登录</p>
          <div class="field">
            <svg
              viewBox="0 0 16 16"
              fill="currentColor"
              height="16"
              width="16"
              xmlns="http://www.w3.org/2000/svg"
              class="input-icon"
            >
              <path
                d="M13.106 7.222c0-2.967-2.249-5.032-5.482-5.032-3.35 0-5.646 2.318-5.646 5.702 0 3.493 2.235 5.708 5.762 5.708.862 0 1.689-.123 2.304-.335v-.862c-.43.199-1.354.328-2.29.328-2.926 0-4.813-1.88-4.813-4.798 0-2.844 1.921-4.881 4.594-4.881 2.735 0 4.608 1.688 4.608 4.156 0 1.682-.554 2.769-1.416 2.769-.492 0-.772-.28-.772-.76V5.206H8.923v.834h-.11c-.266-.595-.881-.964-1.6-.964-1.4 0-2.378 1.162-2.378 2.823 0 1.737.957 2.906 2.379 2.906.8 0 1.415-.39 1.709-1.087h.11c.081.67.703 1.148 1.503 1.148 1.572 0 2.57-1.415 2.57-3.643zm-7.177.704c0-1.197.54-1.907 1.456-1.907.93 0 1.524.738 1.524 1.907S8.308 9.84 7.371 9.84c-.895 0-1.442-.725-1.442-1.914z"
              ></path>
            </svg>
            <input
              v-model="email"
              type="text"
              class="input-field"
              placeholder="Email"
              autocomplete="off"
              @input="handleEmailInput"
            />
            <div class="email-suggestions" v-if="emailSuggestions.length">
              <div 
                v-for="suggestion in emailSuggestions" 
                :key="suggestion"
                @click="selectEmailSuggestion(suggestion)"
              >
                {{ suggestion }}
              </div>
            </div>
          </div>
          <div class="field">
            <svg
              viewBox="0 0 16 16"
              fill="currentColor"
              height="16"
              width="16"
              xmlns="http://www.w3.org/2000/svg"
              class="input-icon"
            >
              <path
                d="M8 1a2 2 0 0 1 2 2v4H6V3a2 2 0 0 1 2-2zm3 6V3a3 3 0 0 0-6 0v4a2 2 0 0 0-2 2v5a2 2 0 0 0 2 2h6a2 2 0 0 0 2-2V9a2 2 0 0 0-2-2z"
              ></path>
            </svg>
            <input
              v-model="password"
              :type="showPassword ? 'text' : 'password'"
              class="input-field"
              placeholder="Password"
            />
            <span class="password-toggle" @click="togglePasswordVisibility">
              <svg v-if="showPassword" viewBox="0 0 24 24" width="16" height="16">
                <path fill="currentColor" d="M12,9A3,3 0 0,1 15,12A3,3 0 0,1 12,15A3,3 0 0,1 9,12A3,3 0 0,1 12,9M12,4.5C17,4.5 21.27,7.61 23,12C21.27,16.39 17,19.5 12,19.5C7,19.5 2.73,16.39 1,12C2.73,7.61 7,4.5 12,4.5M3.18,12C4.83,15.36 8.24,17.5 12,17.5C15.76,17.5 19.17,15.36 20.82,12C19.17,8.64 15.76,6.5 12,6.5C8.24,6.5 4.83,8.64 3.18,12Z" />
              </svg>
              <svg v-else viewBox="0 0 24 24" width="16" height="16">
                <path fill="currentColor" d="M11.83,9L15,12.16C15,12.11 15,12.05 15,12A3,3 0 0,0 12,9C11.94,9 11.89,9 11.83,9M7.53,9.8L9.08,11.35C9.03,11.56 9,11.77 9,12A3,3 0 0,0 12,15C12.22,15 12.44,14.97 12.65,14.92L14.2,16.47C13.53,16.8 12.79,17 12,17A5,5 0 0,1 7,12C7,11.21 7.2,10.47 7.53,9.8M2,4.27L4.28,6.55L4.73,7C3.08,8.3 1.78,10 1,12C2.73,16.39 7,19.5 12,19.5C13.55,19.5 15.03,19.2 16.38,18.66L16.81,19.08L19.73,22L21,20.73L3.27,3L2,4.27Z" />
              </svg>
            </span>
          </div>
          <div class="btn">
            <button type="button" class="button1" @click="login()">
              &nbsp;&nbsp;&nbsp;&nbsp;登录&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
            </button>
            <button type="button" class="button2" @click="goRegister()">&nbsp;注册&nbsp;</button>
          </div>
          <button class="button3" @click="showForgotPassword">忘记密码</button>
        </form>
      </div>
    </div>
    <!-- 添加Element UI弹窗 -->
    <el-dialog title="提示" :visible.sync="dialogVisible" width="30%" center>
      <span>请联系管理员重置密码</span>
      <span slot="footer" class="dialog-footer">
        <el-button type="primary" @click="dialogVisible = false"
          >确 定</el-button
        >
      </span>
    </el-dialog>
  </div>
</template>

<script>
import axios from 'axios';
export default {
  data() {
    return {
      email: "",
      password: "",
      dialogVisible: false,
      emailSuggestions: [],
      showPassword: false  // 添加showPassword状态
    };
  },
  methods: {
    handleEmailInput() {
      if (this.email.includes('@')) {
        this.emailSuggestions = [];
        return;
      }
      
      const domains = ['qq.com', '163.com', 'gmail.com', 'outlook.com', 'yahoo.com'];
      this.emailSuggestions = domains.map(domain => `${this.email}@${domain}`);
    },
    selectEmailSuggestion(suggestion) {
      this.email = suggestion;
      this.emailSuggestions = [];
    },
    showForgotPassword() {
      this.dialogVisible = true;
    },
    async login() {
      if (!this.email || !this.password) {
        this.$message.error('请输入邮箱和密码');
        return;
      }
      
      try {
        const response = await axios.post('/user/login', {
          email: this.email,
          password: this.password
        });

        if (response.data.code === 200) {
          this.$message.success(response.data.message);
          this.$router.push('/home');
        } else {
          this.$message.error(response.data.message);
        }
      } catch (error) {
        if (error.response) {
          this.$message.error(error.response.data.message || '登录失败');
        } else {
          this.$message.error('网络错误，请稍后重试');
        }
      }
    },
    goRegister() {
      this.$router.push('/register');
    },
    togglePasswordVisibility() {  // 添加切换密码可见性的方法
      this.showPassword = !this.showPassword;
    }
  },
};
</script>

<style scoped>
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

/* 新增外层容器样式 */
.login-wrapper {
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
  padding: 2px; /* 添加内边距使发光效果更明显 */
  width: 380px; /* 固定卡片宽度 */
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
  position: relative;  /* 添加相对定位 */
}

.email-suggestions {
  position: absolute;
  top: calc(100% + 5px);  /* 调整距离 */
  left: 0;
  width: calc(100% - 1.2em);  /* 减去左右padding */
  margin: 0 0.6em;  /* 与输入框对齐 */
  background-color: #252525;
  border-radius: 0 0 5px 5px;
  z-index: 10;
  max-height: 200px;
  overflow-y: auto;
}

.input-icon {
  height: 1.3em;
  width: 1.3em;
  fill: white;
}

.input-field {
  background: none;
  border: none;
  outline: none;
  width: 100%;
  color: #d3d3d3;
}

.form .btn {
  display: flex;
  justify-content: center;
  flex-direction: row;
  margin-top: 2.5em;
}

.button1 {
  padding: 0.5em;
  padding-left: 1.1em;
  padding-right: 1.1em;
  border-radius: 5px;
  margin-right: 0.5em;
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

.button2 {
  padding: 0.5em;
  padding-left: 2.3em;
  padding-right: 2.3em;
  border-radius: 5px;
  border: none;
  outline: none;
  transition: 0.4s ease-in-out;
  background-color: #252525;
  color: white;
}

.button2:hover {
  background-color: black;
  color: white;
}

.button3 {
  margin-bottom: 3em;
  padding: 0.5em;
  border-radius: 5px;
  border: none;
  outline: none;
  transition: 0.4s ease-in-out;
  background-color: #252525;
  color: white;
}

.button3:hover {
  background-color: red;
  color: white;
}

/* 添加弹窗样式 */
.el-dialog {
  background: #1e1e1e !important;
  border-radius: 10px !important;
}

.el-dialog__title {
  color: white !important;
}

.el-dialog__body {
  color: white !important;
  background: #1e1e1e !important;
}

.el-dialog__footer {
  background: #1e1e1e !important;
}

/* 修改系统名称样式 */
.system-title {
  color: white;
  text-align: center;
  margin-bottom: 30px;
  font-size: 2rem;
  text-shadow: 0 0 10px rgba(255, 255, 255, 0.5);
  position: fixed;
  top: 10%; /* 调整到更靠上的位置 */
  width: 100%;
  z-index: 1;
  pointer-events: none;
}
.email-suggestions {
  position: absolute;
  top: 100%;
  left: 0;
  width: 100%;
  background-color: #252525;
  border-radius: 0 0 5px 5px;
  z-index: 10;
  max-height: 200px;
  overflow-y: auto;
}

.email-suggestions div {
  padding: 8px 16px;
  cursor: pointer;
  color: #d3d3d3;
}

.email-suggestions div:hover {
  background-color: #171717;
  color: white;
}
.password-toggle {
  position: absolute;
  right: 15px;
  cursor: pointer;
  color: #d3d3d3;
}

.password-toggle:hover {
  color: white;
}
</style>
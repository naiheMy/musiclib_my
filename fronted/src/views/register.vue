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
            <input
              v-model="password"
              :type="showPassword ? 'text' : 'password'"
              class="input-field"
              placeholder="密码"
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
          <div class="field">
            <input
              v-model="confirmPassword"
              :type="showPassword ? 'text' : 'password'"
              class="input-field"
              placeholder="确认密码"
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
import axios from 'axios';

export default {
  data() {
    return {
      username: "",
      email: "",
      password: "",
      confirmPassword: "",
      gender: 0,
      age: "",
      avatar: "",
      emailSuggestions: [],  // 添加邮箱建议列表
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
    goLogin() {
      this.$router.push("/login");
    },
    togglePasswordVisibility() {  // 添加切换密码可见性的方法
      this.showPassword = !this.showPassword;
    },
    async register() {
      if (!this.username || !this.email || !this.password || !this.confirmPassword) {
        this.$message.error('请填写完整信息');
        return;
      }
      
      if (this.password !== this.confirmPassword) {
        this.$message.error('两次输入的密码不一致');
        return;
      }

      try {
        const response = await axios.post('/user/add', {
          username: this.username,
          email: this.email,
          password: this.password,
          gender: this.gender,
          age: this.age,
          avatar: this.avatar
        });

        if (response.data.code === 200) {
          this.$message.success(response.data.message);
          this.$router.push('/login');
        } else {
          this.$message.error(response.data.message);
        }
      } catch (error) {
        if (error.response) {
          this.$message.error(error.response.data.message || '注册失败');
        } else {
          this.$message.error('网络错误，请稍后重试');
        }
      }
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
  margin-top: 0.5em;
  margin-bottom: 0.5em; /* 从1em调整为0.5em */
}

.button1 {
  padding: 0.5em;
  padding-left: 1.1em;
  padding-right: 1.1em;
  border-radius: 5px;
  margin-right: 0.5em;
  border: none;  /* 移除margin-bottom */
  outline: none;
  transition: 0.4s ease-in-out;
  background-color: #252525;
  color: white;
  width: 40%;  /* 添加宽度设置 */
}

.button1:hover {
  background-color: black;
  color: white;
}

/* 保持.login-link样式不变 */
.login-link {
  text-align: center;
  color: #d3d3d3;
  margin-top: 0.5em;
  margin-bottom: 1em;
}

.login-link a {
  color: #00ff75;
  cursor: pointer;
  text-decoration: none;
}

.login-link a:hover {
  text-decoration: underline;
}

.email-suggestions {
  position: absolute;
  top: calc(100% + 5px);
  left: 0;
  width: calc(100% - 1.2em);
  margin: 0 0.6em;
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
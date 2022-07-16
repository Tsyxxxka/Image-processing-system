<template>
  <div class="basic" style="background: #fff; min-height: 100%">
    <el-head>
      <Navigation/>
    </el-head>
    <el-container style="position: absolute; height: 95%; width: 100%; border: 0">
      <el-container style="margin-top: 5%; margin-right: 236px; margin-left: 236px">
        <el-header style="text-align: center; font-size: 36px">
          <div class="heading">
            {{ headmsg }}
          </div>
        </el-header>

        <el-main style="text-align: left; font-size: 18px">
          <el-divider content-position="left">项目概览</el-divider>
          <p style="margin-left: 2em; margin-bottom: 0; line-height: 2em">
            {{ intromsg }}
            <br>
            可以进行基础的图片处理功能，如：翻转、旋转、灰度化、二值化、反色、去噪、边缘检测等。
          </p>
          <el-divider content-position="left">项目介绍</el-divider>
          <p style="margin-left: 2em; margin-top: 0; line-height: 2em">
            项目成员：滕思怡 10190350453，刘雨杰
            <br>
            项目结构:
          </p>
          <div class="code">
            <div class="code_inline">
              - \apps \\后端Python项目代码
              <br>
              - \static \\前端Vue项目代码
            </div>
          </div>
          <p style="margin-left: 2em; margin-bottom: 0; line-height: 2em">
            项目部署位置：
          </p>
          <ul style="margin-top: 0; margin-left: 2em; margin-bottom: 0; line-height: 2em; list-style-type:circle">
            <li>前端端口：9091</li>
            <li>后端端口：5000</li>
          </ul>
          <p style="margin-left: 2em; margin-top: 0; margin-bottom: 0; line-height: 2em">
            项目环境:
          </p>
          <ul style="margin-top: 0; margin-left: 2em; line-height: 2em; list-style-type:circle">
            <li>前端</li>
          </ul>
          <div class="front_env">
            <div class="front_env_inline">
              - Vue: 2.6.11
              <br>
              - element-ui: 2.15.8
              <br>
              - vue-router: 3.5.4
            </div>
          </div>
          <ul style="margin-left: 2em; line-height: 2em; list-style-type:circle">
            <li>后端：</li>
          </ul>
          <div class="back_env">
            <div class="back_env_inline">
              - Python: 3.8
              <br>
              - Flask: 2.1.2
              <br>
              - Flask-Cors: 3.0.10
              <br>
              - Pillow: 9.1.1
              <br>
              - matplotLib: 3.5.2
              <br>
              - numpy: 1.22.4
              <br>
              - opencv-python: 4.55.64
            </div>
          </div>
          <p style="margin-left: 2em; margin-top: 0; margin-bottom: 0; line-height: 2em">
            需要注意：/apps/assets/default_usage/default_pic.jpg与/apps/results/default_usage/default_res.jpg不可删除。
          </p>
          <el-divider content-position="left">项目功能</el-divider>
          <p style="margin-left: 2em; margin-top: 0; margin-bottom: 0; line-height: 2em">
            项目功能：
          </p>
          <ul style="margin-top: 0; margin-left: 2em; line-height: 2em; list-style-type:circle">
            <li>基础功能：灰度化、二值化、逻辑运算（基于灰度图）、四则运算、翻转、平移、放缩</li>
            <li>图像分析：灰度直方图、彩色直方图</li>
            <li>图像分割：基于多种算子的边缘检测、线条变化检测</li>
            <li>图像平滑和锐化：针对空域与频域的多种平滑和锐化功能</li>
            <li>图像形态学：腐蚀、膨胀、开运算、闭运算</li>
            <li>图像修复：添加高斯噪声或椒盐噪声、均值滤波、统计滤波、频域滤波</li>
          </ul>
        </el-main>

        <el-footer height="10px">
          <Copyright/>
        </el-footer>
      </el-container>
    </el-container>
  </div>
</template>

<script>
import Navigation from "@/components/global/Navigation"
import Copyright from "@/components/global/Copyright"
import Head from "@/components/global/Head"

export default {
  name: "Home",
  data() {
    return {
      headmsg: '图像处理系统',
      intromsg: '一个简单的图像处理系统。'
    }
  },
  methods: {},
  components: {
    Head,
    Navigation,
    Copyright
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.code {
  font-family: Menlo, math;
  font-size: 70%;
  background: #e9e9e9;
  margin-left: 20%;
  margin-right: 20%;
  border: solid #333333;
}

.code .code_inline {
  margin: 2em;
}

.front_env {
  font-family: Menlo, math;
  font-size: 70%;
  background: #e9e9e9;
  margin-left: 20%;
  margin-right: 20%;
  border: solid #333333;
}

.front_env .front_env_inline {
  margin: 2em;
}

.back_env {
  font-family: Menlo, math;
  font-size: 70%;
  background: #e9e9e9;
  margin-left: 20%;
  margin-right: 20%;
  border: solid #333333;
  margin-bottom: 2em;
}

.back_env .back_env_inline {
  margin: 2em;
}
</style>

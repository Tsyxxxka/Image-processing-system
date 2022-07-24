<template>
  <div style="background: #fff; min-height: 100%">
    <el-head>
      <Navigation/>
    </el-head>
    <el-container style="position: absolute; height: 95%; width: 100%; border: 0">
      <el-container style="margin-top: 5%; margin-right: 236px; margin-left: 236px">
        <el-header style="text-align: center; font-size: 36px">
          <div class="content-title">
            {{ headmsg }}
          </div>
        </el-header>
        <div class="content">
          <el-carousel :interval="4000" type="card" height="400px" indicator-position="outside">
            <el-carousel-item v-for="item in imgs" v-bind:key="item">
              <img class="bannerImg" :src="item.url">
            </el-carousel-item>
          </el-carousel>
          <el-divider content-position="left">项目小组成员</el-divider>
          <el-table :data="tableData" style="width: 1000px; margin-left:30px; font-size: 18px;">
            <el-table-column prop="name" label="姓名" width="200" />
            <el-table-column prop="schoolID" label="学号" width="200" />
            <el-table-column prop="mail" label="邮箱" width="280" />
            <el-table-column prop="work" label="主要工作" width="300" />
          </el-table>
          <el-divider content-position="left">项目主要功能</el-divider>
          <p style="text-align: left; font-size: 18px;margin-left: 2em; margin-bottom: 0; line-height: 2em">
            项目最终完成难度系数： 1.5
            <br>
            在实现课堂基础要求的图像处理功能之外，还通过阅读相关文献、借鉴相关开源代码，实现了图像的风格迁移功能，对项目的现实应用有了较为明确的定位。
            <br>
            项目基础功能：
            <br>
            图片上传
            <br>
            图像编辑：翻转、平移、旋转、放缩
            <br>
            图像转换：图像灰度化、二值化
            <br>
            图像分析：灰度直方图、彩色直方图
            <br>
            图像边缘检测：Robert、Sobel、Laplacian、LoG、Canny
            <br>
            图像增强：平滑、锐化
            <br>
            图像形态学：腐蚀、膨胀、开运算、闭运算
            <br>
            图像风格迁移
          </p>
          <el-divider content-position="left">项目主要技术栈</el-divider>
          <p style="text-align: left; font-size: 18px;margin-left: 2em; margin-bottom: 0; line-height: 2em">
            前端：Vue，ElementUI，Vue-Router
            <br>
            后端：Flask，Python，open-cv，tensorflow，numpy，matplotLib，Pillow
          </p>
          <el-divider content-position="left">项目快速启动</el-divider>
          <p style="text-align: left; font-size: 18px;margin-left: 2em; margin-bottom: 0; line-height: 2em">
            bash run.sh
          </p>
        </div>
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
      intromsg: '一个简单的图像处理系统。',
      tableData : [{
        name: '滕思怡',
        schoolID : '10190350453',
        mail:'tsyxxxka@gmail.com',
        work: '基础功能实现与图片风格迁移',
      },
      {
        name: '刘雨杰',
        schoolID : '',
        mail:'',
        work: '相关应用调研与基础功能实现',
      }],
      imgs: [
        {url: require('../assets/picture/front1.jpg'), link: '/content1'},
        {url: require('../assets/picture/front2.png'), link: '/content2'},
        {url: require('../assets/picture/front3.jpeg'), link: '/content3'},
        {url: require('../assets/picture/front4.jpg'), link: '/content4'}
      ]
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

.content {
    padding: 25px 25px;
    margin: 25px auto;
    background-color: #fff;
    border-radius: 20px;
    border: #e3e1e4 2px solid;
    font-size: 18px;
}

.content-title {
    color: #335A66;
    font-size: 40px;
    border: none;
    text-align: center;
}
</style>

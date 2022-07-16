<template>
  <div>
    <el-menu background-color="#545c64" 
             text-color="#fff"
             mode="horizontal" 
             default-active="$route.path" 
             router="true">
      <el-menu-item />
      <el-menu-item index="/">
        <i class="el-icon-s-home"></i>
        <span slot="title">主页</span>
      </el-menu-item>

      <el-menu-item index="/basic_func">
        <i class="el-icon-picture-outline"></i>
        <span slot="title">基础功能</span>
      </el-menu-item>

      <el-menu-item index="/histogram">
        <i class="el-icon-s-data"></i>
        <span slot="title">图像分析</span>
      </el-menu-item>

      <el-menu-item index="/segmentation">
        <i class="el-icon-scissors"></i>
        <span slot="title">图像分割</span>
      </el-menu-item>

      <el-submenu index="/smooth_sharpen">
        <template slot="title">
          <i class="el-icon-s-operation"></i>
          <span slot="title">图像平滑与锐化</span>
        </template>

        <el-menu-item index="/smooth_sharpen/smooth">图像平滑</el-menu-item>
        <el-menu-item index="/smooth_sharpen/sharpen">图像锐化</el-menu-item>

      </el-submenu>

      <el-menu-item index="/morphological">
        <i class="el-icon-magic-stick"></i>
        <span slot="title">图像形态学</span>
      </el-menu-item>

      <el-submenu index="/fix">
        <template slot="title">
          <i class="el-icon-s-opportunity"></i>
        <span slot="title">图像修复</span>
        </template>

        <el-menu-item index="/fix/noise">添加噪声</el-menu-item>
        <el-menu-item index="/fix/repair">图像去噪</el-menu-item>

      </el-submenu>

      <el-menu-item @click.native="drawer = true">
        <i class="el-icon-upload"></i>
        <span slot="title">图片上传</span>
      </el-menu-item>

      <el-drawer
          :visible.sync="drawer"
          :with-header="false">
        <FileUpload/>
      </el-drawer>
    </el-menu>
  </div>
</template>

<script>
import FileUpload from "@/components/global/FileUpload"

export default {
  name: "Navigation",
  components: {FileUpload},
  data() {
    return {
      drawer: false
    }
  }
}
</script>

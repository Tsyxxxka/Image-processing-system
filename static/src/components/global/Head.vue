<template>
  <div class="header">
    <div class="head">
      <el-button @click="drawer = true" type="primary" style="width:140px;">
        上传图片
      </el-button>

      <el-drawer
          :visible.sync="drawer"
          :with-header="false">
        <FileUpload/>
      </el-drawer>
    </div>
  </div>
</template>

<script>
import FileUpload from "@/components/global/FileUpload"

export default {
  name: "Head",
  components: {FileUpload},
  data() {
    return {
      drawer: false,
    };
  }
}
</script>

<style scoped>
.header{
  justify-content: left;
  margin-top: 20px;
}
</style>
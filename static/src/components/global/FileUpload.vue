<template>
  <div class="upload">
    <el-upload
        class="upload-demo"
        drag
        multiple
        action="http://127.0.0.1:5000/api/file/upload"
        :on-preview="handlePreview"
        :on-remove="handleRemove"
        :before-upload="beforeAvatarUpload"
        :on-success="handleSuccess"
        :on-error="handleError"
        :file-list="fileList"
        list-type="picture">
      <i class="el-icon-upload"></i>
      <div class="el-upload__text">将文件拖到此处，或<em>点击上传</em></div>
      <div class="el-upload__tip" slot="tip">只能上传jpg文件，且不超过2MB</div>
    </el-upload>
  </div>
</template>

<script>
export default {
  name: "FileUpload",
  data() {
    return {
      fileList: [],
      uploadResult: ''
    };
  },
  methods: {
    beforeAvatarUpload(file) {
      const isJPG = file.type === 'image/jpeg';
      const isLt2M = file.size / 1024 / 1024 < 2;

      if (!isJPG) {
        this.$message.error('上传头像图片只能是 JPG 格式!');
      }
      if (!isLt2M) {
        this.$message.error('上传头像图片大小不能超过 2MB!');
      }
      if (this.fileMaintain.isExistFile(file.name)) {
        this.$message.error('同名文件已存在!');
      }

      return isJPG && isLt2M && (!this.fileMaintain.isExistFile(file.name));
    },
    handleRemove(file, fileList) {
      console.log(file, fileList);
    },
    handlePreview(file) {
      console.log(file);
    },
    handleSuccess(res, file) {
      this.fileMaintain.saveFileList(file.name)

      this.uploadResult = res

      if (this.uploadResult.code === 1) {
        this.$message({
          message: this.uploadResult.msg,
          type: 'success'
        });
      } else if (this.uploadResult.code === 0) {
        this.$message.error(this.uploadResult.msg)
      }
    },
    handleError() {
      this.$message.error('上传文件失败');
    }
  }
}
</script>

<style scoped>
.upload {
  margin-top: 70px;
  margin-left: 30px;
  margin-right: 30px;
  margin-bottom: 70px;
}
</style>
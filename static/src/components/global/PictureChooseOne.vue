<template>
  <div style="width: 100%; max-height: 100%">
    <el-table
        ref="multipleTable"
        :data="fileList"
        tooltip-effect="dark"
        height="320"
        style="width: 100%"
        @selection-change="handleSelectionChange">
      <el-table-column
          type="selection"
          min-width="10%">
      </el-table-column>
      <el-table-column
          align="center"
          prop="fileName"
          label="图片名称"
          min-width="50%">
      </el-table-column>
      <el-table-column
          align="center"
          label="图片预览"
          min-width="40%">
        <template slot-scope="scope">
          <el-popover placement="top-start" title="" trigger="hover">
            <img :src="'http://127.0.0.1:5000/api/get_ori_file/' + scope.row.fileName" alt=""
                 style="width: 150px; height:auto">
            <img slot="reference" :src="'http://127.0.0.1:5000/api/get_ori_file/' + scope.row.fileName"
                 style="width: 70px; height: auto">
          </el-popover>
          <span>{{ scope.row.title }}</span>
        </template>
      </el-table-column>
    </el-table>
    <el-button @click="freshData()" style="margin-top: 15px">刷新</el-button>
    <el-button @click="toggleSelection()" style="margin-top: 15px">取消选择</el-button>
  </div>
</template>

<script>
export default {
  name: "PictureChooseOne",
  data() {
    return {
      fileList: [],
      multipleSelection: []
    }
  },
  created() {
    this.fileList = this.fileMaintain.curFileList()
  },
  methods: {
    handleSelectionChange(val) {
      this.multipleSelection = val;
      for (var i = 0; i < this.multipleSelection.length; i ++) {
        this.multipleSelection[i].fileUrl = this.constant.data().OriFileBaseUrl + this.multipleSelection[i].fileName;
      }
    },
    toggleSelection(rows) {
      if (rows) {
        rows.forEach(row => {
          this.$refs.multipleTable.toggleRowSelection(row);
        });
      } else {
        this.$refs.multipleTable.clearSelection();
      }
    },
    freshData() {
      this.fileList = this.fileMaintain.curFileList()
    }
  }
}
</script>

<style scoped>

</style>
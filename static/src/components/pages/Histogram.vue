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
          <el-divider content-position="left">直方图分析</el-divider>
          {{ intromsg }}
          <el-tabs type="border-card" style="margin-top: 30px; min-height: 80%">
            <el-tab-pane label="灰度直方图">
              <el-steps :active="gray_hist_active" finish-status="success" simple style="margin-top: 10px">
                <el-step title="选择图片"></el-step>
                <el-step title="输入参数"></el-step>
                <el-step title="处理图片"></el-step>
              </el-steps>

              <div v-show="gray_hist_active === 0" style="margin-top: 20px;">
                <PictureChooseOne ref="gray_histSelection"/>
              </div>

              <div v-show="gray_hist_active === 1"
                   style="text-align: center; margin-top: 20px; min-height: 375px; max-height: 375px">
                <div style="margin-left: 20%; margin-right: 20%">
                  <el-form :model="gray_histForm" class="demo-form-inline">
                    <el-form-item label="输出图像名称"
                                  label-width="30%"
                                  :rules="[
                      { required: true, message: '名称不能为空'}
                      ]"
                                  style="align-content: center; margin-left: 10%; margin-right: 10%; width: 60%">
                      <el-input v-model="gray_histForm.res_name">
                        <template slot="append">.jpg</template>
                      </el-input>
                    </el-form-item>
                  </el-form>
                </div>
              </div>

              <div v-show="gray_hist_active === 2"
                   style="text-align: center; margin-top: 20px; min-height: 375px; max-height: 375px">
                <div>
                  <span class="demonstration">原图片</span>
                  <br>
                  <img :src="this.displayImg[0].fileUrl" alt=""
                       style="width: auto; height: auto; max-width: 400px; max-height: 300px; margin-top: 30px">
                </div>
              </div>

              <div v-show="gray_hist_active === 3"
                   style="text-align: center; margin-top: 20px; min-height: 375px; max-height: 375px">
                <div>
                  <span class="demonstration">结果图片</span>
                  <br>
                  <img :src="this.processResult.result_name" alt=""
                       style="width: auto; height: auto; max-width: 400px; max-height: 300px; margin-top: 30px">
                </div>
              </div>

              <el-button style="margin-left: 80%; margin-top: 10px;" @click="cancel">取消</el-button>
              <el-button v-show="gray_hist_active <= 2" :loading="gray_histLoad" style="margin-left: 10px; margin-top: 10px;"
                         @click="gray_hist_next">下一步
              </el-button>
              <el-button v-show="gray_hist_active >= 3" :loading="gray_histLoad" style="margin-left: 10px; margin-top: 10px;"
                         @click="cancel">完成
              </el-button>
            </el-tab-pane>

            <el-tab-pane label="彩色直方图">
              <el-steps :active="bgr_hist_active" finish-status="success" simple style="margin-top: 10px">
                <el-step title="选择图片"></el-step>
                <el-step title="输入参数"></el-step>
                <el-step title="处理图片"></el-step>
              </el-steps>

              <div v-show="bgr_hist_active === 0" style="margin-top: 20px;">
                <PictureChooseOne ref="bgr_histSelection"/>
              </div>

              <div v-show="bgr_hist_active === 1"
                   style="text-align: center; margin-top: 20px; min-height: 375px; max-height: 375px">
                <div style="margin-left: 20%; margin-right: 20%">
                  <el-form :model="bgr_histForm" class="demo-form-inline">
                    <el-form-item label="输出图像名称"
                                  label-width="30%"
                                  :rules="[
                      { required: true, message: '名称不能为空'}
                      ]"
                                  style="align-content: center; margin-left: 10%; margin-right: 10%; width: 60%">
                      <el-input v-model="bgr_histForm.res_name">
                        <template slot="append">.jpg</template>
                      </el-input>
                    </el-form-item>
                  </el-form>
                </div>
              </div>

              <div v-show="bgr_hist_active === 2"
                   style="text-align: center; margin-top: 20px; min-height: 375px; max-height: 375px">
                <div>
                  <span class="demonstration">原图片</span>
                  <br>
                  <img :src="this.displayImg[0].fileUrl" alt=""
                       style="width: auto; height: auto; max-width: 400px; max-height: 300px; margin-top: 30px">
                </div>
              </div>

              <div v-show="bgr_hist_active === 3"
                   style="text-align: center; margin-top: 20px; min-height: 375px; max-height: 375px">
                <div>
                  <span class="demonstration">结果图片</span>
                  <br>
                  <img :src="this.processResult.result_name" alt=""
                       style="width: auto; height: auto; max-width: 400px; max-height: 300px; margin-top: 30px">
                </div>
              </div>

              <el-button style="margin-left: 80%; margin-top: 10px;" @click="cancel">取消</el-button>
              <el-button v-show="bgr_hist_active <= 2" :loading="bgr_histLoad" style="margin-left: 10px; margin-top: 10px;"
                         @click="bgr_hist_next">下一步
              </el-button>
              <el-button v-show="bgr_hist_active >= 3" :loading="bgr_histLoad" style="margin-left: 10px; margin-top: 10px;"
                         @click="cancel">完成
              </el-button>
            </el-tab-pane>

          </el-tabs>
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
import PictureChooseOne from "@/components/global/PictureChooseOne"

export default {
  name: "Histogram",
  data() {
    return {
      headmsg: '图像分析',
      intromsg: '\xa0\xa0\xa0\xa0\xa0\xa0\xa0主要包含了图像的灰度直方图分析与彩色直方图分析等功能。',
      selection: [],
      displayImg: [
        {
          fileName: '../../../assets/picture/default_pic.jpg'
        },
        {
          fileName: '../../../assets/picture/default_pic.jpg'
        }
      ],
      processResult: {
        code: '',
        message: '',
        result_name: '../../../assets/picture/default_pic.jpg'
      },
      gray_hist_active: 0,
      gray_histForm: {
        res_name: ''
      },
      gray_histLoad: false,
      bgr_hist_active: 0,
      bgr_histForm: {
        res_name: ''
      },
      bgr_histLoad: false
    }
  },
  components: {
    Head,
    Navigation,
    Copyright,
    PictureChooseOne
  },
  methods: {
    cancel() {

      this.selection = [];
      this.displayImg = [{fileName: '../../../assets/picture/default_pic.jpg'}, {fileName: '../../../assets/picture/default_pic.jpg'}];

      this.clear_active();

      this.gray_histForm.res_name = '';
      this.bgr_histForm.res_name = '';

      this.gray_histLoad = false;
      this.bgr_histLoad = false;

      this.processResult = {
        code: '',
        message: '',
        result_name: '../../../assets/picture/default_pic.jpg'
      };
    },
    clear_active() {
      this.gray_hist_active = 0;
      this.bgr_hist_active = 0;
    },
    async gray_hist_next() {
      let tmp = this.gray_hist_active;
      this.clear_active();
      this.gray_hist_active = tmp;
      if (this.gray_hist_active === 0) {
        this.selection = this.$refs["gray_histSelection"].multipleSelection;
        this.displayImg[0] = this.selection[0];
        if (this.selection.length !== 1) {
          this.$alert('选择的图片数量不是一张！', '数量错误', {
            confirmButtonText: '确定'
          });
          return
        }

      } else if (this.gray_hist_active === 1) {
        if (this.gray_histForm.res_name === '') {
          this.$alert('输出图像名称不能为空！', '命名错误', {
            confirmButtonText: '确定'
          });
          return
        }
        this.gray_histForm.res_name = this.utils.calculate_res_name(this.gray_histForm.res_name);
      } else if (this.gray_hist_active === 2) {
        const axios = require('axios')

        this.gray_histLoad = true;

        await axios.get(
            this.constant.data().BaseUrl + '/histogram/gray', {
              params: {
                img_name: this.selection[0].fileName,
                result_name: this.gray_histForm.res_name
              }
            }
        ).then(
            (res) => {
              this.processResult = res.data;
              if (this.processResult.code === '1') {
                this.$message({
                  message: '图片处理成功！',
                  type: 'success'
                });
              } else if (this.processResult.code === '2') {
                this.$message.error('图片处理成功！');
              }
            }
        )

        this.gray_histLoad = false;


      } else if (this.gray_hist_active === 3) {
        this.gray_hist_active = 0;

        return
      }


      this.gray_hist_active++;
    },
    async bgr_hist_next() {
      let tmp = this.bgr_hist_active;
      this.clear_active();
      this.bgr_hist_active = tmp;
      if (this.bgr_hist_active === 0) {
        this.selection = this.$refs["bgr_histSelection"].multipleSelection;
        this.displayImg[0] = this.selection[0];
        if (this.selection.length !== 1) {
          this.$alert('选择的图片数量不是一张！', '数量错误', {
            confirmButtonText: '确定'
          });
          return
        }

      } else if (this.bgr_hist_active === 1) {
        if (this.bgr_histForm.res_name === '') {
          this.$alert('输出图像名称不能为空！', '命名错误', {
            confirmButtonText: '确定'
          });
          return
        }
        this.bgr_histForm.res_name = this.utils.calculate_res_name(this.bgr_histForm.res_name);
      } else if (this.bgr_hist_active === 2) {
        const axios = require('axios')

        this.bgr_histLoad = true;

        await axios.get(
            this.constant.data().BaseUrl + '/histogram/bgr', {
              params: {
                img_name: this.selection[0].fileName,
                result_name: this.bgr_histForm.res_name
              }
            }
        ).then(
            (res) => {
              this.processResult = res.data;
              if (this.processResult.code === '1') {
                this.$message({
                  message: '图片处理成功！',
                  type: 'success'
                });
              } else if (this.processResult.code === '2') {
                this.$message.error('图片处理成功！');
              }
            }
        )

        this.bgr_histLoad = false;


      } else if (this.bgr_hist_active === 3) {
        this.bgr_hist_active = 0;

        return
      }


      this.bgr_hist_active++;
    }
  }
}
</script>

<style scoped>

</style>
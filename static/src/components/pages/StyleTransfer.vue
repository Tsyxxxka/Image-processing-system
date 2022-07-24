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
          <el-divider content-position="left">图片风格迁移</el-divider>
          {{ intromsg }}
          <el-tabs type="border-card" style="margin-top: 30px; min-height: 80%">
            <el-tab-pane label="风格迁移">
              <el-steps :active="gauss_noise_active" finish-status="success" simple style="margin-top: 10px">
                <el-step title="选择风格图片"></el-step>
                <el-step title="选择内容图片"></el-step>
                <el-step title="输入参数"></el-step>
                <el-step title="处理图片"></el-step>
              </el-steps>

              <div v-show="gauss_noise_active === 0" style="margin-top: 20px;">
                <PictureChooseOne ref="gauss_noiseSelection1"/>
              </div>

              <div v-show="gauss_noise_active === 1" style="margin-top: 20px;">
                <PictureChooseOne ref="gauss_noiseSelection2"/>
              </div>

              <div v-show="gauss_noise_active === 2"
                   style="text-align: center; margin-top: 20px; min-height: 375px; max-height: 375px">
                <div style="margin-left: 20%; margin-right: 20%">
                  <el-form :model="gauss_noiseForm" class="demo-form-inline">
                    <el-form-item label="输出图像名称"
                                  label-width="30%"
                                  :rules="[
                      { required: true, message: '名称不能为空'}
                      ]"
                                  style="align-content: center; margin-left: 10%; margin-right: 10%; width: 60%">
                      <el-input v-model="gauss_noiseForm.res_name">
                        <template slot="append">.jpg</template>
                      </el-input>
                    </el-form-item>
                  </el-form>
                </div>
              </div>

              <div v-show="gauss_noise_active === 3"
                   style="text-align: center; margin-top: 20px; min-height: 375px; max-height: 375px">
                <div>
                  <span class="demonstration">原图片</span>
                  <br>
                  <img :src="this.displayImg[0].fileUrl" alt=""
                       style="width: auto; height: auto; max-width: 400px; max-height: 300px; margin-top: 30px">
                </div>
              </div>

              <div v-show="gauss_noise_active === 4"
                   style="text-align: center; margin-top: 20px; min-height: 375px; max-height: 375px">
                <div>
                  <span class="demonstration">结果图片</span>
                  <br>
                  <img :src="this.processResult.result_name" alt=""
                       style="width: auto; height: auto; max-width: 400px; max-height: 300px; margin-top: 30px">
                </div>
              </div>

              <el-button style="margin-left: 80%; margin-top: 10px;" @click="cancel">取消</el-button>
              <el-button v-show="gauss_noise_active <= 3" :loading="gauss_noiseLoad" style="margin-left: 10px; margin-top: 10px;"
                         @click="gauss_noise_next">下一步
              </el-button>
              <el-button v-show="gauss_noise_active >= 4" :loading="gauss_noiseLoad" style="margin-left: 10px; margin-top: 10px;"
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
  name: "Style",
  data() {
    return {
      headmsg: '图片风格迁移',
      intromsg: '\xa0\xa0\xa0\xa0\xa0\xa0\xa0实现了任意风格和任意内容图像的风格迁移功能。',
      selection_style: [],
      selection_content: [],
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
      gauss_noise_active: 0,
      gauss_noiseForm: {
        res_name: ''
      },
      gauss_noiseLoad: false,
      sault_pepper_noise_active: 0,
      sault_pepper_noiseForm: {
        res_name: '',
        ran_x1: null,
        ran_y1: null,
        ran_x2: null,
        ran_y2: null
      },
      sault_pepper_noiseLoad: false
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

      this.selection_style = [];
      this.selection_content = [];
      this.displayImg = [{fileName: '../../../assets/picture/default_pic.jpg'}, {fileName: '../../../assets/picture/default_pic.jpg'}];

      this.clear_active();

      this.gauss_noiseForm.res_name = '';
      this.sault_pepper_noiseForm.res_name = '';
      this.sault_pepper_noiseForm.ran_x1 = null;
      this.sault_pepper_noiseForm.ran_y1 = null;
      this.sault_pepper_noiseForm.ran_x2 = null;
      this.sault_pepper_noiseForm.ran_y2 = null;

      this.gauss_noiseLoad = false;
      this.sault_pepper_noiseLoad = false;

      this.processResult = {
        code: '',
        message: '',
        result_name: '../../../assets/picture/default_pic.jpg'
      };
    },
    clear_active() {
      this.gauss_noise_active = 0;
      this.sault_pepper_noise_active = 0;
    },
    async gauss_noise_next() {
      let tmp = this.gauss_noise_active;
      this.clear_active();
      this.gauss_noise_active = tmp;
      if (this.gauss_noise_active === 0) {
        this.selection_style = this.$refs["gauss_noiseSelection1"].multipleSelection;
        this.displayImg[0] = this.selection_style[0];
        if (this.selection_style.length !== 1) {
          this.$alert('选择的图片数量不是一张！', '数量错误', {
            confirmButtonText: '确定'
          });
          return
        }

      } else if (this.gauss_noise_active === 1) {
        this.selection_content = this.$refs["gauss_noiseSelection2"].multipleSelection;
        this.displayImg[0] = this.selection_content[0];
        if (this.selection_content.length !== 1) {
          this.$alert('选择的图片数量不是一张！', '数量错误', {
            confirmButtonText: '确定'
          });
          return
        }


      } else if (this.gauss_noise_active === 2) {
        if (this.gauss_noiseForm.res_name === '') {
          this.$alert('输出图像名称不能为空！', '命名错误', {
            confirmButtonText: '确定'
          });
          return
        }
        this.gauss_noiseForm.res_name = this.utils.calculate_res_name(this.gauss_noiseForm.res_name);
      } else if (this.gauss_noise_active === 3) {
        const axios = require('axios')

        this.gauss_noiseLoad = true;

        await axios.get(
            this.constant.data().BaseUrl + '/styleTransfer/style_transfer', {
              params: {
                img_style_name: this.selection_style[0].fileName,
                img_content_name: this.selection_content[0].fileName,
                result_name: this.gauss_noiseForm.res_name
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

        this.gauss_noiseLoad = false;


      } else if (this.gauss_noise_active === 3) {
        this.gauss_noise_active = 0;

        return
      }


      this.gauss_noise_active++;
    },
  }
}
</script>

<style scoped>

</style>
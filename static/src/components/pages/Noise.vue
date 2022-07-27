<template>
  <div class="basic" style="background: #e9e9e9; min-height: 100%">
    <el-head>
      <Navigation/>
    </el-head>
    <el-container style="position: absolute; height: 100%; width: 100%; border: 0">

      <el-container style="margin-top: 5%; margin-right: 300px; margin-left: 300px">
        <el-header style="text-align: center; font-size: 36px">
          <div class="heading">
            {{ headmsg }}
          </div>
        </el-header>

        <el-main style="text-align: left; font-size: 18px">
          {{ intromsg }}
          <el-tabs type="border-card" style="margin-top: 30px; min-height: 80%">
            <el-tab-pane label="高斯噪声">
              <el-steps :active="gauss_noise_active" align-center finish-status="success"style="margin-top: 40px">
                <el-step title="选择图片"></el-step>
                <el-step title="输入参数"></el-step>
                <el-step title="处理图片"></el-step>
              </el-steps>

              <div v-show="gauss_noise_active === 0" style="margin-top: 20px;">
                <PictureChooseOne ref="gauss_noiseSelection"/>
              </div>

              <div v-show="gauss_noise_active === 1"
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

              <div v-show="gauss_noise_active === 2"
                   style="text-align: center; margin-top: 20px; min-height: 375px; max-height: 375px">
                <div>
                  <span class="demonstration">原图片</span>
                  <br>
                  <img :src="this.displayImg[0].fileUrl" alt=""
                       style="width: auto; height: auto; max-width: 400px; max-height: 300px; margin-top: 30px">
                </div>
              </div>

              <div v-show="gauss_noise_active === 3"
                   style="text-align: center; margin-top: 20px; min-height: 375px; max-height: 375px">
                <div>
                  <span class="demonstration">结果图片</span>
                  <br>
                  <img :src="this.processResult.result_name" alt=""
                       style="width: auto; height: auto; max-width: 400px; max-height: 300px; margin-top: 30px">
                </div>
              </div>

              <el-button style="margin-left: 80%; margin-top: 30px;" @click="cancel">取消操作</el-button>
              <el-button v-show="gauss_noise_active <= 2" :loading="gauss_noiseLoad" style="margin-left: 10px; margin-top: 10px;"
                         @click="gauss_noise_next">下一步
              </el-button>
              <el-button v-show="gauss_noise_active >= 3" :loading="gauss_noiseLoad" style="margin-left: 10px; margin-top: 10px;"
                         @click="cancel">完成
              </el-button>

            </el-tab-pane>
            <el-tab-pane label="椒盐噪声">
              <el-steps :active="sault_pepper_noise_active" align-center finish-status="success"style="margin-top: 40px">
                <el-step title="选择图片"></el-step>
                <el-step title="输入参数"></el-step>
                <el-step title="处理图片"></el-step>
              </el-steps>

              <div v-show="sault_pepper_noise_active === 0" style="margin-top: 20px;">
                <PictureChooseOne ref="sault_pepper_noiseSelection"/>
              </div>

              <div v-show="sault_pepper_noise_active === 1"
                   style="text-align: center; margin-top: 20px; min-height: 375px; max-height: 375px">
                <div style="margin-left: 20%; margin-right: 20%">
                  <el-form :model="sault_pepper_noiseForm" class="demo-form-inline">
                    <el-form-item label="输出图像名称"
                                  label-width="30%"
                                  :rules="[
                      { required: true, message: '名称不能为空'}
                      ]"
                                  style="align-content: center; margin-left: 10%; margin-right: 10%; width: 60%">
                      <el-input v-model="sault_pepper_noiseForm.res_name">
                        <template slot="append">.jpg</template>
                      </el-input>
                    </el-form-item>


                    <el-form-item label="胡椒噪声范围"
                                  :rules="[
                      { required: true, message: '范围值不能为空'}
                      ]"
                                  style="align-content: center; margin-left: 10%; margin-right: 10%; width:80%">
                      <el-col :span="7">
                        <el-input placeholder="最小值" v-model="sault_pepper_noiseForm.ran_x1">
                        </el-input>
                      </el-col>
                      <el-col class="line" :span="2">-</el-col>
                      <el-col :span="7">
                        <el-input placeholder="无穷大输入'MAX'" v-model="sault_pepper_noiseForm.ran_y1">
                        </el-input>
                      </el-col>
                    </el-form-item>

                    <el-form-item label="食盐噪声范围"
                                  :rules="[
                      { required: true, message: '范围值不能为空'}
                      ]"
                                  style="align-content: center; margin-left: 10%; margin-right: 10%; width:80%">
                      <el-col :span="7">
                        <el-input placeholder="最小值" v-model="sault_pepper_noiseForm.ran_x2">
                        </el-input>
                      </el-col>
                      <el-col class="line" :span="2">-</el-col>
                      <el-col :span="7">
                        <el-input placeholder="无穷大输入'MAX'" v-model="sault_pepper_noiseForm.ran_y2">
                        </el-input>
                      </el-col>
                    </el-form-item>


                  </el-form>
                </div>
              </div>

              <div v-show="sault_pepper_noise_active === 2"
                   style="text-align: center; margin-top: 20px; min-height: 375px; max-height: 375px">
                <div>
                  <span class="demonstration">原图片</span>
                  <br>
                  <img :src="this.displayImg[0].fileUrl" alt=""
                       style="width: auto; height: auto; max-width: 400px; max-height: 300px; margin-top: 30px">
                </div>
              </div>

              <div v-show="sault_pepper_noise_active === 3"
                   style="text-align: center; margin-top: 20px; min-height: 375px; max-height: 375px">
                <div>
                  <span class="demonstration">结果图片</span>
                  <br>
                  <img :src="this.processResult.result_name" alt=""
                       style="width: auto; height: auto; max-width: 400px; max-height: 300px; margin-top: 30px">
                </div>
              </div>

              <el-button style="margin-left: 80%; margin-top: 30px;" @click="cancel">取消操作</el-button>
              <el-button v-show="sault_pepper_noise_active <= 2" :loading="sault_pepper_noiseLoad" style="margin-left: 10px; margin-top: 10px;"
                         @click="sault_pepper_noise_next">下一步
              </el-button>
              <el-button v-show="sault_pepper_noise_active >= 3" :loading="sault_pepper_noiseLoad" style="margin-left: 10px; margin-top: 10px;"
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
  name: "Noise",
  data() {
    return {
      headmsg: '添加噪声',
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

      this.selection = [];
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
        this.selection = this.$refs["gauss_noiseSelection"].multipleSelection;
        this.displayImg[0] = this.selection[0];
        if (this.selection.length !== 1) {
          this.$alert('选择的图片数量不是一张！', '数量错误', {
            confirmButtonText: '确定'
          });
          return
        }

      } else if (this.gauss_noise_active === 1) {
        if (this.gauss_noiseForm.res_name === '') {
          this.$alert('输出图像名称不能为空！', '命名错误', {
            confirmButtonText: '确定'
          });
          return
        }
        this.gauss_noiseForm.res_name = this.utils.calculate_res_name(this.gauss_noiseForm.res_name);
      } else if (this.gauss_noise_active === 2) {
        const axios = require('axios')

        this.gauss_noiseLoad = true;

        await axios.get(
            this.constant.data().BaseUrl + '/repair/gauss_noise', {
              params: {
                img_name: this.selection[0].fileName,
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
    async sault_pepper_noise_next() {
      let tmp = this.sault_pepper_noise_active;
      this.clear_active();
      this.sault_pepper_noise_active = tmp;
      if (this.sault_pepper_noise_active === 0) {
        this.selection = this.$refs["sault_pepper_noiseSelection"].multipleSelection;
        this.displayImg[0] = this.selection[0];
        if (this.selection.length !== 1) {
          this.$alert('选择的图片数量不是一张！', '数量错误', {
            confirmButtonText: '确定'
          });
          return
        }

      } else if (this.sault_pepper_noise_active === 1) {
        if ((this.sault_pepper_noiseForm.res_name === '') || (this.sault_pepper_noiseForm.ran_x1 === null) || (this.sault_pepper_noiseForm.ran_y1 === null) || (this.sault_pepper_noiseForm.ran_x2 === null) || (this.sault_pepper_noiseForm.ran_y2 === null)) {
          this.$alert('输出图像名称不能为空！<br>噪声范围不能为空！', '命名错误', {
            confirmButtonText: '确定',
            dangerouslyUseHTMLString: true
          });
          return
        }

        var tmp1;
        var tmp2;

        if (this.sault_pepper_noiseForm.ran_y1 !== 'MAX'){
            this.sault_pepper_noiseForm.ran_y1 = parseInt(this.sault_pepper_noiseForm.ran_y1)
            tmp1 = this.sault_pepper_noiseForm.ran_y1;
        }
        else {
            tmp1 =  Number.MAX_VALUE;
        }

        if (this.sault_pepper_noiseForm.ran_y2 !== 'MAX'){
            this.sault_pepper_noiseForm.ran_y2 = parseInt(this.sault_pepper_noiseForm.ran_y2)
            tmp2 = this.sault_pepper_noiseForm.ran_y2;
        }
        else {
            tmp2 =  Number.MAX_VALUE;
        }

        this.sault_pepper_noiseForm.ran_x1 = parseInt(this.sault_pepper_noiseForm.ran_x1)
        this.sault_pepper_noiseForm.ran_x2 = parseInt(this.sault_pepper_noiseForm.ran_x2)

        if((!this.utils.isMaxInteger(this.sault_pepper_noiseForm.ran_x1)) || (!this.utils.isMaxInteger(this.sault_pepper_noiseForm.ran_y1)) || (!this.utils.isMaxInteger(this.sault_pepper_noiseForm.ran_x2)) || (!this.utils.isMaxInteger(this.sault_pepper_noiseForm.ran_y2))) {
            this.$alert('噪声范围必须为数字！', '参数错误', {
                confirmButtonText: '确定'
            });
            return
        }

        if((this.sault_pepper_noiseForm.ran_x1 < 0) || (tmp1 < 0) || (this.sault_pepper_noiseForm.ran_x2 < 0) || (tmp2 < 0)) {
            this.$alert('噪声范围不能为负！', '参数错误', {
                confirmButtonText: '确定'
            });
            return
        }

        if((this.sault_pepper_noiseForm.ran_x1 > tmp1) || (this.sault_pepper_noiseForm.ran_x2 > tmp2)) {
            this.$alert('最小值不得大于最大值！', '参数错误', {
                confirmButtonText: '确定'
            });
            return
        }

        this.sault_pepper_noiseForm.res_name = this.utils.calculate_res_name(this.sault_pepper_noiseForm.res_name);
      } else if (this.sault_pepper_noise_active === 2) {
        const axios = require('axios')

        this.sault_pepper_noiseLoad = true;

        await axios.get(
            this.constant.data().BaseUrl + '/repair/sault_pepper_noise', {
              params: {
                img_name: this.selection[0].fileName,
                result_name: this.sault_pepper_noiseForm.res_name,
                ran_x1: this.sault_pepper_noiseForm.ran_x1,
                ran_y1: this.sault_pepper_noiseForm.ran_y1,
                ran_x2: this.sault_pepper_noiseForm.ran_x2,
                ran_y2: this.sault_pepper_noiseForm.ran_y2
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

        this.sault_pepper_noiseLoad = false;


      } else if (this.sault_pepper_noise_active === 3) {
        this.sault_pepper_noise_active = 0;

        return
      }


      this.sault_pepper_noise_active++;
    }
  }
}
</script>

<style scoped>

</style>
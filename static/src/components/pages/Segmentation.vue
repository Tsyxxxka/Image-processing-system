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
            <el-tab-pane label="Roberts 算子">
              <el-steps :active="roberts_active" align-center finish-status="success"style="margin-top: 40px">
                <el-step title="选择图片"></el-step>
                <el-step title="输入参数"></el-step>
                <el-step title="处理图片"></el-step>
              </el-steps>

              <div v-show="roberts_active === 0" style="margin-top: 20px;">
                <PictureChooseOne ref="robertsSelection"/>
              </div>

              <div v-show="roberts_active === 1"
                   style="text-align: center; margin-top: 20px; min-height: 375px; max-height: 375px">
                <div style="margin-left: 20%; margin-right: 20%">
                  <el-form :model="robertsForm" class="demo-form-inline">
                    <el-form-item label="输出图像名称"
                                  label-width="30%"
                                  :rules="[
                      { required: true, message: '名称不能为空'}
                      ]"
                                  style="align-content: center; margin-left: 10%; margin-right: 10%; width: 60%">
                      <el-input v-model="robertsForm.res_name">
                        <template slot="append">.jpg</template>
                      </el-input>
                    </el-form-item>


                    <el-form-item label="权值"
                                  :rules="[
                      { required: true, message: '权值不能为空'},
                      { type: 'number', message: '权值必须为数字值'}
                      ]"
                                  style="align-content: center; margin-left: 10%; margin-right: 10%; width:80%">
                      <el-col :span="7">
                        <el-input placeholder="x权值，推荐0.5" v-model="robertsForm.val1">
                        </el-input>
                      </el-col>
                      <el-col class="line" :span="2">,</el-col>
                      <el-col :span="7">
                        <el-input placeholder="y权值，推荐0.5" v-model="robertsForm.val2">
                        </el-input>
                      </el-col>
                    </el-form-item>

                    <el-form-item label="偏置值"
                                  label-width="30%"
                                  :rules=" [
                                  { required: true, message:'偏置值不能为空'},
                                  { type: 'number', message: '偏置值必须为数字值'}
                    ]"
                                  style="align-content: center; margin-left: 10%; margin-right: 10%; width: 60%">
                      <el-input placeholder="推荐0" v-model="robertsForm.exp">
                      </el-input>
                    </el-form-item>


                  </el-form>
                </div>
              </div>

              <div v-show="roberts_active === 2"
                   style="text-align: center; margin-top: 20px; min-height: 375px; max-height: 375px">
                <div>
                  <span class="demonstration">原图片</span>
                  <br>
                  <img :src="this.displayImg[0].fileUrl" alt=""
                       style="width: auto; height: auto; max-width: 400px; max-height: 300px; margin-top: 30px">
                </div>
              </div>

              <div v-show="roberts_active === 3"
                   style="text-align: center; margin-top: 20px; min-height: 375px; max-height: 375px">
                <div>
                  <span class="demonstration">结果图片</span>
                  <br>
                  <img :src="this.processResult.result_name" alt=""
                       style="width: auto; height: auto; max-width: 400px; max-height: 300px; margin-top: 30px">
                </div>
              </div>

              <el-button style="margin-left: 80%; margin-top: 30px;" @click="cancel">取消操作</el-button>
              <el-button v-show="roberts_active <= 2" :loading="robertsLoad" style="margin-left: 10px; margin-top: 10px;"
                         @click="roberts_next">下一步
              </el-button>
              <el-button v-show="roberts_active >= 3" :loading="robertsLoad" style="margin-left: 10px; margin-top: 10px;"
                         @click="cancel">完成
              </el-button>
            </el-tab-pane>
            <el-tab-pane label="Sobel 算子">
              <el-steps :active="sobel_active" align-center finish-status="success"style="margin-top: 40px">
                <el-step title="选择图片"></el-step>
                <el-step title="输入参数"></el-step>
                <el-step title="处理图片"></el-step>
              </el-steps>

              <div v-show="sobel_active === 0" style="margin-top: 20px;">
                <PictureChooseOne ref="sobelSelection"/>
              </div>

              <div v-show="sobel_active === 1"
                   style="text-align: center; margin-top: 20px; min-height: 375px; max-height: 375px">
                <div style="margin-left: 20%; margin-right: 20%">
                  <el-form :model="sobelForm" class="demo-form-inline">
                    <el-form-item label="输出图像名称"
                                  label-width="30%"
                                  :rules="[
                      { required: true, message: '名称不能为空'}
                      ]"
                                  style="align-content: center; margin-left: 10%; margin-right: 10%; width: 60%">
                      <el-input v-model="sobelForm.res_name">
                        <template slot="append">.jpg</template>
                      </el-input>
                    </el-form-item>


                    <el-form-item label="权值"
                                  :rules="[
                      { required: true, message: '权值不能为空'},
                      { type: 'number', message: '权值必须为数字值'}
                      ]"
                                  style="align-content: center; margin-left: 10%; margin-right: 10%; width:80%">
                      <el-col :span="7">
                        <el-input placeholder="x权值，推荐0.5" v-model="sobelForm.val1">
                        </el-input>
                      </el-col>
                      <el-col class="line" :span="2">,</el-col>
                      <el-col :span="7">
                        <el-input placeholder="y权值，推荐0.5" v-model="sobelForm.val2">
                        </el-input>
                      </el-col>
                    </el-form-item>

                    <el-form-item label="偏置值"
                                  label-width="30%"
                                  :rules=" [
                                  { required: true, message:'偏置值不能为空'},
                                  { type: 'number', message: '偏置值必须为数字值'}
                    ]"
                                  style="align-content: center; margin-left: 10%; margin-right: 10%; width: 60%">
                      <el-input placeholder="推荐0" v-model="sobelForm.exp">
                      </el-input>
                    </el-form-item>


                  </el-form>
                </div>
              </div>

              <div v-show="sobel_active === 2"
                   style="text-align: center; margin-top: 20px; min-height: 375px; max-height: 375px">
                <div>
                  <span class="demonstration">原图片</span>
                  <br>
                  <img :src="this.displayImg[0].fileUrl" alt=""
                       style="width: auto; height: auto; max-width: 400px; max-height: 300px; margin-top: 30px">
                </div>
              </div>

              <div v-show="sobel_active === 3"
                   style="text-align: center; margin-top: 20px; min-height: 375px; max-height: 375px">
                <div>
                  <span class="demonstration">结果图片</span>
                  <br>
                  <img :src="this.processResult.result_name" alt=""
                       style="width: auto; height: auto; max-width: 400px; max-height: 300px; margin-top: 30px">
                </div>
              </div>

              <el-button style="margin-left: 80%; margin-top: 30px;" @click="cancel">取消操作</el-button>
              <el-button v-show="sobel_active <= 2" :loading="sobelLoad" style="margin-left: 10px; margin-top: 10px;"
                         @click="sobel_next">下一步
              </el-button>
              <el-button v-show="sobel_active >= 3" :loading="sobelLoad" style="margin-left: 10px; margin-top: 10px;"
                         @click="cancel">完成
              </el-button>
            </el-tab-pane>
            <el-tab-pane label="Laplacian 算子">
              <el-steps :active="laplacian_active" align-center finish-status="success"style="margin-top: 40px">
                <el-step title="选择图片"></el-step>
                <el-step title="输入参数"></el-step>
                <el-step title="处理图片"></el-step>
              </el-steps>

              <div v-show="laplacian_active === 0" style="margin-top: 20px;">
                <PictureChooseOne ref="laplacianSelection"/>
              </div>

              <div v-show="laplacian_active === 1"
                   style="text-align: center; margin-top: 20px; min-height: 375px; max-height: 375px">
                <div style="margin-left: 20%; margin-right: 20%">
                  <el-form :model="laplacianForm" class="demo-form-inline">
                    <el-form-item label="输出图像名称"
                                  label-width="30%"
                                  :rules="[
                      { required: true, message: '名称不能为空'}
                      ]"
                                  style="align-content: center; margin-left: 10%; margin-right: 10%; width: 60%">
                      <el-input v-model="laplacianForm.res_name">
                        <template slot="append">.jpg</template>
                      </el-input>
                    </el-form-item>

                    <el-form-item label="滤波核数"
                                  label-width="30%"
                                  :rules=" [
                                  { required: true, message:'核数不能为空'},
                                  { type: 'number', message: '核数必须为数字值'}
                    ]"
                                  style="align-content: center; margin-left: 10%; margin-right: 10%; width: 60%">
                      <el-input placeholder="奇数，推荐3" v-model="laplacianForm.kernel_size">
                      </el-input>
                    </el-form-item>

                    <el-form-item label="偏置值"
                                  label-width="30%"
                                  :rules=" [
                                  { required: true, message:'偏置值不能为空'},
                                  { type: 'number', message: '偏置值必须为数字值'}
                    ]"
                                  style="align-content: center; margin-left: 10%; margin-right: 10%; width: 60%">
                      <el-input placeholder="推荐0" v-model="laplacianForm.exp">
                      </el-input>
                    </el-form-item>

                    <el-form-item label="处理核数"
                                  label-width="30%"
                                  :rules=" [
                                  { required: true, message:'核数不能为空'},
                                  { type: 'number', message: '核数必须为数字值'}
                    ]"
                                  style="align-content: center; margin-left: 10%; margin-right: 10%; width: 60%">
                      <el-input placeholder="奇数，推荐3" v-model="laplacianForm.k_size">
                      </el-input>
                    </el-form-item>


                  </el-form>
                </div>
              </div>

              <div v-show="laplacian_active === 2"
                   style="text-align: center; margin-top: 20px; min-height: 375px; max-height: 375px">
                <div>
                  <span class="demonstration">原图片</span>
                  <br>
                  <img :src="this.displayImg[0].fileUrl" alt=""
                       style="width: auto; height: auto; max-width: 400px; max-height: 300px; margin-top: 30px">
                </div>
              </div>

              <div v-show="laplacian_active === 3"
                   style="text-align: center; margin-top: 20px; min-height: 375px; max-height: 375px">
                <div>
                  <span class="demonstration">结果图片</span>
                  <br>
                  <img :src="this.processResult.result_name" alt=""
                       style="width: auto; height: auto; max-width: 400px; max-height: 300px; margin-top: 30px">
                </div>
              </div>

              <el-button style="margin-left: 80%; margin-top: 30px;" @click="cancel">取消操作</el-button>
              <el-button v-show="laplacian_active <= 2" :loading="laplacianLoad" style="margin-left: 10px; margin-top: 10px;"
                         @click="laplacian_next">下一步
              </el-button>
              <el-button v-show="laplacian_active >= 3" :loading="laplacianLoad" style="margin-left: 10px; margin-top: 10px;"
                         @click="cancel">完成
              </el-button>
            </el-tab-pane>
            <el-tab-pane label="LoG 算子">
              <el-steps :active="LoG_active" align-center finish-status="success"style="margin-top: 40px">
                <el-step title="选择图片"></el-step>
                <el-step title="输入参数"></el-step>
                <el-step title="处理图片"></el-step>
              </el-steps>

              <div v-show="LoG_active === 0" style="margin-top: 20px;">
                <PictureChooseOne ref="LoGSelection"/>
              </div>

              <div v-show="LoG_active === 1"
                   style="text-align: center; margin-top: 20px; min-height: 375px; max-height: 375px">
                <div style="margin-left: 20%; margin-right: 20%">
                  <el-form :model="LoGForm" class="demo-form-inline">
                    <el-form-item label="输出图像名称"
                                  label-width="30%"
                                  :rules="[
                      { required: true, message: '名称不能为空'}
                      ]"
                                  style="align-content: center; margin-left: 10%; margin-right: 10%; width: 60%">
                      <el-input v-model="LoGForm.res_name">
                        <template slot="append">.jpg</template>
                      </el-input>
                    </el-form-item>
                  </el-form>
                </div>
              </div>

              <div v-show="LoG_active === 2"
                   style="text-align: center; margin-top: 20px; min-height: 375px; max-height: 375px">
                <div>
                  <span class="demonstration">原图片</span>
                  <br>
                  <img :src="this.displayImg[0].fileUrl" alt=""
                       style="width: auto; height: auto; max-width: 400px; max-height: 300px; margin-top: 30px">
                </div>
              </div>

              <div v-show="LoG_active === 3"
                   style="text-align: center; margin-top: 20px; min-height: 375px; max-height: 375px">
                <div>
                  <span class="demonstration">结果图片</span>
                  <br>
                  <img :src="this.processResult.result_name" alt=""
                       style="width: auto; height: auto; max-width: 400px; max-height: 300px; margin-top: 30px">
                </div>
              </div>

              <el-button style="margin-left: 80%; margin-top: 30px;" @click="cancel">取消操作</el-button>
              <el-button v-show="LoG_active <= 2" :loading="LoGLoad" style="margin-left: 10px; margin-top: 10px;"
                         @click="LoG_next">下一步
              </el-button>
              <el-button v-show="LoG_active >= 3" :loading="LoGLoad" style="margin-left: 10px; margin-top: 10px;"
                         @click="cancel">完成
              </el-button>

            </el-tab-pane>
            <el-tab-pane label="Canny 算子">
              <el-steps :active="canny_active" align-center finish-status="success"style="margin-top: 40px">
                <el-step title="选择图片"></el-step>
                <el-step title="输入参数"></el-step>
                <el-step title="处理图片"></el-step>
              </el-steps>

              <div v-show="canny_active === 0" style="margin-top: 20px;">
                <PictureChooseOne ref="cannySelection"/>
              </div>

              <div v-show="canny_active === 1"
                   style="text-align: center; margin-top: 20px; min-height: 375px; max-height: 375px">
                <div style="margin-left: 20%; margin-right: 20%">
                  <el-form :model="cannyForm" class="demo-form-inline">
                    <el-form-item label="输出图像名称"
                                  label-width="30%"
                                  :rules="[
                      { required: true, message: '名称不能为空'}
                      ]"
                                  style="align-content: center; margin-left: 10%; margin-right: 10%; width: 60%">
                      <el-input v-model="cannyForm.res_name">
                        <template slot="append">.jpg</template>
                      </el-input>
                    </el-form-item>

                    <el-form-item label="滤波核数"
                                  label-width="30%"
                                  :rules=" [
                                  { required: true, message:'核数不能为空'},
                                  { type: 'number', message: '核数必须为数字值'}
                    ]"
                                  style="align-content: center; margin-left: 10%; margin-right: 10%; width: 60%">
                      <el-input placeholder="奇数，推荐3" v-model="cannyForm.kernel_size">
                      </el-input>
                    </el-form-item>

                    <el-form-item label="偏置值"
                                  label-width="30%"
                                  :rules=" [
                                  { required: true, message:'偏置值不能为空'},
                                  { type: 'number', message: '偏置值必须为数字值'}
                    ]"
                                  style="align-content: center; margin-left: 10%; margin-right: 10%; width: 60%">
                      <el-input placeholder="推荐0" v-model="cannyForm.exp">
                      </el-input>
                    </el-form-item>


                  </el-form>
                </div>
              </div>

              <div v-show="canny_active === 2"
                   style="text-align: center; margin-top: 20px; min-height: 375px; max-height: 375px">
                <div>
                  <span class="demonstration">原图片</span>
                  <br>
                  <img :src="this.displayImg[0].fileUrl" alt=""
                       style="width: auto; height: auto; max-width: 400px; max-height: 300px; margin-top: 30px">
                </div>
              </div>

              <div v-show="canny_active === 3"
                   style="text-align: center; margin-top: 20px; min-height: 375px; max-height: 375px">
                <div>
                  <span class="demonstration">结果图片</span>
                  <br>
                  <img :src="this.processResult.result_name" alt=""
                       style="width: auto; height: auto; max-width: 400px; max-height: 300px; margin-top: 30px">
                </div>
              </div>

              <el-button style="margin-left: 80%; margin-top: 30px;" @click="cancel">取消操作</el-button>
              <el-button v-show="canny_active <= 2" :loading="cannyLoad" style="margin-left: 10px; margin-top: 10px;"
                         @click="canny_next">下一步
              </el-button>
              <el-button v-show="canny_active >= 3" :loading="cannyLoad" style="margin-left: 10px; margin-top: 10px;"
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
import PictureChooseOne from "@/components/global/PictureChooseOne";

export default {
  name: "Segmentation",
  data() {
    return {
      headmsg: '图像分割',
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
      roberts_active: 0,
      robertsForm: {
        res_name: '',
        val1: null,
        val2: null,
        exp: null
      },
      robertsLoad: false,
      sobel_active: 0,
      sobelForm: {
        res_name: '',
        val1: null,
        val2: null,
        exp: null
      },
      sobelLoad: false,
      laplacian_active: 0,
      laplacianForm: {
        res_name: '',
        kernel_size: null,
        exp: null,
        k_size: null
      },
      laplacianLoad: false,
      LoG_active: 0,
      LoGForm: {
        res_name: ''
      },
      LoGLoad: false,
      canny_active: 0,
      cannyForm: {
        res_name: '',
        kernel_size: null,
        exp: null
      },
      cannyLoad: false,
      hough_lines_active: 0,
      hough_linesForm: {
        res_name: ''
      },
      hough_linesLoad: false,
      hough_linesP_active: 0,
      hough_linesPForm: {
        res_name: ''
      },
      hough_linesPLoad: false
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

      this.robertsForm.res_name = '';
      this.robertsForm.val1 = null;
      this.robertsForm.val2 = null;
      this.robertsForm.exp = null;
      this.sobelForm.res_name = '';
      this.sobelForm.val1 = null;
      this.sobelForm.val2 = null;
      this.sobelForm.exp = null;
      this.laplacianForm.res_name = '';
      this.laplacianForm.kernel_size = null;
      this.laplacianForm.exp = null;
      this.laplacianForm.k_size = null;
      this.LoGForm.res_name = '';
      this.cannyForm.res_name = '';
      this.cannyForm.kernel_size = null;
      this.cannyForm.exp = null;
      this.hough_linesForm.res_name = '';
      this.hough_linesPForm.res_name = '';

      this.robertsLoad = false;
      this.sobelLoad = false;
      this.laplacianLoad = false;
      this.LoGLoad = false;
      this.cannyLoad = false;
      this.hough_linesLoad = false;
      this.hough_linesPLoad = false;

      this.processResult = {
        code: '',
        message: '',
        result_name: '../../../assets/picture/default_pic.jpg'
      };
    },
    clear_active() {
      this.roberts_active = 0;
      this.sobel_active = 0;
      this.laplacian_active = 0;
      this.LoG_active = 0;
      this.canny_active = 0;
      this.hough_lines_active = 0;
      this.hough_linesP_active = 0;
    },
    async roberts_next() {
      let tmp = this.roberts_active;
      this.clear_active();
      this.roberts_active = tmp;
      if (this.roberts_active === 0) {
        this.selection = this.$refs["robertsSelection"].multipleSelection;
        this.displayImg[0] = this.selection[0];
        if (this.selection.length !== 1) {
          this.$alert('选择的图片数量不是一张！', '数量错误', {
            confirmButtonText: '确定'
          });
          return
        }

      } else if (this.roberts_active === 1) {
        if ((this.robertsForm.res_name === '') || (this.robertsForm.val1 === null) || (this.robertsForm.val2 === null) || (this.robertsForm.exp === null)) {
          this.$alert('输出图像名称不能为空！<br>权值不能为空！<br>偏置值不能为空！', '参数错误', {
            confirmButtonText: '确定',
            dangerouslyUseHTMLString: true
          });
          return
        }
        this.robertsForm.val1 = parseFloat(this.robertsForm.val1);
        this.robertsForm.val2 = parseFloat(this.robertsForm.val2);
        this.robertsForm.exp = parseFloat(this.robertsForm.exp);
        if ((!this.utils.isFloat(this.robertsForm.val1)) || (!this.utils.isFloat(this.robertsForm.val2)) || (!this.utils.isFloat(this.robertsForm.exp))) {
          this.$alert('权值必须为数字！<br>偏置值必须为数字！', '参数错误', {
            confirmButtonText: '确定',
            dangerouslyUseHTMLString: true
          });
          return
        }
        if ((this.robertsForm.val1 < 0) || (this.robertsForm.val2 < 0)) {
          this.$alert('权值不能为负！', '参数错误', {
            confirmButtonText: '确定'
          });
          return
        }
        this.robertsForm.res_name = this.utils.calculate_res_name(this.robertsForm.res_name);
      } else if (this.roberts_active === 2) {
        const axios = require('axios')

        this.robertsLoad = true;

        await axios.get(
            this.constant.data().BaseUrl + '/segmentation/roberts', {
              params: {
                img_name: this.selection[0].fileName,
                result_name: this.robertsForm.res_name,
                val1: this.robertsForm.val1,
                val2: this.robertsForm.val2,
                exp: this.robertsForm.exp
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

        this.robertsLoad = false;


      } else if (this.roberts_active === 3) {
        this.roberts_active = 0;

        return
      }


      this.roberts_active++;
    },
    async sobel_next() {
      let tmp = this.sobel_active;
      this.clear_active();
      this.sobel_active = tmp;
      if (this.sobel_active === 0) {
        this.selection = this.$refs["sobelSelection"].multipleSelection;
        this.displayImg[0] = this.selection[0];
        if (this.selection.length !== 1) {
          this.$alert('选择的图片数量不是一张！', '数量错误', {
            confirmButtonText: '确定'
          });
          return
        }

      } else if (this.sobel_active === 1) {
        if ((this.sobelForm.res_name === '') || (this.sobelForm.val1 === null) || (this.sobelForm.val2 === null) || (this.sobelForm.exp === null)) {
          this.$alert('输出图像名称不能为空！<br>权值不能为空！<br>偏置值不能为空！', '参数错误', {
            confirmButtonText: '确定',
            dangerouslyUseHTMLString: true
          });
          return
        }
        this.sobelForm.val1 = parseFloat(this.sobelForm.val1);
        this.sobelForm.val2 = parseFloat(this.sobelForm.val2);
        this.sobelForm.exp = parseFloat(this.sobelForm.exp);
        if ((!this.utils.isFloat(this.sobelForm.val1)) || (!this.utils.isFloat(this.sobelForm.val2)) || (!this.utils.isFloat(this.sobelForm.exp))) {
          this.$alert('权值必须为数字！<br>偏置值必须为数字！', '参数错误', {
            confirmButtonText: '确定',
            dangerouslyUseHTMLString: true
          });
          return
        }
        if ((this.sobelForm.val1 < 0) || (this.sobelForm.val2 < 0)) {
          this.$alert('权值不能为负！', '参数错误', {
            confirmButtonText: '确定'
          });
          return
        }
        this.sobelForm.res_name = this.utils.calculate_res_name(this.sobelForm.res_name);
      } else if (this.sobel_active === 2) {
        const axios = require('axios')

        this.sobelLoad = true;

        await axios.get(
            this.constant.data().BaseUrl + '/segmentation/sobel', {
              params: {
                img_name: this.selection[0].fileName,
                result_name: this.sobelForm.res_name,
                val1: this.sobelForm.val1,
                val2: this.sobelForm.val2,
                exp: this.sobelForm.exp
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

        this.sobelLoad = false;


      } else if (this.sobel_active === 3) {
        this.sobel_active = 0;

        return
      }


      this.sobel_active++;
    },
    async laplacian_next() {
      let tmp = this.laplacian_active;
      this.clear_active();
      this.laplacian_active = tmp;
      if (this.laplacian_active === 0) {
        this.selection = this.$refs["laplacianSelection"].multipleSelection;
        this.displayImg[0] = this.selection[0];
        if (this.selection.length !== 1) {
          this.$alert('选择的图片数量不是一张！', '数量错误', {
            confirmButtonText: '确定'
          });
          return
        }

      } else if (this.laplacian_active === 1) {
        if ((this.laplacianForm.res_name === '') || (this.laplacianForm.kernel_size === null) || (this.laplacianForm.exp === null) || (this.laplacianForm.k_size === null)) {
          this.$alert('输出图像名称不能为空！<br>滤波核数不能为空！<br>权值不能为空！<br>处理核数不能为空！', '参数错误', {
            confirmButtonText: '确定',
            dangerouslyUseHTMLString: true
          });
          return
        }
        this.laplacianForm.kernel_size = parseInt(this.laplacianForm.kernel_size);
        this.laplacianForm.exp = parseFloat(this.laplacianForm.exp);
        this.laplacianForm.k_size = parseInt(this.laplacianForm.k_size);
        if ((!this.utils.isInteger(this.laplacianForm.kernel_size)) || (!this.utils.isFloat(this.laplacianForm.exp)) || (!this.utils.isInteger(this.laplacianForm.k_size))) {
          this.$alert('滤波核数必须为数字！<br>权值必须为数字！<br>处理核数必须为数字！', '参数错误', {
            confirmButtonText: '确定',
            dangerouslyUseHTMLString: true
          });
          return
        }
        if ((this.laplacianForm.kernel_size % 2 === 0) || (this.laplacianForm.k_size % 2 === 0) || (this.laplacianForm.kernel_size <= 0) || (this.laplacianForm.k_size <= 0)) {
          this.$alert('核数必须为正奇数！', '参数错误', {
            confirmButtonText: '确定'
          });
          return
        }
        this.laplacianForm.res_name = this.utils.calculate_res_name(this.laplacianForm.res_name);
      } else if (this.laplacian_active === 2) {
        const axios = require('axios')

        this.laplacianLoad = true;

        await axios.get(
            this.constant.data().BaseUrl + '/segmentation/laplacian', {
              params: {
                img_name: this.selection[0].fileName,
                result_name: this.laplacianForm.res_name,
                kernel_size: this.laplacianForm.kernel_size,
                exp: this.laplacianForm.exp,
                k_size: this.laplacianForm.k_size
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

        this.laplacianLoad = false;


      } else if (this.laplacian_active === 3) {
        this.laplacian_active = 0;

        return
      }


      this.laplacian_active++;
    },
    async LoG_next() {
      let tmp = this.LoG_active;
      this.clear_active();
      this.LoG_active = tmp;
      if (this.LoG_active === 0) {
        this.selection = this.$refs["LoGSelection"].multipleSelection;
        this.displayImg[0] = this.selection[0];
        if (this.selection.length !== 1) {
          this.$alert('选择的图片数量不是一张！', '数量错误', {
            confirmButtonText: '确定'
          });
          return
        }

      } else if (this.LoG_active === 1) {
        if (this.LoGForm.res_name === '') {
          this.$alert('输出图像名称不能为空！', '命名错误', {
            confirmButtonText: '确定'
          });
          return
        }
        this.LoGForm.res_name = this.utils.calculate_res_name(this.LoGForm.res_name);
      } else if (this.LoG_active === 2) {
        const axios = require('axios')

        this.LoGLoad = true;

        await axios.get(
            this.constant.data().BaseUrl + '/segmentation/LoG', {
              params: {
                img_name: this.selection[0].fileName,
                result_name: this.LoGForm.res_name
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

        this.LoGLoad = false;


      } else if (this.LoG_active === 3) {
        this.LoG_active = 0;

        return
      }


      this.LoG_active++;
    },
    async canny_next() {
      let tmp = this.canny_active;
      this.clear_active();
      this.canny_active = tmp;
      if (this.canny_active === 0) {
        this.selection = this.$refs["cannySelection"].multipleSelection;
        this.displayImg[0] = this.selection[0];
        if (this.selection.length !== 1) {
          this.$alert('选择的图片数量不是一张！', '数量错误', {
            confirmButtonText: '确定'
          });
          return
        }

      } else if (this.canny_active === 1) {
        if ((this.cannyForm.res_name === '') || (this.cannyForm.kernel_size === null) || (this.cannyForm.exp === null)) {
          this.$alert('输出图像名称不能为空！<br>滤波核数不能为空！<br>权值不能为空！', '参数错误', {
            confirmButtonText: '确定',
            dangerouslyUseHTMLString: true
          });
          return
        }
        this.cannyForm.kernel_size = parseInt(this.cannyForm.kernel_size);
        this.cannyForm.exp = parseFloat(this.cannyForm.exp);
        if ((!this.utils.isInteger(this.cannyForm.kernel_size)) || (!this.utils.isFloat(this.cannyForm.exp))) {
          this.$alert('滤波核数必须为数字！<br>权值必须为数字！', '参数错误', {
            confirmButtonText: '确定',
            dangerouslyUseHTMLString: true
          });
          return
        }
        if ((this.cannyForm.kernel_size % 2 === 0) || (this.cannyForm.kernel_size <= 0)) {
          this.$alert('滤波核数必须为正奇数！', '参数错误', {
            confirmButtonText: '确定'
          });
          return
        }
        this.cannyForm.res_name = this.utils.calculate_res_name(this.cannyForm.res_name);
      } else if (this.canny_active === 2) {
        const axios = require('axios')

        this.cannyLoad = true;

        await axios.get(
            this.constant.data().BaseUrl + '/segmentation/canny', {
              params: {
                img_name: this.selection[0].fileName,
                result_name: this.cannyForm.res_name,
                kernel_size: this.cannyForm.kernel_size,
                exp: this.cannyForm.exp
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

        this.cannyLoad = false;


      } else if (this.canny_active === 3) {
        this.canny_active = 0;

        return
      }


      this.canny_active++;
    },
    async hough_lines_next() {
      let tmp = this.hough_lines_active;
      this.clear_active();
      this.hough_lines_active = tmp;
      if (this.hough_lines_active === 0) {
        this.selection = this.$refs["hough_linesSelection"].multipleSelection;
        this.displayImg[0] = this.selection[0];
        if (this.selection.length !== 1) {
          this.$alert('选择的图片数量不是一张！', '数量错误', {
            confirmButtonText: '确定'
          });
          return
        }

      } else if (this.hough_lines_active === 1) {
        if (this.hough_linesForm.res_name === '') {
          this.$alert('输出图像名称不能为空！', '命名错误', {
            confirmButtonText: '确定'
          });
          return
        }
        this.hough_linesForm.res_name = this.utils.calculate_res_name(this.hough_linesForm.res_name);
      } else if (this.hough_lines_active === 2) {
        const axios = require('axios')

        this.hough_linesLoad = true;

        await axios.get(
            this.constant.data().BaseUrl + '/segmentation/hough_lines', {
              params: {
                img_name: this.selection[0].fileName,
                result_name: this.hough_linesForm.res_name
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

        this.hough_linesLoad = false;


      } else if (this.hough_lines_active === 3) {
        this.hough_lines_active = 0;

        return
      }


      this.hough_lines_active++;
    },
    async hough_linesP_next() {
      let tmp = this.hough_linesP_active;
      this.clear_active();
      this.hough_linesP_active = tmp;
      if (this.hough_linesP_active === 0) {
        this.selection = this.$refs["hough_linesPSelection"].multipleSelection;
        this.displayImg[0] = this.selection[0];
        if (this.selection.length !== 1) {
          this.$alert('选择的图片数量不是一张！', '数量错误', {
            confirmButtonText: '确定'
          });
          return
        }

      } else if (this.hough_linesP_active === 1) {
        if (this.hough_linesPForm.res_name === '') {
          this.$alert('输出图像名称不能为空！', '命名错误', {
            confirmButtonText: '确定'
          });
          return
        }
        this.hough_linesPForm.res_name = this.utils.calculate_res_name(this.hough_linesPForm.res_name);
      } else if (this.hough_linesP_active === 2) {
        const axios = require('axios')

        this.hough_linesPLoad = true;

        await axios.get(
            this.constant.data().BaseUrl + '/segmentation/hough_lines_p', {
              params: {
                img_name: this.selection[0].fileName,
                result_name: this.hough_linesPForm.res_name
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

        this.hough_linesPLoad = false;


      } else if (this.hough_linesP_active === 3) {
        this.hough_linesP_active = 0;

        return
      }


      this.hough_linesP_active++;
    }
  }
}
</script>

<style scoped>

</style>
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
            <el-tab-pane label="Roberts 梯度算子">
              <el-steps :active="robert_active" align-center finish-status="success"style="margin-top: 40px">
                <el-step title="选择图片"></el-step>
                <el-step title="输入参数"></el-step>
                <el-step title="处理图片"></el-step>
              </el-steps>

              <div v-show="robert_active === 0" style="margin-top: 20px;">
                <PictureChooseOne ref="robertSelection"/>
              </div>

              <div v-show="robert_active === 1"
                   style="text-align: center; margin-top: 20px; min-height: 375px; max-height: 375px">
                <div style="margin-left: 20%; margin-right: 20%">
                  <el-form :model="robertForm" class="demo-form-inline">
                    <el-form-item label="输出图像名称"
                                  label-width="30%"
                                  :rules="[
                      { required: true, message: '名称不能为空'}
                      ]"
                                  style="align-content: center; margin-left: 10%; margin-right: 10%; width: 60%">
                      <el-input v-model="robertForm.res_name">
                        <template slot="append">.jpg</template>
                      </el-input>
                    </el-form-item>
                  </el-form>
                </div>
              </div>

              <div v-show="robert_active === 2"
                   style="text-align: center; margin-top: 20px; min-height: 375px; max-height: 375px">
                <div>
                  <span class="demonstration">原图片</span>
                  <br>
                  <img :src="this.displayImg[0].fileUrl" alt=""
                       style="width: auto; height: auto; max-width: 400px; max-height: 300px; margin-top: 30px">
                </div>
              </div>

              <div v-show="robert_active === 3"
                   style="text-align: center; margin-top: 20px; min-height: 375px; max-height: 375px">
                <div>
                  <span class="demonstration">结果图片</span>
                  <br>
                  <img :src="this.processResult.result_name" alt=""
                       style="width: auto; height: auto; max-width: 400px; max-height: 300px; margin-top: 30px">
                </div>
              </div>

              <el-button style="margin-left: 70%; margin-top: 30px;" @click="cancel">取消操作</el-button>
              <el-button v-show="robert_active <= 2" :loading="robertLoad" style="margin-left: 10px; margin-top: 10px;"
                         @click="robert_next">下一步
              </el-button>
              <el-button v-show="robert_active >= 3" :loading="robertLoad" style="margin-left: 10px; margin-top: 10px;"
                         @click="cancel">完成
              </el-button>

            </el-tab-pane>
            <el-tab-pane label="Laplacian 梯度算子">
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

              <el-button style="margin-left: 70%; margin-top: 30px;" @click="cancel">取消操作</el-button>
              <el-button v-show="laplacian_active <= 2" :loading="laplacianLoad" style="margin-left: 10px; margin-top: 10px;"
                         @click="laplacian_next">下一步
              </el-button>
              <el-button v-show="laplacian_active >= 3" :loading="laplacianLoad" style="margin-left: 10px; margin-top: 10px;"
                         @click="cancel">完成
              </el-button>

            </el-tab-pane>
            <el-tab-pane label="Sobel 梯度算子">
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

              <el-button style="margin-left: 70%; margin-top: 30px;" @click="cancel">取消操作</el-button>
              <el-button v-show="sobel_active <= 2" :loading="sobelLoad" style="margin-left: 10px; margin-top: 10px;"
                         @click="sobel_next">下一步
              </el-button>
              <el-button v-show="sobel_active >= 3" :loading="sobelLoad" style="margin-left: 10px; margin-top: 10px;"
                         @click="cancel">完成
              </el-button>

            </el-tab-pane>
            <el-tab-pane label="Prewitt 梯度算子">
              <el-steps :active="prewitt_active" align-center finish-status="success"style="margin-top: 40px">
                <el-step title="选择图片"></el-step>
                <el-step title="输入参数"></el-step>
                <el-step title="处理图片"></el-step>
              </el-steps>

              <div v-show="prewitt_active === 0" style="margin-top: 20px;">
                <PictureChooseOne ref="prewittSelection"/>
              </div>

              <div v-show="prewitt_active === 1"
                   style="text-align: center; margin-top: 20px; min-height: 375px; max-height: 375px">
                <div style="margin-left: 20%; margin-right: 20%">
                  <el-form :model="prewittForm" class="demo-form-inline">
                    <el-form-item label="输出图像名称"
                                  label-width="30%"
                                  :rules="[
                      { required: true, message: '名称不能为空'}
                      ]"
                                  style="align-content: center; margin-left: 10%; margin-right: 10%; width: 60%">
                      <el-input v-model="prewittForm.res_name">
                        <template slot="append">.jpg</template>
                      </el-input>
                    </el-form-item>
                  </el-form>
                </div>
              </div>

              <div v-show="prewitt_active === 2"
                   style="text-align: center; margin-top: 20px; min-height: 375px; max-height: 375px">
                <div>
                  <span class="demonstration">原图片</span>
                  <br>
                  <img :src="this.displayImg[0].fileUrl" alt=""
                       style="width: auto; height: auto; max-width: 400px; max-height: 300px; margin-top: 30px">
                </div>
              </div>

              <div v-show="prewitt_active === 3"
                   style="text-align: center; margin-top: 20px; min-height: 375px; max-height: 375px">
                <div>
                  <span class="demonstration">结果图片</span>
                  <br>
                  <img :src="this.processResult.result_name" alt=""
                       style="width: auto; height: auto; max-width: 400px; max-height: 300px; margin-top: 30px">
                </div>
              </div>

              <el-button style="margin-left: 70%; margin-top: 30px;" @click="cancel">取消操作</el-button>
              <el-button v-show="prewitt_active <= 2" :loading="prewittLoad" style="margin-left: 10px; margin-top: 10px;"
                         @click="prewitt_next">下一步
              </el-button>
              <el-button v-show="prewitt_active >= 3" :loading="prewittLoad" style="margin-left: 10px; margin-top: 10px;"
                         @click="cancel">完成
              </el-button>

            </el-tab-pane>
            <el-tab-pane label="理想高通滤波器">
              <el-steps :active="ideal_filter_active" align-center finish-status="success" style="margin-top: 40px">
                <el-step title="选择图片"></el-step>
                <el-step title="输入参数"></el-step>
                <el-step title="处理图片"></el-step>
              </el-steps>

              <div v-show="ideal_filter_active === 0" style="margin-top: 20px;">
                <PictureChooseOne ref="ideal_filterSelection"/>
              </div>

              <div v-show="ideal_filter_active === 1"
                   style="text-align: center; margin-top: 20px; min-height: 375px; max-height: 375px">
                <div style="margin-left: 20%; margin-right: 20%">
                  <el-form :model="ideal_filterForm" class="demo-form-inline">
                    <el-form-item label="输出图像名称"
                                  label-width="30%"
                                  :rules="[
                      { required: true, message: '名称不能为空'}
                      ]"
                                  style="align-content: center; margin-left: 10%; margin-right: 10%; width: 60%">
                      <el-input v-model="ideal_filterForm.res_name">
                        <template slot="append">.jpg</template>
                      </el-input>
                    </el-form-item>

                    <el-form-item label="阈值"
                                  label-width="30%"
                                  :rules=" [
                                  { required: true, message:'阈值不能为空'},
                                  { type: 'number', message: '阈值必须为数字值'}
                    ]"
                                  style="align-content: center; margin-left: 10%; margin-right: 10%; width: 60%">
                      <el-input placeholder="0～255" v-model="ideal_filterForm.d0">
                      </el-input>
                    </el-form-item>


                  </el-form>
                </div>
              </div>

              <div v-show="ideal_filter_active === 2"
                   style="text-align: center; margin-top: 20px; min-height: 375px; max-height: 375px">
                <div>
                  <span class="demonstration">原图片</span>
                  <br>
                  <img :src="this.displayImg[0].fileUrl" alt=""
                       style="width: auto; height: auto; max-width: 400px; max-height: 300px; margin-top: 30px">
                </div>
              </div>

              <div v-show="ideal_filter_active === 3"
                   style="text-align: center; margin-top: 20px; min-height: 375px; max-height: 375px">
                <div>
                  <span class="demonstration">结果图片</span>
                  <br>
                  <img :src="this.processResult.result_name" alt=""
                       style="width: auto; height: auto; max-width: 400px; max-height: 300px; margin-top: 30px">
                </div>
              </div>

              <el-button style="margin-left: 70%; margin-top: 30px;" @click="cancel">取消操作</el-button>
              <el-button v-show="ideal_filter_active <= 2" :loading="ideal_filterLoad" style="margin-left: 10px; margin-top: 10px;"
                         @click="ideal_filter_next">下一步
              </el-button>
              <el-button v-show="ideal_filter_active >= 3" :loading="ideal_filterLoad" style="margin-left: 10px; margin-top: 10px;"
                         @click="cancel">完成
              </el-button>
            </el-tab-pane>
            <el-tab-pane label="巴特沃斯高通滤波器">
              <el-steps :active="barte_filter_active" align-center finish-status="success"style="margin-top: 40px">
                <el-step title="选择图片"></el-step>
                <el-step title="输入参数"></el-step>
                <el-step title="处理图片"></el-step>
              </el-steps>

              <div v-show="barte_filter_active === 0" style="margin-top: 20px;">
                <PictureChooseOne ref="barte_filterSelection"/>
              </div>

              <div v-show="barte_filter_active === 1"
                   style="text-align: center; margin-top: 20px; min-height: 375px; max-height: 375px">
                <div style="margin-left: 20%; margin-right: 20%">
                  <el-form :model="barte_filterForm" class="demo-form-inline">
                    <el-form-item label="输出图像名称"
                                  label-width="30%"
                                  :rules="[
                      { required: true, message: '名称不能为空'}
                      ]"
                                  style="align-content: center; margin-left: 10%; margin-right: 10%; width: 60%">
                      <el-input v-model="barte_filterForm.res_name">
                        <template slot="append">.jpg</template>
                      </el-input>
                    </el-form-item>

                    <el-form-item label="阈值"
                                  label-width="30%"
                                  :rules=" [
                                  { required: true, message:'阈值不能为空'},
                                  { type: 'number', message: '阈值必须为数字值'}
                    ]"
                                  style="align-content: center; margin-left: 10%; margin-right: 10%; width: 60%">
                      <el-input placeholder="0～255" v-model="barte_filterForm.d0">
                      </el-input>
                    </el-form-item>

                    <el-form-item label="阶数"
                                  label-width="30%"
                                  :rules=" [
                                  { required: true, message:'阶数不能为空'},
                                  { type: 'number', message: '阶数必须为数字值'}
                    ]"
                                  style="align-content: center; margin-left: 10%; margin-right: 10%; width: 60%">
                      <el-input v-model="barte_filterForm.rank">
                      </el-input>
                    </el-form-item>


                  </el-form>
                </div>
              </div>

              <div v-show="barte_filter_active === 2"
                   style="text-align: center; margin-top: 20px; min-height: 375px; max-height: 375px">
                <div>
                  <span class="demonstration">原图片</span>
                  <br>
                  <img :src="this.displayImg[0].fileUrl" alt=""
                       style="width: auto; height: auto; max-width: 400px; max-height: 300px; margin-top: 30px">
                </div>
              </div>

              <div v-show="barte_filter_active === 3"
                   style="text-align: center; margin-top: 20px; min-height: 375px; max-height: 375px">
                <div>
                  <span class="demonstration">结果图片</span>
                  <br>
                  <img :src="this.processResult.result_name" alt=""
                       style="width: auto; height: auto; max-width: 400px; max-height: 300px; margin-top: 30px">
                </div>
              </div>

              <el-button style="margin-left: 70%; margin-top: 30px;" @click="cancel">取消操作</el-button>
              <el-button v-show="barte_filter_active <= 2" :loading="barte_filterLoad" style="margin-left: 10px; margin-top: 10px;"
                         @click="barte_filter_next">下一步
              </el-button>
              <el-button v-show="barte_filter_active >= 3" :loading="barte_filterLoad" style="margin-left: 10px; margin-top: 10px;"
                         @click="cancel">完成
              </el-button>
            </el-tab-pane>
            <el-tab-pane label="高斯高通滤波器">
              <el-steps :active="exp_filter_active" align-center finish-status="success"style="margin-top: 40px">
                <el-step title="选择图片"></el-step>
                <el-step title="输入参数"></el-step>
                <el-step title="处理图片"></el-step>
              </el-steps>

              <div v-show="exp_filter_active === 0" style="margin-top: 20px;">
                <PictureChooseOne ref="exp_filterSelection"/>
              </div>

              <div v-show="exp_filter_active === 1"
                   style="text-align: center; margin-top: 20px; min-height: 375px; max-height: 375px">
                <div style="margin-left: 20%; margin-right: 20%">
                  <el-form :model="exp_filterForm" class="demo-form-inline">
                    <el-form-item label="输出图像名称"
                                  label-width="30%"
                                  :rules="[
                      { required: true, message: '名称不能为空'}
                      ]"
                                  style="align-content: center; margin-left: 10%; margin-right: 10%; width: 60%">
                      <el-input v-model="exp_filterForm.res_name">
                        <template slot="append">.jpg</template>
                      </el-input>
                    </el-form-item>

                    <el-form-item label="阈值"
                                  label-width="30%"
                                  :rules=" [
                                  { required: true, message:'阈值不能为空'},
                                  { type: 'number', message: '阈值必须为数字值'}
                    ]"
                                  style="align-content: center; margin-left: 10%; margin-right: 10%; width: 60%">
                      <el-input placeholder="0～255" v-model="exp_filterForm.d0">
                      </el-input>
                    </el-form-item>

                    <el-form-item label="阶数"
                                  label-width="30%"
                                  :rules=" [
                                  { required: true, message:'阶数不能为空'},
                                  { type: 'number', message: '阶数必须为数字值'}
                    ]"
                                  style="align-content: center; margin-left: 10%; margin-right: 10%; width: 60%">
                      <el-input v-model="exp_filterForm.rank">
                      </el-input>
                    </el-form-item>


                  </el-form>
                </div>
              </div>

              <div v-show="exp_filter_active === 2"
                   style="text-align: center; margin-top: 20px; min-height: 375px; max-height: 375px">
                <div>
                  <span class="demonstration">原图片</span>
                  <br>
                  <img :src="this.displayImg[0].fileUrl" alt=""
                       style="width: auto; height: auto; max-width: 400px; max-height: 300px; margin-top: 30px">
                </div>
              </div>

              <div v-show="exp_filter_active === 3"
                   style="text-align: center; margin-top: 20px; min-height: 375px; max-height: 375px">
                <div>
                  <span class="demonstration">结果图片</span>
                  <br>
                  <img :src="this.processResult.result_name" alt=""
                       style="width: auto; height: auto; max-width: 400px; max-height: 300px; margin-top: 30px">
                </div>
              </div>

              <el-button style="margin-left: 70%; margin-top: 30px;" @click="cancel">取消操作</el-button>
              <el-button v-show="exp_filter_active <= 2" :loading="exp_filterLoad" style="margin-left: 10px; margin-top: 10px;"
                         @click="exp_filter_next">下一步
              </el-button>
              <el-button v-show="exp_filter_active >= 3" :loading="exp_filterLoad" style="margin-left: 10px; margin-top: 10px;"
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
  name: "Sharpen",
  data() {
    return {
      headmsg: '图像锐化',
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
      robert_active: 0,
      robertForm: {
        res_name: ''
      },
      robertLoad: false,
      laplacian_active: 0,
      laplacianForm: {
        res_name: ''
      },
      laplacianLoad: false,
      sobel_active: 0,
      sobelForm: {
        res_name: ''
      },
      sobelLoad: false,
      prewitt_active: 0,
      prewittForm: {
        res_name: ''
      },
      prewittLoad: false,
      ideal_filter_active: 0,
      ideal_filterForm: {
        res_name: '',
        d0: null
      },
      ideal_filterLoad: false,
      barte_filter_active: 0,
      barte_filterForm: {
        res_name: '',
        d0: null,
        rank: null
      },
      barte_filterLoad: false,
      exp_filter_active: 0,
      exp_filterForm: {
        res_name: '',
        d0: null,
        rank: null
      },
      exp_filterLoad: false
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

      this.robertForm.res_name = '';
      this.laplacianForm.res_name = '';
      this.sobelForm.res_name = '';
      this.prewittForm.res_name = '';
      this.ideal_filterForm.res_name = '';
      this.ideal_filterForm.d0 = null;
      this.barte_filterForm.res_name = '';
      this.barte_filterForm.d0 = null;
      this.barte_filterForm.rank = null;
      this.exp_filterForm.res_name = '';
      this.exp_filterForm.d0 = null;
      this.exp_filterForm.rank = null;

      this.robertLoad = false;
      this.laplacianLoad = false;
      this.sobelLoad = false;
      this.prewittLoad = false;
      this.ideal_filterLoad = false;
      this.barte_filterLoad = false;
      this.exp_filterLoad = false;

      this.processResult = {
        code: '',
        message: '',
        result_name: '../../../assets/picture/default_pic.jpg'
      };
    },
    clear_active() {
      this.robert_active = 0;
      this.laplacian_active = 0;
      this.sobel_active = 0;
      this.prewitt_active = 0;
      this.ideal_filter_active = 0;
      this.barte_filter_active = 0;
      this.exp_filter_active = 0;
    },
    async robert_next() {
      let tmp = this.robert_active;
      this.clear_active();
      this.robert_active = tmp;
      if (this.robert_active === 0) {
        this.selection = this.$refs["robertSelection"].multipleSelection;
        this.displayImg[0] = this.selection[0];
        if (this.selection.length !== 1) {
          this.$alert('选择的图片数量不是一张！', '数量错误', {
            confirmButtonText: '确定'
          });
          return
        }

      } else if (this.robert_active === 1) {
        if (this.robertForm.res_name === '') {
          this.$alert('输出图像名称不能为空！', '命名错误', {
            confirmButtonText: '确定'
          });
          return
        }
        this.robertForm.res_name = this.utils.calculate_res_name(this.robertForm.res_name);
      } else if (this.robert_active === 2) {
        const axios = require('axios')

        this.robertLoad = true;

        await axios.get(
            this.constant.data().BaseUrl + '/smooth_sharpen/shar_robert', {
              params: {
                img_name: this.selection[0].fileName,
                result_name: this.robertForm.res_name
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

        this.robertLoad = false;


      } else if (this.robert_active === 3) {
        this.robert_active = 0;

        return
      }


      this.robert_active++;
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
        if (this.laplacianForm.res_name === '') {
          this.$alert('输出图像名称不能为空！', '命名错误', {
            confirmButtonText: '确定'
          });
          return
        }
        this.laplacianForm.res_name = this.utils.calculate_res_name(this.laplacianForm.res_name);
      } else if (this.laplacian_active === 2) {
        const axios = require('axios')

        this.laplacianLoad = true;

        await axios.get(
            this.constant.data().BaseUrl + '/smooth_sharpen/shar_laplacian', {
              params: {
                img_name: this.selection[0].fileName,
                result_name: this.laplacianForm.res_name
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
        if (this.sobelForm.res_name === '') {
          this.$alert('输出图像名称不能为空！', '命名错误', {
            confirmButtonText: '确定'
          });
          return
        }
        this.sobelForm.res_name = this.utils.calculate_res_name(this.sobelForm.res_name);
      } else if (this.sobel_active === 2) {
        const axios = require('axios')

        this.sobelLoad = true;

        await axios.get(
            this.constant.data().BaseUrl + '/smooth_sharpen/shar_sobel', {
              params: {
                img_name: this.selection[0].fileName,
                result_name: this.sobelForm.res_name
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
    async prewitt_next() {
      let tmp = this.prewitt_active;
      this.clear_active();
      this.prewitt_active = tmp;
      if (this.prewitt_active === 0) {
        this.selection = this.$refs["prewittSelection"].multipleSelection;
        this.displayImg[0] = this.selection[0];
        if (this.selection.length !== 1) {
          this.$alert('选择的图片数量不是一张！', '数量错误', {
            confirmButtonText: '确定'
          });
          return
        }

      } else if (this.prewitt_active === 1) {
        if (this.prewittForm.res_name === '') {
          this.$alert('输出图像名称不能为空！', '命名错误', {
            confirmButtonText: '确定'
          });
          return
        }
        this.prewittForm.res_name = this.utils.calculate_res_name(this.prewittForm.res_name);
      } else if (this.prewitt_active === 2) {
        const axios = require('axios')

        this.prewittLoad = true;

        await axios.get(
            this.constant.data().BaseUrl + '/smooth_sharpen/shar_prewitt', {
              params: {
                img_name: this.selection[0].fileName,
                result_name: this.prewittForm.res_name
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

        this.prewittLoad = false;


      } else if (this.prewitt_active === 3) {
        this.prewitt_active = 0;

        return
      }


      this.prewitt_active++;
    },
    async ideal_filter_next() {
      let tmp = this.ideal_filter_active;
      this.clear_active();
      this.ideal_filter_active = tmp;
      if (this.ideal_filter_active === 0) {
        this.selection = this.$refs["ideal_filterSelection"].multipleSelection;
        this.displayImg[0] = this.selection[0];
        if (this.selection.length !== 1) {
          this.$alert('选择的图片数量不是一张！', '数量错误', {
            confirmButtonText: '确定'
          });
          return
        }

      } else if (this.ideal_filter_active === 1) {
        if ((this.ideal_filterForm.res_name === '') || (this.ideal_filterForm.d0 === null)) {
          this.$alert('输出图像名称不能为空！<br>阈值不能为空！', '参数错误', {
            confirmButtonText: '确定',
            dangerouslyUseHTMLString: true
          });
          return
        }
        this.ideal_filterForm.d0 = parseInt(this.ideal_filterForm.d0);
        if (!this.utils.isInteger(this.ideal_filterForm.d0)) {
          this.$alert('阈值必须为数字！', '参数错误', {
            confirmButtonText: '确定'
          });
          return
        }
        if ((this.ideal_filterForm.d0 < 0) || (this.ideal_filterForm.d0 > 255)) {
          this.$alert('阈值必须在0～255之间！', '参数错误', {
            confirmButtonText: '确定'
          });
          return
        }
        this.ideal_filterForm.res_name = this.utils.calculate_res_name(this.ideal_filterForm.res_name);
      } else if (this.ideal_filter_active === 2) {
        const axios = require('axios')

        this.ideal_filterLoad = true;

        await axios.get(
            this.constant.data().BaseUrl + '/smooth_sharpen/shar_ideal_high', {
              params: {
                img_name: this.selection[0].fileName,
                result_name: this.ideal_filterForm.res_name,
                d0: this.ideal_filterForm.d0
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

        this.ideal_filterLoad = false;


      } else if (this.ideal_filter_active === 3) {
        this.ideal_filter_active = 0;

        return
      }


      this.ideal_filter_active++;
    },
    async barte_filter_next() {
      let tmp = this.barte_filter_active;
      this.clear_active();
      this.barte_filter_active = tmp;
      if (this.barte_filter_active === 0) {
        this.selection = this.$refs["barte_filterSelection"].multipleSelection;
        this.displayImg[0] = this.selection[0];
        if (this.selection.length !== 1) {
          this.$alert('选择的图片数量不是一张！', '数量错误', {
            confirmButtonText: '确定'
          });
          return
        }

      } else if (this.barte_filter_active === 1) {
        if ((this.barte_filterForm.res_name === '') || (this.barte_filterForm.d0 === null) || (this.barte_filterForm.rank === null)) {
          this.$alert('输出图像名称不能为空！<br>阈值不能为空！<br>阶数不能为空！', '参数错误', {
            confirmButtonText: '确定',
            dangerouslyUseHTMLString: true
          });
          return
        }
        this.barte_filterForm.d0 = parseInt(this.barte_filterForm.d0);
        this.barte_filterForm.rank = parseInt(this.barte_filterForm.rank);
        if ((!this.utils.isInteger(this.barte_filterForm.d0)) || (!this.utils.isInteger(this.barte_filterForm.rank))) {
          this.$alert('阈值必须为数字！<br>阶数必须为数字！', '参数错误', {
            confirmButtonText: '确定',
            dangerouslyUseHTMLString: true
          });
          return
        }
        if ((this.barte_filterForm.d0 < 0) || (this.barte_filterForm.d0 > 255)) {
          this.$alert('阈值必须在0～255之间！', '参数错误', {
            confirmButtonText: '确定'
          });
          return
        }
        this.barte_filterForm.res_name = this.utils.calculate_res_name(this.barte_filterForm.res_name);
      } else if (this.barte_filter_active === 2) {
        const axios = require('axios')

        this.barte_filterLoad = true;

        await axios.get(
            this.constant.data().BaseUrl + '/smooth_sharpen/shar_barte_filter', {
              params: {
                img_name: this.selection[0].fileName,
                result_name: this.barte_filterForm.res_name,
                d0: this.barte_filterForm.d0,
                rank: this.barte_filterForm.rank
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

        this.barte_filterLoad = false;


      } else if (this.barte_filter_active === 3) {
        this.barte_filter_active = 0;

        return
      }


      this.barte_filter_active++;
    },
    async exp_filter_next() {
      let tmp = this.exp_filter_active;
      this.clear_active();
      this.exp_filter_active = tmp;
      if (this.exp_filter_active === 0) {
        this.selection = this.$refs["exp_filterSelection"].multipleSelection;
        this.displayImg[0] = this.selection[0];
        if (this.selection.length !== 1) {
          this.$alert('选择的图片数量不是一张！', '数量错误', {
            confirmButtonText: '确定'
          });
          return
        }

      } else if (this.exp_filter_active === 1) {
        if ((this.exp_filterForm.res_name === '') || (this.exp_filterForm.d0 === null) || (this.exp_filterForm.rank === null)) {
          this.$alert('输出图像名称不能为空！<br>阈值不能为空！<br>阶数不能为空！', '参数错误', {
            confirmButtonText: '确定',
            dangerouslyUseHTMLString: true
          });
          return
        }
        this.exp_filterForm.d0 = parseInt(this.exp_filterForm.d0);
        this.exp_filterForm.rank = parseInt(this.exp_filterForm.rank);
        if ((!this.utils.isInteger(this.exp_filterForm.d0)) || (!this.utils.isInteger(this.exp_filterForm.rank))) {
          this.$alert('阈值必须为数字！<br>阶数必须为数字！', '参数错误', {
            confirmButtonText: '确定',
            dangerouslyUseHTMLString: true
          });
          return
        }
        if ((this.exp_filterForm.d0 < 0) || (this.exp_filterForm.d0 > 255)) {
          this.$alert('阈值必须在0～255之间！', '参数错误', {
            confirmButtonText: '确定'
          });
          return
        }
        this.exp_filterForm.res_name = this.utils.calculate_res_name(this.exp_filterForm.res_name);
      } else if (this.exp_filter_active === 2) {
        const axios = require('axios')

        this.exp_filterLoad = true;

        await axios.get(
            this.constant.data().BaseUrl + '/smooth_sharpen/shar_exp_filter', {
              params: {
                img_name: this.selection[0].fileName,
                result_name: this.exp_filterForm.res_name,
                d0: this.exp_filterForm.d0,
                rank: this.exp_filterForm.rank
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

        this.exp_filterLoad = false;


      } else if (this.exp_filter_active === 3) {
        this.exp_filter_active = 0;

        return
      }


      this.exp_filter_active++;
    }
  }
}
</script>

<style scoped>

</style>
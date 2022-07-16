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
          <el-divider content-position="left">图像平滑</el-divider>
          {{ intromsg }}
          <el-tabs type="border-card" style="margin-top: 30px; min-height: 80%">
            <el-tab-pane label="领域平均法">
              <el-steps :active="neighbour_average_active" finish-status="success" simple style="margin-top: 10px">
                <el-step title="选择图片"></el-step>
                <el-step title="输入参数"></el-step>
                <el-step title="处理图片"></el-step>
              </el-steps>

              <div v-show="neighbour_average_active === 0" style="margin-top: 20px;">
                <PictureChooseOne ref="neighbour_averageSelection"/>
              </div>

              <div v-show="neighbour_average_active === 1"
                   style="text-align: center; margin-top: 20px; min-height: 375px; max-height: 375px">
                <div style="margin-left: 20%; margin-right: 20%">
                  <el-form :model="neighbour_averageForm" class="demo-form-inline">
                    <el-form-item label="输出图像名称"
                                  label-width="30%"
                                  :rules="[
                      { required: true, message: '名称不能为空'}
                      ]"
                                  style="align-content: center; margin-left: 10%; margin-right: 10%; width: 60%">
                      <el-input v-model="neighbour_averageForm.res_name">
                        <template slot="append">.jpg</template>
                      </el-input>
                    </el-form-item>

                    <el-form-item label="核数"
                                  label-width="30%"
                                  :rules=" [
                                  { required: true, message:'核数不能为空'},
                                  { type: 'number', message: '核数必须为数字值'}
                    ]"
                                  style="align-content: center; margin-left: 10%; margin-right: 10%; width: 60%">
                      <el-input placeholder="奇数，推荐3" v-model="neighbour_averageForm.kernel_size">
                      </el-input>
                    </el-form-item>


                  </el-form>
                </div>
              </div>

              <div v-show="neighbour_average_active === 2"
                   style="text-align: center; margin-top: 20px; min-height: 375px; max-height: 375px">
                <div>
                  <span class="demonstration">原图片</span>
                  <br>
                  <img :src="this.displayImg[0].fileUrl" alt=""
                       style="width: auto; height: auto; max-width: 400px; max-height: 300px; margin-top: 30px">
                </div>
              </div>

              <div v-show="neighbour_average_active === 3"
                   style="text-align: center; margin-top: 20px; min-height: 375px; max-height: 375px">
                <div>
                  <span class="demonstration">结果图片</span>
                  <br>
                  <img :src="this.processResult.result_name" alt=""
                       style="width: auto; height: auto; max-width: 400px; max-height: 300px; margin-top: 30px">
                </div>
              </div>

              <el-button style="margin-left: 80%; margin-top: 10px;" @click="cancel">取消</el-button>
              <el-button v-show="neighbour_average_active <= 2" :loading="neighbour_averageLoad" style="margin-left: 10px; margin-top: 10px;"
                         @click="neighbour_average_next">下一步
              </el-button>
              <el-button v-show="neighbour_average_active >= 3" :loading="neighbour_averageLoad" style="margin-left: 10px; margin-top: 10px;"
                         @click="cancel">完成
              </el-button>
            </el-tab-pane>
            <el-tab-pane label="中值滤波法">
              <el-steps :active="median_filter_active" finish-status="success" simple style="margin-top: 10px">
                <el-step title="选择图片"></el-step>
                <el-step title="输入参数"></el-step>
                <el-step title="处理图片"></el-step>
              </el-steps>

              <div v-show="median_filter_active === 0" style="margin-top: 20px;">
                <PictureChooseOne ref="median_filterSelection"/>
              </div>

              <div v-show="median_filter_active === 1"
                   style="text-align: center; margin-top: 20px; min-height: 375px; max-height: 375px">
                <div style="margin-left: 20%; margin-right: 20%">
                  <el-form :model="median_filterForm" class="demo-form-inline">
                    <el-form-item label="输出图像名称"
                                  label-width="30%"
                                  :rules="[
                      { required: true, message: '名称不能为空'}
                      ]"
                                  style="align-content: center; margin-left: 10%; margin-right: 10%; width: 60%">
                      <el-input v-model="median_filterForm.res_name">
                        <template slot="append">.jpg</template>
                      </el-input>
                    </el-form-item>

                    <el-form-item label="核数"
                                  label-width="30%"
                                  :rules=" [
                                  { required: true, message:'核数不能为空'},
                                  { type: 'number', message: '核数必须为数字值'}
                    ]"
                                  style="align-content: center; margin-left: 10%; margin-right: 10%; width: 60%">
                      <el-input placeholder="奇数，推荐3" v-model="median_filterForm.kernel_size">
                      </el-input>
                    </el-form-item>


                  </el-form>
                </div>
              </div>

              <div v-show="median_filter_active === 2"
                   style="text-align: center; margin-top: 20px; min-height: 375px; max-height: 375px">
                <div>
                  <span class="demonstration">原图片</span>
                  <br>
                  <img :src="this.displayImg[0].fileUrl" alt=""
                       style="width: auto; height: auto; max-width: 400px; max-height: 300px; margin-top: 30px">
                </div>
              </div>

              <div v-show="median_filter_active === 3"
                   style="text-align: center; margin-top: 20px; min-height: 375px; max-height: 375px">
                <div>
                  <span class="demonstration">结果图片</span>
                  <br>
                  <img :src="this.processResult.result_name" alt=""
                       style="width: auto; height: auto; max-width: 400px; max-height: 300px; margin-top: 30px">
                </div>
              </div>

              <el-button style="margin-left: 80%; margin-top: 10px;" @click="cancel">取消</el-button>
              <el-button v-show="median_filter_active <= 2" :loading="median_filterLoad" style="margin-left: 10px; margin-top: 10px;"
                         @click="median_filter_next">下一步
              </el-button>
              <el-button v-show="median_filter_active >= 3" :loading="median_filterLoad" style="margin-left: 10px; margin-top: 10px;"
                         @click="cancel">完成
              </el-button>
            </el-tab-pane>
            <el-tab-pane label="理想低通滤波器">
              <el-steps :active="ideal_filter_active" finish-status="success" simple style="margin-top: 10px">
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

              <el-button style="margin-left: 80%; margin-top: 10px;" @click="cancel">取消</el-button>
              <el-button v-show="ideal_filter_active <= 2" :loading="ideal_filterLoad" style="margin-left: 10px; margin-top: 10px;"
                         @click="ideal_filter_next">下一步
              </el-button>
              <el-button v-show="ideal_filter_active >= 3" :loading="ideal_filterLoad" style="margin-left: 10px; margin-top: 10px;"
                         @click="cancel">完成
              </el-button>
            </el-tab-pane>
            <el-tab-pane label="巴特沃斯低通滤波器">
              <el-steps :active="barte_filter_active" finish-status="success" simple style="margin-top: 10px">
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

              <el-button style="margin-left: 80%; margin-top: 10px;" @click="cancel">取消</el-button>
              <el-button v-show="barte_filter_active <= 2" :loading="barte_filterLoad" style="margin-left: 10px; margin-top: 10px;"
                         @click="barte_filter_next">下一步
              </el-button>
              <el-button v-show="barte_filter_active >= 3" :loading="barte_filterLoad" style="margin-left: 10px; margin-top: 10px;"
                         @click="cancel">完成
              </el-button>
            </el-tab-pane>
            <el-tab-pane label="指数低通滤波器">
              <el-steps :active="exp_filter_active" finish-status="success" simple style="margin-top: 10px">
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

              <el-button style="margin-left: 80%; margin-top: 10px;" @click="cancel">取消</el-button>
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
import PictureChooseOne from "@/components/global/PictureChooseOne"

export default {
  name: "Smooth",
  data() {
    return {
      headmsg: '图像平滑',
      intromsg: '\xa0\xa0\xa0\xa0\xa0\xa0\xa0主要包含了图像的空域平滑与频域平滑等功能。',
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
      neighbour_average_active: 0,
      neighbour_averageForm: {
        res_name: '',
        kernel_size: null
      },
      neighbour_averageLoad: false,
      median_filter_active: 0,
      median_filterForm: {
        res_name: '',
        kernel_size: null
      },
      median_filterLoad: false,
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

      this.neighbour_averageForm.res_name = '';
      this.neighbour_averageForm.kernel_size = null;
      this.median_filterForm.res_name = '';
      this.median_filterForm.kernel_size = null;
      this.ideal_filterForm.res_name = '';
      this.ideal_filterForm.d0 = null;
      this.barte_filterForm.res_name = '';
      this.barte_filterForm.d0 = null;
      this.barte_filterForm.rank = null;
      this.exp_filterForm.res_name = '';
      this.exp_filterForm.d0 = null;
      this.exp_filterForm.rank = null;

      this.neighbour_averageLoad = false;
      this.median_filterLoad = false;
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
      this.neighbour_average_active = 0;
      this.median_filter_active = 0;
      this.ideal_filter_active = 0;
      this.barte_filter_active = 0;
      this.exp_filter_active = 0;
    },
    async neighbour_average_next() {
      let tmp = this.neighbour_average_active;
      this.clear_active();
      this.neighbour_average_active = tmp;
      if (this.neighbour_average_active === 0) {
        this.selection = this.$refs["neighbour_averageSelection"].multipleSelection;
        this.displayImg[0] = this.selection[0];
        if (this.selection.length !== 1) {
          this.$alert('选择的图片数量不是一张！', '数量错误', {
            confirmButtonText: '确定'
          });
          return
        }

      } else if (this.neighbour_average_active === 1) {
        if ((this.neighbour_averageForm.res_name === '') || (this.neighbour_averageForm.kernel_size === null)) {
          this.$alert('输出图像名称不能为空！<br>核数不能为空！', '参数错误', {
            confirmButtonText: '确定',
            dangerouslyUseHTMLString: true
          });
          return
        }
        this.neighbour_averageForm.kernel_size = parseInt(this.neighbour_averageForm.kernel_size);
        if (!this.utils.isInteger(this.neighbour_averageForm.kernel_size)) {
          this.$alert('核数必须为数字！', '参数错误', {
            confirmButtonText: '确定'
          });
          return
        }
        if ((this.neighbour_averageForm.kernel_size % 2 === 0) || (this.neighbour_averageForm.kernel_size <= 0)) {
          this.$alert('核数必须为正奇数！', '参数错误', {
            confirmButtonText: '确定'
          });
          return
        }
        this.neighbour_averageForm.res_name = this.utils.calculate_res_name(this.neighbour_averageForm.res_name);
      } else if (this.neighbour_average_active === 2) {
        const axios = require('axios')

        this.neighbour_averageLoad = true;

        await axios.get(
            this.constant.data().BaseUrl + '/smooth_sharpen/smoo_neighbour_average', {
              params: {
                img_name: this.selection[0].fileName,
                result_name: this.neighbour_averageForm.res_name,
                kernel_size: this.neighbour_averageForm.kernel_size
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

        this.neighbour_averageLoad = false;


      } else if (this.neighbour_average_active === 3) {
        this.neighbour_average_active = 0;

        return
      }


      this.neighbour_average_active++;
    },
    async median_filter_next() {
      let tmp = this.median_filter_active;
      this.clear_active();
      this.median_filter_active = tmp;
      if (this.median_filter_active === 0) {
        this.selection = this.$refs["median_filterSelection"].multipleSelection;
        this.displayImg[0] = this.selection[0];
        if (this.selection.length !== 1) {
          this.$alert('选择的图片数量不是一张！', '数量错误', {
            confirmButtonText: '确定'
          });
          return
        }

      } else if (this.median_filter_active === 1) {
        if ((this.median_filterForm.res_name === '') || (this.median_filterForm.kernel_size === null)) {
          this.$alert('输出图像名称不能为空！<br>核数不能为空！', '参数错误', {
            confirmButtonText: '确定',
            dangerouslyUseHTMLString: true
          });
          return
        }
        this.median_filterForm.kernel_size = parseInt(this.median_filterForm.kernel_size);
        if (!this.utils.isInteger(this.median_filterForm.kernel_size)) {
          this.$alert('核数必须为数字！', '参数错误', {
            confirmButtonText: '确定'
          });
          return
        }
        if ((this.median_filterForm.kernel_size % 2 === 0) || (this.median_filterForm.kernel_size <= 0)) {
          this.$alert('核数必须为正奇数！', '参数错误', {
            confirmButtonText: '确定'
          });
          return
        }
        this.median_filterForm.res_name = this.utils.calculate_res_name(this.median_filterForm.res_name);
      } else if (this.median_filter_active === 2) {
        const axios = require('axios')

        this.median_filterLoad = true;

        await axios.get(
            this.constant.data().BaseUrl + '/smooth_sharpen/smoo_median_filter', {
              params: {
                img_name: this.selection[0].fileName,
                result_name: this.median_filterForm.res_name,
                kernel_size: this.median_filterForm.kernel_size
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

        this.median_filterLoad = false;


      } else if (this.median_filter_active === 3) {
        this.median_filter_active = 0;

        return
      }


      this.median_filter_active++;
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
            this.constant.data().BaseUrl + '/smooth_sharpen/smoo_ideal_filter', {
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
            this.constant.data().BaseUrl + '/smooth_sharpen/smoo_barte_filter', {
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
            this.constant.data().BaseUrl + '/smooth_sharpen/smoo_exp_filter', {
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
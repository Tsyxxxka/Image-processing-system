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
            <el-tab-pane label="几何均值滤波">
              <el-steps :active="geometric_average_filter_active" align-center finish-status="success"style="margin-top: 40px">
                <el-step title="选择图片"></el-step>
                <el-step title="输入参数"></el-step>
                <el-step title="处理图片"></el-step>
              </el-steps>

              <div v-show="geometric_average_filter_active === 0" style="margin-top: 20px;">
                <PictureChooseOne ref="geometric_average_filterSelection"/>
              </div>

              <div v-show="geometric_average_filter_active === 1"
                   style="text-align: center; margin-top: 20px; min-height: 375px; max-height: 375px">
                <div style="margin-left: 20%; margin-right: 20%">
                  <el-form :model="geometric_average_filterForm" class="demo-form-inline">
                    <el-form-item label="输出图像名称"
                                  label-width="30%"
                                  :rules="[
                      { required: true, message: '名称不能为空'}
                      ]"
                                  style="align-content: center; margin-left: 10%; margin-right: 10%; width: 60%">
                      <el-input v-model="geometric_average_filterForm.res_name">
                        <template slot="append">.jpg</template>
                      </el-input>
                    </el-form-item>

                    <el-form-item label="滤波器大小"
                                  :rules="[
                      { required: true, message: '像素值不能为空'},
                      { type: 'number', message: '像素值必须为数字值'}
                      ]"
                                  style="align-content: center; margin-left: 10%; margin-right: 10%; width:80%">
                      <el-col :span="7">
                        <el-input placeholder="奇数，推荐1" v-model="geometric_average_filterForm.filter_size_p">
                        </el-input>
                      </el-col>
                      <el-col class="line" :span="2">*</el-col>
                      <el-col :span="7">
                        <el-input placeholder="奇数，推荐3" v-model="geometric_average_filterForm.filter_size_q">
                        </el-input>
                      </el-col>
                    </el-form-item>
                  </el-form>
                </div>
              </div>

              <div v-show="geometric_average_filter_active === 2"
                   style="text-align: center; margin-top: 20px; min-height: 375px; max-height: 375px">
                <div>
                  <span class="demonstration">原图片</span>
                  <br>
                  <img :src="this.displayImg[0].fileUrl" alt=""
                       style="width: auto; height: auto; max-width: 400px; max-height: 300px; margin-top: 30px">
                </div>
              </div>

              <div v-show="geometric_average_filter_active === 3"
                   style="text-align: center; margin-top: 20px; min-height: 375px; max-height: 375px">
                <div>
                  <span class="demonstration">结果图片</span>
                  <br>
                  <img :src="this.processResult.result_name" alt=""
                       style="width: auto; height: auto; max-width: 400px; max-height: 300px; margin-top: 30px">
                </div>
              </div>

              <el-button style="margin-left: 70%; margin-top: 30px;" @click="cancel">取消操作</el-button>
              <el-button v-show="geometric_average_filter_active <= 2" :loading="geometric_average_filterLoad" style="margin-left: 10px; margin-top: 10px;"
                         @click="geometric_average_filter_next">下一步
              </el-button>
              <el-button v-show="geometric_average_filter_active >= 3" :loading="geometric_average_filterLoad" style="margin-left: 10px; margin-top: 10px;"
                         @click="cancel">完成
              </el-button>

            </el-tab-pane>
            <el-tab-pane label="谐波均值滤波">
              <el-steps :active="harmonic_average_filter_active" align-center finish-status="success"style="margin-top: 40px">
                <el-step title="选择图片"></el-step>
                <el-step title="输入参数"></el-step>
                <el-step title="处理图片"></el-step>
              </el-steps>

              <div v-show="harmonic_average_filter_active === 0" style="margin-top: 20px;">
                <PictureChooseOne ref="harmonic_average_filterSelection"/>
              </div>

              <div v-show="harmonic_average_filter_active === 1"
                   style="text-align: center; margin-top: 20px; min-height: 375px; max-height: 375px">
                <div style="margin-left: 20%; margin-right: 20%">
                  <el-form :model="harmonic_average_filterForm" class="demo-form-inline">
                    <el-form-item label="输出图像名称"
                                  label-width="30%"
                                  :rules="[
                      { required: true, message: '名称不能为空'}
                      ]"
                                  style="align-content: center; margin-left: 10%; margin-right: 10%; width: 60%">
                      <el-input v-model="harmonic_average_filterForm.res_name">
                        <template slot="append">.jpg</template>
                      </el-input>
                    </el-form-item>

                    <el-form-item label="滤波器大小"
                                  :rules="[
                      { required: true, message: '像素值不能为空'},
                      { type: 'number', message: '像素值必须为数字值'}
                      ]"
                                  style="align-content: center; margin-left: 10%; margin-right: 10%; width:80%">
                      <el-col :span="7">
                        <el-input placeholder="奇数，推荐3" v-model="harmonic_average_filterForm.filter_size_p">
                        </el-input>
                      </el-col>
                      <el-col class="line" :span="2">*</el-col>
                      <el-col :span="7">
                        <el-input placeholder="奇数，推荐3" v-model="harmonic_average_filterForm.filter_size_q">
                        </el-input>
                      </el-col>
                    </el-form-item>
                  </el-form>
                </div>
              </div>

              <div v-show="harmonic_average_filter_active === 2"
                   style="text-align: center; margin-top: 20px; min-height: 375px; max-height: 375px">
                <div>
                  <span class="demonstration">原图片</span>
                  <br>
                  <img :src="this.displayImg[0].fileUrl" alt=""
                       style="width: auto; height: auto; max-width: 400px; max-height: 300px; margin-top: 30px">
                </div>
              </div>

              <div v-show="harmonic_average_filter_active === 3"
                   style="text-align: center; margin-top: 20px; min-height: 375px; max-height: 375px">
                <div>
                  <span class="demonstration">结果图片</span>
                  <br>
                  <img :src="this.processResult.result_name" alt=""
                       style="width: auto; height: auto; max-width: 400px; max-height: 300px; margin-top: 30px">
                </div>
              </div>

              <el-button style="margin-left: 70%; margin-top: 30px;" @click="cancel">取消操作</el-button>
              <el-button v-show="harmonic_average_filter_active <= 2" :loading="harmonic_average_filterLoad" style="margin-left: 10px; margin-top: 10px;"
                         @click="harmonic_average_filter_next">下一步
              </el-button>
              <el-button v-show="harmonic_average_filter_active >= 3" :loading="harmonic_average_filterLoad" style="margin-left: 10px; margin-top: 10px;"
                         @click="cancel">完成
              </el-button>

            </el-tab-pane>
            <el-tab-pane label="最小值滤波">
              <el-steps :active="min_filter_active" align-center finish-status="success"style="margin-top: 40px">
                <el-step title="选择图片"></el-step>
                <el-step title="输入参数"></el-step>
                <el-step title="处理图片"></el-step>
              </el-steps>

              <div v-show="min_filter_active === 0" style="margin-top: 20px;">
                <PictureChooseOne ref="min_filterSelection"/>
              </div>

              <div v-show="min_filter_active === 1"
                   style="text-align: center; margin-top: 20px; min-height: 375px; max-height: 375px">
                <div style="margin-left: 20%; margin-right: 20%">
                  <el-form :model="min_filterForm" class="demo-form-inline">
                    <el-form-item label="输出图像名称"
                                  label-width="30%"
                                  :rules="[
                      { required: true, message: '名称不能为空'}
                      ]"
                                  style="align-content: center; margin-left: 10%; margin-right: 10%; width: 60%">
                      <el-input v-model="min_filterForm.res_name">
                        <template slot="append">.jpg</template>
                      </el-input>
                    </el-form-item>
                  </el-form>
                </div>
              </div>

              <div v-show="min_filter_active === 2"
                   style="text-align: center; margin-top: 20px; min-height: 375px; max-height: 375px">
                <div>
                  <span class="demonstration">原图片</span>
                  <br>
                  <img :src="this.displayImg[0].fileUrl" alt=""
                       style="width: auto; height: auto; max-width: 400px; max-height: 300px; margin-top: 30px">
                </div>
              </div>

              <div v-show="min_filter_active === 3"
                   style="text-align: center; margin-top: 20px; min-height: 375px; max-height: 375px">
                <div>
                  <span class="demonstration">结果图片</span>
                  <br>
                  <img :src="this.processResult.result_name" alt=""
                       style="width: auto; height: auto; max-width: 400px; max-height: 300px; margin-top: 30px">
                </div>
              </div>

              <el-button style="margin-left: 70%; margin-top: 30px;" @click="cancel">取消操作</el-button>
              <el-button v-show="min_filter_active <= 2" :loading="min_filterLoad" style="margin-left: 10px; margin-top: 10px;"
                         @click="min_filter_next">下一步
              </el-button>
              <el-button v-show="min_filter_active >= 3" :loading="min_filterLoad" style="margin-left: 10px; margin-top: 10px;"
                         @click="cancel">完成
              </el-button>

            </el-tab-pane>
            <el-tab-pane label="最大值滤波">
              <el-steps :active="max_filter_active" align-center finish-status="success"style="margin-top: 40px">
                <el-step title="选择图片"></el-step>
                <el-step title="输入参数"></el-step>
                <el-step title="处理图片"></el-step>
              </el-steps>

              <div v-show="max_filter_active === 0" style="margin-top: 20px;">
                <PictureChooseOne ref="max_filterSelection"/>
              </div>

              <div v-show="max_filter_active === 1"
                   style="text-align: center; margin-top: 20px; min-height: 375px; max-height: 375px">
                <div style="margin-left: 20%; margin-right: 20%">
                  <el-form :model="max_filterForm" class="demo-form-inline">
                    <el-form-item label="输出图像名称"
                                  label-width="30%"
                                  :rules="[
                      { required: true, message: '名称不能为空'}
                      ]"
                                  style="align-content: center; margin-left: 10%; margin-right: 10%; width: 60%">
                      <el-input v-model="max_filterForm.res_name">
                        <template slot="append">.jpg</template>
                      </el-input>
                    </el-form-item>
                  </el-form>
                </div>
              </div>

              <div v-show="max_filter_active === 2"
                   style="text-align: center; margin-top: 20px; min-height: 375px; max-height: 375px">
                <div>
                  <span class="demonstration">原图片</span>
                  <br>
                  <img :src="this.displayImg[0].fileUrl" alt=""
                       style="width: auto; height: auto; max-width: 400px; max-height: 300px; margin-top: 30px">
                </div>
              </div>

              <div v-show="max_filter_active === 3"
                   style="text-align: center; margin-top: 20px; min-height: 375px; max-height: 375px">
                <div>
                  <span class="demonstration">结果图片</span>
                  <br>
                  <img :src="this.processResult.result_name" alt=""
                       style="width: auto; height: auto; max-width: 400px; max-height: 300px; margin-top: 30px">
                </div>
              </div>

              <el-button style="margin-left: 70%; margin-top: 30px;" @click="cancel">取消操作</el-button>
              <el-button v-show="max_filter_active <= 2" :loading="max_filterLoad" style="margin-left: 10px; margin-top: 10px;"
                         @click="max_filter_next">下一步
              </el-button>
              <el-button v-show="max_filter_active >= 3" :loading="max_filterLoad" style="margin-left: 10px; margin-top: 10px;"
                         @click="cancel">完成
              </el-button>

            </el-tab-pane>
            <el-tab-pane label="中值滤波">
              <el-steps :active="max_filter_active" align-center finish-status="success"style="margin-top: 40px">
                <el-step title="选择图片"></el-step>
                <el-step title="输入参数"></el-step>
                <el-step title="处理图片"></el-step>
              </el-steps>

              <div v-show="max_filter_active === 0" style="margin-top: 20px;">
                <PictureChooseOne ref="max_filterSelection"/>
              </div>

              <div v-show="max_filter_active === 1"
                   style="text-align: center; margin-top: 20px; min-height: 375px; max-height: 375px">
                <div style="margin-left: 20%; margin-right: 20%">
                  <el-form :model="max_filterForm" class="demo-form-inline">
                    <el-form-item label="输出图像名称"
                                  label-width="30%"
                                  :rules="[
                      { required: true, message: '名称不能为空'}
                      ]"
                                  style="align-content: center; margin-left: 10%; margin-right: 10%; width: 60%">
                      <el-input v-model="max_filterForm.res_name">
                        <template slot="append">.jpg</template>
                      </el-input>
                    </el-form-item>
                  </el-form>
                </div>
              </div>

              <div v-show="max_filter_active === 2"
                   style="text-align: center; margin-top: 20px; min-height: 375px; max-height: 375px">
                <div>
                  <span class="demonstration">原图片</span>
                  <br>
                  <img :src="this.displayImg[0].fileUrl" alt=""
                       style="width: auto; height: auto; max-width: 400px; max-height: 300px; margin-top: 30px">
                </div>
              </div>

              <div v-show="max_filter_active === 3"
                   style="text-align: center; margin-top: 20px; min-height: 375px; max-height: 375px">
                <div>
                  <span class="demonstration">结果图片</span>
                  <br>
                  <img :src="this.processResult.result_name" alt=""
                       style="width: auto; height: auto; max-width: 400px; max-height: 300px; margin-top: 30px">
                </div>
              </div>

              <el-button style="margin-left: 70%; margin-top: 30px;" @click="cancel">取消操作</el-button>
              <el-button v-show="max_filter_active <= 2" :loading="max_filterLoad" style="margin-left: 10px; margin-top: 10px;"
                         @click="max_filter_next">下一步
              </el-button>
              <el-button v-show="max_filter_active >= 3" :loading="max_filterLoad" style="margin-left: 10px; margin-top: 10px;"
                         @click="cancel">完成
              </el-button>

            </el-tab-pane>
            <el-tab-pane label="频域带通滤波器">
              <el-steps :active="range_filter_active" align-center finish-status="success"style="margin-top: 40px">
                <el-step title="选择图片"></el-step>
                <el-step title="输入参数"></el-step>
                <el-step title="处理图片"></el-step>
              </el-steps>

              <div v-show="range_filter_active === 0" style="margin-top: 20px;">
                <PictureChooseOne ref="range_filterSelection"/>
              </div>

              <div v-show="range_filter_active === 1"
                   style="text-align: center; margin-top: 20px; min-height: 375px; max-height: 375px">
                <div style="margin-left: 20%; margin-right: 20%">
                  <el-form :model="range_filterForm" class="demo-form-inline">
                    <el-form-item label="输出图像名称"
                                  label-width="30%"
                                  :rules="[
                      { required: true, message: '名称不能为空'}
                      ]"
                                  style="align-content: center; margin-left: 10%; margin-right: 10%; width: 60%">
                      <el-input v-model="range_filterForm.res_name">
                        <template slot="append">.jpg</template>
                      </el-input>
                    </el-form-item>


                    <el-form-item label="可通过像素值范围"
                                  :rules="[
                      { required: true, message: '范围值不能为空'}
                      ]"
                                  style="align-content: center; margin-left: 10%; margin-right: 10%; width:80%">
                      <el-col :span="7">
                        <el-input placeholder="最小值" v-model="range_filterForm.min">
                        </el-input>
                      </el-col>
                      <el-col class="line" :span="2">-</el-col>
                      <el-col :span="7">
                        <el-input placeholder="无穷大输入'MAX'" v-model="range_filterForm.max">
                        </el-input>
                      </el-col>
                    </el-form-item>

                    <el-form-item label="未通过像素新值"
                                  label-width="30%"
                                  style="align-content: center; margin-left: 10%; margin-right: 130%; width: 60%">
                      <el-select v-model="range_filterForm.color" placeholder="请选择翻转方向">
                        <el-option label="0" value="0"></el-option>
                        <el-option label="255" value="255"></el-option>
                      </el-select>
                    </el-form-item>


                  </el-form>
                </div>
              </div>

              <div v-show="range_filter_active === 2"
                   style="text-align: center; margin-top: 20px; min-height: 375px; max-height: 375px">
                <div>
                  <span class="demonstration">原图片</span>
                  <br>
                  <img :src="this.displayImg[0].fileUrl" alt=""
                       style="width: auto; height: auto; max-width: 400px; max-height: 300px; margin-top: 30px">
                </div>
              </div>

              <div v-show="range_filter_active === 3"
                   style="text-align: center; margin-top: 20px; min-height: 375px; max-height: 375px">
                <div>
                  <span class="demonstration">结果图片</span>
                  <br>
                  <img :src="this.processResult.result_name" alt=""
                       style="width: auto; height: auto; max-width: 400px; max-height: 300px; margin-top: 30px">
                </div>
              </div>

              <el-button style="margin-left: 70%; margin-top: 30px;" @click="cancel">取消操作</el-button>
              <el-button v-show="range_filter_active <= 2" :loading="range_filterLoad" style="margin-left: 10px; margin-top: 10px;"
                         @click="range_filter_next">下一步
              </el-button>
              <el-button v-show="range_filter_active >= 3" :loading="range_filterLoad" style="margin-left: 10px; margin-top: 10px;"
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
  name: "Repair",
  data() {
    return {
      headmsg: '图像去噪',
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
      arithmetic_average_filter_active: 0,
      arithmetic_average_filterForm: {
        res_name: '',
        filter_size_p: null,
        filter_size_q: null
      },
      arithmetic_average_filterLoad: false,
      geometric_average_filter_active: 0,
      geometric_average_filterForm: {
        res_name: '',
        filter_size_p: null,
        filter_size_q: null
      },
      geometric_average_filterLoad: false,
      harmonic_average_filter_active: 0,
      harmonic_average_filterForm: {
        res_name: '',
        filter_size_p: null,
        filter_size_q: null
      },
      harmonic_average_filterLoad: false,
      min_filter_active: 0,
      min_filterForm: {
        res_name: ''
      },
      min_filterLoad: false,
      max_filter_active: 0,
      max_filterForm: {
        res_name: ''
      },
      max_filterLoad: false,
      median_filter_active: 0,
      median_filterForm: {
        res_name: ''
      },
      median_filterLoad: false,
      range_filter_active: 0,
      range_filterForm: {
        res_name: '',
        min: null,
        max: null,
        color: '0'
      },
      range_filterLoad: false
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

      this.arithmetic_average_filterForm.res_name = '';
      this.arithmetic_average_filterForm.filter_size_p = null;
      this.arithmetic_average_filterForm.filter_size_q = null;
      this.geometric_average_filterForm.res_name = '';
      this.geometric_average_filterForm.filter_size_p = null;
      this.geometric_average_filterForm.filter_size_q = null;
      this.harmonic_average_filterForm.res_name = '';
      this.harmonic_average_filterForm.filter_size_p = null;
      this.harmonic_average_filterForm.filter_size_q = null;
      this.min_filterForm.res_name = '';
      this.max_filterForm.res_name = '';
      this.median_filterForm.res_name = '';
      this.range_filterForm.res_name = '';
      this.range_filterForm.min = null;
      this.range_filterForm.max = null;
      this.range_filterForm.color = '0';

      this.arithmetic_average_filterLoad = false;
      this.geometric_average_filterLoad = false;
      this.harmonic_average_filterLoad = false;
      this.min_filterLoad = false;
      this.max_filterLoad = false;
      this.median_filterLoad = false;
      this.range_filterLoad = false;

      this.processResult = {
        code: '',
        message: '',
        result_name: '../../../assets/picture/default_pic.jpg'
      };
    },
    clear_active() {
      this.arithmetic_average_filter_active = 0;
      this.geometric_average_filter_active = 0;
      this.harmonic_average_filter_active = 0;
      this.max_filter_active = 0;
      this.min_filter_active = 0;
      this.median_filter_active = 0;
      this.range_filter_active = 0;
    },
    async arithmetic_average_filter_next() {
      let tmp = this.arithmetic_average_filter_active;
      this.clear_active();
      this.arithmetic_average_filter_active = tmp;
      if (this.arithmetic_average_filter_active === 0) {
        this.selection = this.$refs["arithmetic_average_filterSelection"].multipleSelection;
        this.displayImg[0] = this.selection[0];
        if (this.selection.length !== 1) {
          this.$alert('选择的图片数量不是一张！', '数量错误', {
            confirmButtonText: '确定'
          });
          return
        }

      } else if (this.arithmetic_average_filter_active === 1) {
        if ((this.arithmetic_average_filterForm.res_name === '') || (this.arithmetic_average_filterForm.filter_size_p === '') || (this.arithmetic_average_filterForm.filter_size_q === '')) {
          this.$alert('输出图像名称不能为空！<br>滤波器大小不能为空！', '命名错误', {
            confirmButtonText: '确定',
            dangerouslyUseHTMLString: true
          });
          return
        }

        this.arithmetic_average_filterForm.filter_size_p = parseInt(this.arithmetic_average_filterForm.filter_size_p);
        this.arithmetic_average_filterForm.filter_size_q = parseInt(this.arithmetic_average_filterForm.filter_size_q);

        if ((!this.utils.isInteger(this.arithmetic_average_filterForm.filter_size_p)) || (!this.utils.isInteger(this.arithmetic_average_filterForm.filter_size_q))) {
            this.$alert('滤波器大小必须为数字！', '参数错误', {
                confirmButtonText: '确定'
            });
      return
        }
        if ((this.arithmetic_average_filterForm.filter_size_p % 2 === 0) || (this.arithmetic_average_filterForm.filter_size_q % 2 === 0) || (this.arithmetic_average_filterForm.filter_size_p <= 0) || (this.arithmetic_average_filterForm.filter_size_q <= 0)) {
          this.$alert('核数必须为正奇数！', '参数错误', {
            confirmButtonText: '确定'
          });
          return
        }


        this.arithmetic_average_filterForm.res_name = this.utils.calculate_res_name(this.arithmetic_average_filterForm.res_name);
      } else if (this.arithmetic_average_filter_active === 2) {
        const axios = require('axios')

        this.arithmetic_average_filterLoad = true;

        await axios.get(
            this.constant.data().BaseUrl + '/repair/arithmetic_average_filter', {
              params: {
                img_name: this.selection[0].fileName,
                result_name: this.arithmetic_average_filterForm.res_name,
                filter_size_p: this.arithmetic_average_filterForm.filter_size_p,
                filter_size_q: this.arithmetic_average_filterForm.filter_size_q
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

        this.arithmetic_average_filterLoad = false;


      } else if (this.arithmetic_average_filter_active === 3) {
        this.arithmetic_average_filter_active = 0;

        return
      }


      this.arithmetic_average_filter_active++;
    },
    async geometric_average_filter_next() {
      let tmp = this.geometric_average_filter_active;
      this.clear_active();
      this.geometric_average_filter_active = tmp;
      if (this.geometric_average_filter_active === 0) {
        this.selection = this.$refs["geometric_average_filterSelection"].multipleSelection;
        this.displayImg[0] = this.selection[0];
        if (this.selection.length !== 1) {
          this.$alert('选择的图片数量不是一张！', '数量错误', {
            confirmButtonText: '确定'
          });
          return
        }

      } else if (this.geometric_average_filter_active === 1) {
        if ((this.geometric_average_filterForm.res_name === '') || (this.geometric_average_filterForm.filter_size_p === '') || (this.geometric_average_filterForm.filter_size_q === '')) {
          this.$alert('输出图像名称不能为空！<br>滤波器大小不能为空！', '命名错误', {
            confirmButtonText: '确定',
            dangerouslyUseHTMLString: true
          });
          return
        }

        this.geometric_average_filterForm.filter_size_p = parseInt(this.geometric_average_filterForm.filter_size_p);
        this.geometric_average_filterForm.filter_size_q = parseInt(this.geometric_average_filterForm.filter_size_q);

        if ((!this.utils.isInteger(this.geometric_average_filterForm.filter_size_p)) || (!this.utils.isInteger(this.geometric_average_filterForm.filter_size_q))) {
            this.$alert('滤波器大小必须为数字！', '参数错误', {
                confirmButtonText: '确定'
            });
      return
        }
        if ((this.geometric_average_filterForm.filter_size_p % 2 === 0) || (this.geometric_average_filterForm.filter_size_q % 2 === 0) || (this.geometric_average_filterForm.filter_size_p <= 0) || (this.geometric_average_filterForm.filter_size_q <= 0)) {
          this.$alert('核数必须为正奇数！', '参数错误', {
            confirmButtonText: '确定'
          });
          return
        }


        this.geometric_average_filterForm.res_name = this.utils.calculate_res_name(this.geometric_average_filterForm.res_name);
      } else if (this.geometric_average_filter_active === 2) {
        const axios = require('axios')

        this.geometric_average_filterLoad = true;

        await axios.get(
            this.constant.data().BaseUrl + '/repair/geometric_average_filter', {
              params: {
                img_name: this.selection[0].fileName,
                result_name: this.geometric_average_filterForm.res_name,
                filter_size_p: this.geometric_average_filterForm.filter_size_p,
                filter_size_q: this.geometric_average_filterForm.filter_size_q
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

        this.geometric_average_filterLoad = false;


      } else if (this.geometric_average_filter_active === 3) {
        this.geometric_average_filter_active = 0;

        return
      }


      this.geometric_average_filter_active++;
    },
    async harmonic_average_filter_next() {
      let tmp = this.harmonic_average_filter_active;
      this.clear_active();
      this.harmonic_average_filter_active = tmp;
      if (this.harmonic_average_filter_active === 0) {
        this.selection = this.$refs["harmonic_average_filterSelection"].multipleSelection;
        this.displayImg[0] = this.selection[0];
        if (this.selection.length !== 1) {
          this.$alert('选择的图片数量不是一张！', '数量错误', {
            confirmButtonText: '确定'
          });
          return
        }

      } else if (this.harmonic_average_filter_active === 1) {
        if ((this.harmonic_average_filterForm.res_name === '') || (this.harmonic_average_filterForm.filter_size_p === '') || (this.harmonic_average_filterForm.filter_size_q === '')) {
          this.$alert('输出图像名称不能为空！<br>滤波器大小不能为空！', '命名错误', {
            confirmButtonText: '确定',
            dangerouslyUseHTMLString: true
          });
          return
        }

        this.harmonic_average_filterForm.filter_size_p = parseInt(this.harmonic_average_filterForm.filter_size_p);
        this.harmonic_average_filterForm.filter_size_q = parseInt(this.harmonic_average_filterForm.filter_size_q);

        if ((!this.utils.isInteger(this.harmonic_average_filterForm.filter_size_p)) || (!this.utils.isInteger(this.harmonic_average_filterForm.filter_size_q))) {
            this.$alert('滤波器大小必须为数字！', '参数错误', {
                confirmButtonText: '确定'
            });
      return
        }
        if ((this.harmonic_average_filterForm.filter_size_p % 2 === 0) || (this.harmonic_average_filterForm.filter_size_q % 2 === 0) || (this.harmonic_average_filterForm.filter_size_p <= 0) || (this.harmonic_average_filterForm.filter_size_q <= 0)) {
          this.$alert('核数必须为正奇数！', '参数错误', {
            confirmButtonText: '确定'
          });
          return
        }


        this.harmonic_average_filterForm.res_name = this.utils.calculate_res_name(this.harmonic_average_filterForm.res_name);
      } else if (this.harmonic_average_filter_active === 2) {
        const axios = require('axios')

        this.harmonic_average_filterLoad = true;

        await axios.get(
            this.constant.data().BaseUrl + '/repair/harmonic_average_filter', {
              params: {
                img_name: this.selection[0].fileName,
                result_name: this.harmonic_average_filterForm.res_name,
                filter_size_p: this.harmonic_average_filterForm.filter_size_p,
                filter_size_q: this.harmonic_average_filterForm.filter_size_q
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

        this.harmonic_average_filterLoad = false;


      } else if (this.harmonic_average_filter_active === 3) {
        this.harmonic_average_filter_active = 0;

        return
      }


      this.harmonic_average_filter_active++;
    },
    async min_filter_next() {
      let tmp = this.min_filter_active;
      this.clear_active();
      this.min_filter_active = tmp;
      if (this.min_filter_active === 0) {
        this.selection = this.$refs["min_filterSelection"].multipleSelection;
        this.displayImg[0] = this.selection[0];
        if (this.selection.length !== 1) {
          this.$alert('选择的图片数量不是一张！', '数量错误', {
            confirmButtonText: '确定'
          });
          return
        }

      } else if (this.min_filter_active === 1) {
        if (this.min_filterForm.res_name === '') {
          this.$alert('输出图像名称不能为空！', '命名错误', {
            confirmButtonText: '确定'
          });
          return
        }
        this.min_filterForm.res_name = this.utils.calculate_res_name(this.min_filterForm.res_name);
      } else if (this.min_filter_active === 2) {
        const axios = require('axios')

        this.min_filterLoad = true;

        await axios.get(
            this.constant.data().BaseUrl + '/repair/min_filter', {
              params: {
                img_name: this.selection[0].fileName,
                result_name: this.min_filterForm.res_name
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

        this.min_filterLoad = false;


      } else if (this.min_filter_active === 3) {
        this.min_filter_active = 0;

        return
      }


      this.min_filter_active++;
    },
    async max_filter_next() {
      let tmp = this.max_filter_active;
      this.clear_active();
      this.max_filter_active = tmp;
      if (this.max_filter_active === 0) {
        this.selection = this.$refs["max_filterSelection"].multipleSelection;
        this.displayImg[0] = this.selection[0];
        if (this.selection.length !== 1) {
          this.$alert('选择的图片数量不是一张！', '数量错误', {
            confirmButtonText: '确定'
          });
          return
        }

      } else if (this.max_filter_active === 1) {
        if (this.max_filterForm.res_name === '') {
          this.$alert('输出图像名称不能为空！', '命名错误', {
            confirmButtonText: '确定'
          });
          return
        }
        this.max_filterForm.res_name = this.utils.calculate_res_name(this.max_filterForm.res_name);
      } else if (this.max_filter_active === 2) {
        const axios = require('axios')

        this.max_filterLoad = true;

        await axios.get(
            this.constant.data().BaseUrl + '/repair/max_filter', {
              params: {
                img_name: this.selection[0].fileName,
                result_name: this.max_filterForm.res_name
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

        this.max_filterLoad = false;


      } else if (this.max_filter_active === 3) {
        this.max_filter_active = 0;

        return
      }


      this.max_filter_active++;
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
        if (this.median_filterForm.res_name === '') {
          this.$alert('输出图像名称不能为空！', '命名错误', {
            confirmButtonText: '确定'
          });
          return
        }
        this.median_filterForm.res_name = this.utils.calculate_res_name(this.median_filterForm.res_name);
      } else if (this.median_filter_active === 2) {
        const axios = require('axios')

        this.median_filterLoad = true;

        await axios.get(
            this.constant.data().BaseUrl + '/repair/median_filter', {
              params: {
                img_name: this.selection[0].fileName,
                result_name: this.median_filterForm.res_name
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
    async range_filter_next() {
      let tmp = this.range_filter_active;
      this.clear_active();
      this.range_filter_active = tmp;
      if (this.range_filter_active === 0) {
        this.selection = this.$refs["range_filterSelection"].multipleSelection;
        this.displayImg[0] = this.selection[0];
        if (this.selection.length !== 1) {
          this.$alert('选择的图片数量不是一张！', '数量错误', {
            confirmButtonText: '确定'
          });
          return
        }

      } else if (this.range_filter_active === 1) {
        if ((this.range_filterForm.res_name === '') || (this.range_filterForm.min === null) || (this.range_filterForm.max === null) || (this.range_filterForm.color === null)) {
          this.$alert('输出图像名称不能为空！<br>噪声范围不能为空！', '命名错误', {
            confirmButtonText: '确定',
            dangerouslyUseHTMLString: true
          });
          return
        }

        var tmp_max;

        if (this.range_filterForm.max !== 'MAX'){
            this.range_filterForm.max = parseInt(this.range_filterForm.max)
            tmp_max = this.range_filterForm.max;
        }
        else {
            tmp_max =  Number.MAX_VALUE;
        }

        this.range_filterForm.min = parseInt(this.range_filterForm.min)

        if((!this.utils.isMaxInteger(this.range_filterForm.min)) || (!this.utils.isMaxInteger(this.range_filterForm.max))) {
            this.$alert('可通过像素值范围必须为数字！', '参数错误', {
                confirmButtonText: '确定'
            });
            return
        }

        if((this.range_filterForm.min < 0) || (tmp_max < 0)) {
            this.$alert('可通过像素值范围不能为负！', '参数错误', {
                confirmButtonText: '确定'
            });
            return
        }

        if(this.range_filterForm.min > tmp_max) {
            this.$alert('最小值不得大于最大值！', '参数错误', {
                confirmButtonText: '确定'
            });
            return
        }

        this.range_filterForm.res_name = this.utils.calculate_res_name(this.range_filterForm.res_name);
      } else if (this.range_filter_active === 2) {
        const axios = require('axios')

        this.range_filterLoad = true;

        await axios.get(
            this.constant.data().BaseUrl + '/repair/range_filter', {
              params: {
                img_name: this.selection[0].fileName,
                result_name: this.range_filterForm.res_name,
                min: this.range_filterForm.min,
                max: this.range_filterForm.max,
                color: this.range_filterForm.color
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

        this.range_filterLoad = false;


      } else if (this.range_filter_active === 3) {
        this.range_filter_active = 0;

        return
      }


      this.range_filter_active++;
    }
  }
}
</script>

<style scoped>

</style>
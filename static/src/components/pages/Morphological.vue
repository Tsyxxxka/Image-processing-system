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
          <el-divider content-position="left">图像形态学</el-divider>
          {{ intromsg }}
          <el-tabs type="border-card" style="margin-top: 30px; min-height: 80%">
            <el-tab-pane label="腐蚀">
              <el-steps :active="erode_active" finish-status="success" simple style="margin-top: 10px">
                <el-step title="选择图片"></el-step>
                <el-step title="输入参数"></el-step>
                <el-step title="处理图片"></el-step>
              </el-steps>

              <div v-show="erode_active === 0" style="margin-top: 20px;">
                <PictureChooseOne ref="erodeSelection"/>
              </div>

              <div v-show="erode_active === 1"
                   style="text-align: center; margin-top: 20px; min-height: 375px; max-height: 375px">
                <div style="margin-left: 20%; margin-right: 20%">
                  <el-form :model="erodeForm" class="demo-form-inline">
                    <el-form-item label="输出图像名称"
                                  label-width="30%"
                                  :rules="[
                      { required: true, message: '名称不能为空'}
                      ]"
                                  style="align-content: center; margin-left: 10%; margin-right: 10%; width: 60%">
                      <el-input v-model="erodeForm.res_name">
                        <template slot="append">.jpg</template>
                      </el-input>
                    </el-form-item>

                    <el-form-item label="结构元类型"
                                  label-width="30%"
                                  style="align-content: center; margin-left: 10%; margin-right: 130%; width: 60%">
                      <el-select v-model="erodeForm.kernel_type" placeholder="请选择结构元类型">
                        <el-option label="十字形" value="cross"></el-option>
                        <el-option label="矩形" value="rectangle"></el-option>
                      </el-select>
                    </el-form-item>

                    <el-form-item label="结构元核数"
                                  label-width="30%"
                                  :rules=" [
                                  { required: true, message:'核数不能为空'},
                                  { type: 'number', message: '核数必须为数字值'}
                    ]"
                                  style="align-content: center; margin-left: 10%; margin-right: 10%; width: 60%">
                      <el-input placeholder="奇数，推荐3" v-model="erodeForm.kernel_size">
                      </el-input>
                    </el-form-item>


                  </el-form>
                </div>
              </div>

              <div v-show="erode_active === 2"
                   style="text-align: center; margin-top: 20px; min-height: 375px; max-height: 375px">
                <div>
                  <span class="demonstration">原图片</span>
                  <br>
                  <img :src="this.displayImg[0].fileUrl" alt=""
                       style="width: auto; height: auto; max-width: 400px; max-height: 300px; margin-top: 30px">
                </div>
              </div>

              <div v-show="erode_active === 3"
                   style="text-align: center; margin-top: 20px; min-height: 375px; max-height: 375px">
                <div>
                  <span class="demonstration">结果图片</span>
                  <br>
                  <img :src="this.processResult.result_name" alt=""
                       style="width: auto; height: auto; max-width: 400px; max-height: 300px; margin-top: 30px">
                </div>
              </div>

              <el-button style="margin-left: 80%; margin-top: 10px;" @click="cancel">取消</el-button>
              <el-button v-show="erode_active <= 2" :loading="erodeLoad" style="margin-left: 10px; margin-top: 10px;"
                         @click="erode_next">下一步
              </el-button>
              <el-button v-show="erode_active >= 3" :loading="erodeLoad" style="margin-left: 10px; margin-top: 10px;"
                         @click="cancel">完成
              </el-button>
            </el-tab-pane>
            <el-tab-pane label="膨胀">
              <el-steps :active="dilate_active" finish-status="success" simple style="margin-top: 10px">
                <el-step title="选择图片"></el-step>
                <el-step title="输入参数"></el-step>
                <el-step title="处理图片"></el-step>
              </el-steps>

              <div v-show="dilate_active === 0" style="margin-top: 20px;">
                <PictureChooseOne ref="dilateSelection"/>
              </div>

              <div v-show="dilate_active === 1"
                   style="text-align: center; margin-top: 20px; min-height: 375px; max-height: 375px">
                <div style="margin-left: 20%; margin-right: 20%">
                  <el-form :model="dilateForm" class="demo-form-inline">
                    <el-form-item label="输出图像名称"
                                  label-width="30%"
                                  :rules="[
                      { required: true, message: '名称不能为空'}
                      ]"
                                  style="align-content: center; margin-left: 10%; margin-right: 10%; width: 60%">
                      <el-input v-model="dilateForm.res_name">
                        <template slot="append">.jpg</template>
                      </el-input>
                    </el-form-item>

                    <el-form-item label="结构元类型"
                                  label-width="30%"
                                  style="align-content: center; margin-left: 10%; margin-right: 130%; width: 60%">
                      <el-select v-model="dilateForm.kernel_type" placeholder="请选择结构元类型">
                        <el-option label="十字形" value="cross"></el-option>
                        <el-option label="矩形" value="rectangle"></el-option>
                      </el-select>
                    </el-form-item>

                    <el-form-item label="结构元核数"
                                  label-width="30%"
                                  :rules=" [
                                  { required: true, message:'核数不能为空'},
                                  { type: 'number', message: '核数必须为数字值'}
                    ]"
                                  style="align-content: center; margin-left: 10%; margin-right: 10%; width: 60%">
                      <el-input placeholder="奇数，推荐3" v-model="dilateForm.kernel_size">
                      </el-input>
                    </el-form-item>


                  </el-form>
                </div>
              </div>

              <div v-show="dilate_active === 2"
                   style="text-align: center; margin-top: 20px; min-height: 375px; max-height: 375px">
                <div>
                  <span class="demonstration">原图片</span>
                  <br>
                  <img :src="this.displayImg[0].fileUrl" alt=""
                       style="width: auto; height: auto; max-width: 400px; max-height: 300px; margin-top: 30px">
                </div>
              </div>

              <div v-show="dilate_active === 3"
                   style="text-align: center; margin-top: 20px; min-height: 375px; max-height: 375px">
                <div>
                  <span class="demonstration">结果图片</span>
                  <br>
                  <img :src="this.processResult.result_name" alt=""
                       style="width: auto; height: auto; max-width: 400px; max-height: 300px; margin-top: 30px">
                </div>
              </div>

              <el-button style="margin-left: 80%; margin-top: 10px;" @click="cancel">取消</el-button>
              <el-button v-show="dilate_active <= 2" :loading="dilateLoad" style="margin-left: 10px; margin-top: 10px;"
                         @click="dilate_next">下一步
              </el-button>
              <el-button v-show="dilate_active >= 3" :loading="dilateLoad" style="margin-left: 10px; margin-top: 10px;"
                         @click="cancel">完成
              </el-button>
            </el-tab-pane>
            <el-tab-pane label="开运算">
              <el-steps :active="mor_open_active" finish-status="success" simple style="margin-top: 10px">
                <el-step title="选择图片"></el-step>
                <el-step title="输入参数"></el-step>
                <el-step title="处理图片"></el-step>
              </el-steps>

              <div v-show="mor_open_active === 0" style="margin-top: 20px;">
                <PictureChooseOne ref="mor_openSelection"/>
              </div>

              <div v-show="mor_open_active === 1"
                   style="text-align: center; margin-top: 20px; min-height: 375px; max-height: 375px">
                <div style="margin-left: 20%; margin-right: 20%">
                  <el-form :model="mor_openForm" class="demo-form-inline">
                    <el-form-item label="输出图像名称"
                                  label-width="30%"
                                  :rules="[
                      { required: true, message: '名称不能为空'}
                      ]"
                                  style="align-content: center; margin-left: 10%; margin-right: 10%; width: 60%">
                      <el-input v-model="mor_openForm.res_name">
                        <template slot="append">.jpg</template>
                      </el-input>
                    </el-form-item>

                    <el-form-item label="结构元类型"
                                  label-width="30%"
                                  style="align-content: center; margin-left: 10%; margin-right: 130%; width: 60%">
                      <el-select v-model="mor_openForm.kernel_type" placeholder="请选择结构元类型">
                        <el-option label="十字形" value="cross"></el-option>
                        <el-option label="矩形" value="rectangle"></el-option>
                      </el-select>
                    </el-form-item>

                    <el-form-item label="结构元核数"
                                  label-width="30%"
                                  :rules=" [
                                  { required: true, message:'核数不能为空'},
                                  { type: 'number', message: '核数必须为数字值'}
                    ]"
                                  style="align-content: center; margin-left: 10%; margin-right: 10%; width: 60%">
                      <el-input placeholder="奇数，推荐3" v-model="mor_openForm.kernel_size">
                      </el-input>
                    </el-form-item>


                  </el-form>
                </div>
              </div>

              <div v-show="mor_open_active === 2"
                   style="text-align: center; margin-top: 20px; min-height: 375px; max-height: 375px">
                <div>
                  <span class="demonstration">原图片</span>
                  <br>
                  <img :src="this.displayImg[0].fileUrl" alt=""
                       style="width: auto; height: auto; max-width: 400px; max-height: 300px; margin-top: 30px">
                </div>
              </div>

              <div v-show="mor_open_active === 3"
                   style="text-align: center; margin-top: 20px; min-height: 375px; max-height: 375px">
                <div>
                  <span class="demonstration">结果图片</span>
                  <br>
                  <img :src="this.processResult.result_name" alt=""
                       style="width: auto; height: auto; max-width: 400px; max-height: 300px; margin-top: 30px">
                </div>
              </div>

              <el-button style="margin-left: 80%; margin-top: 10px;" @click="cancel">取消</el-button>
              <el-button v-show="mor_open_active <= 2" :loading="mor_openLoad" style="margin-left: 10px; margin-top: 10px;"
                         @click="mor_open_next">下一步
              </el-button>
              <el-button v-show="mor_open_active >= 3" :loading="mor_openLoad" style="margin-left: 10px; margin-top: 10px;"
                         @click="cancel">完成
              </el-button>
            </el-tab-pane>
            <el-tab-pane label="闭运算">
              <el-steps :active="mor_close_active" finish-status="success" simple style="margin-top: 10px">
                <el-step title="选择图片"></el-step>
                <el-step title="输入参数"></el-step>
                <el-step title="处理图片"></el-step>
              </el-steps>

              <div v-show="mor_close_active === 0" style="margin-top: 20px;">
                <PictureChooseOne ref="mor_closeSelection"/>
              </div>

              <div v-show="mor_close_active === 1"
                   style="text-align: center; margin-top: 20px; min-height: 375px; max-height: 375px">
                <div style="margin-left: 20%; margin-right: 20%">
                  <el-form :model="mor_closeForm" class="demo-form-inline">
                    <el-form-item label="输出图像名称"
                                  label-width="30%"
                                  :rules="[
                      { required: true, message: '名称不能为空'}
                      ]"
                                  style="align-content: center; margin-left: 10%; margin-right: 10%; width: 60%">
                      <el-input v-model="mor_closeForm.res_name">
                        <template slot="append">.jpg</template>
                      </el-input>
                    </el-form-item>

                    <el-form-item label="结构元类型"
                                  label-width="30%"
                                  style="align-content: center; margin-left: 10%; margin-right: 130%; width: 60%">
                      <el-select v-model="mor_closeForm.kernel_type" placeholder="请选择结构元类型">
                        <el-option label="十字形" value="cross"></el-option>
                        <el-option label="矩形" value="rectangle"></el-option>
                      </el-select>
                    </el-form-item>

                    <el-form-item label="结构元核数"
                                  label-width="30%"
                                  :rules=" [
                                  { required: true, message:'核数不能为空'},
                                  { type: 'number', message: '核数必须为数字值'}
                    ]"
                                  style="align-content: center; margin-left: 10%; margin-right: 10%; width: 60%">
                      <el-input placeholder="奇数，推荐3" v-model="mor_closeForm.kernel_size">
                      </el-input>
                    </el-form-item>


                  </el-form>
                </div>
              </div>

              <div v-show="mor_close_active === 2"
                   style="text-align: center; margin-top: 20px; min-height: 375px; max-height: 375px">
                <div>
                  <span class="demonstration">原图片</span>
                  <br>
                  <img :src="this.displayImg[0].fileUrl" alt=""
                       style="width: auto; height: auto; max-width: 400px; max-height: 300px; margin-top: 30px">
                </div>
              </div>

              <div v-show="mor_close_active === 3"
                   style="text-align: center; margin-top: 20px; min-height: 375px; max-height: 375px">
                <div>
                  <span class="demonstration">结果图片</span>
                  <br>
                  <img :src="this.processResult.result_name" alt=""
                       style="width: auto; height: auto; max-width: 400px; max-height: 300px; margin-top: 30px">
                </div>
              </div>

              <el-button style="margin-left: 80%; margin-top: 10px;" @click="cancel">取消</el-button>
              <el-button v-show="mor_close_active <= 2" :loading="mor_closeLoad" style="margin-left: 10px; margin-top: 10px;"
                         @click="mor_close_next">下一步
              </el-button>
              <el-button v-show="mor_close_active >= 3" :loading="mor_closeLoad" style="margin-left: 10px; margin-top: 10px;"
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
  name: "Morphological",
  data() {
    return {
      headmsg: '图像形态学',
      intromsg: '\xa0\xa0\xa0\xa0\xa0\xa0\xa0主要包含了图像的腐蚀、膨胀、开运算、闭运算等功能。',
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
      erode_active: 0,
      erodeForm: {
        res_name: '',
        kernel_type: 'cross',
        kernel_size: null
      },
      erodeLoad: false,
      dilate_active: 0,
      dilateForm: {
        res_name: '',
        kernel_type: 'cross',
        kernel_size: null
      },
      dilateLoad: false,
      mor_open_active: 0,
      mor_openForm: {
        res_name: '',
        kernel_type: 'cross',
        kernel_size: null
      },
      mor_openLoad: false,
      mor_close_active: 0,
      mor_closeForm: {
        res_name: '',
        kernel_type: 'cross',
        kernel_size: null
      },
      mor_closeLoad: false
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

      this.erodeForm.res_name = '';
      this.erodeForm.kernel_type = 'cross';
      this.erodeForm.kernel_size = null;
      this.dilateForm.res_name = '';
      this.dilateForm.kernel_type = 'cross';
      this.dilateForm.kernel_size = null;
      this.mor_openForm.res_name = '';
      this.mor_openForm.kernel_type = 'cross';
      this.mor_openForm.kernel_size = null;
      this.mor_closeForm.res_name = '';
      this.mor_closeForm.kernel_type = 'cross';
      this.mor_closeForm.kernel_size = null;

      this.erodeLoad = false;
      this.dilateLoad = false;
      this.mor_openLoad = false;
      this.mor_closeLoad = false;

      this.processResult = {
        code: '',
        message: '',
        result_name: '../../../assets/picture/default_pic.jpg'
      };
    },
    clear_active() {
      this.erode_active = 0;
      this.dilate_active = 0;
      this.mor_open_active = 0;
      this.mor_close_active = 0;
    },
    async erode_next() {
      let tmp = this.erode_active;
      this.clear_active();
      this.erode_active = tmp;
      if (this.erode_active === 0) {
        this.selection = this.$refs["erodeSelection"].multipleSelection;
        this.displayImg[0] = this.selection[0];
        if (this.selection.length !== 1) {
          this.$alert('选择的图片数量不是一张！', '数量错误', {
            confirmButtonText: '确定'
          });
          return
        }

      } else if (this.erode_active === 1) {
        if ((this.erodeForm.res_name === '') || (this.erodeForm.kernel_size === null)) {
          this.$alert('输出图像名称不能为空！<br>结构元核数不能为空！', '参数错误', {
            confirmButtonText: '确定',
            dangerouslyUseHTMLString: true
          });
          return
        }
        this.erodeForm.kernel_size = parseInt(this.erodeForm.kernel_size);
        if ((!this.utils.isInteger(this.erodeForm.kernel_size))) {
          this.$alert('结构元核数必须为数字！', '参数错误', {
            confirmButtonText: '确定'
          });
          return
        }
        if ((this.erodeForm.kernel_size % 2 === 0) || (this.erodeForm.kernel_size <= 0)) {
          this.$alert('结构元核数必须为正奇数！', '参数错误', {
            confirmButtonText: '确定'
          });
          return
        }
        this.erodeForm.res_name = this.utils.calculate_res_name(this.erodeForm.res_name);
      } else if (this.erode_active === 2) {
        const axios = require('axios')

        this.erodeLoad = true;

        await axios.get(
            this.constant.data().BaseUrl + '/morphological/erode', {
              params: {
                img_name: this.selection[0].fileName,
                result_name: this.erodeForm.res_name,
                kernel_type: this.erodeForm.kernel_type,
                kernel_size: this.erodeForm.kernel_size
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

        this.erodeLoad = false;


      } else if (this.erode_active === 3) {
        this.erode_active = 0;

        return
      }


      this.erode_active++;
    },
    async dilate_next() {
      let tmp = this.dilate_active;
      this.clear_active();
      this.dilate_active = tmp;
      if (this.dilate_active === 0) {
        this.selection = this.$refs["dilateSelection"].multipleSelection;
        this.displayImg[0] = this.selection[0];
        if (this.selection.length !== 1) {
          this.$alert('选择的图片数量不是一张！', '数量错误', {
            confirmButtonText: '确定'
          });
          return
        }

      } else if (this.dilate_active === 1) {
        if ((this.dilateForm.res_name === '') || (this.dilateForm.kernel_size === null)) {
          this.$alert('输出图像名称不能为空！<br>结构元核数不能为空！', '参数错误', {
            confirmButtonText: '确定',
            dangerouslyUseHTMLString: true
          });
          return
        }
        this.dilateForm.kernel_size = parseInt(this.dilateForm.kernel_size);
        if ((!this.utils.isInteger(this.dilateForm.kernel_size))) {
          this.$alert('结构元核数必须为数字！', '参数错误', {
            confirmButtonText: '确定'
          });
          return
        }
        if ((this.dilateForm.kernel_size % 2 === 0) || (this.dilateForm.kernel_size <= 0)) {
          this.$alert('结构元核数必须为正奇数！', '参数错误', {
            confirmButtonText: '确定'
          });
          return
        }
        this.dilateForm.res_name = this.utils.calculate_res_name(this.dilateForm.res_name);
      } else if (this.dilate_active === 2) {
        const axios = require('axios')

        this.dilateLoad = true;

        await axios.get(
            this.constant.data().BaseUrl + '/morphological/dilate', {
              params: {
                img_name: this.selection[0].fileName,
                result_name: this.dilateForm.res_name,
                kernel_type: this.dilateForm.kernel_type,
                kernel_size: this.dilateForm.kernel_size
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

        this.dilateLoad = false;


      } else if (this.dilate_active === 3) {
        this.dilate_active = 0;

        return
      }


      this.dilate_active++;
    },
    async mor_open_next() {
      let tmp = this.mor_open_active;
      this.clear_active();
      this.mor_open_active = tmp;
      if (this.mor_open_active === 0) {
        this.selection = this.$refs["mor_openSelection"].multipleSelection;
        this.displayImg[0] = this.selection[0];
        if (this.selection.length !== 1) {
          this.$alert('选择的图片数量不是一张！', '数量错误', {
            confirmButtonText: '确定'
          });
          return
        }

      } else if (this.mor_open_active === 1) {
        if ((this.mor_openForm.res_name === '') || (this.mor_openForm.kernel_size === null)) {
          this.$alert('输出图像名称不能为空！<br>结构元核数不能为空！', '参数错误', {
            confirmButtonText: '确定',
            dangerouslyUseHTMLString: true
          });
          return
        }
        this.mor_openForm.kernel_size = parseInt(this.mor_openForm.kernel_size);
        if ((!this.utils.isInteger(this.mor_openForm.kernel_size))) {
          this.$alert('结构元核数必须为数字！', '参数错误', {
            confirmButtonText: '确定'
          });
          return
        }
        if ((this.mor_openForm.kernel_size % 2 === 0) || (this.mor_openForm.kernel_size <= 0)) {
          this.$alert('结构元核数必须为正奇数！', '参数错误', {
            confirmButtonText: '确定'
          });
          return
        }
        this.mor_openForm.res_name = this.utils.calculate_res_name(this.mor_openForm.res_name);
      } else if (this.mor_open_active === 2) {
        const axios = require('axios')

        this.mor_openLoad = true;

        await axios.get(
            this.constant.data().BaseUrl + '/morphological/mor_open', {
              params: {
                img_name: this.selection[0].fileName,
                result_name: this.mor_openForm.res_name,
                kernel_type: this.mor_openForm.kernel_type,
                kernel_size: this.mor_openForm.kernel_size
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

        this.mor_openLoad = false;


      } else if (this.mor_open_active === 3) {
        this.mor_open_active = 0;

        return
      }


      this.mor_open_active++;
    },
    async mor_close_next() {
      let tmp = this.mor_close_active;
      this.clear_active();
      this.mor_close_active = tmp;
      if (this.mor_close_active === 0) {
        this.selection = this.$refs["mor_closeSelection"].multipleSelection;
        this.displayImg[0] = this.selection[0];
        if (this.selection.length !== 1) {
          this.$alert('选择的图片数量不是一张！', '数量错误', {
            confirmButtonText: '确定'
          });
          return
        }

      } else if (this.mor_close_active === 1) {
        if ((this.mor_closeForm.res_name === '') || (this.mor_closeForm.kernel_size === null)) {
          this.$alert('输出图像名称不能为空！<br>结构元核数不能为空！', '参数错误', {
            confirmButtonText: '确定',
            dangerouslyUseHTMLString: true
          });
          return
        }
        this.mor_closeForm.kernel_size = parseInt(this.mor_closeForm.kernel_size);
        if ((!this.utils.isInteger(this.mor_closeForm.kernel_size))) {
          this.$alert('结构元核数必须为数字！', '参数错误', {
            confirmButtonText: '确定'
          });
          return
        }
        if ((this.mor_closeForm.kernel_size % 2 === 0) || (this.mor_closeForm.kernel_size <= 0)) {
          this.$alert('结构元核数必须为正奇数！', '参数错误', {
            confirmButtonText: '确定'
          });
          return
        }
        this.mor_closeForm.res_name = this.utils.calculate_res_name(this.mor_closeForm.res_name);
      } else if (this.mor_close_active === 2) {
        const axios = require('axios')

        this.mor_closeLoad = true;

        await axios.get(
            this.constant.data().BaseUrl + '/morphological/mor_close', {
              params: {
                img_name: this.selection[0].fileName,
                result_name: this.mor_closeForm.res_name,
                kernel_type: this.mor_closeForm.kernel_type,
                kernel_size: this.mor_closeForm.kernel_size
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

        this.mor_closeLoad = false;


      } else if (this.mor_close_active === 3) {
        this.mor_close_active = 0;

        return
      }


      this.mor_close_active++;
    }
  }
}
</script>

<style scoped>

</style>
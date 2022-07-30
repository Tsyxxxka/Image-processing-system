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
            <el-tab-pane label="灰度化">
              <el-steps :active="graying_active" align-center finish-status="success" style="margin-top: 40px">
                <el-step title="选择图片"></el-step>
                <el-step title="输入参数"></el-step>
                <el-step title="处理图片"></el-step>
              </el-steps>

              <div v-show="graying_active === 0" style="margin-top: 20px;">
                <PictureChooseOne ref="grayingSelection"/>
              </div>

              <div v-show="graying_active === 1"
                   style="text-align: center; margin-top: 20px; min-height: 375px; max-height: 375px">
                <div style="margin-left: 20%; margin-right: 20%">
                  <el-form :model="grayingForm" class="demo-form-inline">
                    <el-form-item label="输出图像名称"
                                  label-width="30%"
                                  :rules="[
                      { required: true, message: '名称不能为空'}
                      ]"
                                  style="align-content: center; margin-left: 10%; margin-right: 10%; width: 60%">
                      <el-input v-model="grayingForm.res_name">
                        <template slot="append">.jpg</template>
                      </el-input>
                    </el-form-item>
                  </el-form>
                </div>
              </div>

              <div v-show="graying_active === 2"
                   style="text-align: center; margin-top: 20px; min-height: 375px; max-height: 375px">
                <div>
                  <span class="demonstration">原图片</span>
                  <br>
                  <img :src="this.displayImg[0].fileUrl" alt=""
                       style="width: auto; height: auto; max-width: 400px; max-height: 300px; margin-top: 30px">
                </div>
              </div>

              <div v-show="graying_active === 3"
                   style="text-align: center; margin-top: 20px; min-height: 375px; max-height: 375px">
                <div>
                  <span class="demonstration">结果图片</span>
                  <br>
                  <img :src="this.processResult.result_name" alt=""
                       style="width: auto; height: auto; max-width: 400px; max-height: 300px; margin-top: 30px">
                </div>
              </div>

              <el-button style="margin-left: 70%; margin-top: 30px;" @click="cancel">取消操作</el-button>
              <el-button v-show="graying_active <= 2" :loading="grayingLoad" style="margin-left: 10px; margin-top: 10px;"
                         @click="graying_next">下一步
              </el-button>
              <el-button v-show="graying_active >= 3" :loading="grayingLoad" style="margin-left: 10px; margin-top: 10px;"
                         @click="cancel">完成
              </el-button>

            </el-tab-pane>
            <el-tab-pane label="二值化">
              <el-steps :active="thre_active" align-center finish-status="success" style="margin-top: 40px">
                <el-step title="选择图片"></el-step>
                <el-step title="输入参数"></el-step>
                <el-step title="处理图片"></el-step>
              </el-steps>

              <div v-show="thre_active === 0" style="margin-top: 20px;">
                <PictureChooseOne ref="threSelection"/>
              </div>

              <div v-show="thre_active === 1"
                   style="text-align: center; margin-top: 20px; min-height: 375px; max-height: 375px">
                <div style="margin-left: 20%; margin-right: 20%">
                  <el-form :model="threForm" class="demo-form-inline">
                    <el-form-item label="输出图像名称"
                                  label-width="30%"
                                  :rules="[
                      { required: true, message: '名称不能为空'}
                      ]"
                                  style="align-content: center; margin-left: 10%; margin-right: 10%; width: 60%">
                      <el-input v-model="threForm.res_name">
                        <template slot="append">.jpg</template>
                      </el-input>
                    </el-form-item>
                  </el-form>
                </div>
              </div>

              <div v-show="thre_active === 2"
                   style="text-align: center; margin-top: 20px; min-height: 375px; max-height: 375px">
                <div>
                  <span class="demonstration">原图片</span>
                  <br>
                  <img :src="this.displayImg[0].fileUrl" alt=""
                       style="width: auto; height: auto; max-width: 400px; max-height: 300px; margin-top: 30px">
                </div>
              </div>

              <div v-show="thre_active === 3"
                   style="text-align: center; margin-top: 20px; min-height: 375px; max-height: 375px">
                <div>
                  <span class="demonstration">结果图片</span>
                  <br>
                  <img :src="this.processResult.result_name" alt=""
                       style="width: auto; height: auto; max-width: 400px; max-height: 300px; margin-top: 30px">
                </div>
              </div>

              <el-button style="margin-left: 70%; margin-top: 30px;" @click="cancel">取消操作</el-button>
              <el-button v-show="thre_active <= 2" :loading="threLoad" style="margin-left: 10px; margin-top: 10px;"
                         @click="thre_next">下一步
              </el-button>
              <el-button v-show="thre_active >= 3" :loading="threLoad" style="margin-left: 10px; margin-top: 10px;"
                         @click="cancel">完成
              </el-button>
            </el-tab-pane>
            
            <el-tab-pane label="图像翻转">
              <el-steps :active="flip_active" align-center finish-status="success"style="margin-top: 40px">
                <el-step title="选择图片"></el-step>
                <el-step title="输入参数"></el-step>
                <el-step title="处理图片"></el-step>
              </el-steps>

              <div v-show="flip_active === 0" style="margin-top: 20px;">
                <PictureChooseOne ref="flipSelection"/>
              </div>

              <div v-show="flip_active === 1"
                   style="text-align: center; margin-top: 20px; min-height: 375px; max-height: 375px">
                <div style="margin-left: 20%; margin-right: 20%">
                  <el-form :model="flipForm" class="demo-form-inline">
                    <el-form-item label="输出图像名称"
                                  label-width="30%"
                                  :rules="[
                      { required: true, message: '名称不能为空'}
                      ]"
                                  style="align-content: center; margin-left: 10%; margin-right: 10%; width: 60%">
                      <el-input v-model="flipForm.res_name">
                        <template slot="append">.jpg</template>
                      </el-input>
                    </el-form-item>
                    <el-form-item label="翻转方向"
                                  label-width="30%"
                                  style="align-content: center; margin-left: 10%; margin-right: 130%; width: 60%">
                      <el-select v-model="flipForm.fli_choi" placeholder="请选择翻转方向">
                        <el-option label="水平翻转" value="horizontal"></el-option>
                        <el-option label="垂直翻转" value="vertical"></el-option>
                        <el-option label="对角翻转" value="diagonal"></el-option>
                      </el-select>
                    </el-form-item>
                  </el-form>
                </div>
              </div>

              <div v-show="flip_active === 2"
                   style="text-align: center; margin-top: 20px; min-height: 375px; max-height: 375px">
                <div>
                  <span class="demonstration">原图片</span>
                  <br>
                  <img :src="this.displayImg[0].fileUrl" alt=""
                       style="width: auto; height: auto; max-width: 400px; max-height: 300px; margin-top: 30px">
                </div>
              </div>

              <div v-show="flip_active === 3"
                   style="text-align: center; margin-top: 20px; min-height: 375px; max-height: 375px">
                <div>
                  <span class="demonstration">结果图片</span>
                  <br>
                  <img :src="this.processResult.result_name" alt=""
                       style="width: auto; height: auto; max-width: 400px; max-height: 300px; margin-top: 30px">
                </div>
              </div>

              <el-button style="margin-left: 70%; margin-top: 30px;" @click="cancel">取消操作</el-button>
              <el-button v-show="flip_active <= 2" :loading="flipLoad" style="margin-left: 10px; margin-top: 10px;"
                         @click="flip_next">下一步
              </el-button>
              <el-button v-show="flip_active >= 3" :loading="flipLoad" style="margin-left: 10px; margin-top: 10px;"
                         @click="cancel">完成
              </el-button>
            </el-tab-pane>
            <el-tab-pane label="图像平移">
              <el-steps :active="move_active" align-center finish-status="success"style="margin-top: 40px">
                <el-step title="选择图片"></el-step>
                <el-step title="输入参数"></el-step>
                <el-step title="处理图片"></el-step>
              </el-steps>

              <div v-show="move_active === 0" style="margin-top: 20px;">
                <PictureChooseOne ref="moveSelection"/>
              </div>

              <div v-show="move_active === 1"
                   style="text-align: center; margin-top: 20px; min-height: 375px; max-height: 375px">
                <div style="margin-left: 20%; margin-right: 20%">
                  <el-form :model="moveForm" class="demo-form-inline">
                    <el-form-item label="输出图像名称"
                                  label-width="30%"
                                  :rules="[
                      { required: true, message: '名称不能为空'}
                      ]"
                                  style="align-content: center; margin-left: 10%; margin-right: 10%; width: 60%">
                      <el-input v-model="moveForm.res_name">
                        <template slot="append">.jpg</template>
                      </el-input>
                    </el-form-item>


                    <el-form-item label="坐标轴移动像素值"
                                  :rules="[
                      { required: true, message: '像素值不能为空'},
                      { type: 'number', message: '像素值必须为数字值'}
                      ]"
                                  style="align-content: center; margin-left: 10%; margin-right: 10%; width:80%">
                      <el-col :span="7">
                        <el-input placeholder="x轴移动像素值" v-model="moveForm.move_x">
                        </el-input>
                      </el-col>
                      <el-col class="line" :span="2">,</el-col>
                      <el-col :span="7">
                        <el-input placeholder="y轴移动像素值" v-model="moveForm.move_y">
                        </el-input>
                      </el-col>
                    </el-form-item>


                  </el-form>
                </div>
              </div>

              <div v-show="move_active === 2"
                   style="text-align: center; margin-top: 20px; min-height: 375px; max-height: 375px">
                <div>
                  <span class="demonstration">原图片</span>
                  <br>
                  <img :src="this.displayImg[0].fileUrl" alt=""
                       style="width: auto; height: auto; max-width: 400px; max-height: 300px; margin-top: 30px">
                </div>
              </div>

              <div v-show="move_active === 3"
                   style="text-align: center; margin-top: 20px; min-height: 375px; max-height: 375px">
                <div>
                  <span class="demonstration">结果图片</span>
                  <br>
                  <img :src="this.processResult.result_name" alt=""
                       style="width: auto; height: auto; max-width: 400px; max-height: 300px; margin-top: 30px">
                </div>
              </div>

              <el-button style="margin-left: 70%; margin-top: 30px;" @click="cancel">取消操作</el-button>
              <el-button v-show="move_active <= 2" :loading="moveLoad" style="margin-left: 10px; margin-top: 10px;"
                         @click="move_next">下一步
              </el-button>
              <el-button v-show="move_active >= 3" :loading="moveLoad" style="margin-left: 10px; margin-top: 10px;"
                         @click="cancel">完成
              </el-button>
            </el-tab-pane>
            <el-tab-pane label="图像旋转">
              <el-steps :active="rotate_active" align-center finish-status="success"style="margin-top: 40px">
                <el-step title="选择图片"></el-step>
                <el-step title="输入参数"></el-step>
                <el-step title="处理图片"></el-step>
              </el-steps>

              <div v-show="rotate_active === 0" style="margin-top: 20px;">
                <PictureChooseOne ref="rotateSelection"/>
              </div>

              <div v-show="rotate_active === 1"
                   style="text-align: center; margin-top: 20px; min-height: 375px; max-height: 375px">
                <div style="margin-left: 20%; margin-right: 20%">
                  <el-form :model="rotateForm" class="demo-form-inline">
                    <el-form-item label="输出图像名称"
                                  label-width="30%"
                                  :rules="[
                                  { required: true, message: '名称不能为空'}
                                  ]"
                                  style="align-content: center; margin-left: 10%; margin-right: 10%; width: 60%">
                      <el-input v-model="rotateForm.res_name">
                        <template slot="append">.jpg</template>
                      </el-input>
                    </el-form-item>

                    <el-form-item label="图片旋转角度"
                                  label-width="30%"
                                  :rules=" [
                                  { required: true, message:'角度值不能为空'},
                                  { type: 'number', message: '角度值必须为数字值'}
                    ]"
                                  style="align-content: center; margin-left: 10%; margin-right: 10%; width: 60%">
                      <el-input v-model="rotateForm.angle">
                      </el-input>
                    </el-form-item>


                  </el-form>
                </div>
              </div>

              <div v-show="rotate_active === 2"
                   style="text-align: center; margin-top: 20px; min-height: 375px; max-height: 375px">
                <div>
                  <span class="demonstration">原图片</span>
                  <br>
                  <img :src="this.displayImg[0].fileUrl" alt=""
                       style="width: auto; height: auto; max-width: 400px; max-height: 300px; margin-top: 30px">
                </div>
              </div>

              <div v-show="rotate_active === 3"
                   style="text-align: center; margin-top: 20px; min-height: 375px; max-height: 375px">
                <div>
                  <span class="demonstration">结果图片</span>
                  <br>
                  <img :src="this.processResult.result_name" alt=""
                       style="width: auto; height: auto; max-width: 400px; max-height: 300px; margin-top: 30px">
                </div>
              </div>

              <el-button style="margin-left: 70%; margin-top: 30px;" @click="cancel">取消操作</el-button>
              <el-button v-show="rotate_active <= 2" :loading="rotateLoad" style="margin-left: 10px; margin-top: 10px;"
                         @click="rotate_next">下一步
              </el-button>
              <el-button v-show="rotate_active >= 3" :loading="rotateLoad" style="margin-left: 10px; margin-top: 10px;"
                         @click="cancel">完成
              </el-button>
            </el-tab-pane>
            <el-tab-pane label="图像放缩">
              <el-steps :active="resize_active" align-center finish-status="success"style="margin-top: 40px">
                <el-step title="选择图片"></el-step>
                <el-step title="输入参数"></el-step>
                <el-step title="处理图片"></el-step>
              </el-steps>

              <div v-show="resize_active === 0" style="margin-top: 20px;">
                <PictureChooseOne ref="resizeSelection"/>
              </div>

              <div v-show="resize_active === 1"
                   style="text-align: center; margin-top: 20px; min-height: 375px; max-height: 375px">
                <div style="margin-left: 20%; margin-right: 20%">
                  <el-form :model="resizeForm" class="demo-form-inline">
                    <el-form-item label="输出图像名称"
                                  label-width="30%"
                                  :rules="[
                      { required: true, message: '名称不能为空'}
                      ]"
                                  style="align-content: center; margin-left: 10%; margin-right: 10%; width: 60%">
                      <el-input v-model="resizeForm.res_name">
                        <template slot="append">.jpg</template>
                      </el-input>
                    </el-form-item>


                    <el-form-item label="坐标轴放缩倍数"
                                  :rules="[
                      { required: true, message: '倍数不能为空'},
                      { type: 'number', message: '倍数必须为数字值'}
                      ]"
                                  style="align-content: center; margin-left: 10%; margin-right: 10%; width:80%">
                      <el-col :span="7">
                        <el-input placeholder="x轴放缩倍数" v-model="resizeForm.size_x">
                        </el-input>
                      </el-col>
                      <el-col class="line" :span="2">,</el-col>
                      <el-col :span="7">
                        <el-input placeholder="y轴放缩倍数" v-model="resizeForm.size_y">
                        </el-input>
                      </el-col>
                    </el-form-item>


                  </el-form>
                </div>
              </div>

              <div v-show="resize_active === 2"
                   style="text-align: center; margin-top: 20px; min-height: 375px; max-height: 375px">
                <div>
                  <span class="demonstration">原图片</span>
                  <br>
                  <img :src="this.displayImg[0].fileUrl" alt=""
                       style="width: auto; height: auto; max-width: 400px; max-height: 300px; margin-top: 30px">
                </div>
              </div>

              <div v-show="resize_active === 3"
                   style="text-align: center; margin-top: 20px; min-height: 375px; max-height: 375px">
                <div>
                  <span class="demonstration">结果图片</span>
                  <br>
                  <img :src="this.processResult.result_name" alt=""
                       style="width: auto; height: auto; max-width: 400px; max-height: 300px; margin-top: 30px">
                </div>
              </div>

              <el-button style="margin-left: 70%; margin-top: 30px;" @click="cancel">取消操作</el-button>
              <el-button v-show="resize_active <= 2" :loading="resizeLoad" style="margin-left: 10px; margin-top: 10px;"
                         @click="resize_next">下一步
              </el-button>
              <el-button v-show="resize_active >= 3" :loading="resizeLoad" style="margin-left: 10px; margin-top: 10px;"
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
  name: "BasicFunc",
  data() {
    return {
      headmsg: '图像编辑',
      graying_active: 0,
      selection: [],
      displayImg: [
        {
          fileName: '../../../assets/picture/default_pic.jpg'
        },
        {
          fileName: '../../../assets/picture/default_pic.jpg'
        }
      ],
      grayingForm: {
        res_name: ''
      },
      processResult: {
        code: '',
        message: '',
        result_name: '../../../assets/picture/default_pic.jpg'
      },
      grayingLoad: false,
      thre_active: 0,
      threForm: {
        res_name: ''
      },
      threLoad: false,
      logical_and_active: 0,
      logical_andForm: {
        res_name: ''
      },
      logical_andLoad: false,
      logical_or_active: 0,
      logical_orForm: {
        res_name: ''
      },
      logical_orLoad: false,
      logical_not_active: 0,
      logical_notForm: {
        res_name: ''
      },
      logical_notLoad: false,
      add_active: 0,
      addForm: {
        res_name: ''
      },
      addLoad: false,
      subtract_active: 0,
      subtractForm: {
        res_name: ''
      },
      subtractLoad: false,
      multiply_active: 0,
      multiplyForm: {
        res_name: ''
      },
      multiplyLoad: false,
      divide_active: 0,
      divideForm: {
        res_name: ''
      },
      divideLoad: false,
      flip_active: 0,
      flipForm: {
        res_name: '',
        fli_choi: 'horizontal'
      },
      flipLoad: false,
      move_active: 0,
      moveForm: {
        res_name: '',
        move_x: null,
        move_y: null
      },
      moveLoad: false,
      rotate_active: 0,
      rotateForm: {
        res_name: '',
        angle: null
      },
      rotateLoad: false,
      resize_active: 0,
      resizeForm: {
        res_name: '',
        size_x: null,
        size_y: null
      },
      resizeLoad: false
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

      this.grayingForm.res_name = '';
      this.threForm.res_name = '';
      this.logical_andForm.res_name = '';
      this.logical_orForm.res_name = '';
      this.logical_notForm.res_name = '';
      this.addForm.res_name = '';
      this.subtractForm.res_name = '';
      this.multiplyForm.res_name = '';
      this.divideForm.res_name = '';
      this.flipForm.res_name = '';
      this.flipForm.fli_choi = 'horizontal';
      this.moveForm.res_name = '';
      this.moveForm.move_x = null;
      this.moveForm.move_y = null;
      this.rotateForm.res_name = '';
      this.rotateForm.angle = null;
      this.resizeForm.res_name = '';
      this.resizeForm.size_x = null;
      this.resizeForm.size_y = null;

      this.grayingLoad = false;
      this.threLoad = false;
      this.logical_andLoad = false;
      this.logical_andLoad = false;
      this.logical_notLoad = false;
      this.addLoad = false;
      this.subtractLoad = false;
      this.multiplyLoad = false;
      this.divideLoad = false;
      this.flipLoad = false;
      this.moveLoad = false;
      this.rotateLoad = false;
      this.resizeLoad = false;

      this.processResult = {
        code: '',
        message: '',
        result_name: '../../../assets/picture/default_pic.jpg'
      };
    },
    clear_active() {
      this.graying_active = 0;
      this.thre_active = 0;
      this.logical_and_active = 0;
      this.logical_or_active = 0;
      this.logical_not_active = 0;
      this.add_active = 0;
      this.subtract_active = 0;
      this.multiply_active = 0;
      this.divide_active = 0;
      this.flip_active = 0;
      this.move_active = 0;
      this.rotate_active = 0;
      this.resize_active = 0;
    },
    async graying_next() {
      let tmp = this.graying_active;
      this.clear_active();
      this.graying_active = tmp;
      if (this.graying_active === 0) {
        this.selection = this.$refs["grayingSelection"].multipleSelection;
        this.displayImg[0] = this.selection[0];
        if (this.selection.length !== 1) {
          this.$alert('选择的图片数量不是一张！', '数量错误', {
            confirmButtonText: '确定'
          });
          return
        }

      } else if (this.graying_active === 1) {
        if (this.grayingForm.res_name === '') {
          this.$alert('输出图像名称不能为空！', '命名错误', {
            confirmButtonText: '确定'
          });
          return
        }
        this.grayingForm.res_name = this.utils.calculate_res_name(this.grayingForm.res_name);
      } else if (this.graying_active === 2) {
        const axios = require('axios')

        this.grayingLoad = true;

        await axios.get(
            this.constant.data().BaseUrl + '/basic_func/graying', {
              params: {
                img_name: this.selection[0].fileName,
                result_name: this.grayingForm.res_name
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

        this.grayingLoad = false;


      } else if (this.graying_active === 3) {
        this.graying_active = 0;

        return
      }


      this.graying_active++;
    },
    async thre_next() {
      let tmp = this.thre_active;
      this.clear_active();
      this.thre_active = tmp;
      if (this.thre_active === 0) {
        this.selection = this.$refs["threSelection"].multipleSelection;
        this.displayImg[0] = this.selection[0];
        if (this.selection.length !== 1) {
          this.$alert('选择的图片数量不是一张！', '数量错误', {
            confirmButtonText: '确定'
          });
          return
        }

      } else if (this.thre_active === 1) {
        if (this.threForm.res_name === '') {
          this.$alert('输出图像名称不能为空！', '命名错误', {
            confirmButtonText: '确定'
          });
          return
        }
        this.threForm.res_name = this.utils.calculate_res_name(this.threForm.res_name);
      } else if (this.thre_active === 2) {
        const axios = require('axios')

        this.threLoad = true;

        await axios.get(
            this.constant.data().BaseUrl + '/basic_func/thresholding', {
              params: {
                img_name: this.selection[0].fileName,
                result_name: this.threForm.res_name
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

        this.threLoad = false;


      } else if (this.thre_active === 3) {
        this.thre_active = 0;

        return
      }


      this.thre_active++;
    },
    async logical_and_next() {
      let tmp = this.logical_and_active;
      this.clear_active();
      this.logical_and_active = tmp;
      if (this.logical_and_active === 0) {
        this.selection = this.$refs["logical_andSelection"].multipleSelection;
        this.displayImg[0] = this.selection[0];
        this.displayImg[1] = this.selection[1];
        if (this.selection.length !== 2) {
          this.$alert('选择的图片数量不是两张！', '数量错误', {
            confirmButtonText: '确定'
          });
          return
        }

      } else if (this.logical_and_active === 1) {
        if (this.logical_andForm.res_name === '') {
          this.$alert('输出图像名称不能为空！', '命名错误', {
            confirmButtonText: '确定'
          });
          return
        }
        this.logical_andForm.res_name = this.utils.calculate_res_name(this.logical_andForm.res_name);
      } else if (this.logical_and_active === 2) {
        const axios = require('axios')

        this.logical_andLoad = true;

        await axios.get(
            this.constant.data().BaseUrl + '/basic_func/logical_and', {
              params: {
                img_name1: this.selection[0].fileName,
                img_name2: this.selection[1].fileName,
                result_name: this.logical_andForm.res_name
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

        this.logical_andLoad = false;


      } else if (this.logical_and_active === 3) {
        this.logical_and_active = 0;

        return
      }


      this.logical_and_active++;
    },
    async logical_or_next() {
      let tmp = this.logical_or_active;
      this.clear_active();
      this.logical_or_active = tmp;
      if (this.logical_or_active === 0) {
        this.selection = this.$refs["logical_orSelection"].multipleSelection;
        this.displayImg[0] = this.selection[0];
        this.displayImg[1] = this.selection[1];
        if (this.selection.length !== 2) {
          this.$alert('选择的图片数量不是两张！', '数量错误', {
            confirmButtonText: '确定'
          });
          return
        }

      } else if (this.logical_or_active === 1) {
        if (this.logical_orForm.res_name === '') {
          this.$alert('输出图像名称不能为空！', '命名错误', {
            confirmButtonText: '确定'
          });
          return
        }
        this.logical_orForm.res_name = this.utils.calculate_res_name(this.logical_orForm.res_name);
      } else if (this.logical_or_active === 2) {
        const axios = require('axios')

        this.logical_orLoad = true;

        await axios.get(
            this.constant.data().BaseUrl + '/basic_func/logical_or', {
              params: {
                img_name1: this.selection[0].fileName,
                img_name2: this.selection[1].fileName,
                result_name: this.logical_orForm.res_name
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

        this.logical_orLoad = false;


      } else if (this.logical_or_active === 3) {
        this.logical_or_active = 0;

        return
      }


      this.logical_or_active++;
    },
    async logical_not_next() {
      let tmp = this.logical_not_active;
      this.clear_active();
      this.logical_not_active = tmp;
      if (this.logical_not_active === 0) {
        this.selection = this.$refs["logical_notSelection"].multipleSelection;
        this.displayImg[0] = this.selection[0];
        if (this.selection.length !== 1) {
          this.$alert('选择的图片数量不是一张！', '数量错误', {
            confirmButtonText: '确定'
          });
          return
        }

      } else if (this.logical_not_active === 1) {
        if (this.logical_notForm.res_name === '') {
          this.$alert('输出图像名称不能为空！', '命名错误', {
            confirmButtonText: '确定'
          });
          return
        }
        this.logical_notForm.res_name = this.utils.calculate_res_name(this.logical_notForm.res_name);
      } else if (this.logical_not_active === 2) {
        const axios = require('axios')

        this.logical_notLoad = true;

        await axios.get(
            this.constant.data().BaseUrl + '/basic_func/logical_not', {
              params: {
                img_name: this.selection[0].fileName,
                result_name: this.logical_notForm.res_name
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

        this.logical_notLoad = false;


      } else if (this.logical_not_active === 3) {
        this.logical_not_active = 0;

        return
      }


      this.logical_not_active++;
    },
    async add_next() {
      let tmp = this.add_active;
      this.clear_active();
      this.add_active = tmp;
      if (this.add_active === 0) {
        this.selection = this.$refs["addSelection"].multipleSelection;
        this.displayImg[0] = this.selection[0];
        this.displayImg[1] = this.selection[1];
        if (this.selection.length !== 2) {
          this.$alert('选择的图片数量不是两张！', '数量错误', {
            confirmButtonText: '确定'
          });
          return
        }

      } else if (this.add_active === 1) {
        if (this.addForm.res_name === '') {
          this.$alert('输出图像名称不能为空！', '命名错误', {
            confirmButtonText: '确定'
          });
          return
        }
        this.addForm.res_name = this.utils.calculate_res_name(this.addForm.res_name);
      } else if (this.add_active === 2) {
        const axios = require('axios')

        this.addLoad = true;

        await axios.get(
            this.constant.data().BaseUrl + '/basic_func/add', {
              params: {
                img_name1: this.selection[0].fileName,
                img_name2: this.selection[1].fileName,
                result_name: this.addForm.res_name
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

        this.addLoad = false;


      } else if (this.add_active === 3) {
        this.add_active = 0;

        return
      }


      this.add_active++;
    },
    async subtract_next() {
      let tmp = this.subtract_active;
      this.clear_active();
      this.subtract_active = tmp;
      if (this.subtract_active === 0) {
        this.selection = this.$refs["subtractSelection"].multipleSelection;
        this.displayImg[0] = this.selection[0];
        this.displayImg[1] = this.selection[1];
        if (this.selection.length !== 2) {
          this.$alert('选择的图片数量不是两张！', '数量错误', {
            confirmButtonText: '确定'
          });
          return
        }

      } else if (this.subtract_active === 1) {
        if (this.subtractForm.res_name === '') {
          this.$alert('输出图像名称不能为空！', '命名错误', {
            confirmButtonText: '确定'
          });
          return
        }
        this.subtractForm.res_name = this.utils.calculate_res_name(this.subtractForm.res_name);
      } else if (this.subtract_active === 2) {
        const axios = require('axios')

        this.subtractLoad = true;

        await axios.get(
            this.constant.data().BaseUrl + '/basic_func/subtract', {
              params: {
                img_name1: this.selection[0].fileName,
                img_name2: this.selection[1].fileName,
                result_name: this.subtractForm.res_name
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

        this.subtractLoad = false;


      } else if (this.subtract_active === 3) {
        this.subtract_active = 0;

        return
      }


      this.subtract_active++;
    },
    async multiply_next() {
      let tmp = this.multiply_active;
      this.clear_active();
      this.multiply_active = tmp;
      if (this.multiply_active === 0) {
        this.selection = this.$refs["multiplySelection"].multipleSelection;
        this.displayImg[0] = this.selection[0];
        this.displayImg[1] = this.selection[1];
        if (this.selection.length !== 2) {
          this.$alert('选择的图片数量不是两张！', '数量错误', {
            confirmButtonText: '确定'
          });
          return
        }

      } else if (this.multiply_active === 1) {
        if (this.multiplyForm.res_name === '') {
          this.$alert('输出图像名称不能为空！', '命名错误', {
            confirmButtonText: '确定'
          });
          return
        }
        this.multiplyForm.res_name = this.utils.calculate_res_name(this.multiplyForm.res_name);
      } else if (this.multiply_active === 2) {
        const axios = require('axios')

        this.multiplyLoad = true;

        await axios.get(
            this.constant.data().BaseUrl + '/basic_func/multiply', {
              params: {
                img_name1: this.selection[0].fileName,
                img_name2: this.selection[1].fileName,
                result_name: this.multiplyForm.res_name
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

        this.multiplyLoad = false;


      } else if (this.multiply_active === 3) {
        this.multiply_active = 0;

        return
      }


      this.multiply_active++;
    },
    async divide_next() {
      let tmp = this.divide_active;
      this.clear_active();
      this.divide_active = tmp;
      if (this.divide_active === 0) {
        this.selection = this.$refs["divideSelection"].multipleSelection;
        this.displayImg[0] = this.selection[0];
        this.displayImg[1] = this.selection[1];
        if (this.selection.length !== 2) {
          this.$alert('选择的图片数量不是两张！', '数量错误', {
            confirmButtonText: '确定'
          });
          return
        }

      } else if (this.divide_active === 1) {
        if (this.divideForm.res_name === '') {
          this.$alert('输出图像名称不能为空！', '命名错误', {
            confirmButtonText: '确定'
          });
          return
        }
        this.divideForm.res_name = this.utils.calculate_res_name(this.divideForm.res_name);
      } else if (this.divide_active === 2) {
        const axios = require('axios')

        this.divideLoad = true;

        await axios.get(
            this.constant.data().BaseUrl + '/basic_func/divide', {
              params: {
                img_name1: this.selection[0].fileName,
                img_name2: this.selection[1].fileName,
                result_name: this.divideForm.res_name
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

        this.divideLoad = false;


      } else if (this.divide_active === 3) {
        this.divide_active = 0;

        return
      }


      this.divide_active++;
    },
    async flip_next() {
      let tmp = this.flip_active;
      this.clear_active();
      this.flip_active = tmp;
      if (this.flip_active === 0) {
        this.selection = this.$refs["flipSelection"].multipleSelection;
        this.displayImg[0] = this.selection[0];
        if (this.selection.length !== 1) {
          this.$alert('选择的图片数量不是一张！', '数量错误', {
            confirmButtonText: '确定'
          });
          return
        }

      } else if (this.flip_active === 1) {
        if (this.flipForm.res_name === '') {
          this.$alert('输出图像名称不能为空！', '命名错误', {
            confirmButtonText: '确定'
          });
          return
        }
        this.flipForm.res_name = this.utils.calculate_res_name(this.flipForm.res_name);
      } else if (this.flip_active === 2) {
        const axios = require('axios')

        this.flipLoad = true;

        await axios.get(
            this.constant.data().BaseUrl + '/basic_func/flip', {
              params: {
                img_name: this.selection[0].fileName,
                result_name: this.flipForm.res_name,
                fli_choi: this.flipForm.fli_choi
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

        this.flipLoad = false;


      } else if (this.flip_active === 3) {
        this.flip_active = 0;

        return
      }


      this.flip_active++;
    },
    async move_next() {
      let tmp = this.move_active;
      this.clear_active();
      this.move_active = tmp;
      if (this.move_active === 0) {
        this.selection = this.$refs["moveSelection"].multipleSelection;
        this.displayImg[0] = this.selection[0];
        if (this.selection.length !== 1) {
          this.$alert('选择的图片数量不是一张！', '数量错误', {
            confirmButtonText: '确定'
          });
          return
        }

      } else if (this.move_active === 1) {
        if ((this.moveForm.res_name === '') || (this.moveForm.move_x === null) || (this.moveForm.move_y === null)) {
          this.$alert('输出图像名称不能为空！<br>坐标轴移动像素值不能为空！', '参数错误', {
            confirmButtonText: '确定',
            dangerouslyUseHTMLString: true
          });
          return
        }
        this.moveForm.move_x = parseInt(this.moveForm.move_x);
        this.moveForm.move_y = parseInt(this.moveForm.move_y);
        if ((!this.utils.isInteger(this.moveForm.move_x)) || (!this.utils.isInteger(this.moveForm.move_y))) {
          this.$alert('坐标轴移动像素值必须为整数！', '参数错误', {
            confirmButtonText: '确定'
          });
          return
        }
        this.moveForm.res_name = this.utils.calculate_res_name(this.moveForm.res_name);
      } else if (this.move_active === 2) {
        const axios = require('axios')

        this.moveLoad = true;

        await axios.get(
            this.constant.data().BaseUrl + '/basic_func/move', {
              params: {
                img_name: this.selection[0].fileName,
                result_name: this.moveForm.res_name,
                move_x: this.moveForm.move_x,
                move_y: this.moveForm.move_y
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

        this.moveLoad = false;


      } else if (this.move_active === 3) {
        this.move_active = 0;

        return
      }


      this.move_active++;
    },
    async rotate_next() {
      let tmp = this.rotate_active;
      this.clear_active();
      this.rotate_active = tmp;
      if (this.rotate_active === 0) {
        this.selection = this.$refs["rotateSelection"].multipleSelection;
        this.displayImg[0] = this.selection[0];
        if (this.selection.length !== 1) {
          this.$alert('选择的图片数量不是一张！', '数量错误', {
            confirmButtonText: '确定'
          });
          return
        }

      } else if (this.rotate_active === 1) {
        if ((this.rotateForm.res_name === '') || (this.rotateForm.angle === null)) {
          this.$alert('输出图像名称不能为空！<br>角度不能为空！', '参数错误', {
            confirmButtonText: '确定',
            dangerouslyUseHTMLString: true
          });
          return
        }
        this.rotateForm.angle = parseInt(this.rotateForm.angle);
        if (!this.utils.isInteger(this.rotateForm.angle)) {
          this.$alert('角度值必须为数字！', '参数错误', {
            confirmButtonText: '确定'
          });
          return
        }
        this.rotateForm.res_name = this.utils.calculate_res_name(this.rotateForm.res_name);
      } else if (this.rotate_active === 2) {
        const axios = require('axios')

        this.rotateLoad = true;

        await axios.get(
            this.constant.data().BaseUrl + '/basic_func/rotate', {
              params: {
                img_name: this.selection[0].fileName,
                result_name: this.rotateForm.res_name,
                angle: this.rotateForm.angle
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

        this.rotateLoad = false;


      } else if (this.rotate_active === 3) {
        this.rotate_active = 0;

        return
      }


      this.rotate_active++;
    },
    async resize_next() {
      let tmp = this.resize_active;
      this.clear_active();
      this.resize_active = tmp;
      if (this.resize_active === 0) {
        this.selection = this.$refs["resizeSelection"].multipleSelection;
        this.displayImg[0] = this.selection[0];
        if (this.selection.length !== 1) {
          this.$alert('选择的图片数量不是一张！', '数量错误', {
            confirmButtonText: '确定'
          });
          return
        }

      } else if (this.resize_active === 1) {
        if ((this.resizeForm.res_name === '') || (this.resizeForm.size_x === null) || (this.resizeForm.size_y === null)) {
          this.$alert('输出图像名称不能为空！<br>坐标轴放缩倍数不能为空！', '参数错误', {
            confirmButtonText: '确定',
            dangerouslyUseHTMLString: true
          });
          return
        }
        this.resizeForm.size_x = parseFloat(this.resizeForm.size_x);
        this.resizeForm.size_y = parseFloat(this.resizeForm.size_y);
        if ((!this.utils.isFloat(this.resizeForm.size_x)) || (!this.utils.isFloat(this.resizeForm.size_y))) {
          this.$alert('坐标轴放缩倍数必须为数字！', '参数错误', {
            confirmButtonText: '确定'
          });
          return
        }
        if ((this.resizeForm.size_x) <= 0 || (this.resizeForm.size_y) <= 0) {
          this.$alert('坐标轴放缩倍数必须为正实数！', '参数错误', {
            confirmButtonText: '确定'
          });
          return
        }
        this.resizeForm.res_name = this.utils.calculate_res_name(this.resizeForm.res_name);
      } else if (this.resize_active === 2) {
        const axios = require('axios')

        this.resizeLoad = true;

        await axios.get(
            this.constant.data().BaseUrl + '/basic_func/resize', {
              params: {
                img_name: this.selection[0].fileName,
                result_name: this.resizeForm.res_name,
                size_x: this.resizeForm.size_x,
                size_y: this.resizeForm.size_y
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

        this.resizeLoad = false;


      } else if (this.resize_active === 3) {
        this.resize_active = 0;

        return
      }


      this.resize_active++;
    }
  }
}
</script>

<style scoped>

</style>
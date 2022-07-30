import os
import numpy as np
from tqdm import tqdm
import tensorflow as tf
from apps.service.model import NeuralStyleTransferModel
from apps.service import settings
from apps.service import utils


def _compute_content_loss(noise_features, target_features):
    """
    计算指定层上两个特征之间的内容loss
    :param noise_features: 噪声图片在指定层的特征
    :param target_features: 内容图片在指定层的特征
    """
    content_loss = tf.reduce_sum(tf.square(noise_features - target_features))
    # 计算系数
    x = 2. * M * N
    content_loss = content_loss / x
    return content_loss


def compute_content_loss(noise_content_features, target_content_features):
    """
    计算并当前图片的内容loss
    :param noise_content_features: 噪声图片的内容特征
    """
    # 初始化内容损失
    content_losses = []
    # 加权计算内容损失
    for (noise_feature, factor), (target_feature, _) in zip(noise_content_features, target_content_features):
        layer_content_loss = _compute_content_loss(noise_feature, target_feature)
        content_losses.append(layer_content_loss * factor)
    return tf.reduce_sum(content_losses)


def gram_matrix(feature):
    """
    计算给定特征的格拉姆矩阵
    """
    # 先交换维度，把channel维度提到最前面
    x = tf.transpose(feature, perm=[2, 0, 1])
    # reshape，压缩成2d
    x = tf.reshape(x, (x.shape[0], -1))
    # 计算x和x的逆的乘积
    return x @ tf.transpose(x)


def _compute_style_loss(noise_feature, target_feature):
    """
    计算指定层上两个特征之间的风格loss
    :param noise_feature: 噪声图片在指定层的特征
    :param target_feature: 风格图片在指定层的特征
    """
    noise_gram_matrix = gram_matrix(noise_feature)
    style_gram_matrix = gram_matrix(target_feature)
    style_loss = tf.reduce_sum(tf.square(noise_gram_matrix - style_gram_matrix))
    # 计算系数
    x = 4. * (M ** 2) * (N ** 2)
    return style_loss / x


def compute_style_loss(noise_style_features, target_style_features):
    """
    计算并返回图片的风格loss
    :param noise_style_features: 噪声图片的风格特征
    """
    style_losses = []
    for (noise_feature, factor), (target_feature, _) in zip(noise_style_features, target_style_features):
        layer_style_loss = _compute_style_loss(noise_feature, target_feature)
        style_losses.append(layer_style_loss * factor)
    return tf.reduce_sum(style_losses)


def total_loss(noise_features, target_content_features, target_style_features):
    """
    计算总损失
    :param noise_features: 噪声图片特征数据
    """
    content_loss = compute_content_loss(noise_features['content'], target_content_features)
    style_loss = compute_style_loss(noise_features['style'], target_style_features)
    return content_loss * settings.CONTENT_LOSS_FACTOR + style_loss * settings.STYLE_LOSS_FACTOR



# 创建模型
model = NeuralStyleTransferModel()

M = settings.WIDTH * settings.HEIGHT
N = 3


# 使用tf.function加速训练
@tf.function
def train_one_step(optimizer, noise_image, target_content_features, target_style_features):
    """
    一次迭代过程
    """
    # 求loss
    with tf.GradientTape() as tape:
        noise_outputs = model(noise_image)
        loss = total_loss(noise_outputs, target_content_features, target_style_features)
    # 求梯度
    grad = tape.gradient(loss, noise_image)
    # 梯度下降，更新噪声图片
    optimizer.apply_gradients([(grad, noise_image)])
    return loss


def style_transfer(img_style_path, img_content_path, result_path, epoch, per_epoch, learn_rate):
    learn_rate = learn_rate or settings.LEARNING_RATE
    
    # 使用Adma优化器
    optimizer = tf.keras.optimizers.Adam(learning_rate=learn_rate)
    
    # 加载内容图片
    content_image = utils.load_images(img_content_path)
    # 风格图片
    style_image = utils.load_images(img_style_path)
    
    # 计算出目标内容图片的内容特征备用
    target_content_features = model([content_image, ])['content']
    # 计算目标风格图片的风格特征
    target_style_features = model([style_image, ])['style']
        
    # 基于内容图片随机生成一张噪声图片
    noise_image = tf.Variable((content_image + np.random.uniform(-0.2, 0.2, (1, settings.HEIGHT, settings.WIDTH, 3))) / 2)

    epoch = epoch or settings.EPOCHS
    per_epoch = per_epoch or settings.STEPS_PER_EPOCH

    # 共训练epoch个epochs
    for epo in range(epoch):
        # 使用tqdm提示训练进度
        with tqdm(total=per_epoch, desc='Epoch {}/{}'.format(epo + 1, epoch)) as pbar:
            # 每个epoch训练per_epoch次
            for step in range(per_epoch):
                _loss = train_one_step(optimizer, noise_image, target_content_features, target_style_features)
                pbar.set_postfix({'loss': '%.4f' % float(_loss)})
                pbar.update(1)
            # 每个epoch保存一次图片
    print(222)
    utils.save_image(noise_image, result_path)

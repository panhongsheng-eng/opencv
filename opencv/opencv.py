#导入Opencv库
import cv2 as cv

# 读取照片
img = cv.imread('rlsb.jpg')
# 显示图片
cv.imshow('read_img',img)
#等待键盘输入 单位是毫秒 传入0 是无限等待
cv.waitKey(3000)
#释放当前内存 由于opencv底层是C++编写的
cv.destroyAllWindows()



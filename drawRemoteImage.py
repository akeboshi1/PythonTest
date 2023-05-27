import matplotlib.pyplot as plt
import imageio.v2 as imageio
url = "https://p1-tt.byteimg.com/origin/pgc-image/fe41801208fa40d394352e0df71e9202?from=pc"

# 此方法读取的图像和OpenCV一样，都是numpy.ndarray对象，只不过通道相反
# img[:,:,::-1] 转化为OpenCV图像格式
img = imageio.imread(url)
plt.imshow(img)
plt.show()
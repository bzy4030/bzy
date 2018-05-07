import fac_compare as fc
fac_compare = fc.face_recognition()   # 创建对象
fac_compare.inputPerson(name='jobs', img_path='\\faces\\left2.png')  # name中写第一个人名字，img_name为图片名字，注意要放在faces文件夹中
vector = fac_compare.create128DVectorSpace()  # 提取128维向量，是dlib.vector类的对象
person_data1 = fc.savePersonData(fac_compare, vector)   # 将提取出的数据保存到data文件夹，为便于操作返回numpy数组，内容还是一样的

# 导入第二张图片，并提取特征向量
fac_compare.inputPerson(name='jobs2', img_path='\\faces\\right2.png')
vector = fac_compare.create128DVectorSpace()  # 提取128维向量，是dlib.vector类的对象
person_data2 = fc.savePersonData(fac_compare, vector)

# 计算欧式距离，判断是否是同一个人
fc.comparePersonData(person_data1, person_data2)
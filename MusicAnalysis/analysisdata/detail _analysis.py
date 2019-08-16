from MusicAnalysis.analysisdata import Data_Collection


class DataAnalysis(object):

    def __init__(self):
        self.Cdata = Data_Collection.DataCollection()

    def ShowData(self):
        data = self.Cdata.collection()
        # print(data)

    # 线性回归
    def linear_regression(self):
        data = self.Cdata.collection()

    # 逻辑回归
    def logic_regression(self):
        data = self.Cdata.collection()

    # 神经网络
    def neural_network(self):
        data = self.Cdata.collection()

    # 主成分分析pca
    def PCA(self):
        data = self.Cdata.collection()

    # 支持向量机
    def SVM(self):
        data = self.Cdata.collection()


if __name__ == "__main__":

    detail = DataAnalysis()
    detail.ShowData()

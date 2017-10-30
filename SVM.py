import numpy as np #For handling array data
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')
#Self-exlainatory
#Take random data to keep going
data = {-1:np.array([[2,4],[3,6],[5,9]]),1:np.array([[5,2],[12,14],[2,9]])}
#OOP begins
class SVM:
    def _init_(self,visualization=True):
        self.visualization = visualization
        self.colors = {1:'r',-1:'b'}
        if self.visualization:
            self.fig = plt.figure()
            self.ax = self.fig.add_subplot(1,1,1)
    #Training our model
    def fit(self,data):
        self.data = data
        #{ ||W||:[W,b] }
        opt_dict = {}
        transforms = [[1,1],[-1,1],[-1,-1],[1,-1]]
        all_data = []
        for yi in self.data:
            for featureset in self.data[yi]:
                for feature in featureset:
                    all_data.append(feature)
        self.max_feature_value = max(all_data)
        self.min_feature_value = min(all_data)
        all_data = None
        step_size = [self.max_feature_value*0.1,self.max_feature_value*0.01,self.max_feature_value*0.001,]
        b_range_multiple = 5
        b_multiple = 5
        latest_optimum = self.max_feature_value*10
        for steps in step_size:
            w = np.array([latest_optimum,latest_optimum])
            optimized = False
            while not optimized:
                pass
        
    def predict(self,features):
        classify = np.sign(np.dot(np.array(features),self.w)+self.b) #Sign of w.x+b
        return classify

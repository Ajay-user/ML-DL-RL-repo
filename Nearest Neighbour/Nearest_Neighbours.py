
import numpy as np

class NearestNeighbours:

    def __init__(self, images, labels, norm='l1'):
        self.train_images = images.reshape(images.shape[0],-1)
        self.train_labels = labels
        self.norm=norm.lower()
    
    def distance_measure(self, train, test, i):
        if self.norm == 'l2':
            return np.sum(np.sqrt( np.square( train-test[i,:] )), axis=1)
        else:
            return np.sum(np.abs(train - test[i,:]), axis=1)


    def __call__(self, images):
        num_images = images.shape[0]
        test_images = images.reshape(num_images,-1)
        preds = np.zeros(num_images, dtype=np.int32)

        # find nearest training image for each of the test-images
        # using L1-distance (sum of absolute differences)
        # or     
        # using L2-distance (sum of squared differences)
        for i in range(num_images):
            distance = self.distance_measure(self.train_images, test_images, i)
            least_dist_id = np.argmin(distance)
            preds[i]=self.train_labels[least_dist_id]
        
        return preds

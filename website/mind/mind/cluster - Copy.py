import numpy as np
from sklearn.cluster import KMeans
from sklearn.cluster import DBSCAN
from sklearn import metrics
from sklearn import datasets
from sklearn.datasets.samples_generator import make_blobs
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from param import *
class Cluster:
	pass

class MyKMeans(Cluster):
    name = Alias(['kmeans','cluster'])
    n_clusters = Numeric(['into clusters','into these types','into'])
    std_dev = Numeric(['standard deviation','sd','std dev'])

    def execute(self,data_source):
        ##############################################################################
        # Import Sabthok Data
        # import pymysql

        # conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='', db='whispers_sabthok')
        # cur = conn.cursor()

        # cur.execute("SELECT id FROM customers")
        # totUsers = 0
        # for row in cur:
        #   totUsers += 1

        # cur.execute("SELECT customer_id,price FROM orders")


        # X = np.zeros((totUsers,3))
        # for row in cur:
        #    X[row[0]-1,0] +=1
        #    X[row[0]-1,1] +=row[1]

        # X = StandardScaler().fit_transform(X)
        ##############################################################################

        # centers = [[1, 1], [-1, -1], [1, -1]]
        # iris = datasets.load_iris()
        # X = iris.data
        # np.savetxt("data_cluster3d.csv", X, delimiter=",")
        # print(X)

        X = np.loadtxt(open(data_source,"rb"),delimiter=",")#,skiprows=1)



        estimators = {'k_means_iris_3': KMeans(n_clusters=self.n_clusters.get())}

        fignum = 1
        for name, est in estimators.items():
            fig = plt.figure(fignum)
            plt.clf()
            ax = Axes3D(fig, rect=[0, 0, .95, 1], elev=48, azim=134)

            plt.cla()
            est.fit(X)
            labels = est.labels_

            ax.scatter(X[:, 2], X[:, 0], X[:, 1], c=labels.astype(np.float))

            ax.w_xaxis.set_ticklabels([])
            ax.w_yaxis.set_ticklabels([])
            ax.w_zaxis.set_ticklabels([])
            ax.set_xlabel('X')
            ax.set_ylabel('Y')
            ax.set_zlabel('Z')
            fignum = fignum + 1

        plt.show()

class MyDBSCAN(Cluster):
    name = Alias(['kmeans','cluster'])

    def execute(self,data_source):
        ##############################################################################
        # Import Sabthok Data
        # import pymysql

        # conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='', db='whispers_sabthok')
        # cur = conn.cursor()

        # cur.execute("SELECT id FROM customers")
        # totUsers = 0
        # for row in cur:
        #   totUsers += 1

        # cur.execute("SELECT customer_id,price FROM orders")


        # X = np.zeros((totUsers,2))
        # for row in cur:
        #    X[row[0]-1,0] +=1
        #    X[row[0]-1,1] +=row[1]

        # X = StandardScaler().fit_transform(X)
        ##############################################################################

        ##############################################################################
        # Generate sample data
        # centers = [[1, 1], [-1, -1], [1, -1],[-1, 1]]
        # X, labels_true = make_blobs(n_samples=750, centers=centers, cluster_std=0.25,
        #                             random_state=0)

        # np.savetxt("data_cluster2d.csv", X, delimiter=",")


        ##############################################################################

        X = np.loadtxt(open(data_source,"rb"),delimiter=",")#,skiprows=1)


        X = StandardScaler().fit_transform(X)
        # Compute DBSCAN
        db = DBSCAN().fit(X)
        core_samples_mask = np.zeros_like(db.labels_, dtype=bool)
        core_samples_mask[db.core_sample_indices_] = True
        labels = db.labels_

        # Number of clusters in labels, ignoring noise if present.
        n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)

        print('Estimated number of clusters: %d' % n_clusters_)
        # print("Homogeneity: %0.3f" % metrics.homogeneity_score(labels_true, labels))
        # print("Completeness: %0.3f" % metrics.completeness_score(labels_true, labels))
        # print("V-measure: %0.3f" % metrics.v_measure_score(labels_true, labels))
        # print("Adjusted Rand Index: %0.3f"
        #       % metrics.adjusted_rand_score(labels_true, labels))
        # print("Adjusted Mutual Information: %0.3f"
        #       % metrics.adjusted_mutual_info_score(labels_true, labels))
        # print("Silhouette Coefficient: %0.3f"
        #       % metrics.silhouette_score(X, labels))

        ##############################################################################
        # Plot result
        import matplotlib.pyplot as plt

        # Black removed and is used for noise instead.
        unique_labels = set(labels)
        colors = plt.cm.Spectral(np.linspace(0, 1, len(unique_labels)))
        for k, col in zip(unique_labels, colors):
            if k == -1:
                # Black used for noise.
                col = 'k'

            class_member_mask = (labels == k)

            xy = X[class_member_mask & core_samples_mask]
            plt.plot(xy[:, 0], xy[:, 1], 'o', markerfacecolor=col,
                     markeredgecolor='k', markersize=14)

            xy = X[class_member_mask & ~core_samples_mask]
            plt.plot(xy[:, 0], xy[:, 1], 'o', markerfacecolor=col,
                     markeredgecolor='k', markersize=6)

        plt.title('Estimated number of clusters: %d' % n_clusters_)
        plt.show()
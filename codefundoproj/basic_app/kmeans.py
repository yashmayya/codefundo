from sklearn.cluster import KMeans

def cluster_funct(input_array, k):
    kmeans = KMeans(n_clusters=k, random_state=0).fit(input_array)
    output_array=kmeans.cluster_centers_
    return output_array

# input_array = [[8.3,7], [-3,9], [6,5], [4,-2], [3,-9]]
# outp = cluster_funct(input_array, 3)
# print(outp)

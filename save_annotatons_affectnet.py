import pickle
from tqdm import tqdm

save_dir = './result'
data_pickle = pickle.load(open('./result/data_affectnet.pkl', 'rb'))
for data_type in ['train', 'val']:
    data = data_pickle[data_type]
    for sample in tqdm(data):
        with open(save_dir + '\\' + data_type + '_label' + '.txt', 'a') as f:
            f.write(sample.image_path + ' ' + str(sample.expression) + ' \n')

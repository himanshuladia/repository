import librosa
import os
import pickle
import pandas as pd
import numpy as np
from tqdm import tqdm
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier

def predict(folderpath):
	names = []
	paths = []
	audios = os.listdir(folderpath)
	for audio in audios:
		names.append(audio.split('.')[0])
		paths.append(os.path.join(folderpath, audio))

	ref = pd.DataFrame(names, columns=['File name'])
	ref = pd.concat([ref, pd.DataFrame(paths, columns=['path'])], axis=1)

	df = pd.DataFrame(columns=['feature'])
	count = 0
	for path in tqdm(ref['path']):
		X, sample_rate = librosa.load(path, res_type='kaiser_fast', duration=2.5, sr=44100)
		mfccs = np.mean(librosa.feature.mfcc(y=X, sr=np.array(sample_rate), n_mfcc=13), axis=0)
		df.loc[count] = [mfccs]
		count += 1

	df = pd.concat([ref, pd.DataFrame(df['feature'].values.tolist())], axis=1)
	df = df.fillna(0)

	X = np.array(df.drop(['File name', 'path'], axis=1))

	with open('model/mean.pkl', 'rb') as f:
		mean = pickle.load(f)

	with open('model/std.pkl', 'rb') as f:
		std = pickle.load(f)

	with open('model/model.sav', 'rb') as f:
		model = pickle.load(f)

	with open('model/labels', 'rb') as f:
		lb = pickle.load(f)

	X = (X - mean)/std
	prediction = model.predict(X)
	print(prediction)
	prediction = lb.inverse_transform(prediction)

	result = pd.concat([df['File name'], pd.DataFrame(prediction, columns=['prediction'])], axis=1)

	result.to_csv('output.csv', index=False)
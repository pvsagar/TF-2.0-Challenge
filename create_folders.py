import os
directory = './traintestdata'
os.mkdir(directory)
#create the train,validation and test folders
train_folder = os.path.join(directory, 'train')
os.mkdir(train_folder)
test_folder = os.path.join(directory, 'test')
os.mkdir(test_folder)
val_folder = os.path.join(directory, 'validation')
os.mkdir(val_folder)

# Make new folders inside train
os.mkdir(os.path.join(train_folder, 'nv'))
os.mkdir(os.path.join(train_folder, 'mel'))
os.mkdir(os.path.join(train_folder, 'bkl'))
os.mkdir(os.path.join(train_folder, 'bcc'))
os.mkdir(os.path.join(train_folder, 'akiec'))
os.mkdir(os.path.join(train_folder, 'vasc'))
os.mkdir(os.path.join(train_folder, 'df'))

# Make new folders inside test
os.mkdir(os.path.join(test_folder, 'nv'))
os.mkdir(os.path.join(test_folder, 'mel'))
os.mkdir(os.path.join(test_folder, 'bkl'))
os.mkdir(os.path.join(test_folder, 'bcc'))
os.mkdir(os.path.join(test_folder, 'akiec'))
os.mkdir(os.path.join(test_folder, 'vasc'))
os.mkdir(os.path.join(test_folder, 'df'))

# Make new folders inside validation
os.mkdir(os.path.join(val_folder, 'nv'))
os.mkdir(os.path.join(val_folder, 'mel'))
os.mkdir(os.path.join(val_folder, 'bkl'))
os.mkdir(os.path.join(val_folder, 'bcc'))
os.mkdir(os.path.join(val_folder, 'akiec'))
os.mkdir(os.path.join(val_folder, 'vasc'))
os.mkdir(os.path.join(val_folder, 'df'))
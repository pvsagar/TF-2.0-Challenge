import os
import xlrd
from PIL import Image
import shutil
#Getting data from metadata file
metadata='HAM10000_metadata.xls'
metadata=xlrd.open_workbook(metadata) 
data=metadata.sheet_by_index(0)
akiec,bcc,bkl,df,mel,vasc,nv=[],[],[],[],[],[],[]

cancer_category=['akiec','bcc','bkl','df','mel','vasc','nv']
for x in range(10015):
    cancer_type=data.cell_value(x, 2)
    image_id=data.cell_value(x,1)
    if(cancer_type==cancer_category[0]):
        akiec.append(image_id)
    elif(cancer_type==cancer_category[1]):
        bcc.append(image_id)
    elif(cancer_type==cancer_category[2]):
        bkl.append(image_id)
    elif(cancer_type==cancer_category[3]):
        df.append(image_id)
    elif(cancer_type==cancer_category[4]):
        mel.append(image_id)
    elif(cancer_type==cancer_category[5]):
        vasc.append(image_id)
    elif(cancer_type==cancer_category[6]):
        nv.append(image_id)
nv=nv[0:1100]
print('Classification of skin cancer images:','\n akiec:',len(akiec),'\n bcc:',len(bcc),'\n bkl:',len(bkl),'\n df',len(df),'\n mel:',len(mel),'\n nv:',len(nv),'\n vasc:',len(vasc))

category_list=[akiec,bcc,bkl,df,mel,vasc,nv]
#Get training data
imagepath='./traintestdata/train'
imagelocation='./images'
counter=0
for x in category_list:
    for y in x:
        image=Image.open(imagelocation+'/'+y+'.jpg')
        image.save(imagepath+'/'+cancer_category[counter]+'/'+y+'.jpg')
    counter=counter+1
    
#Getting images for validation by moving from train folder location
source_path='./traintestdata/train'
destination_path='./traintestdata/test'
counter2=0
for x in category_list:
    for p,q in zip(x, range(int(0.2*len(x)))):
        shutil.move(source_path+'/'+cancer_category[counter2]+'/'+p+'.jpg',destination_path+'/'+cancer_category[counter2])
    counter2=counter2+1

#Getting images for validation
source_val='./traintestdata/train'

destination_val='./traintestdata/validation'
akiecdir=os.listdir("./traintestdata/train/akiec")
meldir=os.listdir("./traintestdata/train/mel")
dfdir=os.listdir("./traintestdata/train/df")
vascdir=os.listdir("./traintestdata/train/vasc")
nvdir=os.listdir("./traintestdata/train/nv")
bkldir=os.listdir("./traintestdata/train/bkl")
bccdir=os.listdir("./traintestdata/train/bcc")
directory=[akiecdir,bccdir,bkldir,dfdir,meldir,vascdir,nvdir]
counter3=0
for x in category_list:
    for i,j in zip(directory[counter3], range(int(0.2*len(x)))):
        shutil.copy(source_val+'/'+cancer_category[counter3]+'/'+i,destination_val+'/'+cancer_category[counter3])
    counter3=counter3+1

  
datapaths=['./traintestdata/train','./traintestdata/validation','./traintestdata/test']
for x in datapaths:
    name=x.split("/")
    print('\nImages for',name[2])
    print('akiec:',len(os.listdir(x+'/'+'akiec')))
    print('bcc:',len(os.listdir(x+'/'+'bcc')))
    print('bkl:',len(os.listdir(x+'/'+'bkl')))
    print('df:',len(os.listdir(x+'/'+'df')))
    print('mel:',len(os.listdir(x+'/'+'mel')))
    print('nv:',len(os.listdir(x+'/'+'nv')))
    print('vasc:',len(os.listdir(x+'/'+'vasc')))

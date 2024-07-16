import requests, os,re 
os.chdir(r"D:\projects\mrg_data_download")

hdflinks = open('download.txt').readlines()

#clean links for breakline characters
for link in hdflinks: 
    index = hdflinks.index(link)
    link = re.sub('\n','',link)
    hdflinks[index] = link

print(hdflinks)

for link in hdflinks:
    print(link)
    with requests.Session() as session:
        req = session.request('get', link)
        r = session.get(req.url, auth=('tekson', '@mZY6NWrcrk#F7w'))
        imagename = link.split('.')
        
        with open('./HDF5/'+imagename[9][:14]+'.HDF5', 'wb') as f:
            f.write(r.content)
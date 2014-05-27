import sys, os, numpy as np

directory = str(sys.argv[1])
total_list = os.listdir(directory)
filenames = sorted([directory+'/'+element for element in total_list if 'result' in element])


export = open(directory+'/results.csv', 'w')
head = 'Id,x_center,y_center,z_center,c_bdmv,c_bdmv_max,c_bdmv_min,c_bdmw,c_bdmw_max,c_bdmw_min,r_vir_bdmv,r_vir_bdmw,n_vir_bdmv,n_vir_bdmw,n_tot'

with export as outfile:
    for fname in filenames:
        with open(fname) as infile:
            for line in infile:
                outfile.write(line)   

data = np.loadtxt(directory+'/results.csv',delimiter=',')
data = data[data[:,0].argsort()]

np.savetxt(directory+'/results.csv',data,fmt='%d,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%d,%d,%d',header=head)
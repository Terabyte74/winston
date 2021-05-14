import os
#
print("getting script from 'requirements_installer_script.txt'... ", end='')
try:
    temp = open("requirements_installer_script.txt", 'r')
    script = temp.read()
    temp.close()
    print("DONE")
except:
    print("FAILED")
#
print("creating 'happy.bat' file... ", end='')
try:
    temp = open("happy.bat", 'w')
    temp.write(script)
    temp.close()
    print("DONE")
except:
    print("FAILED")
#
print("executing 'happy.bat' file... ", end='')
try:
    os.system("happy.bat")
    print("DONE")
except:
    print("FAILED")
#
print("deleting 'happy.bat' file... ", end='')
try:
    os.unlink("happy.bat")
    print("DONE")
except:
    print("FAILED")
#
print("\n[All requirements were succesfully installed!]\n")
#
print("creating '[main_env]winston_link.bat' file... ",end='')
try:
    path = os.getcwd()
    path = (path.replace('wizard_for_dummies', ''))
    os.chdir(path)
    temp = open('[main_env]winston_link.bat', 'w')
    temp.write("cd "+path+'\n'+
               "start python run.py \n"+
               "exit")
    temp.close()
    print("DONE")
except:
    print("FAILED")
#

    
input('ALL FINISHED (:')
    

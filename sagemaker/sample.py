import shutil
import tarfile

shutil.copy2("models\\model.pth", "sagemaker\\code\\model.pth")
with tarfile.open("model.tar.gz", "w:gz") as tar:
    tar.add("sagemaker\\code")

try:
    shutil.move("model.tar.gz", ".")
except:
    print('error')

    shutil.rmtree("sagemaker\\code")
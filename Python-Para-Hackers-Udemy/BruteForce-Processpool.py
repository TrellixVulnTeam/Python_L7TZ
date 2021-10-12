from multiprocessing.dummy import Pool as ThreadPool
from tqdm import tqdm
import pikepdf
import time

passwd = list(range(0,999))
loop = tqdm(total=len(passwd), position=0, leave=False)

def test_pdf(pwd):
    try:
        pikepdf.Pdf.open('doc.pdf', password=str(pwd).zfill(3))
        print('Senha: '+ str(pwd).zfill(3))
        print('Tempo: '+ str(time.time() - start_time))
        exit()
    except:
        loop.update(1)
        pass


start_time = time.time()
pool = ThreadPool(4)
results = pool.map(test_pdf, passwd)

pool.close()
pool.join()



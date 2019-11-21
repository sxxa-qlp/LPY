from multiprocessing import Pool
import os,random,time

def long_time_task(name):
	print('run task %s (%s)...'%(name,os.getpip))
	start = time.time()
	time.sleep(random.random()*3)
	end = time.time()
	print('Task %s runs %0.2f seconds.'%(neme,(end - start)))

if __name__=='__main__':
	print('parent process %s.'%os.getpid())
	p = Pool(9)
	for i in range(10):
		p.apply_async(long_time_task,args= (i,))
	print('waiting for all subprocessing done...')
	p.close()
	p.join()
	print('all subprocessing done')
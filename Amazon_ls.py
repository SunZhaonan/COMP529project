#!/usr/bin/env python
# -*- coding: utf-8 -*-
# filename: pexpect_test.py
'''
Created on 2012-03-31
 
@author: qvb3d
'''
import pexpect
import time
if __name__ == '__main__':
	user = 'ec2-user'
	ip = 'ec2-204-236-198-67.compute-1.amazonaws.com'
	command = 'python Print.py 2'
	child = pexpect.spawn('ssh -l %s -i Zhaonan.pem %s %s' % (user,ip,command))

	fout = open('mylog.txt','w')
	fout.write("-----------Log File------------")
	child.logfile =fout

#	child.expect(pexpect.EOF)
#	print(child.before)

#	while True:
#		index = child.expect(["\n",pexpect.EOF,pexpect.TIMEOUT]) 
#		if index == 0: 
#			log = child.before
#			print log
#		elif index == 1:
#			break
#		elif index == 2:
#			break        #continue to wait 
#	child.logfile_send = sys.stdout
	child.expect(pexpect.EOF)
	fout.close()
	pass

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# filename: pexpect_test.py
'''
Created on 2012-10-03
 
@author: Zhaonan
'''

import pexpect
import getpass

if __name__ == '__main__':
	user = 'zs6'#raw_input('user name:')
	ip = 'ssh.clear.rice.edu'
	command = '/bin/ls'
	mypassword =  getpass.getpass('your password:')
	child = pexpect.spawn('ssh -l %s %s %s' % (user,ip,command))
	child.expect('password: ')
	child.sendline (mypassword)
#	child.sendline('/bin/ls')     # Give control of the child to the user.
	child.expect(pexpect.EOF)
	print(child.before)
	pass

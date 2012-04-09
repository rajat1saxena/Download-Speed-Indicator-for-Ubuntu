#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.

#    Certain parts of the code are inpired by syspeek indicator's code <https://code.launchpad.net/~vicox/syspeek/trunk>.
#    So this code is based on the work of Georg Schmidl

import time
import threading
import gtk
import gobject

class net:
	last_rec = 0
	last_tran = 0

	REC = 1
	TRAN = 9

	def check(self):
		rec = 0
		tran = 0

		f = open('/proc/net/dev','r')
		lines = f.readlines()
		f.close()
		
		for line in lines:
			row = line.split()
			if row[0]=="wlan0:" or row[0]=="ppp0:":
				rec = int(row[self.REC])
				tran = int(row[self.TRAN])
	
		diff_rec = (rec - self.last_rec)/1024.0
		diff_tran = (tran - self.last_tran)/1024.0

		self.last_rec = rec
		self.last_tran = tran
	
		print("Down: "+"%.2f"%diff_rec+" Kbps")
		
		return "Down: "+"%.2f"%diff_rec+" Kbps"

class net_thread(threading.Thread):
	def __init__(self,indi):
		threading.Thread.__init__(self)
		self.indi = indi

	def update_ind(self,rec_val):
		self.indi.set_label(rec_val)
				

	def run(self):
		obj = net()
		while(True):
			rec_val=obj.check()
			gobject.idle_add(self.update_ind,rec_val)
			time.sleep(1)

if __name__ == "__main__":
	net_thread().setDaemon(True)
	net_thread().start()

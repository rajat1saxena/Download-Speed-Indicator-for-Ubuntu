#
#    Copywrite (C) 2012 Rajat Saxena <rajat.saxena.work@gmail.com>
#
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


import pygtk
pygtk.require('2.0')
import gtk
import appindicator
import net
import threading
import gobject
import time
import os

gobject.threads_init()

class app:
	def invoke_sysmon(self):
		os.spawnlp(os.P_NOWAIT,'gnome-system-monitor','gnome-system-monitor')
		os.wait3(os.WNOHANG)

	def close_prog(self):
		print "Bye dear!"
		packets.stop()
		gtk.main_quit()

	ind = appindicator.Indicator("netspeed","network-receive",appindicator.CATEGORY_APPLICATION_STATUS)
	ind.set_status(appindicator.STATUS_ACTIVE)
	#ind.set_label("Down:")

	#create a menu
	menu = gtk.Menu()

	#create a menu item
	item = gtk.MenuItem("System Monitor")
	item.connect('activate',invoke_sysmon)

	item2 = gtk.MenuItem("Exit")
	item2.connect('activate',close_prog)

	menu.append(item)
	menu.append(item2)

	item.show()
	item2.show()

	ind.set_menu(menu)

	global packets
	packets = net.net_thread(ind)

	packets.start()



if __name__ == "__main__":


	app = app()

	gtk.main()

from PriorityPeople import PriorityPeople
import MySQLdb
import pymongo

class Dataupdate:
	def __init__(self):
		self.conn_mon = pymongo.Connection(host='10.1.1.111',port=12345)
		self.conn_my = MySQLdb.connect(host='arnetminer.org',user='root',passwd='eserver4009',db='arnet_db')
		self.db_mon = self.conn_mon['arnet_db']
		self.table = self.db_mon['pubication_test']
		self.cursor = self.conn_my.cursor()
	def update(self,aid):
		try:
		  papers = self.table.find_one({'_id':aid}).get('paper')
		except:
			pass
		else:

			for paper in papers:
				if 'pid_in_mysql' in paper:
					citation = paper['citation']
					pid = paper['pid_in_mysql']
					self.cursor.execute('select ncitation from publication where id = %d'%pid)
					ocitation = self.cursor.fetchall()
					try:
						ocitation = ocitation[0][0]
					except:
						ocitation = -1
					if ocitation < citation:
						self.cursor.execute('update publication SET ncitation = %d where id = %d'%(citation,pid))
					else:
						continue
				else:
					continue
	def update_prior_people(self,pointer):
		aid = PriorityPeople[pointer]
		self.update(aid)


if __name__ == "__main__":
	for i in range(0,len(PriorityPeople)):
		a.update_prior_people(i)




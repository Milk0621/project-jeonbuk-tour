import pymysql
import sys
sys.path.append(".")
from vo.similar_vo import SimilerVO

class SimilarDAO:
    def __init__(self):
        self.conn = pymysql.connect(
            host="158.247.211.92",
            port=3306,
            user="milk",
            password="0621",
            database="hotplace"
        )
        self.cursor = self.conn.cursor()
    
    #유사도 조회    
    def select_similar(self, no):
        sql = "select * from place inner join similar on place.contentid = similar.no inner join place p on p.contentid = similar.sno where place.contentid = %s order by similar desc"
        self.cursor.execute(sql, (no))
        similars = []
        for similar in similars:
            
            
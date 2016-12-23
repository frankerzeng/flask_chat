# coding=utf-8
import leancloud


class Dao:
    table_obj = ''
    query_obj = ''

    def __init__(self, table):
        leancloud.init(app_id="0B3RSiGKtdTgvI71YjOU1vH1-gzGzoHsz",
                       app_key="S6OYjdngNuJXtVbjRe6pHmIn",
                       master_key="6M2oJ078ShPrA4suu5XV7n7D")
        table_object = leancloud.Object.extend(table)
        self.table_obj = table_object()
        self.query_obj = leancloud.Query

    def add(self, data):
        print '--------新增数据--------'
        print data

        for key in data:
            self.table_obj.set(key, data[key])
        rst = self.table_obj.save()
        print rst

    def query(self, sql):
        print '--------sql语句--------'
        print sql
        rst = self.query_obj.do_cloud_query(sql)
        print rst
        return rst


if __name__ == '__main__':
    dao = Dao('zfl')
    dao.add({"name": "zfl"})
    # r 原始数据不转义
    dao.query(r"insert into zfl(name) values('shuai')")

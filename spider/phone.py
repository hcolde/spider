from spider import Spider
import multiprocessing
import xlwt

def _S_(num):
	headers = {
		'Accept':r'*/*',
		'X-Requested-With': 'XMLHttpRequest',
		'Accept-Encoding': 'gzip, deflate',
		'Accept-Language':'zh-CN,zh;q=0.8',
		'User-Agent':r'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
	}
	url = r'http://star.super.cn/CampusV2/StudentSkip/checkMobileNumber.action'
	oknum = []
	for i in range(0, 9999999):
		n = str(i)
		number = '130'+num+n.rjust(7,'0')

		data = {'mobileNumber': number}

		proxies = {
		  "http": "http://27.40.135.110:61234",
		  "https": "https://182.90.12.188:8118",
		}

		spider = Spider(headers = headers, data = data, proxies = proxies)
		if spider.Req(url = url, method = 'POST'):
			responce = spider.Json()
			if responce:
				code = responce['data']['statusInt'] #0:该手机号已被注册 1:该手机号没注册
				if code == 0:
					oknum.append(number)

	if len(oknum) > 0:
		wb = xlwt.Workbook()
		wbsheet = wb.add_sheet('number')
		for j in range(0, len(oknum)):
			wbsheet.write(j, 0, oknum[j])
		path = r'C:\Users\Administrator\Desktop\130'+num+'.xls'
		wb.save(path)

if __name__ == '__main__':
	yd = ['134', '135', '136', '137', '138', '139', '147', '150', '151', '152', '157', '158', '159', '178', '182', '183', '184', '187', '188']
	lt = ['186', '185', '156', '131', '130', '155', '132', '176']
	dx = ['133', '153', '180', '181', '189', '177', '173', '199']
	
	pro = []
	for i in range(0, 10):
		p = multiprocessing.Process(target = _S_, args = (str(i),))
		p.daemo = True
		pro.append(p)

	for j in range(0, 10):
		pro[j].start()
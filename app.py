import os
from sanic import Sanic
from sanic.response import redirect, html


app = Sanic()

@app.route('/success')
async def success(request):
	return html("""
		<!DOCTYPE html>
		<html>
			<head>
				<title>linux</title>
			</head>
			<body>
				<h1 style="text-align: center;margin-top: 150px;font-size: 50px;color: #C24061FF">恭喜您！作业提交成功</h1>
				<h1 style="text-align: center;color: #FF0000FF;margin-top: 20px;font-size: 57px">请不要进行二次提交</h1>
				<h1 style="text-align: center;color: #D6D6D6FF;margin-top: 100px;font-size: 40px">你所有的努力都不会白费，生活会以另一种方式报答你</h1>
			</body>
		</html>
	""")


@app.route('/', methods=['POST', 'GET'])
async def upload(request):
	if request.method == 'POST':
		f = request.files.get("file")
		basepath = os.path.dirname(__file__)
		upload_path = os.path.join(basepath, 'static', f.name)
		with open(upload_path, 'wb') as fw:
			fw.write(f.body)
		return redirect(app.url_for('success'))
	return html("""
		<!DOCTYPE html>
		<html lang="en">
			<head>
				<meta charset="UTF-8">
				<link href="favicon.ico" rel="shortcut icon">
				<link rel="stylesheet" href="https://cdn.staticfile.org/twitter-bootstrap/3.3.7/css/bootstrap.min.css">
				<title>linux</title>
			</head>
			<body>
				<div class="container">
					<div class="row">
						<h1 style="text-align: center;font-size: 70px;  color: #C24061FF;margin-top: 120px;font-weight: bolder;">《Linux操作系统》课堂作业</h1>
					</div>
					
					<div class="row col-md-offset-2" style="margin-top: 80px">
						<form action="" enctype='multipart/form-data' method='POST'>
							<div class="row btn btn-lg ">
								<input type="file" name="file" class="btn btn-primary" style="font-size: 25px">
							</div>
							<div class="row btn btn-lg ">
								<input type="submit" value="确定提交作业" style="text-align: center;font-size: 30px" class="btn btn-danger ">
							</div>
						</form>
					</div>
				</div>
			</body>
		</html>
	""")

if __name__ == "__main__":
	app.run(host="0.0.0.0", port=9000,access_log=False, workers=4)

const puppeteer = require('puppeteer');
const fs = require('fs');
const path = require('path')
const readline = require('readline');
const url_path = 'urls.txt';

var date = new Date();
var year = date.getFullYear();
var month = date.getMonth()+1;
var day = date.getDate();
const folder = 'screenshot_'+year+'_'+month+'_'+day+'/';
(async () => {
	//同步
	delDir(folder);
	fs.mkdirSync(folder);
    const browser = await puppeteer.launch({
        headless: true,
        args: ['--no-sandbox', '--disable-setuid-sandbox']
    });
	const page = await browser.newPage();
    var urls = []

	let url_lines = await read_file(url_path);
    for (var i = 0; i < url_lines.length; i++) {
//    	console.log(url_lines[i]);
    	var arr = url_lines[i].toString().split(",");
        urls.push(arr)
    }
    for (var i = 0; i < urls.length; i++) {
    	var item = urls[i];
    	var url = item[1].trim();
    	var name = item[0].trim()+".jpeg";
    	var desc = item[2].trim();
    	console.log(desc+"["+name+"]:"+url);
    	
	    await page.setViewport({
	        width: 720,
	        height: 1280,
	        isMobile: true
	    });
		await page.goto(url);

	    await autoScroll(page);

	    await page.screenshot({
	        path: folder+name,
	        fullPage: true
	    });
	    console.log(desc + " Done");
    }
    await browser.close();
    console.log("Sending Email");
    var exec = require('child_process').exec;
    var arg1 = folder
    exec('python3 PageCrawler.py '+ arg1, function(error,stdout,stderr){
    if(error) {
        console.info('stderr : '+stderr);
    }
    console.log("Email Done");
});
})();

function autoScroll(page) {
    return page.evaluate(() => {
        return new Promise((resolve, reject) => {
            var totalHeight = 0;
            var distance = 500;
            var timer = setInterval(() => {
                var scrollHeight = document.body.scrollHeight;
                window.scrollBy(0, distance);
                totalHeight += distance;
                if (totalHeight >= scrollHeight) {
                    clearInterval(timer);
                    resolve();
                }
            }, 30);
        })
    });
}

function read_file(filename) {
	let fileFullName = path.resolve(__dirname, filename)

	return new Promise((resolve, reject) => {
		var fRead = fs.createReadStream(fileFullName);
	    var objReadline = readline.createInterface({
	        input:fRead
	    });
	    var arr = new Array();
	    objReadline.on('line',function (line) {
	        arr.push(line);
	    });
	    objReadline.on('close',function () {
	        // callback(arr);
	        resolve(arr);
	    });
	})
}

function delDir(path){
    let files = [];
    if(fs.existsSync(path)){
        files = fs.readdirSync(path);
        files.forEach((file, index) => {
            let curPath = path + "/" + file;
            if(fs.statSync(curPath).isDirectory()){
                delDir(curPath); //递归删除文件夹
            } else {
                fs.unlinkSync(curPath); //删除文件
            }
        });
        fs.rmdirSync(path);
    }
}
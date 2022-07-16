export default {
    fileMethods: {
        // 返回当前登录中的用户的id
        saveFileList(filename) {
            var fileList = JSON.parse(sessionStorage.getItem('fileList') || '[]')

            let tmp = {fileName: filename}

            if (fileList.find(val => val.fileName === filename) === undefined) {
                fileList.push(tmp)
                sessionStorage.setItem('fileList', JSON.stringify(fileList))
            }


        },
        curFileList() {
            let fileList = JSON.parse(sessionStorage.getItem('fileList') || '[]')
            return fileList
        },
        isExistFile(filename) {
            let fileList = JSON.parse(sessionStorage.getItem('fileList') || '[]')
            return fileList.find(val => val.fileName === filename) !== undefined;

        }
    }
}
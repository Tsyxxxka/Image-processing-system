export default {
    methods: {
        isInteger(n) {
            return Number.isInteger(n)
        },
        isFloat(f) {
            let tmp = parseInt(f);
            if (!Number.isInteger(tmp)){
                return false
            }

            if (Number.isInteger(f)){
                return true
            }

            return f === +f && f !== (f|0);
        },
        isMaxInteger(n) {
            if (n === 'MAX')
                return true
            return Number.isInteger(n)
        },
        calculate_res_name(res_name){
            var tmp_name = res_name
            res_name += '.jpg'
            var resList = JSON.parse(sessionStorage.getItem('resList') || '[]')

            if (resList.find(val => val.resName === res_name) !== undefined) {
                let target = resList.findIndex(val => val.resName === res_name)
                resList[target].num ++ ;
                tmp_name = tmp_name + resList[target].num.toString()
                tmp_name = this.calculate_res_name(tmp_name)

                let tmp = {resName: tmp_name, num: 0}
                resList.push(tmp)
                sessionStorage.setItem('resList', JSON.stringify(resList))
                return tmp_name
            }
            else {
                tmp_name += '.jpg'
                let tmp = {resName: tmp_name, num: 0}
                resList.push(tmp)
                sessionStorage.setItem('resList', JSON.stringify(resList))
                return tmp_name
            }
        }
    }
}
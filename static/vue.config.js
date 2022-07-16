module.exports = {
    publicPath: './',
    devServer: {
        disableHostCheck: false,
        host: "127.0.0.1",
        port: 9091,
        https: false,
        hotOnly: false,
        proxy: null
    },
    lintOnSave: false
};
// module.exports = {
//     devServer: {
//         host: 'localhost',
//         port: 4000,
//         public: '0.0.0.0:4000',
//         proxy: 'http://localhost:3000'
//             // proxy: {
//             //     '^/api': {
//             //         target: 'http://localhost:3000',
//             //         changeOrigin: true,
//             //         logLevel: 'debug',
//             //         pathRewrite: { '^/api': '/' },
//             //     },
//             // },
//     },
// }

module.exports = {
    devServer: {
        proxy: 'http://localhost:3000'
    }
}
module.exports = {
    devServer: {
        host: 'localhost',
        // port: 4000,
        // public: '0.0.0.0:4000',
        proxy: {
            '^/api': {
            target: 'http://localhost:3001',
            changeOrigin: true,
            logLevel: 'debug',
            pathRewrite: { '^/api': '/' },
            },
        },
    },
  }
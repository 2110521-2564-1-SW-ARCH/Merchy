import axios from "axios"
axios.defaults.withCredentials = true

// export default axios.create({
//     baseURL: "http://localhost:3000/api",
//     headers: {
//         "Content-type": "application/json",
//        // 'Access-Control-Allow-Credentials':true
//        // "Access-Control-Allow-Origin" : "*"
//     }
// });

export default axios.create({
    baseURL: "https://gatewaymerchy.run.goorm.io/api",
    headers: {
        "Content-type": "application/json",
        // 'Access-Control-Allow-Credentials':true
       // "Access-Control-Allow-Origin" : "*"
    }
});
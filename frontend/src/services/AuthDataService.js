import http from "../http-common";

class AuthDataService {
    async login(data) {
        return await http.post("/login", data)
    }

    logout() {
        return http.get("/logout")
    }

    get() {
        return http.get("/user")
    }

    create(data) {
        return http.post("/user", data)
    }

    update(data) {
        return http.put(`/user/`, data)
    }

    delete() {
        return http.delete(`/user`)
    }

    loginLazada() {
        return http.get('/lazada/login')
    }

}

export default new AuthDataService();
import http from "../http-common";

class InventoryDataService {

    async getAllEntries() {
        return await http.get("/order")
    }

    async getOneEntry(entryId) {
        return await http.get(`/order/${entryId}`)
    }

    async getAllItems() {
        return await http.get("/item")
    }

    async getOneItem(itemId) {
        return await http.get(`/item/${itemId}`)
    }

    async createItem(data) {
        return await http.post(`/item`,data)
    }
    
    async updateItem(itemId,data) {
        return await http.put(`/item/${itemId}`, data)
    }

    async deleteItem(itemId) {
        return await http.delete(`/item/${itemId}`)
    }

    async getAllAccount() {
        return await http.get("/accounting?resourceType=sales&startDate=2020-11-19T00:00:00&endDate=2021-11-19T23:59:59&scale=year")
    }

}

export default new InventoryDataService();
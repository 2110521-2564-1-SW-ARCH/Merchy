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

    async getAllAccount(start, end, scale) {
        return await http.get(`/accounting/?resourceType=sales&startDate=${start}T00:00:00&endDate=${end}T23:59:59&scale=${scale}`)
        // return await http.get("/accounting/")
        // return await http.get("/idk/wow")
    }

}

export default new InventoryDataService();
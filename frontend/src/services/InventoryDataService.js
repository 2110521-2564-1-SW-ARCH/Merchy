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

}

export default new InventoryDataService();
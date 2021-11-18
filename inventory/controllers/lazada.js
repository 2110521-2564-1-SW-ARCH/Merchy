const Item = require('../models/Item');
const LAZADA = {}


// {
// 	"userId": 123,
// 	"platform": "lazada",
// 	"primaryCategory": 555,
// 	"attributes": {
// 		"name": "Pencil",
// 		"description": "This pen writes and it's wonderful", 
// 		"shortDescription": "It writes", 
// 		"brand": "Gucci" 
// 	},
// 	"skus": [
// 		{
// 			"sellerSku": "Pencil-Red",
// 			"price": 20,
// 			"quantity": 100,
// 			"packageHeight": 2,
// 			"packageLength": 2,
// 			"packageWidth": 2,
// 			"packageWeight": 2,
// 			"images": ["https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.dreamstime.com%2Fred-pencil-white-short-thick-isolated-background-image158241568&psig=AOvVaw0-mipt0pWcsSlpww2f_pW1&ust=1637134664941000&source=images&cd=vfe&ved=0CAsQjRxqFwoTCKDc2IqwnPQCFQAAAAAdAAAAABAD"]
// 		}
// 	]
// }


LAZADA.createItem = async function (request) {
    let item = new Item(request)
    // create a product in LAZADA via API and then attach the return skuIds in the item instance
    return await item.save()
}

module.exports = LAZADA
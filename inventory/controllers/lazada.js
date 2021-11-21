const Item = require('../models/Item');
const axios = require("axios")
const crypto = require("crypto")
const LazadaAPI = require("lazada-open-platform-sdk")

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

const LAZADA = {}
ACCESS_TOKEN = ""
APP_KEY = process.env.LAZADA_APP_KEY
APP_SECRET = process.env.LAZADA_APP_SECRET
REGION = "THAILAND"

function signRequest(apiName, params, secret) {
    // only accepts the sha256 sign method
    let paramsString = apiName
    for (let [param, value] of Object.entries(params)) {
        paramsString += `${param}${value}`
    }
    console.log(paramsString)
    return crypto.createHmac("sha256", secret).update(paramsString).digest("hex").toUpperCase()
}

LAZADA.createItem = async function (request) {
    const lazadaApi = new LazadaAPI(APP_KEY, APP_SECRET, REGION, ACCESS_TOKEN)
    let lazadaItem = await lazadaApi.createProduct({payload: "<Request><Product><PrimaryCategory>6614</PrimaryCategory><SPUId/><AssociatedSku/><Images><Image>https://my-live-02.slatic.net/p/765888ef9ec9e81106f451134c94048f.jpg</Image><Image>https://my-live-02.slatic.net/p/9eca31edef9f05f7e42f0f19e4d412a3.jpg</Image></Images><Attributes><name>api create product test sample</name><short_description>This is a nice product</short_description><brand>Remark</brand><model>asdf</model><kid_years>Kids (6-10yrs)</kid_years><video>12345 (fill with the video id of the previously uploaded video) optional</video><delivery_option_sof>Yes</delivery_option_sof></Attributes><Skus><Sku><SellerSku>api-create-test-1</SellerSku><color_family>Green</color_family><size>40</size><quantity>1</quantity><price>388.50</price><package_length>11</package_length><package_height>22</package_height><package_weight>33</package_weight><package_width>44</package_width><package_content>this is what's in the box</package_content><Images><Image>http://sg.s.alibaba.lzd.co/original/59046bec4d53e74f8ad38d19399205e6.jpg</Image><Image>http://sg.s.alibaba.lzd.co/original/179715d3de39a1918b19eec3279dd482.jpg</Image></Images></Sku></Skus></Product></Request>"})
        .catch(console.log)
    return {}
    // let item = new Item(request)
    // return await item.save()
}

LAZADA.updateItem = async function ({ id, ...others }) {
    let updatedItem = await Item.findByIdAndUpdate(id, others, { new: true })
    if (!updatedItem) return { success: false }
    return { success: true, updatedItem }
}

module.exports = LAZADA
const Item = require('../models/Item');
const LazadaAPI = require("lazada-open-platform-sdk")
const fs = require("fs")

const LAZADA = {}
ACCESS_TOKEN = process.env.MY_ACCESS_TOKEN
APP_KEY = process.env.LAZADA_APP_KEY
APP_SECRET = process.env.LAZADA_APP_SECRET
REGION = "THAILAND"

async function getCategoryTree() {
    const lazadaApi = new LazadaAPI(APP_KEY, APP_SECRET, REGION)
    let categoryTree = await lazadaApi.getCategoryTree({ language_code: "th_TH"}).catch(console.log)
    fs.writeFile("categoryTree.js", JSON.stringify(categoryTree, null, 4), () => {})
}

LAZADA.createItem = async function (request) {
    const lazadaApi = new LazadaAPI(APP_KEY, APP_SECRET, REGION, ACCESS_TOKEN)

    // create payload
    let payload = "<Request><Product>"
    payload += `<PrimaryCategory>${request.primaryCategory}</PrimaryCategory>`
    payload += "<SPUId></SPUId><AssociatedSku></AssociatedSku>"
    payload += `<Attributes><name>${request.attributes.name}</name><description>${request.attributes.description}</description><brand>${request.attributes.brand}</brand></Attributes>`
    payload += "<Skus>"
    for (const sku of request.skus) {
        payload += `<Sku><SellerSku>${sku.sellerSku}</SellerSku><quantity>${sku.quantity}</quantity><price>${sku.price}</price><package_length>${sku.packageLength}</package_length><package_height>${sku.packageHeight}</package_height><package_weight>${sku.packageWeight}</package_weight><package_width>${sku.packageWidth}</package_width>`
        payload += "<Images>"
        for (const image of sku.images) {
            payload += `<Image>${encodeURIComponent(image)}</Image>`
        }
        payload += "</Images></Sku>"
    }
    payload += "</Skus></Product></Request>"

    let lazadaItem = await lazadaApi.createProduct({payload}).catch(console.log)

    // attach itemId and skuIds from lazadaItem to item
    let item = new Item(request)
    item.itemId = lazadaItem.data.item_id
    for(let i=0; i<item.skus.length; i++){
        item.skus[i].skuId = lazadaItem.data.sku_list[i].sku_id
    }

    return await item.save()
    // return {}
}

LAZADA.updateItem = async function ({ id, ...others }) {
    let updatedItem = await Item.findByIdAndUpdate(id, others, { new: true })
    if (!updatedItem) return { success: false }
    return { success: true, updatedItem }
}

module.exports = LAZADA
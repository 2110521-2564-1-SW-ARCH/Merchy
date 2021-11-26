const axios = require("axios")
const Item = require('../models/Item');
const LazadaAPI = require("lazada-open-platform-sdk")
const fs = require("fs")

const LAZADA = {}

APP_KEY = process.env.LAZADA_APP_KEY
APP_SECRET = process.env.LAZADA_APP_SECRET
REGION = "THAILAND"
AUTHENTICATION_SERVICE_IP = process.env.AUTHENTICATION_SERVICE_IP
AUTHENTICATION_SERVICE_PORT = process.env.AUTHENTICATION_SERVICE_PORT
AUTHENTICATION_SERVICE_PROTOCOL = process.env.AUTHENTICATION_SERVICE_PROTOCOL
AUTHENTICATION_SERVICE_URL = `${AUTHENTICATION_SERVICE_PROTOCOL}://${AUTHENTICATION_SERVICE_IP}`
if(AUTHENTICATION_SERVICE_PORT) AUTHENTICATION_SERVICE_URL += `:${AUTHENTICATION_SERVICE_PORT}`

async function getCategoryTree() {
    const lazadaApi = new LazadaAPI(APP_KEY, APP_SECRET, REGION)
    let categoryTree = await lazadaApi.getCategoryTree({ language_code: "th_TH"}).catch(console.log)
    fs.writeFile("categoryTree.js", JSON.stringify(categoryTree, null, 4), () => {})
}

async function getAccessTokenByUserId(userId) {
    let url = `${AUTHENTICATION_SERVICE_URL}/api/lazada/access-token/${userId}`
    let { data } = await axios.get(url).catch()
    return data.accessToken
}

LAZADA.createItem = async function (request) {
    let accessToken = await getAccessTokenByUserId(request.userId)
    const lazadaApi = new LazadaAPI(APP_KEY, APP_SECRET, REGION, accessToken)

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
    if(! lazadaItem) return {}

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
    // update to lazada
    let accessToken = await getAccessTokenByUserId(others.userId)
    const lazadaApi = new LazadaAPI(APP_KEY, APP_SECRET, REGION, accessToken)

    // create payload
    let payload = "<Request><Product>"
    payload += `<PrimaryCategory>${others.primaryCategory}</PrimaryCategory>`
    payload += "<SPUId></SPUId><AssociatedSku></AssociatedSku>"
    payload += `<Attributes><name>${others.attributes.name}</name><description>${others.attributes.description}</description><brand>${others.attributes.brand}</brand></Attributes>`
    payload += "<Skus>"
    for (const sku of others.skus) {
        payload += `<Sku><SellerSku>${sku.sellerSku}</SellerSku><quantity>${sku.quantity}</quantity><price>${sku.price}</price><package_length>${sku.packageLength}</package_length><package_height>${sku.packageHeight}</package_height><package_weight>${sku.packageWeight}</package_weight><package_width>${sku.packageWidth}</package_width>`
        payload += "<Images>"
        for (const image of sku.images) {
            payload += `<Image>${encodeURIComponent(image)}</Image>`
        }
        payload += "</Images></Sku>"
    }
    payload += "</Skus></Product></Request>"

    let response = await lazadaApi.updateProduct({payload}).catch(console.log)
    if(response.code != "0") return {}

    let updatedItem = await Item.findByIdAndUpdate(id, others, { new: true })
    if (!updatedItem) return { success: false }
    return { success: true, updatedItem }
}

LAZADA.refreshItems = async function ({itemList}) {
    for(const newItem of itemList) {
        let itemId = newItem.itemId
        let oldItem = await Item.findOne({ itemId })
        for(const newSku of newItem.skus) {
            for(const oldSku of oldItem.skus) {
                if(oldSku.skuId == newSku.skuId) oldSku.quantity = newSku.quantity
            }
        }
        await oldItem.save()
    }
    
    return true
}

module.exports = LAZADA
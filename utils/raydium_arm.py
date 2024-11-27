async def main():
    global amm, cex
    load_conf()
    amm = Liquidity(  
        config['solanaEndpoint'], 
        get_amm_id(config["baseMint"]), 
        config['walletSecretKey'],
        config['symbol'] 
    )
    await amm.buy(0.1)
    #cex = CEX(config['symbol'], config['cexAPIKey'], config['cexSecretKey'])
    #await monitor_prices()
    # estimate_sell_usd, cex_price, execution_price = await cex.calc_sell_usd_amount(1)
    # await cex.buy(1, cex_price, execution_price)
    # print(await amm.sell(2))

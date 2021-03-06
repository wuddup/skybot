from util import http, hook


@hook.command(autohelp=False)
def bitcoin(inp, say=None):
    ".bitcoin -- gets current exchange rate for bitcoins from BTC-e"
    data = http.get_json("https://btc-e.com/api/2/btc_usd/ticker")
    say("BTC/USD: \x0307{buy:.0f}\x0f - High: \x0307{high}\x0f"
        " - Low: \x0307{low}\x0f - Volume: {vol_cur:.0f}".format(**data['ticker']))

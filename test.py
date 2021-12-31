from fast_proxy_list import proxies

url = "https://www.github.com"
proxy_list = proxies.get_proxies(url, 20, 'all', 'all', 1, 'pickle', savedir="data", verbose=0)


print(proxy_list)
print(len(proxy_list))

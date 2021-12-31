# proxies
v 1.1

what's to come :
- adding more sources to get free proxies - for now proxies are all from free-proxy-list.net
- code visibility changes 

## Requirements 

python >= 3.7
BeautifulSoup (bs4)
Pebble

## Command line usage

$git clone https://github.com/FabienGaillard/proxies.git

> python3 proxies.py --url YOUR_URL 

### Useful Arguments 

--timeout : Time in seconds before requests times out
--nbr-workers : number of thread workers for a faster execution
--savedir : path to where the file will be saved

## Python package usage

### Code

```
import proxies
from proxies import get_proxies

url = "https//:www.github.com"
get_proxies(url)
````
By default, files are saved in the current directory, use the ```savedir``` argument to change the save path.
Arguments types and values are detailled in the code.


## Changes 

v1.1
- Added arguments parser
- Changes to  __main__
- changes to README.md


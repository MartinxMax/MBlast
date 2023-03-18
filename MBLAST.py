#!/usr/bin/python3
# @Мартин.
import textwrap,argparse,sys,requests,threading,random,time
from urllib.parse import quote
from concurrent.futures import ThreadPoolExecutor
from loguru import logger
version = "@Мартин. Django FUZZ Tool V1.0.0"
Logo=f'''
$$\      $$\ $$$$$$$\  $$\        $$$$$$\   $$$$$$\ $$$$$$$$\ 
$$$\    $$$ |$$  __$$\ $$ |      $$  __$$\ $$  __$$\\__$$  __|
$$$$\  $$$$ |$$ |  $$ |$$ |      $$ /  $$ |$$ /  \__|  $$ |   
$$\$$\$$ $$ |$$$$$$$\ |$$ |      $$$$$$$$ |\$$$$$$\    $$ |   
$$ \$$$  $$ |$$  __$$\ $$ |      $$  __$$ | \____$$\   $$ |   
$$ |\$  /$$ |$$ |  $$ |$$ |      $$ |  $$ |$$\   $$ |  $$ |   
$$ | \_/ $$ |$$$$$$$  |$$$$$$$$\ $$ |  $$ |\$$$$$$  |  $$ |   
\__|     \__|\_______/ \________|\__|  \__| \______/   \__|                                                                                                           
                          {version}      
=============================================================='''
def Init_Loger():
    logger.remove()  # 清除所有默认处理器
    logger.add(
        sink=sys.stdout,
        format="<green>[{time:HH:mm:ss}]</green><level>[{level}]</level> | <level>{message}</level>",
        level="INFO"
    )
class Main():
    def __init__(self,args):
        self.URL = args.URL

    def run(self ):
        if self.URL and '*' in self.URL:
            self.get_Page_satat()
        else:
            logger.error("You did not enter the URL correctly, or did not add * injection points")

    def get_Page_satat(self):
        threadPool = ThreadPoolExecutor(max_workers=5, thread_name_prefix="BY_Martin_")
        for i in range(32,132,5):
            threadPool.submit(self.reques,i,i+5)
        threadPool.shutdown(wait=True)


    def reques(self,START,END):
        for PAYLOAD in range(START,END):
            time.sleep(random.randint(1,2))
            try:
                Status = requests.get(self.URL.replace('*', chr(PAYLOAD)), timeout=2)
            except:
                continue
            else:
                logger.info(f"[{str(Status.status_code)}] [Lenght]:{len(Status.text)} [PAYLOAD]:{self.URL.replace('*', quote(chr(PAYLOAD), 'utf-8'))} [HEX]:{hex(PAYLOAD)} [Ascii]{PAYLOAD} --['{chr(PAYLOAD)}']")

def main():
    print(Logo)
    Init_Loger()
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawTextHelpFormatter,
        epilog=textwrap.dedent('''
                Example:
                    author-Github==>https://github.com/MartinxMax
   
                Basic usage:
                    python3 {PY_F} -url www.xxx.com?xxx=* #Mark the injection point with * at the test point
         
                    '''.format(PY_F=sys.argv[0]
                               )))
    parser.add_argument('-url', '--URL', default=None, help='URL')
    args = parser.parse_args()
    Main(args).run()

if __name__ == '__main__':
    main()
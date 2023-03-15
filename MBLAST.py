#!/usr/bin/python3
# @Мартин.
import textwrap,argparse,sys,requests,threading,random,time
from urllib.parse import quote
from concurrent.futures import ThreadPoolExecutor
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

class Main():
    def __init__(self,args):
        self.URL = args.URL

    def run(self ):
        if self.URL and '*' in self.URL:
            self.get_Page_satat()
        else:
            print('[ERROR]You did not enter the URL correctly, or did not add * injection points\n[EXIT]')


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
                print(f"[INFO][{str(Status.status_code)}]", f"[Lenght]:{len(Status.text)}", f"[PAYLOAD]:{self.URL.replace('*', quote(chr(PAYLOAD), 'utf-8'))}",f"[HEX]:{hex(PAYLOAD)}",f"[Ascii]{PAYLOAD} --['{chr(PAYLOAD)}']")


def main():
    print(Logo)
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
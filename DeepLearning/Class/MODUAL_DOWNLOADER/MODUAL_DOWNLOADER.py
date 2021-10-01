import subprocess as SBP
import multiprocessing as MTP
import numpy as NP

class MODUAL_DOWNLOADER:
    def SHELL_INPUT(SHELL_NUM, MODUAL_LIST):
        for MODUAL_NAME in MODUAL_LIST:
            SBP.run(f"py -m pip install {MODUAL_NAME}")
            
    def MULTIPROCESS(MODUAL_LIST):
        DIVIDED_MODUAL_LIST = NP.array_split(MODUAL_LIST, 4)
        COUNTER = len(DIVIDED_MODUAL_LIST)

        TH1 = MTP.Process(target = MODUAL_DOWNLOADER.SHELL_INPUT, args = (1, DIVIDED_MODUAL_LIST[0]))
        TH2 = MTP.Process(target = MODUAL_DOWNLOADER.SHELL_INPUT, args = (2, DIVIDED_MODUAL_LIST[1]))
        TH3 = MTP.Process(target = MODUAL_DOWNLOADER.SHELL_INPUT, args = (3, DIVIDED_MODUAL_LIST[2]))
        TH4 = MTP.Process(target = MODUAL_DOWNLOADER.SHELL_INPUT, args = (4, DIVIDED_MODUAL_LIST[3]))

        if COUNTER == 1:
            TH1.start()
            TH1.join()
        
        elif COUNTER == 2:
            TH1.start()
            TH2.start()
            TH1.join()
            TH2.join()    
        
        elif COUNTER == 3:
            TH1.start()
            TH2.start()
            TH3.start()
            TH1.join()
            TH2.join()
            TH3.join()
        
        elif COUNTER == 4:
            TH1.start()
            TH2.start()
            TH3.start()
            TH4.start()
            TH1.join()
            TH2.join()
            TH3.join()
            TH4.join()

    def DOWNLOADER(MODUAL_LIST = None):
        

        MODUAL_DOWNLOADER.MULTIPROCESS(MODUAL_LIST = MODUAL_LIST)



if __name__ == "__main__":
    MODUAL_DOWNLOADER.DOWNLOADER(MODUAL_LIST = ["gym"])